import glob
from ntpath import join
import os
from typing import Dict, List
import cv2
import numpy as np
import re


class ReferenceImageFormater:
    def __init__(self, path: str) -> None:
        self.path = path

    def __read_images(self):
        images = []
        for path, notas_path, files in os.walk(self.path):
            if len(files) == 0:
                continue
            front_img_filename = [
                file for file in files if re.search("back", file)
            ][0]
            back_img_filename = [
                file for file in files if re.search("front", file)
            ][0]
            front_img = cv2.imread(f'{path}/{front_img_filename}')
            back_img = cv2.imread(f'{path}/{back_img_filename}')
            note = path.split('/')[1]
            images.extend([
                {
                    'type': "anverso",
                    'file': front_img,
                    'filename': front_img_filename,
                    'note': note
                }, {
                    'type': "reverso",
                    'file': back_img,
                    'filename': back_img_filename,
                    'note': note
                }
            ])

        return images

    @staticmethod
    def __bgr2gray(image: dict):
        image['file'] = cv2.cvtColor(image['file'], cv2.COLOR_BGR2GRAY)
        return image

    @staticmethod
    def __generate_rotations(image: dict):
        img_type, file, filename, note = image.values()
        filename, ext = filename.split(".")
        rotated_180 = {
            'type': f'{img_type}_180',
            'file': cv2.rotate(file, cv2.ROTATE_180),
            'filename': f'{filename}_180.{ext}',
            'note': note
        }

        return [rotated_180]

    def format(self):
        imgs = self.__read_images()
        gray_images = list(map(self.__bgr2gray, imgs))
        imgs = gray_images.copy()
        for img in gray_images:
            imgs.extend(self.__generate_rotations(img))
        return imgs


class ImageFileGenerator:
    def __init__(self, destination_directory: str, images) -> None:
        self.dest_dir = destination_directory
        self.images = images
    
    def generate(self):
        for image in self.images:
            filename = f'{self.dest_dir}/{image["note"]}/{image["filename"]}'
            print(filename)
            cv2.imwrite(filename, image['file'])


def main():
    formater = ReferenceImageFormater("reference-images-input/")
    imgs = formater.format()
    generator = ImageFileGenerator('reference-images', imgs)
    generator.generate()
    """
    show_on_verti = np.concatenate(imgs, axis=0)
    cv2.imshow("Imagens em tons de cinza", show_on_verti)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    """


main()


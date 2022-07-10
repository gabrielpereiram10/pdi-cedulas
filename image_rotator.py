from typing import List

import cv2
from image import Image


class ImageRotator:

    @classmethod
    def rotate(cls, image: Image) -> List[Image]:
        filename, ext = image.filename.split(".")
        count = int(filename[-1]) + 2
        filename = f'{filename[:-1]}{count}'
        note = int(image.filename.split('_')[0])
        rotatted_180 = Image(
            filename=f'{filename}.{ext}',
            file=cv2.rotate(image.file, cv2.ROTATE_180),
            note=note
        )

        count += 2
        filename = f'{filename[:-1]}{count}'
        ant_90 = Image(
            filename=f'{filename}.{ext}',
            file=cv2.rotate(image.file, cv2.ROTATE_90_COUNTERCLOCKWISE),
            note=note
        )

        count += 2
        filename = f'{filename[:-1]}{count}'
        rotatted_90 = Image(
            filename=f'{filename}.{ext}',
            file=cv2.rotate(image.file, cv2.ROTATE_90_CLOCKWISE),
            note=note
        )

        return [rotatted_180, ant_90, rotatted_90]

    @classmethod
    def rotate_all(cls, images: List[Image]) -> List[Image]:
        rotatted_images = []
        for image in images:
            rotatted_images.extend(cls.rotate(image))
        return rotatted_images

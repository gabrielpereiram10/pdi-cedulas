import os
from typing import List

import cv2

from image import Image


def read_images(path: str) -> List[Image]:
    filename_list = os.listdir(path)
    images = []
    path = path if '/' in path else f'{path}/'
    for filename in filename_list:
        image = Image(
            filename=filename,
            file=cv2.imread(f'{path}{filename}'),
            note=filename.split("_")[0]
        )
        images.append(image)
    return images


def write_images(dest_path: str, images: List[Image]):
    dest_path = dest_path if '/' in dest_path else f'{dest_path}/'
    for image in images:
        full_file_name = f'{dest_path}{image.filename}'
        cv2.imwrite(full_file_name, image.file)

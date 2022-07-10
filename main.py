from image import Image
from noise import gaus_noise, poison_noise, sp_noise, speckle_noise
from utils import read_images, write_images


def main():
    # images = read_images("reference/")
    # rotatted_images = ImageRotator.rotate_all(images)
    # images.extend(rotatted_images)
    # write_images("reference-images/", images)

    images = read_images("testes/")
    all_images = images.copy()
    for image in images:
        filename, ext = image.filename.split(".")
        count = int(filename[-1]) + 1
        filename = f'{filename[:-1]}{count}'
        gau_image = Image(
            file=gaus_noise(image),
            filename=f'{filename}.{ext}',
            note=image.note
        )
        all_images.append(gau_image)

        count += 1
        filename = f'{filename[:-1]}{count}'
        sp_image = Image(
            file=sp_noise(image, 0.05),
            filename=f'{filename}.{ext}',
            note=image.note
        )
        all_images.append(sp_image)

        count += 1
        filename = f'{filename[:-1]}{count}'
        poison_image = Image(
            file=poison_noise(image),
            filename=f'{filename}.{ext}',
            note=image.note
        )
        all_images.append(poison_image)

        count += 1
        filename = f'{filename[:-1]}{count}'
        speckle_image = Image(
            file=speckle_noise(image),
            filename=f'{filename}.{ext}',
            note=image.note
        )
        all_images.append(speckle_image)

    write_images("teste-images/", all_images)


main()

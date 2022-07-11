import cv2
from image import Image
from noise import gaus_noise, poison_noise, sp_noise, speckle_noise, median_blur
from utils import read_images, write_images


def main():
    # images = read_images("reference/")
    # rotatted_images = ImageRotator.rotate_all(images)
    # images.extend(rotatted_images)
    # write_images("reference-images/", images)

    images = read_images("teste/")
    all_images = images.copy()
    for image in images:
        filename, ext = image.filename.split(".")
        # count = int(filename[-1]) + 1
        # filename = f'{filename[:-1]}{count}'
        # gau_image = Image(
        #     file=gaus_noise(image),
        #     filename=f'{filename}_gaussiano.{ext}',
        #     note=image.note
        # )
        # all_images.append(gau_image)

        median = Image(
            file=median_blur(image),
            filename=f'{filename}_mediana.{ext}',
            note=image.note
        )
        all_images.append(median)

        sp_image = Image(
            file=sp_noise(image, 0.05),
            filename=f'{filename}_sal_pimenta.{ext}',
            note=image.note
        )
        all_images.append(sp_image)


        median_sp = Image(
            file= cv2.addWeighted(median.file, 0.5, sp_image.file, 0.4, 0),
            filename=f'{filename}_mediana_sal_pimenta.{ext}',
            note=image.note
        )

        all_images.append(median_sp)

        sum_aux= cv2.addWeighted(image.file, 0.5, median_sp.file, 0.4, 0)
        sum_aux2= cv2.addWeighted(median.file, 0.5, sp_image.file, 0.4, 0)

        sum_images = Image(
            file= cv2.addWeighted(sum_aux, 0.5, sum_aux2, 0.4, 0),
            filename=f'{filename}_todas_somadas.{ext}',
            note=image.note
        )

        all_images.append(sum_images)

        

        # count += 1
        # filename = f'{filename[:-1]}{count}'
        # poison_image = Image(
        #     file=poison_noise(image),
        #     filename=f'{filename}.{ext}',
        #     note=image.note
        # )
        # all_images.append(poison_image)

        # count += 1
        # filename = f'{filename[:-1]}{count}'
        # speckle_image = Image(
        #     file=speckle_noise(image),
        #     filename=f'{filename}.{ext}',
        #     note=image.note
        # )
        # all_images.append(speckle_image)

    write_images("teste-images/", all_images)

def main2():
    images = read_images("teste-images/")
    all_images = []
    for image in images:
        filename, ext = image.filename.split(".")
        noiseless = Image(
            file=cv2.fastNlMeansDenoising(image.file, None, 20, 7, 21),
            filename=f'{filename}_noiseless.{ext}',
            note=image.note
        )
        all_images.append(noiseless)
    
    write_images("teste-images-noiseless2/", all_images)

    

main2()

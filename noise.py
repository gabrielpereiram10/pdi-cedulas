import random
import cv2
import numpy as np

from image import Image


# def gaus_noise(image: Image):
#     row, col, ch = image.file.shape
#     mean = 0
#     var = 0.7
#     sigma = var**4
#     gauss = np.random.normal(mean, sigma, (row, col, ch))
#     gauss = gauss.reshape(row, col, ch)
#     noisy = image.file + gauss
#     return noisy


def gaus_noise(image: Image):
    row, col, _ = image.file.shape
    # Gaussian distribution parameters
    mean = 0
    var = 0.1
    sigma = var ** 0.5
    gaussian = np.random.normal(mean, sigma, (row, col, 1))
    gaussian = np.concatenate([gaussian, gaussian, gaussian], axis=2)
    return cv2.addWeighted(image.file, 0.75, 0.25 * gaussian, 0.25, 0)


def sp_noise(image: Image, prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.file.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.file.shape[0]):
        for j in range(image.file.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image.file[i][j]
    return output


def poison_noise(image: Image):
    vals = len(np.unique(image.file))
    vals = 2 ** np.ceil(np.log2(vals))
    noisy = np.random.poisson(image.file * vals) / float(vals)
    return noisy


def speckle_noise(image: Image):
    row, col, ch = image.file.shape
    gauss = np.random.randn(row, col, ch)
    gauss = gauss.reshape(row, col, ch)
    noisy = image.file + image.file * gauss
    return noisy


# def noisy(noise_typ: str,image: Image):
#     if noise_typ == "gauss":
        
#     if noise_typ == "s&p":
#     if noise_typ == "poisson":
#         
#     if noise_typ =="speckle":
#         
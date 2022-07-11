
# Imports
import cv2 as cv
from utils import read_images, write_images

# Call function matcher
def matcher(
            image1,
            image2,
            keypoints1,
            keypoints2,
            descriptors1,
            descriptors2,
            descriptor):

    # img1 = cv.imread(filename = image1, flags = cv.IMREAD_GRAYSCALE)
    # img2 = cv.imread(filename = image2, flags = cv.IMREAD_GRAYSCALE)
    # Se descritor for um Descritor de Recursos Locais utilizar NOME
    if (descriptor == 'SURF'):
        normType = cv.NORM_L2
    else:
        normType = cv.NORM_HAMMING

    # Create BFMatcher object
    BFMatcher = cv.BFMatcher(normType = normType,
                                crossCheck = True)

    # Matching descriptor vectors using Brute Force Matcher
    matches = BFMatcher.match(queryDescriptors = descriptors1,
                                trainDescriptors = descriptors2)

    # # Sort them in the order of their distance
    # matches = sorted(matches, key = lambda x: x.distance)

    # # image = img2.copy()


    # image = cv.drawMatches(img1, keypoints1, img2, keypoints2, matches, None, flags=2)


    # full_file_name = f'results/{image1}_{image2}'
    # cv.imwrite(full_file_name, image)



    return len(matches)


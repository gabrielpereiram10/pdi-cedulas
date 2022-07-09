
# Imports
import cv2 as cv

# Call function matcher
def matcher(descriptors1,
            descriptors2,
            descriptor):

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

    # # Draw first 30 matches
    # globals.output = cv.drawMatches(img1 = image1,
    #                                 keypoints1 = keypoints1,
    #                                 img2 = image2,
    #                                 keypoints2 = keypoints2,
    #                                 matches1to2 = matches[:30],
    #                                 outImg = None,
    #                                 flags = cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    return len(matches)
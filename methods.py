from matplotlib import pyplot as plt
import cv2 as cv
import numpy as np
import os
import pickle



def method_brisk(img_ref):

    # Open and convert a input
    # image from BGR to GRAYSCALE
    image = cv.imread(filename = img_ref, flags = cv.IMREAD_GRAYSCALE)

    # BRISK is a feature detector and descriptor
    # Initiate BRISK detector
    BRISK = cv.BRISK_create()

    # Find the keypoints with BRISK
    keypoints = BRISK.detect(image, None)

    # Print number of keypoints detected
    # print("Number of keypoints Detected:", len(keypoints), "\n")

    # Save Keypoints to a file

    # index = []

    # for point in keypoints:
    #     temp = (point.pt,
    #             point.size,
    #             point.angle,
    #             point.response,
    #             point.octave, 
    #             point.class_id)
        
    #     index.append(temp)
        # print("[i]: TEMP", temp )

        # print(" ---------------------------" )

        # print("[i]: point", point )
        


    # Compute the descriptors with BRISK
    keypoints, descriptors = BRISK.compute(image, keypoints)

    data = {
        'keypoints':keypoints,
        'descriptors': descriptors,
    }

    return data

def method_surf(img_ref):
    image = cv.imread(filename = img_ref, flags = cv.IMREAD_GRAYSCALE)

    surf = cv.SURF_create(400)

    keypoints = surf.detect(image, None)

    keypoints, descriptors = surf.compute(image,keypoints)

    data = {
        'keypoints':keypoints,
        'descriptors': descriptors,
    }

    return data

def method_fast(img_ref):
    image = cv.imread(filename = img_ref, flags = cv.IMREAD_GRAYSCALE)

    fast = cv.FastFeatureDetector_create()

    keypoints = fast.detect(image,None)
    keypoints, descriptors = fast.detectAndCompute(image, None)

    data = {
        'keypoints':keypoints,
        'descriptors': descriptors,
    }

    return data


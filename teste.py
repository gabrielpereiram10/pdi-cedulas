import os
import cv2
from features import matcher
from methods import method_brisk, method_surf, method_fast

if __name__ == "__main__":
    print("[i]: Inicializando...")

    # img1 = "reference-images-input/2/2_front.jpg"

    # img2 = "reference-images-input/testes/2_teste.jpg"

    # result_img1 = method_brisk(img1)

    # result_img2 = method_brisk(img2)

    # teste = matcher(descriptors1=result_img1['descriptors'], descriptors2=result_img2['descriptors'], descriptor="BRISK")

    images_ref = []
    folder_ref = 'reference-images'
    for filename in os.listdir(folder_ref):
        images_ref.append(folder_ref+'/'+filename)

    images_teste = []
    folder_teste = 'images_good'
    for filename in os.listdir(folder_teste):
        images_teste.append(folder_teste+'/'+filename)

    descriptors = ['BRISK']

    for descriptor in descriptors:
        k = 850
        vp = 0
        fp = 0
        fn = 0
        vn = 0
        for image_ref in images_ref:
            for image_teste in images_teste:
                print("[i] REF: ", image_ref)
                print("[i] TESTE: ", image_teste)
                if(descriptor == 'BRISK'):
                    result_ref = method_brisk(image_ref)
                    result_test = method_brisk(image_teste)
                elif(descriptor == 'SURF'):
                    result_ref = method_surf(image_ref)
                    result_test = method_surf(image_teste)
                else:
                    result_ref = method_fast(image_ref)
                    result_test = method_fast(image_teste)

                result_matcher = matcher(
                    image1=image_ref,
                    image2=image_teste,
                    keypoints1=result_ref['keypoints'],
                    keypoints2=result_test['keypoints'],
                    descriptors1=result_ref['descriptors'], 
                    descriptors2=result_test['descriptors'], 
                    descriptor=descriptor
                )

                print("[i] MATCHER: ", result_matcher)

                if(result_matcher >= k):
                    if(image_ref.split('/')[1].split('_')[0] == image_teste.split('/')[1].split('_')[0]):
                        vp+=1
                    else:
                        fp+=1
                else:
                    if(image_ref.split('/')[1].split('_')[0] == image_teste.split('/')[1].split('_')[0]):
                        fn+=1
                    else:
                        vn+=1

        print("DESCRIPTOR: ", descriptor)
        sensibilidade = vp/(vp+fn)
        especificidade = vn/(vn+fp)
        precisao = vp/(vp+fp)

        print("VP: ", vp)
        print("FP: ", fp)
        print("FN: ", fn)
        print("VN: ", vn)

        print("sensibilidade: ", sensibilidade)
        print("especificidade: ", especificidade)
        print("precisao: ", precisao)

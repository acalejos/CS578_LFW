import sys
import dlib
from skimage import io
import numpy as np
import cv2

def detectFace(in_file,out_file):
    # Create a HOG face detector using the built-in dlib class
    face_detector = dlib.get_frontal_face_detector()

    # Load the image into an array
    image = io.imread(in_file)
    image_copy = np.copy(image)

    # Run the HOG face detector on the image data.
    # The result will be the bounding boxes of the faces in our image.
    detected_faces = face_detector(image, 1)

    # Loop through each face we found in the image
    for i, face_rect in enumerate(detected_faces):
    	# Draw a box around each face we found
    	cv2.rectangle(image_copy, (face_rect.left(), face_rect.top()), (face_rect.right(), face_rect.bottom()), (255, 0, 255), 2)
    cv2.imwrite(out_file, image_copy)

def main(argv):
    detectFace(argv[0],argv[1])


if __name__ == '__main__':
    if len(sys.argv) > 3:
        print("Usage: python FaceDetectionHOG.py [input filename] [output filename]")
        #sys.exit(0)
    else:
        main(sys.argv[1:])

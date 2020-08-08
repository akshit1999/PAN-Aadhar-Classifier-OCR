# Aadhar and Pan Classification and Character Recognition


# Importing the libraries 
import Data_Preprocessing
import CNN
import Predictions_CM

import numpy as np
import cv2


# Capturing image from camera

cam = cv2.VideoCapture(0)

cv2.namedWindow("Image Capturing")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()

# Predicting the class of image

from CNN import cnn
import cv2
test_image = np.expand_dims(frame, axis = 0)
test_image = test_image[np.newaxis, ...]
test_image = cv2.resize(test_image, (128, 128)) 
result = cnn.predict(test_image)
if result[0][0] == 1:
  prediction = 'pan'
else:
  prediction = 'aadhar'
  
# OCR Function Calling
import OCR_Aadhar_Pan
from OCR_Aadhar_Pan import OCR
Details = OCR(frame, prediction)

# Printing the details
print(Details)
def OCR(image, prediction):
    
    import cv2
    import pytesseract
    import numpy as np
    # from PIL import ImageGrab
    # import time
    
    img = cv2.imread(r"C:\Users\Akshit Jain\Desktop\Internship Idemia\dataset\single_prediction\pan_or_aadhar_2.jpeg")
    
    # Image Preprocessing
    import Image_Preprocessing
    img = Image_Preprocessing.ImagePrep(img)
    
    # Boundary Boxing
    h, w, c = img.shape
    boxes = pytesseract.image_to_boxes(img, config = " -c tessedit_create_boxfile=1") 
    for b in boxes.splitlines():
        b = b.split(' ')
        img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
    
    cv2.imshow('img', img)
    cv2.waitKey(0)
    
    # Character Recognition in the predicted document
    import PAN_File
    from PAN_File import PAN_Card
    
    import Aadhar_File
    from Aadhar_File import Aadhar_Card
    
    if prediction == 'pan':
        PAN = PAN_Card(img)
        return PAN
        
    else:
        Aadhar = Aadhar_Card(img)
        return Aadhar
        
    
def PAN_Card(img):

    import pytesseract
    from pytesseract import Output
    import cv2
    import re
    
    pan_details = {}
    
    t = pytesseract.image_to_data(img, output_type=Output.DICT)
    d = pytesseract.image_to_string(img)
    
    pan_format = r'[a-zA-Z]{5}[0-9]{4}[a-zA-Z]'
    pan_details["Pan Number"] = re.findall(pan_format, d)
    
    pan_details["Name"] = re.findall(r"/Name [\n]+([a-zA-Z]+[\s][a-zA-Z]+)", d)
    
    pan_details["Father's Name"] = re.findall(r"Father's Name[\n]([a-zA-Z]+[\s][a-zA-Z]+[\s][a-zA-Z]+)", d)
    
    pan_details["Date of Birth"] = re.findall(r"(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19[\d][\d]|20[\d][\d])", d)
    
    n_boxes = len(t['text'])
    for i in range(n_boxes):
        if int(t['conf'][i]) > 60:
            if re.match(pan_format, t['text'][i]):
                (x, y, w, h) = (t['left'][i], t['top'][i], t['width'][i], t['height'][i])
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    cv2.imshow('img', img)
    cv2.waitKey(0)

    return pan_details
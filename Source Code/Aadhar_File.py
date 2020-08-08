def Aadhar_Card(img):
    
    import pytesseract
    from pytesseract import Output
    import re
    import cv2
    
    d = pytesseract.image_to_string(img)
    t = pytesseract.image_to_data(img, output_type=Output.DICT)
    
    aadhar_details = {   }
        
    aadhar_format = r'([\d]{4}[\s][\d]{4}[\s][\d]{4})'
    aadhar_details["Aadhar Number"] = re.findall(aadhar_format, d)
    
    enr_format = r'([\d]{4}/[\d]{5}/[\d]{5})'
    aadhar_details["Enrollment Number"] = re.findall(enr_format, d)
        
    aadhar_details["Phone Number"] = re.findall(r"[\d]{10}", d)
    
    aadhar_details["Date of Birth"] = re.findall(r"(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19[\d][\d]|20[\d][\d])", d)
    
    aadhar_details["Gender"] = re.findall(r"Male|Female|Transgender", d)
    
    if re.search("W/O", d) != 0:
        aadhar_details["Husband's Name"] = re.findall("W/O: ([a-zA-Z]+[\s][a-zA-Z]+)", d)
        aadhar_details["Name"] = re.findall(r"([a-zA-Z]+[\s][a-zA-Z]+)[\n]+W/O:", d)
        
    elif re.search("S/O", d) != 0:
        aadhar_details["Father's Name"] = re.findall("S/O: ([a-zA-Z]+[\s][a-zA-Z]+)", d)
        aadhar_details["Name"] = re.findall(r"([a-zA-Z]+[\s][a-zA-Z]+)[\n]+S/O:", d)
        
    elif re.search("D/O", d) != 0:
        aadhar_details["Father's Name"] = re.findall("D/O: ([a-zA-Z]+[\s][a-zA-Z]+)", d)
        aadhar_details["Name"] = re.findall(r"([a-zA-Z]+[\s][a-zA-Z]+)[\n]+D/O:", d)
    
    elif re.search("C/O", d) != 0:
        aadhar_details["Guardian's Name"] = re.findall("C/O: ([a-zA-Z]+[\s][a-zA-Z]+)", d)
        aadhar_details["Name"] = re.findall(r"([a-zA-Z]+[\s][a-zA-Z]+)[\n]+C/O:", d)
        
    else:
        print('No Match Found!')
    
    aadhar_details["Address"] = re.findall(r" (.)+[\n]([\w\s\n\-]+[\n])[\d]+", d)
    
    aadhar_details["Pin Code"] = re.findall(r"[a-zA-Z]+ ([\d]{6})", d)
    
    n_boxes = len(t['text'])
    for i in range(n_boxes):
        if int(t['conf'][i]) > 60:
            if re.match(aadhar_format, t['text'][i]):
                (x, y, w, h) = (t['left'][i], t['top'][i], t['width'][i], t['height'][i])
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
   
    cv2.imshow('img', img)
    cv2.waitKey(0)
    
    return aadhar_details
def get_captcha_text(img,location, size):
    pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'
    im = Image.open(img) # uses PIL library to open image in memory

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']


    im = im.crop((left, top, right, bottom)) # defines crop points
    im.save('sc.png')
    pytesseract.pytesseract.tesseract_cmd=r'C:/Program Files/Tesseract-OCR/tesseract.exe'
    img=Image.open("sc.png").convert('RGB')
    image = 'sc.png'
    img=cv2.imread(image)
    img=cv2.resize(img,None,fx=1,fy=1,interpolation=cv2.INTER_LINEAR)
    kernal=cv2.medianBlur(img,3)
    tn,img=cv2.threshold(img,0,255,cv2.THRESH_BINARY)
    kernal=cv2.getStructuringElement(cv2.MORPH_RECT,(1,3))
    img=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernal)
    cv2.imwrite("sam.png",img)
    file="sam.png"
    text=pytesseract.image_to_string("sam.png")
    return ''.join(i for i in text if i.isalnum())

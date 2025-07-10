import cv2
import easyocr
import cv2 as cv
import matplotlib.pyplot as plt


#read image
#image path
img_path = r"C:\Users\Abhisek kundu\PycharmProjects\PythonProject\.venv\img.png"
img = cv.imread(img_path)


#instance text decoder
reader = easyocr.Reader(['en'],gpu=False)

#detect text from image
text_ = reader.readtext(img)


#text printing
for i in text_:
    bbox, text, score = i
    print(text)
    cv2.rectangle(img,bbox[0],bbox[2],(0,255,0),5)
    cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,255),2)

plt.imshow(cv2.cvtColor(img,    cv2.COLOR_BGR2RGB))
plt.show()


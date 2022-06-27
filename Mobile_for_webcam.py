import requests
import cv2
import numpy as np
import imutils

# replace url
url = "http://192.168.0.103:8080/shot.jpg"

# while loop to continuously fetch data from url
while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2. imdecode(img_arr, -1)
    img = imutils.resize(img, width+1000, height=1000)
    cv2.lmshow("android_cam", img

               # Escape to exit 
               cv2.waitket(1) == 27
                break
            
            cv2.destroyAllWindows()
    
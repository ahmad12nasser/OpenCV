# ex1
# import cv2
# face_detector =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# img =cv2.imread("assets/image2.jpg")
# faces = face_detector.detectMultiScale(img,1.2,5)
# for (x,y,w,h) in faces:
#     new = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
# cv2.imshow("Image",new)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# ex2:


# ex2
# import cv2
# faces_detector = cv2.CascadeClassifier("opencv-master/data/haarcascades/haarcascade_frontalface_default.xml")
# eye_detector = cv2.CascadeClassifier("opencv-master/data/haarcascades/haarcascade_eye.xml")
# smile_detector = cv2.CascadeClassifier("opencv-master/data/haarcascades/haarcascade_smile.xml")
# img = cv2.imread("assets/image2.jpg")
#
# faces = faces_detector.detectMultiScale(img, 1.2,5)
# for (x,y,w,h) in faces:
#     rectangler = cv2.rectangle(img, (x,y),(x+w,y+h), (0,255,0),3)
#     roi_sta = img[y:y+h, x:x+w]
#     eyes = eye_detector.detectMultiScale(roi_sta)
#     for (ex,ey,eh,ew) in eyes:
#         cv2.rectangle(roi_sta, (ex,ey),(ex+ew,ey+eh),(255,255,0),2)
#     smiles = smile_detector.detectMultiScale(roi_sta)
#     for (sx,sy,sw,sh) in smiles:
#         cv2.rectangle(roi_sta,(sx,sy),(sx+sw,sy+sh),(0,0,255),1)
# cv2.imshow("Image",roi_sta)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ex3:
import cv2

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_detector = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('smile_cascade.xml')

img = cv2.imread("assets/image2.jpg")
faces = face_detector.detectMultiScale(img, 1.2, 5)
for (x, y, w, h) in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    roi_color = img[y:y + h, x:x + w]
    eyes = eye_detector.detectMultiScale(roi_color)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 255, 0), 2)
    smiles = smile_cascade.detectMultiScale(roi_gray, 1.2, 30)
    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh),(0, 0, 255), 2)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

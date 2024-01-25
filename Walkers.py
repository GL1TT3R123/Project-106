# import the opencv library
import cv2
#load the cascade classifier
body_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")



# Define a video capture object
vid = cv2.VideoCapture("walking.py")

while(True):
   
    # Capture the video frame by frame
    ret, frame = vid.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    body=body_classifier.detectMultiScale(grey,1.2,3)
    for x,y,w,h in body:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    # Display the resulting frame
    cv2.imshow("Web cam", frame)
      
    # Quit Window by Spacebar Key
    if cv2.waitKey(25) == 32:
        break
  
# After the loop release the cap object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()
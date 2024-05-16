import cv2
import dlib
import numpy as np

-- capture the frames from my primary camera

cap = cv2.VideoCapture(0)

-- face detector model

face_detector = dlib.get_frontal_face_detector()

-- Capture frames continuously
while True:

    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    -- Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector(gray)

    -- Iterate through all the faces and draw reactangle around each face and also number it.
    i = 0;
    for face in faces:
    -- Find the coordinates of face
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()

        -- Draw the rectangle
        cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

        i = i + 1
        cv2.putText(frame, "Face num "+ str(i), (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    
    cv2.imshow("Frame", frame)

    -- Code to come out of the infinite loop / interrupt the execution

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
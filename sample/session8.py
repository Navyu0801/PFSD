import cv2 as cv

# Load the Haar cascade for face detection
fc = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap=cv.VideoCapture(0)
while True:
    # Read the input image
    ret,frame=cap.read()

    # Convert the image to grayscale
    imgGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = fc.detectMultiScale(imgGray, scaleFactor=1.1, minNeighbors=4)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv.imshow("result",frame)
    if cv.waitKey(1) and 0xFF==(ord('q')):
        break

# Display the image with detected faces
cap.release()
cv.destroyAllWindows()
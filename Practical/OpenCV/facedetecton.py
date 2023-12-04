import cv2

# Load the face cascade file
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open the default camera (usually webcam)
cap = cv2.VideoCapture(0)

while True: 
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        break  # Break the loop if there's an issue capturing the frame

    # Convert the captured frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the frame with face detections
    cv2.imshow('Face Detection', frame)

    # Check if the window is closed
    if cv2.getWindowProperty('Face Detection', cv2.WND_PROP_VISIBLE) < 1:
        break

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()

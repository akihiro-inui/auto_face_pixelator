# import libraries
import cv2
import face_recognition

# Get a reference to webcam
video_capture = cv2.VideoCapture(0)

# Initialize variables
face_locations = []

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)

    # Display the results
    for top, right, bottom, left in face_locations:
        # Resize to small size
        small = cv2.resize(frame[top:bottom, left:right], None, fx=0.05, fy=0.05, interpolation=cv2.INTER_NEAREST)
        # Resize back to original size (face area)
        frame[top:bottom, left:right] = cv2.resize(small, frame[top:bottom, left:right].shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

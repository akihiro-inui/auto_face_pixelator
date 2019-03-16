import cv2
import face_recognition


def mosaic(image):

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_image = image[:, :, ::-1]

    # Find all the faces in the current frame of video
    face_locations = face_recognition.face_locations(rgb_image)

    # Display the results
    for top, right, bottom, left in face_locations:
        # Resize to small size
        small = cv2.resize(image[top:bottom, left:right], None, fx=0.05, fy=0.05, interpolation=cv2.INTER_NEAREST)
        # Resize back to original size (face area)
        image[top:bottom, left:right] = cv2.resize(small, image[top:bottom, left:right].shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

    return image

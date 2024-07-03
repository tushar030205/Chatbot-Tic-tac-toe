import cv2

# Path to the Haar Cascade model
harcascade = "model/haarcascade_frontalface_default.xml"

# Function to detect faces in an image
def detect_faces_image(image_path):
    # Read the image
    img = cv2.imread(image_path)
    
    # Check if the image was successfully loaded
    if img is None:
        print("Error: Unable to load image. Please check the image path.")
        return
    
    # Load the Haar Cascade model for face detection
    facecascade = cv2.CascadeClassifier(harcascade)
    
    # Convert the image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = facecascade.detectMultiScale(img_gray, 1.1, 4)
    
    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Resize the image for display
    resized_img = cv2.resize(img, (800, 600))
    
    # Display the image with detected faces
    cv2.imshow("Detected Faces", resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
detect_faces_image("cv2.jpg")


# Function to detect faces in real-time using webcam
def detect_faces_webcam():
    # Capture video from the webcam
    cap = cv2.VideoCapture(0)
    
    # Set video frame width and height
    cap.set(3, 640)  # width
    cap.set(4, 480)  # height
    
    # Load the Haar Cascade model for face detection
    facecascade = cv2.CascadeClassifier(harcascade)
    
    while True:
        # Read a frame from the webcam
        success, img = cap.read()
        
        # Check if the frame was successfully captured
        if not success:
            print("Error: Unable to capture video.")
            break
        
        # Convert the frame to grayscale
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Detect faces
        faces = facecascade.detectMultiScale(img_gray, 1.1, 4)
        
        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Display the frame with detected faces
        cv2.imshow("Face", img)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()

# Example usage
detect_faces_webcam()
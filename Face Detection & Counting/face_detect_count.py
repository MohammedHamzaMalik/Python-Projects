import cv2  # Import OpenCV

# Getting image path
imagePath = "C:\\Users\\hp\\Desktop\\LetsUpgrade\\face detection\\portrait-of-group-of-people-X29A19.jpg"
# Getting cascading file path
cascPath = "C:\\Users\\hp\\Desktop\\LetsUpgrade\\face detection\\haarcascade_frontalface_default.xml"


faceCascade = cv2.CascadeClassifier(cascPath)  # Creating the haar cascade

# Reading the image
image = cv2.imread(imagePath)
# Converting the image to grayscale, in order to apply the classification
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Making a function to detect objects
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(10, 10),
)

print('Found {0} faces'.format(len(faces)))
print(faces)


for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)  #  Using the built-in rectangle() function


cv2.rectangle(image, (0, image.shape[0] -25),(1000000, image.shape[0]), (255,255,255), 100)
cv2.putText(image, "Number of faces detected: " + str(faces.shape[0]), (0,image.shape[0] - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 1.5,  (0, 0, 0), 2)

# Resizing the image
resize = cv2.resize(image, (int(image.shape[1]/2), int(image.shape[0]/2)))

# Showing the image
cv2.imshow("Faces found", resize)
# Waiting for user to press key
cv2.waitKey(0)

# Closing the image window
cv2.destroyAllWindows()

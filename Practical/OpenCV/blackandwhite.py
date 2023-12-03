import cv2

# Read the image in color
image_path = './krshna.jpg'  # Replace with your image path
img_color = cv2.imread(image_path)

if img_color is None:
    print("Could not read the image. Please check the file path.")
else:
    # Convert the image to grayscale
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    # Display the original and grayscale images
    cv2.imshow('Original Image', img_color)
    cv2.imshow('Grayscale Image', img_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

import cv2
img=cv2.imread("./mailheader-removebg-preview.png",cv2.COLOR_BGR2RGB)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
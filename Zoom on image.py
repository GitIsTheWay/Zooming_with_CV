import cv2

image = cv2.imread(r"E:\MY FILES\Wallpapers\RDT_20220108_1728126884347779768933392.jpg")
zoom_factor = float(input("How much do you want to zoom? "))
dimensions = image.shape
new_Height = (dimensions[0] * zoom_factor)
new_Width = (dimensions[1] * zoom_factor)
zoomed = cv2.resize(image, (int(new_Height), int(new_Width)), interpolation=cv2.INTER_LINEAR)
cv2.imshow("Original image" , image)
cv2.imshow("Zoomed image" ,zoomed )
cv2.waitKey(0)


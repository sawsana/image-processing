import cv2
import matplotlib.pyplot as plt
img = cv2.imread ('hill.jpg')
plt.imshow(img)
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)

import cv2
import numpy as np
import matplotlib.pyplot as plt


image_path = 'gul.jpg'
image = cv2.imread(image_path)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 50, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 50, 50])
upper_red2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = mask1 | mask2

black_background = np.zeros_like(image)

purple_rose = image.copy()
purple_rose[mask != 0] = [128, 0, 128]

sonuc = np.where(mask[..., np.newaxis] != 0, purple_rose, black_background)

output_path = 'gul_purple_rose_black_bg.jpg'
cv2.imwrite(output_path, sonuc)

plt.imshow(cv2.cvtColor(sonuc, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()

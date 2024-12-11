import cv2
import numpy as np

# Load the grayscale depth map
depth_map = cv2.imread('depth_experiment/pots_marigold.png', cv2.IMREAD_GRAYSCALE)

# Ensure the image is in 8-bit format (values range from 0 to 255)
if depth_map is None:
    raise ValueError("Image not found or unable to load.")

# Invert the grayscale depth map
inverted_depth_map = 255 - depth_map

# Save or display the inverted depth map
cv2.imwrite('depth_experiment/pots_marigold_inverted.png', inverted_depth_map)
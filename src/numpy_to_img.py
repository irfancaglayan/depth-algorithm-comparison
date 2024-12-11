import torch
import numpy as np
import cv2

# Load your depth map in .npy format
depth_map = np.load("depth_experiment/depth.npy")

# Scale the depth map to metric scale, with clamp to maintain 0-300 range
canonical_to_real_scale = 707.0493 / 1000.0  # example based on focal length of canonical camera
depth_map = depth_map * canonical_to_real_scale
depth_map = np.clip(depth_map, 0, 300)  # clamp values to [0, 300] range

# Normalize to the 0-255 range for grayscale visualization
normalized_depth_map = (depth_map - depth_map.min()) / (depth_map.max() - depth_map.min()) * 255
inverted_depth_map = 255 - normalized_depth_map  # Invert for visual emphasis

# Convert to uint8
grayscale_depth_map = inverted_depth_map.astype(np.uint8)

# Save as grayscale image
cv2.imwrite("depth_experiment/baby_metric3d.png", grayscale_depth_map)
from PIL import Image
import numpy as np
import os

# Function to load and convert an image to a grayscale array
def load_image(image_path):
    image = Image.open(image_path).convert('L')
    return np.array(image, dtype=np.float32)

# Function to calculate MSE and SQR
def calculate_mse_sqr(ref, est):
    sqr = (est - ref) ** 2
    mse = np.mean(sqr)
    return mse, sqr

# Function to normalize an image array to the range [0, 1]
def normalize_image(image_array):
    return (image_array - np.min(image_array)) / (np.max(image_array) - np.min(image_array))

# Function to process multiple depth maps and calculate MSE (both raw and normalized)
def process_depth_maps(ref_image_path, est_image_paths):
    # Load the reference image
    ref_array = load_image(ref_image_path)

    # Normalize the reference array
    ref_array_norm = normalize_image(ref_array)

    results = []

    for est_image_path in est_image_paths:
        # Load the estimated depth map
        est_array = load_image(est_image_path)

        # Calculate raw MSE and SQR
        mse_raw, sqr_raw = calculate_mse_sqr(ref_array, est_array)

        # Normalize the estimated depth map
        est_array_norm = normalize_image(est_array)

        # Calculate normalized MSE and SQR
        mse_norm, sqr_norm = calculate_mse_sqr(ref_array_norm, est_array_norm)

        # Store the results
        results.append({
            'file_name': os.path.basename(est_image_path),
            'mse_raw': mse_raw,
            'mse_norm': mse_norm
        })

    return results

if __name__ == '__main__':
    # Path to the reference depth map
    ref_image_path = 'bowling_depth.png'

    # List of paths to the estimated depth maps (new maps)
    est_image_paths = [
        'bowling_lotus.png'
        # Add more paths as needed
    ]

    # Process the depth maps and print the results
    results = process_depth_maps(ref_image_path, est_image_paths)

    for result in results:
        print(f"File: {result['file_name']}")
        print(f"  Raw MSE: {result['mse_raw']}")
        print(f"  Normalized MSE: {result['mse_norm']}")
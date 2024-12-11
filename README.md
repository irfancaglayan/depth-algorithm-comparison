# Comparing Monocular Depth Estimation Algorithms
A small-scale exploratory research to compare the performances of various monocular depth estimation algorithms.

## Table of Contents
1. [Introduction](#introduction)
2. [Dataset](#dataset)
3. [Quantitative Results](#quantitative-results)
4. [Qualitative Results](#qualitative-results)
5. [General Observations](#general-observations)

## Introduction
This project explores the performances of the following monocular depth estimation algorithms in comparison with the Middlebury stereo depth maps.
- Depth Anything V2
- Marigold
- UniDepthV2
- Depth Pro
- Lotus

For the following four images, depth estimations accuracies have been computed by the following formulation utilizing Mean Square Error: 

```python
def calculate_mse_sqr(ref, est): 
  sqr = (est - ref) ** 2 
  mse = np.mean(sqr) 
  return mse, sqr
```

Moreover, to observe the accuracies disregarding the scaling differences, normalization has been applied to the images by the following code:

```python
def normalize_image(image_array): 
  return (image_array - np.min(image_array)) / (np.max(image_array) - 
np.min(image_array)) 
```

Following 4 images from the Middlebury dataset have been used for the experiment:

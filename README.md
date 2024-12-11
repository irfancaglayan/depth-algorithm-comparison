# Comparing Monocular Depth Estimation Algorithms
A small-scale exploratory research to compare the performances of various monocular depth estimation algorithms.

## Table of Contents
1. [Introduction](#introduction)
2. [Quantitative Results](#quantitative-results)
3. [General Observations](#general-observations)

## Introduction
This project explores the performances of the following monocular depth estimation algorithms in comparison with the Middlebury stereo depth maps.
- [Depth Anything V2](https://github.com/DepthAnything/Depth-Anything-V2)
- [Marigold](https://github.com/prs-eth/Marigold)
- [UniDepthV2](https://github.com/lpiccinelli-eth/UniDepth)
- [Depth Pro](https://github.com/apple/ml-depth-pro)
- [Lotus](https://github.com/EnVision-Research/Lotus)

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

The images used can be found in [dataset](dataset/) folder. The qualitative results can be found in [results](results/) folder.

## Quantitative Results
### Results for baby.png

| Algorithm         | RAW Image MSE | Normalized Image MSE |
|:-----------------:|:-------------:|:--------------------:|
| Depth Anything V2 | 4533.27       | 0.090                |
| Marigold          | 6613.62       | 0.070                |
| UniDepthV2        | 418.02        | 0.075                |
| Depth Pro         | 3932.21       | 0.090                |
| Lotus             | 6201.44       | 0.098                |

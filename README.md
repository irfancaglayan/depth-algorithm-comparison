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

### Results for bowling.png

| Algorithm         | RAW Image MSE | Normalized Image MSE |
|:-----------------:|:-------------:|:--------------------:|
| Depth Anything V2 | 874.56        | 0.021                |
| Marigold          | 10174.74      | 0.012                |
| UniDepthV2        | 871.53        | 0.026                |
| Depth Pro         | 871.53        | 0.011                |
| Lotus             | 2983.33       | 0.029                |

### Results for midd.png

| Algorithm         | RAW Image MSE | Normalized Image MSE |
|:-----------------:|:-------------:|:--------------------:|
| Depth Anything V2 | 1355.29       | 0.036                |
| Marigold          | 6274.63       | 0.067                |
| UniDepthV2        | 612.38        | 0.026                |
| Depth Pro         | 1463.61       | 0.043                |
| Lotus             | 3044.90       | 0.044                |

### Results for pots.png

| Algorithm         | RAW Image MSE | Normalized Image MSE |
|:-----------------:|:-------------:|:--------------------:|
| Depth Anything V2 | 2088.11       | 0.023                |
| Marigold          | 12498.00      | 0.090                |
| UniDepthV2        | 2077.39       | 0.059                |
| Depth Pro         | 2077.39       | 0.033                |

## General Observations
- Parameters of UniDepthV2 have been updated since its scaling was not on par with the other algorithms. Its depth maps appeared metric enough initially, meaning the distance of the closer and further objects were realistic; however, its coloring had to be adjusted for proper use.
- Scaling of Marigold is highly saturated, causing some details to be lost in the objects. This is not only due to scaling but also to significant depth estimation differences between nearer and farther objects.
- Depth Pro and Lotus Depth have the best performance in capturing object details, such as facial features of the doll, wrinkles in the hat, rims of pots, etc.
- Although UniDepthV2 comes first numerically in the tests, it should be noted that its performance in capturing details is not the best. UniDepthV2 is apparently built for continuous and consistent depth map estimations for videos; therefore, it can be used for real-time applications considering its performance in numerical analyses as well. However, for other applications which require higher-resolution depth maps of still images, DepthAnythingV2 and Depth Pro would be better options. 

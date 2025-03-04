# Pipe_Type_Detection Using PointNet++
## Description
This project is about how a Realsense L515 can detect the Pipe Type which is left right or open in real-time at the ROS platform. The point cloud data is captured by Realsense L515 and Gemini camera. The models were trained using PointNet++ method.

The results show that using the SSG method can reach 95.83% accuracy in predicting the pipe type which is faster than the MSG method (91.67%). It proves that the SSG method is good at predicting pipe type.

## Setup
The models were trained at the windows side using Anaconda. The configurations and settings are shown below:

Dependencies | VERSION
--|--
CUDA	| 12.1
CUDNN	| 8.9.7.29
Python	| 3.8
PyTorch	| 2.1.0
PyTorch Cuda	| 12.1.0
Torch Vision	| 0.16.0

Laptop configuration:

DETAIL | VERSION
--|--
Processer | Intel i7-13700H
Ram | 16 GB
NVIDIA driver | 536.45
GPU | RTX4060-GPU 8 GB

## environment installation
Code below is used for setting up environment in conda:
```shell

conda activate pointnet2 #pointnet2 is my environment name in conda
conda install pytorch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 pytorch-cuda12.1 -c pytorch -c nvidia -y

```

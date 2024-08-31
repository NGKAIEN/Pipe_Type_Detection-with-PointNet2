
## Install
The latest codes are tested on Ubuntu 16.04, CUDA10.1, PyTorch 1.6 and Python 3.7:
```shell
conda install pytorch==1.6.0 cudatoolkit=10.1 -c pytorch
```

## Classification 
### Data Preparation
Data preprocessing using ply2txt.py
Original data captured by the camera in .ply format, it contains 6 elements (x,y,z,r,g,b) and header information. If we want to use pointnet to train model, the file formats need to convert to .txt format, which is only 3 elements we need to remain (x,y,z coordinate).

### Run
You can run different modes with the following codes. The number. of categories is modified to 3.

```shell

# ModelNet40
## Select different models in ./models 
## e.g., pointnet without normal features
python train_classification.py --model pointnet_cls --log_dir pointnet_cls --num_category 3
python test_classification.py --log_dir pointnet_cls

## e.g., pointnet2_ssg without normal features
python train_classification.py --model pointnet2_cls_ssg --log_dir pointnet2_cls_ssg --num_category 3
python test_classification.py --log_dir pointnet2_cls_ssg

## e.g., pointnet2_msg without normal features
python train_classification.py --model pointnet2_cls_msg --log_dir pointnet2_cls_msg --num_category 3
python test_classification.py --log_dir pointnet2_cls_msg

```
### Testing Model Accuracy Using Random Data
Using test_visualizer.py can use the trained model to test random pipe point cloud data that is put inside a specific path. This function can be a base for building a real-time pipe-type detection function.

We can using this file as a function :
``` shell
python test_visualizer.py --logdir pointnet2_cls_msg 
```

### Performance
Accuracy is tested using test_classification.py and the random dataset is captured using the Orbbec Gemini camera.

| Model | Accuracy |
|--|--|
| PointNet (Pytorch without normal) |  79.17 |
| PointNet2_SSG (Pytorch without normal) |  91.67 |
| PointNet2_MSG (Pytorch without normal) |  95.83  |


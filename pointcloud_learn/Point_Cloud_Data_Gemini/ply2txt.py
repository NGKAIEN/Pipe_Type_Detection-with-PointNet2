import open3d as o3d
import numpy as np
import os

# 定义要处理的文件夹路径
folder_path = "H:\\pointcloud_learn\\modified\\pipe_shape_detection_gemini\\data\\pipe_shape_detection2\\open"  # 将此路径替换为你的文件夹路径

# 遍历文件夹中的所有PLY文件
for file_name in os.listdir(folder_path):
    # 检查文件扩展名是否为.ply
    if file_name.endswith('.ply'):
        # 构造PLY文件的完整路径
        ply_path = os.path.join(folder_path, file_name)
        
        # 读取PLY文件
        point_cloud = o3d.io.read_point_cloud(ply_path)
        
        # 提取点云的坐标
        points = np.asarray(point_cloud.points)
        
        # 应用过滤器：删除坐标为[0.000000, 0.000000, 0.000000]的点
        points = points[np.linalg.norm(points - [0, 0, 0], axis=1) > 1e-6]
        
        # 重新排列数据成三维形式
        num_points = len(points)
        max_points = 100000  # 设置最大点数，可以根据需要调整
        padded_points = np.zeros((max_points, 3))  # 创建一个三维数组来存储数据
        
        if num_points > max_points:
            print("Warning: 数据点数超过最大点数，可能会丢失部分数据。")
            padded_points[:max_points] = points[:max_points]
        else:
            padded_points[:num_points] = points
        
        # 构造输出TXT文件的路径（使用原文件名，但扩展名改为.txt）
        txt_path = os.path.join(folder_path, os.path.splitext(file_name)[0] + '.txt')
        
        # 将重新排列后的点云坐标写入TXT文件
        np.savetxt(txt_path, padded_points, fmt='%f', delimiter=',')  # 使用空格分隔x, y, z坐标
        
        print(f"已将 {file_name} 的点云位置信息保存到 {txt_path}")

print("所有文件处理完毕。")
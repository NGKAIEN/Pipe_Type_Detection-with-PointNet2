import open3d as o3d
import numpy as np
import os


folder_path = r"H:\pointcloud_learn\modified\pipe_shape_detection_gemini\data\pipe_shape_detection2"  


for file_name in os.listdir(folder_path):
   
    if file_name.endswith('.ply'):
        
        ply_path = os.path.join(folder_path, file_name)
        
        
        point_cloud = o3d.io.read_point_cloud(ply_path)
        
        
        points = np.asarray(point_cloud.points)
        
       
        txt_path = os.path.join(folder_path, os.path.splitext(file_name)[0] + '.txt')
        
       
        np.savetxt(txt_path, points, fmt='%f', delimiter=',')  
        
        print(f" {file_name} {txt_path}")

print("end;")

import os
import random
import shutil
from pathlib import Path

# 获取当前程序执行的工作目录
current_directory = os.getcwd()
#带类别标签的数据集所在目录（这里将数据集分为了open和close两类）
folder_paths = [Path(current_directory + "/left"), Path(current_directory + "/right"), Path(current_directory + "/open")]
#生成以下目标文件（配置文件）
txt_file_path = Path(current_directory + "/filelist.txt")#记录全部带标签的数据集文件（带后缀名）
txt_file_path2 = Path(current_directory + "/pipe_shape_detection_train.txt")#记录全部带标签的训练文件（不带后缀名）
txt_file_path3 = Path(current_directory + "/pipe_shape_detection_test.txt")#记录全部带标签的测试文件（不带后缀名）
txt_file_path4 = Path(current_directory + "/pipe_shape_detection_shape_names.txt")#记录全部类别（不带后缀名）
txt_file_path5 = Path(current_directory + "/pipe_shape_detection_realtest.txt")#记录不带标签的真实测试文件（不带后缀名）

# 打开目标文件
with txt_file_path.open("w") as txt_file, txt_file_path2.open("w") as txt_file2, txt_file_path3.open("w") as txt_file3, txt_file_path4.open("w") as txt_file4:  # Added txt_file_path5
    for folder_path in folder_paths:
        folder_name = folder_path.name
        file_list = folder_path.glob("*")
        for i, file_path in enumerate(file_list, start=1):
            new_file_name = f"{folder_name}_{str(i).zfill(4)}{file_path.suffix}"
            new_file_path = folder_path / new_file_name
            file_path.rename(new_file_path) #将数据集中的文件名重命名（类别_编号）
            txt_file.write(str(new_file_path.relative_to(os.path.dirname(folder_path))) + "\n")  # 将新文件的相对路径写入filelist.txt
            txt_file2.write(new_file_path.stem + "\n")  # 将新文件的文件名（不包含后缀）写入pantograph2_train.txt
            txt_file3.write(new_file_path.stem + "\n")  # 这里测试集和训练集设成了相同，视自己情况而定
        txt_file4.write(folder_name + "\n")  # 将文件夹名（类别名）写入pantograph2_shape_names.txt

#以下代码是生成真实测试数据Test目录（这里就是简单抽取训练集中的一些数据，标签是通过目录名称体现，这里可以认为这些数据不带标签）
# 从open目录中随机选择n个文件
        
'''
n_test=5
open_files = list(Path(current_directory + "/open").glob("*"))
selected_open_files = random.sample(open_files, n_test)
# 从close目录中随机选择n个文件
close_files = list(Path(current_directory + "/close").glob("*"))
selected_close_files = random.sample(close_files, n_test)
# 将选中的文件复制到Test目录中
test_folder_path = Path(current_directory + "/Test")
test_folder_path.mkdir(exist_ok=True)  # 创建Test目录（如果不存在）
for file_path in selected_open_files + selected_close_files:
    new_file_path = test_folder_path / file_path.name
    shutil.copy(file_path, new_file_path)

#以下代码是将Test目录中文件的文件名（不包含后缀）写入pantograph2_realtest.txt
with txt_file_path5.open("a") as txt_file5:
    test_file_list = test_folder_path.glob("*")
    txt_file5.write("\n".join(file_path.stem for file_path in test_file_list) + "\n")

'''
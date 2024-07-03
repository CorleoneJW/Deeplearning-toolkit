import os
import shutil
from PIL import Image

def copy_and_convert_images(src_folder, dst_folder):
    # 检查目标文件夹是否存在，如果不存在则创建
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)
    
    # 使用 os.walk 递归遍历源文件夹及其所有子文件夹
    for root, dirs, files in os.walk(src_folder):
        for filename in files:
            # 获取文件的完整路径
            src_file = os.path.join(root, filename)
            
            # 检查文件是否为图片类型
            if filename.lower().endswith(('.png', '.jpeg', '.gif', '.bmp', '.tiff')):
                # 如果文件不是 jpg 格式，将其转换为 jpg
                img = Image.open(src_file)
                new_filename = os.path.splitext(filename)[0] + '.jpg'
                dst_file = os.path.join(dst_folder, new_filename)
                img = img.convert('RGB')
                img.save(dst_file, 'JPEG')
                # print(f'已转换并复制: {src_file} -> {dst_file}')
            elif filename.lower().endswith('.jpg'):
                # 如果文件已经是 jpg 格式，直接复制
                shutil.copy(src_file, dst_folder)
                # print(f'已复制: {src_file}')
            else:
                print(f'跳过: {src_file}')
                
# 设置源文件夹和目标文件夹路径
src_folder = 'processed\\non-neoplastic'  # 替换为你的源文件夹路径
dst_folder = 'unified\\non-neoplastic'  # 替换为你的目标文件夹路径

# 调用函数执行复制和转换操作
copy_and_convert_images(src_folder, dst_folder)

print("Converting finished!")
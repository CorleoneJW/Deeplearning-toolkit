import os

# 要清理的文件夹路径
folder_path = '.'

# 遍历文件夹及其子文件夹
for root, dirs, files in os.walk(folder_path, topdown=False):
    for file in files:
        if file.startswith('.'):
            # 构建文件的完整路径
            file_path = os.path.join(root, file)
            
            # 删除文件
            os.remove(file_path)
            
            print(f"已删除文件: {file_path}")
    
    for dir in dirs:
        dir_path = os.path.join(root, dir)
        if dir.startswith('.'):
            # 删除文件夹
            os.rmdir(dir_path)
            print(f"已删除文件夹: {dir_path}")

print("清理操作完成！")

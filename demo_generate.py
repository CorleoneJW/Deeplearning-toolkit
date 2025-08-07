import os
import random
import shutil

def copy_one_file_per_case(src_root, dst_root, file_extensions=None):
    """
    从原始数据集中复制文件结构到目标文件夹中，每个病例目录只保留一个文件。
    
    参数:
    - src_root: 原始数据集根目录
    - dst_root: 新的数据集根目录
    - file_extensions: 限定的文件后缀，如 ['.jpg', '.png']；为 None 表示不过滤
    """
    for dirpath, dirnames, filenames in os.walk(src_root):
        # 判断是否是病例目录（没有子目录）
        if not dirnames and filenames:
            # 筛选符合扩展名的文件
            if file_extensions:
                valid_files = [f for f in filenames if os.path.splitext(f)[1].lower() in file_extensions]
            else:
                valid_files = filenames

            if valid_files:
                selected_file = random.choice(valid_files)
                src_file_path = os.path.join(dirpath, selected_file)

                # 构造目标路径
                relative_path = os.path.relpath(dirpath, src_root)
                dst_case_dir = os.path.join(dst_root, relative_path)
                os.makedirs(dst_case_dir, exist_ok=True)

                shutil.copy2(src_file_path, os.path.join(dst_case_dir, selected_file))
                print(f"[✔] 已复制: {src_file_path} -> {dst_case_dir}")
            else:
                print(f"[!] 目录 {dirpath} 中无有效文件")

        else:
            # 如果是中间目录，确保也创建对应结构
            relative_path = os.path.relpath(dirpath, src_root)
            dst_path = os.path.join(dst_root, relative_path)
            os.makedirs(dst_path, exist_ok=True)

# 用法：
src = "src_data_fodler_path"
dst = "demo_dataset_path"
# copy_one_file_per_case(src, dst, file_extensions=['.jpg', '.png'])  # 可改为 None 表示不过滤文件类型
copy_one_file_per_case(src, dst, file_extensions=None)  # 可改为 None 表示不过滤文件类型
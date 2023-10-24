# 在index的caption后中加入新的文件
import os
def add_filenames(directory, string_incoulded, target_position):
    all_file=target_position+"\n"
    for filename in os.listdir(directory):
        if string_incoulded in filename:
            add_file = os.path.join(directory, filename)
            all_file = all_file+"\n   "+add_file
    with open("index.rst", 'r') as file:
        filedata = file.read()
    filedata = filedata.replace(target_position, all_file)
    with open("index.rst", 'w') as file:
        file.write(filedata)


def delete_lines_with_string(file_path, string):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        add_newline = False  # 标记是否需要添加空行
        for line in lines:
            if string not in line:
                if line.strip():  # 排除空行
                    file.write(line)
                else:
                    add_newline = True  # 标记下一行需要添加空行
            elif add_newline:
                file.write('\n')  # 在删除行后的位置添加空行
                add_newline = False  # 重置标记



# 指定目录路径
directory1 = 'qcl/qiskit'
directory2 = 'qcl/chip'
directory3 = 'qcl/mac'

# 文件名字包含的字符
string_incoulded = ".md"

# 指定目标字符串
target_position1 = '   :caption: QISKIT'
target_position2 = '   :caption: CHIP'
target_position3 = '   :caption: MAC'

# 删除包含'qcl/'的行
delete_lines_with_string('index.rst', 'qcl/')

# 调用函数进行替换
add_filenames(directory1, string_incoulded, target_position1)
add_filenames(directory2, string_incoulded, target_position2)
add_filenames(directory3, string_incoulded, target_position3)
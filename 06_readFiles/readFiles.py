import json
import os
import shutil
import tempfile

# # 演示文件操作：使用临时目录
# workdir = tempfile.mkdtemp(prefix="python_basics_")
# print("本次演示使用的临时目录:", workdir)
#
# # 先准备一个 myfile.txt，供 with 语句读取
# myfile_txt = os.path.join(workdir, "myfile.txt")
# with open(myfile_txt, "w", encoding="utf-8") as f:
#     f.write("第一行\n第二行\n")
#
# # 你可以使用 with 语句来代替 try/finally 对操作进行结束的操作
# with open(myfile_txt, encoding="utf-8") as f:
#     for line in f:
#         print(line, end="")
#
# # 写入文件
# contents = {"aa": 12, "bb": 21}
# myfile1 = os.path.join(workdir, "myfile1.txt")
# with open(myfile1, "w+", encoding="utf-8") as file:
#     file.write(str(contents))        # 写入字符串到文件
#
# myfile2 = os.path.join(workdir, "myfile2.txt")
# with open(myfile2, "w+", encoding="utf-8") as file:
#     file.write(json.dumps(contents))  # 写入对象到文件
#
# # 从文件读取字符串
# with open(myfile1, "r+", encoding="utf-8") as file:
#     contents = file.read()
# print(contents)
# # print: {"aa": 12, "bb": 21}
#
# # 从文件读取 json 对象
# with open(myfile2, "r+", encoding="utf-8") as file:
#     contents = json.load(file)
# print(contents)
# # print: {"aa": 12, "bb": 21}
#
# # Windows 环境调用 open() 读取文件的默认编码为 ANSI，如果需要读取 utf-8 编码的文件，
# # 需要指定 encoding 参数:
# # open("myfile3.txt", "r+", encoding="utf-8")
#
# # 清理本次演示生成的临时文件
# shutil.rmtree(workdir)
# print("已清理临时目录")

# 第一个实参是文件名字符串。第二个实参是包含描述文件使用方式字符的字符串。
# mode 的值包括 'r' ，表示文件只能读取；'w' 表示只能写入（现有同名文件会被覆盖）；
# 'a' 表示打开文件并追加内容，任何写入的数据会自动添加到文件末尾。
# 'r+' 表示打开文件进行读写。mode 实参是可选的，省略时的默认值为 'r'。
with open('workfile.txt') as f:
    read_data = f.read()
    f.close()
    # f.read()     调用 f.close() 关闭文件对象后，再次使用该文件对象将会失败。
    print(f.closed)


# 文件对象的方法
# f.read(size) 可用于读取文件内容，它会读取一些数据，并返回字符串（文本模式），或字节串对象（在二进制模式下）。
# size 是可选的数值参数,如已到达文件末尾，f.read() 返回空字符串 ('')。
with open('workfile.txt') as f:
    data = f.read()
    print(data)
    print(f.read()) # ''
    f.close()

# f.readline() 从文件中读取单行数据；字符串末尾保留换行符 (\n)，只有在文件不以换行符结尾时，文件的最后一行才会省略换行符。
with open('workfile.txt') as f:
    data = f.readline()
    print(data)

# 从文件中读取多行时，可以用循环遍历整个文件对象。
with open('workfile.txt') as f:
    for line in f:
        print(line, end='')

# f.write(string) 把 string 的内容写入文件，并返回写入的字符数。
with open('workfile.txt','w') as f:
    f.write('This is the first line of the file\n.Second line of the file\n')

# f.seek(offset, whence) 可以改变文件对象的位置。
f = open('workfile.txt', 'rb+')
print(f.seek(5))      # 定位到文件中的第 6 个字节
print(f.read(1))
print(f.seek(-3, 2))  # 定位到倒数第 3 个字节
print(f.read(1))

# 使用 json 保存结构化数据¶
import json
x = [1, 'simple', 'list']
print(json.dumps(x))

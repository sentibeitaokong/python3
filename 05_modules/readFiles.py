import json
import os
import shutil
import tempfile

# 演示文件操作：使用临时目录
workdir = tempfile.mkdtemp(prefix="python_basics_")
print("本次演示使用的临时目录:", workdir)

# 先准备一个 myfile.txt，供 with 语句读取
myfile_txt = os.path.join(workdir, "myfile.txt")
with open(myfile_txt, "w", encoding="utf-8") as f:
    f.write("第一行\n第二行\n")

# 你可以使用 with 语句来代替 try/finally 对操作进行结束的操作
with open(myfile_txt, encoding="utf-8") as f:
    for line in f:
        print(line, end="")

# 写入文件
contents = {"aa": 12, "bb": 21}
myfile1 = os.path.join(workdir, "myfile1.txt")
with open(myfile1, "w+", encoding="utf-8") as file:
    file.write(str(contents))        # 写入字符串到文件

myfile2 = os.path.join(workdir, "myfile2.txt")
with open(myfile2, "w+", encoding="utf-8") as file:
    file.write(json.dumps(contents))  # 写入对象到文件

# 从文件读取字符串
with open(myfile1, "r+", encoding="utf-8") as file:
    contents = file.read()
print(contents)
# print: {"aa": 12, "bb": 21}

# 从文件读取 json 对象
with open(myfile2, "r+", encoding="utf-8") as file:
    contents = json.load(file)
print(contents)
# print: {"aa": 12, "bb": 21}

# Windows 环境调用 open() 读取文件的默认编码为 ANSI，如果需要读取 utf-8 编码的文件，
# 需要指定 encoding 参数:
# open("myfile3.txt", "r+", encoding="utf-8")

# 清理本次演示生成的临时文件
shutil.rmtree(workdir)
print("已清理临时目录")
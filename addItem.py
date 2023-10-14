from findItem import findItem
import os
def run():
    exes = open(r"D:\Project\pyFind\allExes.txt", "r+",encoding='utf-8')
    short = input("输入一个简写名字用于查找: ")
    print("你输入的是: " + short)
    path = input("输入exe文件的路径: ")
    print("路径是: " + path)
    cwd = os.path.dirname(path)
    cwd = cwd + '"'
    print("工作目录 是 " + cwd)
    newItem = findItem(short, path, cwd)
    if(exes.read() == ""):
        exes.write(short + " " + path + " " + cwd)
    else:
        exes.write('\n' + short + " " + path + " " + cwd)
    exes.close()
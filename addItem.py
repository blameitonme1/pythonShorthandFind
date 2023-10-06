from findItem import findItem
def run():
    exes = open(r"D:\Project\pyFind\allExes.txt", "r+")
    short = input("输入一个简写名字用于查找: ")
    print("你输入的是: " + short)
    path = input("输入exe文件的路径: ")
    print("路径是: " + path)
    cwd = input("输入exe的工作目录: ")
    print("cwd 是 " + cwd)
    newItem = findItem(short, path, cwd)
    if(exes.read() == ""):
        exes.write(short + " " + path + " " + cwd)
    else:
        exes.write('\n' + short + " " + path + " " + cwd)
    exes.close()
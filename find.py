import re
import os
from findItem import findItem
import subprocess
def run():
    short = input("输入简写名字: ")
    exes = open(r"D:\Project\pyFind\allExes.txt", "r")
    for line in exes:
        item = re.match(r'(\S+)\s+"([^"]+)"\s+"([^"]+)"', line)
        if(item.group(1) == short):
            try:
                # print(item.group(1) + item.group(2))
                subprocess.Popen(item.group(2), shell=True, cwd=item.group(3))
                print("打开文件成功\n")
            except FileNotFoundError:
                print("没有找到该文件, 可能要更新路径\n")
            except Exception as e:
                print("发生了错误: " + str(e) + '\n')
    print("进程结束\n")
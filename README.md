# pythonShorthandFind
自己写的一个powershell脚本，使用自定义的简化名字查找应用程序 (.exe) 并在对应文件夹环境中打开 

使用python的os对本地电脑进行操作，只在windows运行，因为写的是powershell脚本。但是之后可以尝试移植到linux
# 用法
 因为没有添加环境变量，只能引用**绝对路径** python3 D:\Project\pyFind\find.ps1

![一个example](https://raw.githubusercontent.com/blameitonme1/pics/main/ps1example.png)

可以看到想要打开的程序成功打开了，如果shorthand name不正确就报错退出

![成功运行](https://raw.githubusercontent.com/blameitonme1/pics/main/ps1success.png)

# 添加了环境变量之后的用法
  直接输入find.ps1即可
# 更新思路
  可以在脚本加入自动修改环境变量的功能，但是我觉得随意添加环境变量会污染电脑环境，所以还没有想到一个简单一点的解决方法。

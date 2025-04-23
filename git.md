# 上传文件：

## 1、git add -A，提交所有变化。

## 2、git commit -m "修改注释"

怎么抢救一下commit的注释？

$ git commit --amend -m "修改的内容"

查看修改内容

git diff 文件名.文件类型

查看当前版本信息

git log

## 3、向一个空的新仓库中推文件：$ git push -u 仓库名称 分支

只有第一次推的时候需要加上-u，以后的推送只输入：

$ git push 名称 分支

$ git push origin master -f 这个-f就是force，强制推送。

# 连接仓库

![image-20250401230612917](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20250401230612917.png)

使用 git remote -v 命令查看关联状况

git remote -v

# 远程仓库修改后更新本地仓库

1、克隆仓库

git clone 复制的SSH或者HTTPS key

2、取回远程文件

git pull 仓库代名称

那怎么抢救一下文件名？

直接修改文件名重新提交就可以啦。

git add -A —> git commit -m “修改文件名” —> git push origin main

$ git commit --amend的作用：

github不管你做错了啥，他都会给你保存的，就是即使你改了，你的错误记录永远存在！但是使用git commit --amend，你可以神不知鬼不觉悄咪咪修改你的错误commit注释，╭(●｀∀´●)╯只有天知地知你知。


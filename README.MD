南京信息工程大学 INUIST 自动登陆脚本
====
需要Python3 requests库支持
----
CentOS:<br>
`sudo yum -y install python3`<br>
`sudo pip3 install requests`<br>
RHT:<br>
`sudo apt-get -y install python3`<br>
`sudo pip3 install requests`<br>
MACOS:<br>
`sudo brew install python3`<br>
`sudo pip3 install requests`<br>
Windows:<br>
前往[python](https://www.python.org/downloads/windows/)官网下载安装Python3<br>
CMD输入`pip install requests`<br>

使用方法:
----
    在index.txt里依次填入你的
    1.账号
    2.密码
    3.运营商(中国移动/中国电信/中国联通)
    **用回车键分隔** 第三行的结尾不要换行

    之后运行NUISTNetLogin.py就可以自动登录

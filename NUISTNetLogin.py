################################################################################
# @Author: carrgan
# @Date:   2019/09/18
# @Filename: NUISTNetLogin.py
# @Last modified by:   carrgan
# @Last modified time: 2019/09/18
# !usr/bin/python
# Version: V0.1
# @Program:
#	NUISTNetLogin
################################################################################


import requests
import os
import base64
import tkinter as tk
import tkinter

def windows(warn):
	window = tk.Tk()
	window.title('Error')
	sw = window.winfo_screenwidth()
	sh = window.winfo_screenheight()
	x = (sw-300)/2
	y = (sh-100)/2
	window.geometry('300x100+%d+%d'%(x,y))
	l = tk.Label(window,text=warn,font=('Arial', 14),width=50,height=3)
	l.pack()
	def hit_me():
	    exit()
	b = tk.Button(window,
	    text='确定',
	    width=15, height=2,
	    command=hit_me)
	b.pack()
	window.mainloop()

def operator(var):
	return{'中国移动':'CMCC','中国联通':'Unicom','中国电信':'ChinaNet'}.get(var,'CMCC')

def base6(num):
	encode = base64.b64encode(num.encode('utf-8'))
	return(str(encode,'utf-8'))

jy=open('index.txt')
username=jy.readline()
username = username[:-1]
if username.strip()=='':
	windows('请在index.txt中填写正确的账号密码运营商')

b=jy.readline()
b=b[:-1]
password = base6(b)

domain=jy.readline()
domain = operator('domain')

data = {'username':username,'domain':domain,'password':password,'enablemacauth':'0'}
try:
	r = requests.post('http://a.nuist.edu.cn/index.php/index/login',data=data)
	r.raise_for_status()
except:
	windows('网络不畅通哦 Wi-Fi打开了吗')

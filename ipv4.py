#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import subprocess
import tkinter as tk
root = tk.Tk()
root.geometry('400x500')

tk.Label(root, text='IP地址: ').place(x=60, y= 20)
tk.Label(root, text='子网掩码: ').place(x=60, y= 40)
tk.Label(root, text='默认网关: ').place(x=60, y= 60)
tk.Label(root, text='首选DNS: ').place(x=60, y= 80)
tk.Label(root, text='备用DNS: ').place(x=60, y= 100)

# ip.set('example@python.com')
ip = tk.Entry(root)
ip.place(x=170, y=20)

# ip2 = tk.Entry(root,width=4)
# ip2.place(x=180, y=20)

yanma = tk.Entry(root)
yanma.place(x=170, y=40)

wangguan = tk.Entry(root)
wangguan.place(x=170, y=60)

shouxuan = tk.Entry(root)
shouxuan.place(x=170, y=80)

beiyong = tk.Entry(root)
beiyong.place(x=170, y=100)




def insert_point():
	command1='netsh interface ip set address name="以太网" source= static '+ip.get()+' '+yanma.get()+' '+wangguan.get()
	command2='netsh interface ip set dns name="以太网" source= static addr='+shouxuan.get()+' register=primary'
	command3='netsh interface ip add dns name="以太网" addr='+beiyong.get()+' index=2'
	subprocess.Popen(command1, close_fds=True)
	subprocess.Popen(command2, close_fds=True)
	subprocess.Popen(command3, close_fds=True)
	try:
		p=subprocess.Popen('ping 8.8.8.8',  stdout=subprocess.PIPE)
		for i in p.stdout.readlines():
			if('丢失 = 'in i.decode('cp936')):
				result=i.decode('cp936')
				tk.Label(root,text=result).place(x=20, y= 460)
				if(result.split('(')[1].split('%')[0] !='100'):
					tk.Label(root,text='Success!').place(x=150, y= 480)
				else:
					tk.Label(root,text='ERROR!').place(x=150, y= 480)
	except Exception as e:
		tk.Label(root,text='ERROR:'+e).place(x=150, y= 480)


	#tk.Label(root,text='完成').place(x=150, y= 120)
b1 = tk.Button(root,text='设置1',width=15,
            height=2,command=insert_point)
b1.place(x=150, y=130)



tk.Label(root, text='------------------------------------------------------------------------------------ ').place(x=0, y= 180)
tk.Label(root, text='IP地址: ').place(x=60, y= 200)
tk.Label(root, text='子网掩码: ').place(x=60, y= 220)
tk.Label(root, text='默认网关: ').place(x=60, y= 240)
tk.Label(root, text='首选DNS: ').place(x=60, y= 260)
tk.Label(root, text='备用DNS: ').place(x=60, y= 280)

# ip.set('example@python.com')
ip2 = tk.Entry(root)
ip2.place(x=170, y=200)

# ip2 = tk.Entry(root,width=4)
# ip2.place(x=180, y=20)

yanma2 = tk.Entry(root)
yanma2.place(x=170, y=220)

wangguan2 = tk.Entry(root)
wangguan2.place(x=170, y=240)

shouxuan2 = tk.Entry(root)
shouxuan2.place(x=170, y=260)

beiyong2 = tk.Entry(root)
beiyong2.place(x=170, y=280)



def insert_point2():
	command1='netsh interface ip set address name="以太网" source= static '+ip2.get()+' '+yanma2.get()+' '+wangguan2.get()
	command2='netsh interface ip set dns name="以太网" source= static addr='+shouxuan2.get()+' register=primary'
	command3='netsh interface ip add dns name="以太网" addr='+beiyong2.get()+' index=2'
	subprocess.Popen(command1, close_fds=True)
	subprocess.Popen(command2, close_fds=True)
	subprocess.Popen(command3, close_fds=True)
	try:
		p=subprocess.Popen('ping 8.8.8.8',  stdout=subprocess.PIPE)
		for i in p.stdout.readlines():
			if('丢失 = 'in i.decode('cp936')):
				result=i.decode('cp936')
				tk.Label(root,text=result).place(x=20, y= 460)
				if(result.split('(')[1].split('%')[0] !='100'):
					tk.Label(root,text='Success!').place(x=150, y= 480)
				else:
					tk.Label(root,text='ERROR!').place(x=150, y= 480)
	except Exception as e:
		tk.Label(root,text='ERROR:'+e).place(x=150, y= 480)

b2 = tk.Button(root,text='设置2',width=15,
            height=2,command=insert_point2)
b2.place(x=150, y=310)


root.mainloop()


# os.system('netsh interface ip set address name="以太网" source= static 192.168.0.1 255.255.255.0 192.168.0.1')
# os.system('netsh interface ip set dns name="以太网" source= static addr=8.8.8.8 register=primary')
# os.system('netsh interface ip add dns name="以太网" addr=223.5.5.5 index=2 ')

# subprocess.Popen('netsh interface ip set address name="以太网" source= static 192.168.0.1 255.255.255.0 192.168.0.1', close_fds=True)
# subprocess.Popen('netsh interface ip set dns name="以太网" source= static addr=223.6.6.6 register=primary', close_fds=True)
# subprocess.Popen('netsh interface ip add dns name="以太网" addr=223.5.5.5 index=2', close_fds=True)
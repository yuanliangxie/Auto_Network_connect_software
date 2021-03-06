#-*- coding:utf-8 -*-
__edit_author__ = 'yuanliangxie'

import time
import requests
import threading
from PyQt5.QtCore import QThread, pyqtSignal


class Login(QThread):
	stateUpdate = pyqtSignal(object)
	def __init__(self):
		super(Login, self).__init__()
		#检测间隔时间，单位为秒
		self.every = 10
		self._flag = threading.Event()  # 用于暂停线程的标识
		self._flag.set()  # 设置为True
		self._running = threading.Event()  # 用于停止线程的标识
		self._running.set()  # 将running设置为True

	def stop(self):
		self._flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
		self._running.clear()  # 设置为False

	def set_account_password(self, account, password):
		self.account_num = account
		self.password = password

	#模拟登录
	def login(self):
		print(self.getCurrentTime(), u"拼命连网中...")
		url="https://drcom.szu.edu.cn/"
		#消息头
		headers={
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
			'Accept-Encoding': 'gzip, deflate, br',
			'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7",
			'Cache-Control': 'max-age=0',
			'Connection': 'keep-alive',
			'Content-Length': '64',
			'Content-Type': 'application/x-www-form-urlencoded',
			'Cookie': '',
			'Host': 'drcom.szu.edu.cn',
			'Origin': 'https://drcom.szu.edu.cn',
			'Referer': 'https://drcom.szu.edu.cn/a70.htm',
			'Sec-Fetch-Mode': 'navigate',
			'Sec-Fetch-Site': 'same-origin',
			'Sec-Fetch-User': '?1',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36',
		}
		#提交的信息
		payload={
			'DDDDD': self.account_num,
			'upass': self.password,
			'R1': '0',
			'R2': '',
			'R6': '0',
			'para': '00',
			'0MKKey': '123456',
		}
		try:
			requests.post(url,headers=headers,data=payload)
			print(self.getCurrentTime(),u'现在开始看连接是否正常')
		except:
			print("error")
	#判断当前是否可以连网
	def canConnect(self):
		try:
			q=requests.get("https://www.baidu.com", timeout=10)
			if(q.status_code==200):
				return True
			else:
				return False
		except:
			return False

	#获取当前时间
	def getCurrentTime(self):
		return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))

	#主函数
	def run(self):
		print(self.getCurrentTime(), u"Hi，欢迎使用自动登陆系统")
		while True:
			self.login()
			while True:
				can_connect = self.canConnect()
				if not can_connect:
					self.stateUpdate.emit(False)
					break
				else:
					self.stateUpdate.emit(True)
				time.sleep(self.every)
if __name__ == '__main__':
	login = Login()
	login.main()
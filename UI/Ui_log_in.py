#Author:"yuanliangxie"
#coding:utf-8
from PyQt5.QtWidgets import QDesktopWidget, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QFormLayout, QLineEdit, \
	QPushButton, QApplication, QGridLayout, QCheckBox

from PyQt5.QtGui import *
import sys
#import qdarkstyle

class Ui_log_in_Form():
	def center(self):
		screen = QDesktopWidget().screenGeometry()  # 获取屏幕分辨率
		size = self.geometry()  # 获取窗口尺寸
		self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


	def log_in_setUI(self):
		self.main_layout = QVBoxLayout()

		self.show_flat = QLabel()
		self.up_layout = QHBoxLayout()
		self.label1 = QLabel("自动重连上网客户端")
		self.label1.setStyleSheet("QLabel{font-family:'黑体';font-size:20px;color:rgb(255,255,255);}")
		self.label2 = QLabel("Automatic reconnection")
		self.label2.setStyleSheet("QLabel{font-family:'黑体';font-size:15px;color:orange;}")
		self.left_show = QWidget()
		self.left_layout = QVBoxLayout()
		self.left_layout.addStretch(1)
		self.left_layout.addWidget(self.label1)
		self.left_layout.addWidget(self.label2)
		self.left_layout.addStretch(1)
		self.left_show.setLayout(self.left_layout)

		self.up_layout.addStretch(1)
		self.up_layout.addWidget(self.left_show)
		self.show_flat.setLayout(self.up_layout)
		self.show_flat.setPixmap(QPixmap("./UI/blue_sky.jpg"))


		self.middle_flat =  QWidget()
		self.middle_flat.setStyleSheet("QWidget{background-color: white}")
		self.middle_layout = QVBoxLayout()

		self.account_pass = QWidget()
		self.account_pass_layout = QHBoxLayout()

		self.form_layout = QFormLayout()
		self.form_widget = QWidget()

		self.account_label = QLabel("账号：")
		self.password_label = QLabel("密码：")

		self.account_number = QLineEdit("")
		self.password_number = QLineEdit("")

		font = QFont()
		font.setPixelSize(18)

		self.account_label.setFont(font)
		self.password_label.setFont(font)

		self.account_number.setFont(font)
		self.password_number.setFont(font)

		self.choose_widge = QWidget()
		self.choose_layout = QGridLayout()

		self.save_pass = QCheckBox("保存密码")
		self.auto_log = QCheckBox("自动登录")

		self.quit_Button = QPushButton("退出")
		self.log_in_Button = QPushButton("登录")

		self.quit_Button.setStyleSheet("QPushButton{font-family:'黑体';} \
				QPushButton:hover{background-color:rgb(152, 245, 255);}")
		self.log_in_Button.setStyleSheet("QPushButton{font-family:'黑体';} \
				QPushButton:hover{background-color:rgb(152, 245, 255);}")


		self.choose_layout.addWidget(self.save_pass, 0, 0)
		self.choose_layout.addWidget(self.auto_log, 0, 1)
		self.choose_layout.addWidget(self.quit_Button, 1, 0)
		self.choose_layout.addWidget(self.log_in_Button, 1, 1)
		self.choose_widge.setLayout(self.choose_layout)


		self.form_layout.addRow(self.account_label, self.account_number)
		self.form_layout.addRow(self.password_label, self.password_number)
		self.form_widget.setLayout(self.form_layout)

		#self.account_pass_layout.addStretch()
		self.account_pass_layout.addWidget(self.form_widget)
		#self.account_pass_layout.addStretch(0.5)
		self.account_pass.setLayout(self.account_pass_layout)


		self.middle_layout.addWidget(self.account_pass)
		self.middle_layout.addWidget(self.choose_widge)
		self.middle_flat.setLayout(self.middle_layout)

		self.main_layout.addWidget(self.show_flat)
		self.main_layout.addWidget(self.middle_flat)

	#return self.main_layout

	#self.setLayout(self.main_layout)

class test_UI(QWidget, Ui_log_in_Form):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("SECURE and RELAX")
		self.resize(350, 425)
		self.setFixedSize(350, 425)
		self.center()
		self.log_in_setUI()
		self.setLayout(self.main_layout)



if __name__ == '__main__':
	app = QApplication(sys.argv)
	ui_log_in = test_UI()
	ui_log_in.show()
	sys.exit(app.exec_())















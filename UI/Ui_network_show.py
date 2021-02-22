#Author:"yuanliangxie"
#coding:utf-8
from PyQt5.QtWidgets import QDesktopWidget, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QFormLayout, QLineEdit, \
	QPushButton, QApplication
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
import qtawesome
import sys
#import qdarkstyle

class Ui_network_show_Form():

	def center(self):
		screen = QDesktopWidget().screenGeometry()  # 获取屏幕分辨率
		size = self.geometry()  # 获取窗口尺寸
		self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


	def network_show_setUI(self):
		self.main_layout = QVBoxLayout()

		self.show_info = QWidget()
		self.show_info.setStyleSheet("QWidget{background-color: white}")
		self.show_info.setGeometry(0, 0, 200, 400)
		self.show_info_layout = QHBoxLayout()

		self.headshow = QLabel()
		self.headshow.setGeometry(0, 0, 200, 200)
		pixmap = QPixmap("./UI/head_show.jpg")
		scaredPixmap = pixmap.scaled(200, 200, aspectRatioMode=Qt.KeepAspectRatio)
		self.headshow.setPixmap(scaredPixmap)

		self.info_show = QWidget()
		self.info_show_layout = QFormLayout()

		self.account_label = QLabel("账号：")
		self.state_label = QLabel("状态：")
		self.Warning = QLabel("善意提醒:")
		self.Warning.setStyleSheet("QLabel{color: red;}")

		self.account_number = QLineEdit("")
		self.state_content = QLineEdit("")
		self.label_tea = QLabel()
		pixmap = QPixmap("./UI/gouqitea.jpeg")
		scaredPixmap = pixmap.scaled(60, 60, aspectRatioMode=Qt.IgnoreAspectRatio)
		self.label_tea.setPixmap(scaredPixmap)
		self.label_tea.setAlignment(Qt.AlignCenter)

		self.account_number.setStyleSheet("QLineEdit{font-family:'黑体';font-size:20px; border: None; color: black;}")
		self.state_content.setStyleSheet("QLineEdit{font-family:'黑体';font-size:18px; border: None; color: green;}")

		self.info_show_layout.addRow(self.account_label, self.account_number)
		self.info_show_layout.addRow(self.state_label, self.state_content)
		self.info_show_layout.addRow(self.Warning, self.label_tea)


		self.info_show_layout.addWidget(self.label_tea)
		self.info_show.setLayout(self.info_show_layout)

		self.show_info_layout.addWidget(self.headshow)
		self.show_info_layout.addWidget(self.info_show)
		self.show_info.setLayout(self.show_info_layout)

		self.state = QWidget()
		self.state_layout = QHBoxLayout()
		self.label_quit = QPushButton()
		self.label_quit.setGeometry(0, 0, 200, 200)
		pixmap = QPixmap("./UI/quit.png")
		scaredPixmap = pixmap.scaled(200, 200, aspectRatioMode=Qt.KeepAspectRatio)
		self.label_quit.setIcon(QIcon(scaredPixmap))
		self.state_layout.addStretch(2)
		self.state_layout.addWidget(self.label_quit)
		self.state.setLayout(self.state_layout)


		self.main_layout.addWidget(self.show_info)
		self.main_layout.addWidget(self.state)

	#self.setLayout(self.main_layout)

class test_UI(QWidget, Ui_network_show_Form):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("自动重连上网客户端")
		self.resize(420, 300)
		self.setFixedSize(420, 300)
		self.center()
		self.network_show_setUI()
		self.setLayout(self.main_layout)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ui_log = test_UI()
	ui_log.show()
	sys.exit(app.exec_())















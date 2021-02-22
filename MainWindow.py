from PyQt5.QtWidgets import QWidget, QFrame, QDesktopWidget, QApplication
from UI.Ui_log_in import Ui_log_in_Form
from UI.Ui_network_show import Ui_network_show_Form
from Thread_network_connect import Login
import sys
class MainWindow(QWidget):
	def __init__(self):
		super(MainWindow,self).__init__()

		self.QFrame1 = QFrame(self)

		self.QFrame2 = QFrame(self)
		self.QFrame2.setVisible(False)

		self.Ui_log_in = Ui_log_in_Form()
		self.Ui_log_in.log_in_setUI()

		self.Ui_network_show = Ui_network_show_Form()
		self.Ui_network_show.network_show_setUI()




		#对登录界面进行初始化
		self.set_init_Ui_log_in()

		self.login = Login()
		self.login.stateUpdate.connect(self.Update_state_tip)
		self.QFrame1.setLayout(self.Ui_log_in.main_layout)

		self.Ui_log_in.log_in_Button.clicked.connect(self.start_login)
		self.Ui_log_in.quit_Button.clicked.connect(self.close)
		self.Ui_network_show.label_quit.clicked.connect(self.back_to_log_in)


	def center(self):
		screen = QDesktopWidget().screenGeometry()  # 获取屏幕分辨率
		size = self.geometry()  # 获取窗口尺寸
		self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

	def set_init_Ui_log_in(self):
		self.setWindowTitle("SECURE and RELAX")
		self.resize(350, 425)
		self.setFixedSize(350, 425)
		self.QFrame1.resize(350, 425)
		self.QFrame1.setFixedSize(350, 425)
		self.center()

	def set_init_Ui_network_show(self):
		self.setWindowTitle("自动重连上网客户端")
		self.resize(420, 300)
		self.setFixedSize(420, 300)
		self.QFrame2.resize(420, 300)
		self.QFrame2.setFixedSize(420, 300)
		self.center()


	def Update_state_tip(self, is_connect):
		if is_connect:
			self.Ui_network_show.state_content.setText("在线")
		else:
			self.Ui_network_show.state_content.setText("离线")


	def start_login(self):
		account_number = self.Ui_log_in.account_number.text()
		password = self.Ui_log_in.password_number.text()

		#对连接界面进行初始化
		self.set_init_Ui_network_show()
		self.QFrame1.setVisible(False)
		self.QFrame2.setVisible(True)

		self.QFrame2.setLayout(self.Ui_network_show.main_layout)
		self.Ui_network_show.account_number.setText(account_number)
		self.Ui_network_show.state_content.setText("离线")
		#login的设置
		self.login.set_account_password(account_number, password)
		self.login.start()

	def back_to_log_in(self):
		self.login.stop()
		self.Ui_network_show.state_content.setText("离线")
		self.QFrame2.setVisible(False)
		self.QFrame1.setVisible(True)
		self.set_init_Ui_log_in()
		self.QFrame1.setLayout(self.Ui_log_in.main_layout)






if __name__ == '__main__':
	app = QApplication(sys.argv)
	ui_log = MainWindow()
	ui_log.show()
	sys.exit(app.exec_())




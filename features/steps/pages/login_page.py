from .base_page import BasePage
from .dashboard_page import DashBoardPage

class LoginPage(BasePage):

	@property
	def username(self):
		return self.by_id('user_login')

	@property
	def password(self): 
		return self.by_id('user_pass')

	@property
	def login_btn(self):
		return self.by_id('wp-submit')

	@property
	def error_message(self):
		return self.by_id('login_error').text.strip()

	def login(self, user_name, password):
		self.username.send_keys(user_name)
		self.password.send_keys(password)
		self.login_btn.click()

		return DashBoardPage(self.driver)

	def login_and_clear_username(self, username, password):
		self.username.clear()
		self.login(username, password)


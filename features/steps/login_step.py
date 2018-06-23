from behave import * 
import time
from selenium.webdriver.common.action_chains import ActionChains
from steps.pages.login_page import LoginPage


@given('go to login page')
def step_impl(context):
	context.login_page = LoginPage(context.dr)
	context.login_page.url = 'http://localhost/wp-login.php'
	context.login_page.navigate()


@when('login with {user_name} {password}')
def step_impl(context, user_name, password):
	context.dashboard_page = context.login_page.login(user_name, password)


@then('redirect to dashboard page')
def step_impl(context):
	assert 'wp-admin' in context.dr.current_url


@then('display hello {user_name}')
def step_impl(context, user_name):
	greeking_link = context.dashboard_page.greeking_link
	assert user_name in greeking_link.text


# failed
@when('let us login with incorrect {username} and incorrect {password}')
def step_impliment(context, username, password):
	if username == 'empty': username = ''
	if password == 'empty': password = ''
	context.dr.find_element_by_id('user_login').clear()
	context.dr.find_element_by_id('user_login').send_keys(username)
	context.dr.find_element_by_id('user_pass').clear()
	context.dr.find_element_by_id('user_pass').send_keys(password)
	context.dr.find_element_by_id('wp-submit').click()


@then('should display error {message}')
def step_impl(context, message):
	displayed_msg = context.dr.find_element_by_id('login_error').text.strip()
	assert displayed_msg == message


@when('create a post with title and content')
def step_impl(context):
	context.title = 'Post title %s' %(time.time())
	content = 'Post content %s' %(time.time())

	context.dr.get('http://localhost/wp-admin/post-new.php')
	context.dr.find_element_by_name('post_title').send_keys(context.title)
	js = "document.getElementById('content_ifr').contentWindow.document.body.innerHTML = '%s'" %(content)
	context.dr.execute_script(js)
	context.dr.find_element_by_name('publish').click()

	permalink_text = context.dr.find_element_by_id('sample-permalink').text
	context.post_id = permalink_text.split('=')[-1]


@then('the new created post should be existed')
def step_impl(context):
	context.dr.get('http://localhost/wp-admin/edit.php')
	assert context.dr.find_element_by_css_selector('.row-title').text == context.title


@when('delete the new created post')
def step_impl(context):                                                                
	context.dr.get('http://localhost/wp-admin/edit.php')
	context.row_id = 'post-' + context.post_id
	post_row = context.dr.find_element_by_id(context.row_id)
	ActionChains(context.dr).move_to_element(post_row).perform()
	time.sleep(1)
	post_row.find_element_by_css_selector('.submitdelete').click()


@then('the new created post should not exist')
def step_impl(context):                                                                
	try:
		context.dr.find_element_by_id(row_id)
	except:
		assert True
	else:
		assert False, 'Post is not deleted'
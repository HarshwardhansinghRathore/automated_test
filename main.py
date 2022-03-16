from selenium import webdriver
import time

class TestCase:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        self.driver.get('https://testing-assessment-foh15kew9-edvora.vercel.app/')
        self.username = 'User Name'
        self.password = 'Password'

    def register_user(self):
        register_button = self.driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/p[2]/button')
        register_button.click()
        time.sleep(1.5)
        username_field = self.driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/div[1]/div/input')
        username_field.send_keys(self.username)
        password_field = self.driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/div[2]/div/input')
        password_field.send_keys(self.password)
        create_account_button = self.driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/button')
        create_account_button.click()

    def login_user(self):
        self.driver.get('https://testing-assessment-foh15kew9-edvora.vercel.app/')
        time.sleep(1.5)
        login_username = self.driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/div[1]/div/input')
        login_username.send_keys(self.username)
        login_password = self.driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/div[2]/div/input')
        login_password.send_keys(self.password)
        login_button = self.driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/button')
        login_button.click()
        time.sleep(1)
    def redirect_user(self):
        self.driver.get('https://testing-assessment-foh15kew9-edvora.vercel.app/s')


bugs = 0
user = TestCase()

for _ in range(1):
    try:
        user.register_user()
        with open('report.txt', 'a') as f:
            f.write(f"""Test case number - TS001
Test case scenario - user able to register 
Test case title - user registration
Testcase code - 
    register_button = self.driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/p[2]/button')
    register_button.click()
    time.sleep(1.5)
    username_field = self.driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/div[1]/div/input')
    username_field.send_keys(self.username)
    password_field = self.driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/div[2]/div/input')
    password_field.send_keys(self.password)
    create_account_button = self.driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/button')
    create_account_button.click()\n\n""")
    except:
        with open('bug_report.txt', 'a') as f:
            bugs += 1
            f.write(f"""Test case number - TS001
Bug number-{bugs}
Bug title - User unable to register\n\n""")
        break

    try:
        user.login_user()
        with open('report.txt', 'a') as f:
            f.write(f"""Test case number - TS002
Test case scenario - user able to login 
Test case title - user login
Testcase code - 
def login_user(self):
    self.driver.get('https://testing-assessment-foh15kew9-edvora.vercel.app/')
    login_username = self.driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/div[1]/div/input')
    login_username.send_keys(self.username)
    login_password = self.driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/div[2]/div/input')
    login_password.send_keys(self.password)
    login_button = self.driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/button')
    login_button.click()\n\n""")
    except:
        with open('bug_report.txt', 'a') as f:
            bugs += 1
            f.write(f"""Test case number - TS002
Bug number-{bugs}
Bug title - User unable to login\n\n""")
        break

    try:
        user.redirect_user()
        with open('report.txt', 'a') as f:
            f.write(f"""Test case number - TS003
Test case scenario - able to redirect user to settings
Test case title - redirect user to settings
Testcase code - 
    def redirect_user(self):
        self.driver.get('https://testing-assessment-foh15kew9-edvora.vercel.app/s')\n\n""")
    except:
        with open('bug_report.txt', 'a') as f:
            bugs += 1
            f.write(f"""Test case number - TS003
                        Bug number-{bugs}
                        Bug title - User unable to redirect\n\n""")
        break

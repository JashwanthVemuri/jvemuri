import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()  # Update with the actual path to the Chrome driver
driver.maximize_window()

# Navigate to the webpage
driver.get("D:\SPM\Project\index.html")
time.sleep(1)
# Switch to the iframe by index (0 in this example)
iframe = driver.find_element("id", "log")  # Use "name" instead of "id" if it is a name attribute
driver.switch_to.frame(iframe)
time.sleep(3)
input_field = driver.find_element("id", "email")

# Click on the input field to focus on it
input_field.click()

# Enter the desired value into the input field
input_field.send_keys("pinadmin@gmail.com")

time.sleep(3)
input_field = driver.find_element("id", "password")

# Click on the input field to focus on it
input_field.click()

# Enter the desired value into the input field
input_field.send_keys("Admin@123")
time.sleep(3)
button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")

# Click on the button
button.click()

time.sleep(3)

alert = driver.switch_to.alert
alert.accept()
time.sleep(3)

feature_1_element = driver.find_element(By.XPATH, "//div[@class='section'][1]")
feature_1_element.click()
time.sleep(3)

pin = driver.find_element("id", "input")
pin.click()
pin.send_keys("520011")
button = driver.find_element("id", "sub")
button.click()
time.sleep(3)
home = driver.find_element(By.CSS_SELECTOR, "h5")
home.click()
time.sleep(3)

feature_2_element = driver.find_element(By.XPATH, "//div[@class='section'][2]")
feature_2_element.click()

pin1=driver.find_element("id", "start")
pin1.click()
pin1.send_keys("520011")

pin2=driver.find_element("id", "end")
pin2.click()
pin2.send_keys("3097")

calculate=driver.find_element("id", "calculate")
calculate.click()
time.sleep(5)
home = driver.find_element(By.CSS_SELECTOR, "h5")
home.click()
time.sleep(3)

feature_3_element = driver.find_element(By.XPATH, "//div[@class='section'][3]")
feature_3_element.click()

t1=driver.find_element("id","t1")
t1.click()
t1.send_keys("520011")

fin=driver.find_element("id","submit")
fin.click()
time.sleep(3)
home = driver.find_element(By.CSS_SELECTOR, "h5")
home.click()
time.sleep(3)

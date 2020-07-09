from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions   as EC 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.common.exceptions import TimeoutException

driver=webdriver.Chrome("C:/Users/faroo/Desktop/work/drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://www.newsgallery.com/")

assert "NewsGallery | People's Own Media" in driver.title 

driver.find_element_by_id("guest-login-button").click()
driver.find_element_by_id("id_username").send_keys("faheem")
driver.find_element_by_id("id_password").send_keys("faheem")
driver.find_element_by_id("login_button").click()
time.sleep(10)
elm=driver.find_element(By.XPATH,"//*[@id='myBoard']/div/div/div[1]/div/div[1]/a")
print(elm.is_displayed())

driver.implicitly_wait(20)
time.sleep(10)
driver.find_element(By.XPATH,"//*[@id='user-profile-pic']").click()
driver.implicitly_wait(20)

driver.find_element(By.XPATH,"//*[@id='header']/div/div/div[3]/div/div[3]/div/div/div/ul/li[2]/a").click()
driver.find_element(By.XPATH,"//*[@id='personalDetails']/div/h3/a").click()
time.sleep(20)
driver.find_element(By.ID,"id_dob").clear()
driver.find_element(By.ID,"id_dob").send_keys("04/01/1994")
driver.find_element(By.ID,"id_dob").click()
driver.find_element(By.XPATH,"//*[@id='personalDetails']/form/div/h3/a[1]").click()
driver.find_element(By.XPATH,"//*[@id='header']/div/div/div[1]/div/a/img").click()
time.sleep(10)
driver.find_element(By.XPATH,"//*[@id='user-profile-pic']").click()
driver.find_element(By.XPATH,"//*[@id='header']/div/div/div[3]/div/div[3]/div/div/div/ul/li[3]/a").click()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.find_element(By.XPATH,"//*[@id='facebookLink']/a/div/i").click()
#wait=WebDriverWait(driver,10)

# element=wait.until(EC.element_to_be_clickable((By.NAME,"pass")))
# element.send_keys("faheem")

time.sleep(10)
driver.close()
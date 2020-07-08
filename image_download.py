from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import zipfile,os
import time


def download_wait(path_to_downloads):
    seconds = 0
    dl_wait = True
    while dl_wait:
        time.sleep(1)
        dl_wait = False
        for fname in os.listdir(path_to_downloads):
            if fname.endswith('.crdownload'):
                dl_wait = True
        seconds += 1
    return seconds


current_dir = os.getcwd()
print(current_dir)
word=input("Enter Keyword: ")
if not os.path.exists(word):
	os.mkdir(word)

download_path = current_dir+'\\'+word
print(download_path)
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : download_path,"directory_upgrade": True}
chromeOptions.add_experimental_option("prefs",prefs)
#chromedriver = "chromedriver.exe"
#driver=webdriver.Chrome("C:/Users/faroo/Desktop/work/drivers/chromedriver.exe")
driver = webdriver.Chrome("C:/Users/faroo/Desktop/work/drivers/chromedriver.exe", chrome_options=chromeOptions)

# driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()

url="https://all-free-download.com/free-vector/"+word+".html"
driver.get(url)
for i in range(4, 10):
	driver.get(url)
	xPATH = '/html/body/div[1]/div/div/div[2]/div/div/div['+str(i)+']/a[1]/img'
	print(xPATH == "/html/body/div[1]/div/div/div[2]/div/div/div[4]/a[1]/img")
	timeout = 5
	try:
	    element_present = EC.presence_of_element_located((By.XPATH, xPATH))
	    WebDriverWait(driver, timeout).until(element_present)
	    driver.find_element(By.XPATH,xPATH).click()
	except TimeoutException:
		print ("Timed out waiting for page to load")
    	
	
	try:
	    element_present = EC.presence_of_element_located((By.ID,"downloadbt"))
	    WebDriverWait(driver, timeout).until(element_present)
	    driver.find_element(By.ID,"downloadbt").click()
	except TimeoutException:
		print ("Timed out waiting for page to load")
	
	print("sleeping")
	time.sleep(15)
	print("wake")
	

	# driver.execute_script("window.history.go(-1)")
	# time.sleep(1)
	# driver.execute_script("window.history.go(-1)")
	



print (download_wait(current_dir+'\\'+word))
for file in os.listdir(current_dir+'\\'+word):
	if file.endswith(".zip"):
		zip_file_path = current_dir+'\\'+word+"\\"+file
		print(zip_file_path,zip_file_path[:-4])
		with zipfile.ZipFile(zip_file_path,"r") as zip_ref:
			zip_ref.extractall(zip_file_path[:-4])



# imageXpathSelector='//*[@id="ires"]/table/tbody/tr[1]/td[1]/a/img'
# img=driver.find_element_by_xpath(imageXpathSelector)
# src=(img.get_attribute('src'))
# urllib.urlretrieve(src, word+".jpg")
# driver.close()
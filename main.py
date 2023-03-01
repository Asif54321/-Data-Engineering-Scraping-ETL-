import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

url = 'https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787'

driver = webdriver.Chrome(executable_path = "C:/Users/ASIF/Downloads/chromedriver_win32/chromedriver.exe")
# Load the page with JavaScript content
driver.get(url)
time.sleep(5)  # Wait for JavaScript to finish executing
html = driver.page_source


df = pd.read_html(html)

df_main = df[1]

df_main.to_csv('data.csv')

# Close the web driver
driver.quit()
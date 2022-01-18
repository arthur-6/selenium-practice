from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

PATH = 'C:\chromedriver.exe'
driver = webdriver.Chrome(PATH)

url = 'https://www.youtube.com/c/LEMMiNO/videos'

driver.get(url)

videos = driver.find_elements(By.CLASS_NAME, 'style-scope ytd-grid-video-renderer')

vid_list = []

for video in videos:
    title = video.find_element(By.XPATH, './/*[@id="video-title"]').text
    views = video.find_element(By.XPATH,'.//*[@id="metadata-line"]/span[1]').text
    date = video.find_element(By.XPATH,'.//*[@id="metadata-line"]/span[2]').text
    vid_item = {
        'title': title,
        'views': views,
        'date': date
    }
    vid_list.append(vid_item)

vid_dataframe = pd.DataFrame(vid_list)
print(vid_dataframe)

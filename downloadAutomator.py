from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


############ SELECT GM ####################
# player='Magnus+Carlsen'
# player='Fabiano+Caruana'
# player='Hans+Moke+Niemann'
# player='Hikaru+Nakamura'
# player='Wesley+So'
# player='Levon+Aronian'
# player='Anish+Giri'
# player='Ding+Liren'
# player='Ian+Nepomniachtchi'
# player='Alireza+Firouzja'
# player='Shakhriyar+Mamedyarov'
# player='Maxime+Vachier-Lagrave'
# player='Viswanathan+Anand'
# player='Richard+Rapport'
# player='Leinier+Dominguez+Perez'
player='Sergey+Karjakin'


max_pages = 50

############################################

#start chromium driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#implicit wait
driver.implicitly_wait(0.5)
#maximize browser
driver.maximize_window()
#launch URL
driver.get(f'https://www.chess.com/games/search?opening=&openingId=&p1={player}&p2=&sort=')

for page_number in range(0,max_pages):
    #find check all checkbox
    check_box =  driver.find_element(By.CLASS_NAME,'master-games-check-all')
    check_box.click()

    #find download button
    download_button =  driver.find_element(By.CLASS_NAME,'master-games-download-button')
    download_button.click()

    #find next page button and scroll down
    next_button =  driver.find_element(By.CLASS_NAME,'ui_pagination-item-component.pagination-next')
    next_button.location_once_scrolled_into_view
    next_button.click()

#close browser
driver.quit()
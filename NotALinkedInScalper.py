import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import warnings

warnings.filterwarnings('ignore')
 
def not_linkedin_scraper(webpage, page_number, pageend):
    next_page = webpage + str(page_number)
    driver = webdriver.Chrome()
    driver.get("https://linkedin.com/uas/login")

    # Automated method of logging in
    # username = driver.find_element(By.ID, "username")
    # username.sendkeys("<your email>")
    # pword = driver.find_element(By.ID, "password")
    # pword.sendkeys("<your password>")
    # driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    time.sleep(20)

    profile_url = next_page

    i = 1

    while(i <= pageend): 
           
        driver.get(profile_url)    

        start = time.time()
        
        initialScroll = 0
        finalScroll = 1000
        
        while True:
            driver.execute_script(f"window.scrollTo({initialScroll}, {finalScroll})")
            initialScroll = finalScroll
            finalScroll += 1000
        
            time.sleep(3)
        
            end = time.time()
        
            if round(end - start) > 1:
                break

        src = driver.page_source
        soup = BeautifulSoup(src, 'lxml')

        units = soup.find_all('div', {'class': 'entity-result__item'})

        print(units)

        for unit in units:

                unit_name = unit.find('div', class_='presence-entity')['alt']
                unit_company = unit.find('h4', class_='base-search-card__subtitle').text.strip()
                unit_location = unit.find('span', class_='job-search-card__location').text.strip()

                splitter1 = "https://www.linkedin.com/in/"
                splitter2 = "?"
                unit_link = unit.find('a', class_='app-aware-link')['href']

                try: 
                    unit_name = ''.join(unit_link.split(splitter1)[1].split(splitter2)[0])
                except: 
                    unit_name = "Name Fail"

                print(unit_name, unit_link)
        
        i=i+1
        profile_url = next_page = webpage + "&page=" + str(i)

# Do not uncomment this function
# I mean you could 
# But DON'TTTTTTTT
# not_linkedin_scraper('https://www.linkedin.com/search/results/people/?keywords=product%20manager%20singapore&origin=GLOBAL_SEARCH_HEADER', 1, 5)
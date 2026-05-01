from this import d
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from fake_useragent import UserAgent
import time

options = Options()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option(
    "prefs", {"profile.managed_default_content_settings.media_stream": 2}
)
options.add_argument("--start-maximized")
options.add_argument("--disable-infobars")
# options.add_argument('--disable-extensions')
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--window-size=1920,1200")
options.add_argument("--start-fullscreen")
options.add_argument("--mute-audio")
options.add_extension("./ublock.crx")
options.add_argument("--blink-settings=imagesEnabled=false")
options.add_argument("--disable-notifications")
options.add_argument("--disable-features=PreloadMediaEngagementData,MediaEngagementBypassAutoplayPolicies")
options.add_argument("--autoplay-policy=user-required")
ua = UserAgent()
user_agent = ua.random
options.add_argument(f"user-agent={user_agent}")

monpilote = webdriver.Chrome(options=options)
print("Chrome démarré")

monpilote.get("https://otakura.com/")

cartes = "one piece"

mazonecartes = monpilote.find_element(By.XPATH,'/html/body/div[2]/store-header/div/div/nav/div[2]/form/input[2]')

mazonecartes.send_keys(cartes)
mazonecartes.send_keys(Keys.ENTER)

listZoneArticle=WebDriverWait(monpilote,timeout=3).until(expected_conditions.presence_of_all_elements_located((By.XPATH,'//*[@id="facet-main"]/product-list/div/product-item[*]/div[2]/div/a',)))
b = []
b.append(["Article"])
for x in listZoneArticle:
    Article = x.text
    print(Article)
    if Article != "":
        r = [Article]
        b.append(r)

listZonePrix = WebDriverWait(monpilote, timeout=3).until(expected_conditions.presence_of_all_elements_located((By.XPATH,'//*[@id="facet-main"]/product-list/div/product-item[*]/div[2]/div/div/div',)))
a = []
a.append(["Prix"])
for x in listZonePrix:
    Prix = x.text
    print(Prix)
    if Prix != "":
        r = [Prix]
        a.append(r)


e = []
for i in range(len(b)):
    x = a[i][0]
    y = b[i][0]
    r = [y, x]
    e.append(r)

print(e)

import csv

fichier = open("card.csv", "w")
écrivain = csv.writer(fichier, delimiter=",")
écrivain.writerows(e)
fichier.close()
input("Presser une touche pour quitter...")
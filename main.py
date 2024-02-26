import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(by=By.ID, value="cookie")

def preprocess_value(value):
    value = ''.join(filter(lambda char: char.isdigit(), value))
    return value


def get_score():
    score = driver.find_element(By.ID, value="money").text
    return preprocess_value(score)

def get_timemashine():
    time_machine_cost_element = driver.find_element(By.XPATH, "/html/body/div[3]/div[5]/div/div[8]/b")
    timemashine = time_machine_cost_element.text.replace("Time machine - ", "")
    timemashine = timemashine.replace("Brings cookies from the past, before they were even eaten.", "")
    timemashine = timemashine.rstrip()
    timemashine = timemashine.replace(",", "")
    return preprocess_value(timemashine)

def get_portal():
    portal = driver.find_element(By.XPATH, "/html/body/div[3]/div[5]/div/div[7]/b").text
    portal = portal.replace("Portal - ", "")
    portal = portal.replace("Opens a door to the Cookieverse.", "")
    portal = portal.rstrip()
    portal = portal.replace(",", "")
    return preprocess_value(portal)

def get_alchemy():
    alchemy = driver.find_element(By.XPATH, "/html/body/div[3]/div[5]/div/div[6]/b").text
    alchemy = alchemy.replace("Alchemy lab - ", "")
    alchemy = alchemy.replace("Turns gold into cookies!", "")
    alchemy = alchemy.rstrip()
    alchemy = alchemy.replace(",", "")
    return preprocess_value(alchemy)

def get_shipment():
    shipment = driver.find_element(By.XPATH, "/html/body/div[3]/div[5]/div/div[5]/b").text
    shipment = shipment.replace("Shipment - ", "")
    shipment = shipment.replace("Brings in fresh cookies from the cookie planet.", "")
    shipment = shipment.rstrip()
    shipment = shipment.replace(",", "")
    return preprocess_value(shipment)

def get_mine():
    mine = driver.find_element(By.XPATH, "/html/body/div[3]/div[5]/div/div[4]/b").text
    mine = mine.replace("Mine - ", "")
    mine = mine.replace("Mines out cookie dough and chocolate chips.", "")
    mine = mine.rstrip()
    mine = mine.replace(",", "")
    return preprocess_value(mine)

def get_Factory():
    Factory = driver.find_element(By.XPATH, "/html/body/div[3]/div[5]/div/div[3]/b").text
    Factory = Factory.replace("Factory - ", "")
    Factory = Factory.replace("Produces large quantities of cookies.", "")
    Factory = Factory.rstrip()
    return preprocess_value(Factory)

def get_Grandma():
    Grandma = driver.find_element(By.XPATH, "/html/body/div[3]/div[5]/div/div[2]/b").text
    Grandma = Grandma.replace("Grandma - ", "")
    Grandma = Grandma.replace("A nice grandma to bake more cookies.", "")
    Grandma = Grandma.rstrip()
    return preprocess_value(Grandma)

def get_Cursor():
    Cursor = driver.find_element(By.XPATH, "/html/body/div[3]/div[5]/div/div[1]/b").text
    Cursor = Cursor.replace("Cursor - ", "")
    Cursor = Cursor.replace("Autoclicks every 5 seconds.", "")
    Cursor = Cursor.rstrip()
    return preprocess_value(Cursor)


x = 0

while True:

    if x > 15:
        score = get_score()
        timemashine = get_timemashine()
        portal = get_portal()
        alchemy = get_alchemy()
        shipment = get_shipment()
        mine = get_mine()
        factory = get_Factory()
        grandma = get_Grandma()
        cursor = get_Cursor()

        updates = {"buyTime machine": timemashine,
               "buyPortal": portal,
               "buyAlchemy lab": alchemy,
               "buyShipment": shipment,
               "buyMine": mine,
               "buyFactory": factory,
               "buyGrandma": grandma,
               "buyCursor": cursor
               }
        for item, cost in updates.items():
            if int(score) >= int(cost):
                driver.find_element(By.ID, item).click()
        print(updates)
        x = 0
        time.sleep(1)
    else:
        x = 1 + x
        print(x)


    cookie.click()

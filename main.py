from re import I
from pip import main
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path="chromedriver.exe")
lien = ("https://www.jeuxvideo.com/forums/0-51-0-1-0-1-0-blabla-18-25-ans.htm")


def main(lien, username, password, subject, message, execution_count):
    infiny_loop = False
    
    if execution_count == 0:
        infiny_loop = True
        
    
    driver.get(lien)

    AcceptFreeVersion()

    login(username, password)
    
    while execution_count > 0 or infiny_loop == True:
        
        listname = takename()
        
        sendmp(listname, subject, message)
        
        mainpage()
        
        execution_count -= 1
    
    


def AcceptFreeVersion():
    btn = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div/div/div/div[2]/div/span/div/button[2]")
    btn.click()

def login(username, password):
    btn = driver.find_element(by=By.CLASS_NAME, value="icon-account")
    btn.click()
    
    username_box = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div/div[2]/form/div[1]/input")
    password_box = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div/div[2]/form/div[2]/input")
    connect_btn = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div/div[2]/form/div[4]/button")
    
    
    username_box.send_keys(username)
    password_box.send_keys(password)
    connect_btn.click()
    #faire le capchat !
    #do the capchat !
    while driver.current_url != "https://www.jeuxvideo.com/forums/0-51-0-1-0-1-0-blabla-18-25-ans.htm":
        time.sleep(0.1)
    
def takename():
    listname = []
    character = 63
    
    
    while character <= 524:
        for i in range(2,27):
            if character >= 524:
                break
            else:
                if i == 12:
                    pass
                else:
                    x = driver.find_element(by=By.XPATH, value=f"/html/body/div[3]/div[4]/div[2]/div[3]/ul/li[{i}]/a").text
                    character += len(x)
                    character += 1
                    listname.append(x)
                    
        next = driver.find_element(by=By.CLASS_NAME, value="pagi-suivant-actif")
        next.click()
    
    while character > 524:
        character -= len(listname[0])
        del listname [0]
    #if link length => 524 characters = error 403
    
    

    if "alone8y" in listname:
        listname.remove("alone8y")
    
    return listname
        
        
    
    
def sendmp(listname, subject, message):
    
    listname =";".join(listname)
    #if link length => 524 characters = error 403
    link = (f"https://www.jeuxvideo.com/messages-prives/nouveau.php?all_dest={listname}")
    
    driver.get(link)
    
    subject_box = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div/div[2]/div/form/div[4]/input")
    message_box = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div/div[2]/div/form/div[5]/div[1]/div[1]/div[2]/textarea")
    send_btn = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div/div[2]/div/form/div[5]/button")
    
    subject_box.send_keys(subject)
    message_box.send_keys(message)
    send_btn.click()
    while driver.current_url.startswith("https://www.jeuxvideo.com/messages-prives/message.php?id") == False:
        time.sleep(1)
        try: send_btn.click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            print("erreur selenium")
        except selenium.common.exceptions.StaleElementReferenceException:
            print('cet enculé trouve pas')
        
        
def mainpage():
    while driver.current_url.startswith("https://www.jeuxvideo.com/messages-prives/message.php?id") == False:
        time.sleep(0.5)
    driver.get("https://www.jeuxvideo.com/forums/0-51-0-1-0-1-0-blabla-18-25-ans.htm")
            
        
        
        
      
        
    
    
    

main(lien,"interstelard","El31012004", "salut khey !", "Serveur discord venant tout droit du forum 18-25\nNous venons vous apporter :\n-une expérience démocratique\n-une bonne ambiance\n-une modération souple\net surtout la liberté d'expression **TOTALE**\net on donne le script du bot à 300 membres ! \nhttps://discord.gg/rFWUSWjwxp\nhttps://discord.gg/rFWUSWjwxp\nhttps://discord.gg/rFWUSWjwxp\n ps : je suis pas un bot :hap:", 0)
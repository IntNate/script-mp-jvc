
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="chromedriver.exe")

#choisi le forum où tu veux selectioner les gens que tu vas mp, par défaut c'est le blabla 18-25
lien = ("https://www.jeuxvideo.com/forums/0-51-0-1-0-1-0-blabla-18-25-ans.htm")

#ici tu rentres ton pseudo
pseudo = ""

#ici ton mot de passe, si tu n'as pas confiance tu peux laisser les champs vides, 
# faudra juste te connecter à la main => ça devrait te rediriger sur le forum que tu as remplis plus haut
#si ça ne le fait pas rends-y manuellement et laisse la magie opérer 
mot_de_passe = ""

#ici c'est le sujet du message, le truc qu'ils vont voir en tant que notif
sujet = "Oui c'est pour discord"

#ici c'est le messages. /!\ pour revenir à la ligne du dois utiliser "\n" ne reviens pas à la ligne ici /!\
#petit exemple
message = "serveur démocratique avec une bonne ambiance\nhttps://discord.gg/rFWUSWjwxp"

#ici tu choisis combien de fois tu veux faire le script
#si tu laisses 0 il tournera à l'infini
#/!\ici ne met pas le chiffre en guillemet/!\

nombre_executions = 0


def main(lien, username, password, subject, message, ):
    
    
    driver.get(lien)

    AcceptFreeVersion()
    login(username, password)
    running = True
    while running:
        

        
        
        
            
        listname = takename()
            
        sendmp(listname, subject, message)
            
        listname = []
    
    


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
    listnamevar = []
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
                    listnamevar.append(x)
                    
        next = driver.find_element(by=By.CLASS_NAME, value="pagi-suivant-actif")
        try:
            next.click()
        except AttributeError():
            pass
        
    
    while character > 524:
        character -= len(listnamevar[0])
        del listnamevar [0]
    #if link length => 524 characters = error 403
    

    return listnamevar
        
        
    
    
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
    while driver.current_url.startswith("https://www.jeuxvideo.com/messages-prives/nouveau.php"):
        time.sleep(1)
        try: 
            send_btn2 = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[2]/div/div[2]/div/form/div[5]/button')
            send_btn2.click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            pass
        except selenium.common.exceptions.StaleElementReferenceException:
            pass
        except:
            pass
    
    driver.get("https://www.jeuxvideo.com/forums/0-51-0-1-0-1-0-blabla-18-25-ans.htm")
    
    
        
        
def mainpage(driver):
    
    time.sleep(1)
    driver.get("https://www.jeuxvideo.com/forums/0-51-0-1-0-1-0-blabla-18-25-ans.htm")
        
    

            
        
        
        
      
        
    
    
    

main(lien, pseudo, mot_de_passe, sujet, message)
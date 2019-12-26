import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


def readAccount():
    global emailS
    global passS
    global userS
    
    with open('logon.csv', newline="") as csvfile:
        readerF = csv.reader(csvfile)
        i = 0
        for row in readerF:
            if i == 0:
                emailS = row[0]
            if i == 1:
                passS = row[0]
            if i == 2:
                userS = row[0]
                
            i += 1

    print(emailS)
    print(passS)
    print(userS)
    print()


class WebFace:
    def __init__(self):
    
        print("initialisation!")
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.messenger.com/t/" + userS)

        assert "Messenger" in self.driver.title

        wait = WebDriverWait(self.driver, 10)

        email = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='email']")))
        email.clear()
        email.send_keys(emailS)

        passw = self.driver.find_element_by_xpath("//input[@name='pass']")
        passw.clear()
        passw.send_keys(passS)

        passw.send_keys(Keys.RETURN)

        entryLD = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@role='combobox']")))
        msgLD = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='_3058 _ui9 _hh7 _6ybn _s1- _52mr _3oh-']")))
    
        self.plen = 0
        self.clen = 0
    
    def GetMsg(self):    
        
        cdriver = self.driver
        
        msgls = cdriver.find_elements_by_xpath("//div[@class='_3058 _ui9 _hh7 _6ybn _s1- _52mr _3oh-']/div[@class='_aok _7i2m']")

        self.clen = len(msgls)
        
        if self.plen < self.clen:
            self.plen = self.clen

            return(msgls[self.clen-1].get_attribute('aria-label'))

        return(None)

    def Close(self):
        self.driver.close()
        
    def Send(self, msg):
        cdriver = self.driver
        
        if msg == None:
            return
            
        messageBox = cdriver.find_element_by_xpath("//div[@role='combobox']")
        messageBox.send_keys(" ")
        messageBox.send_keys(msg)
        messageBox.send_keys(Keys.RETURN)
        messageBox.clear() 

class Tracker:
# * = repeat with N

#have duck
# state   rcve           send
# 0       -              tduck 
# 1*      what           what
# 2       what           aduck
# 3*      aduck          aduck
# 4*      what           what
# 5       what           aduck
# 6*      aduck          aduck
# 7*      quack          quack
# 8       quack          yes
# 9*      yes            yes
# 10*     ahhh           -

#no duck
# state   rcve           send
# 0       tduck          what 
# 1*      what           what
# 2       what           aduck
# 3*      aduck          aduck
# 4       aduck          what
# 5*      what           what
# 6       what           aduck
# 7*      aduck          aduck
# 8       aduck          quack
# 9*      quack          quack
# 10      quack          yes
# 11*     yes            yes
# 12      yes            ahh


    def __init__(self):
        self.N = 0
        self.Ni = 0
        self.state = 0
        self.hasDuck = True
        self.nextDuck = False
    
    def nextRound(self):        
        self.nextDuck = False
        return "startduck"
        
    def hasDuckReply(self, msg):
        
        rmsg = "huh"
        
        if self.state == 0:
            if msg == "startduck":
                rmsg = "this is a duck"
                self.Ni = -1
                
        if self.state == 1:
            if msg == "a what":
                rmsg = "a what"
                self.Ni += -1
                
        if self.state == 2:
            if msg == "a what":
                rmsg = "a duck"
                self.Ni = -1
    
        if self.state == 3:
            if msg == "a duck":
                rmsg = "a duck"
                self.Ni += -1
    
        if self.state == 4:
            if msg == "a what":
                rmsg = "a what"
                self.Ni += -1
        
        if self.state == 5:
            if msg == "a what":
                rmsg = "a duck"
                self.Ni = -1
                
        if self.state == 6:
            if msg == "a duck":
                rmsg = "a duck"
                self.Ni += -1
    
        if self.state == 7:
            if msg == "does it quack":
                rmsg = "does it quack"
                self.Ni += -1
        
        if self.state == 8:
            if msg == "does it quack":
                rmsg = "yes it quacks"
                self.Ni = -1
    
        if self.state == 9:
            if msg == "yes it quacks":
                rmsg = "yes it quacks"
                self.Ni += -1
                
        if self.state == 10:
            if msg == "ahh":
                rmsg = ""
                self.Ni = -1
        
        return rmsg
    
    def noDuckReply(self, msg):
        
        rmsg = "huh"
        
        if self.state == 0:
            if msg == "this is a duck":
                rmsg = "a what"
                self.Ni = -1
                
        if self.state == 1:
            if msg == "a what":
                rmsg = "a what"
                self.Ni += -1
                
        if self.state == 2:
            if msg == "a what":
                rmsg = "a duck"
                self.Ni = -1
    
        if self.state == 3:
            if msg == "a duck":
                rmsg = "a duck"
                self.Ni += -1
    
        if self.state == 4:
            if msg == "a duck":
                rmsg = "a what"
                self.Ni = -1
        
        if self.state == 5:
            if msg == "a what":
                rmsg = "a what"
                self.Ni += -1
                
        if self.state == 6:
            if msg == "a what":
                rmsg = "a duck"
                self.Ni = -1
    
        if self.state == 7:
            if msg == "a duck":
                rmsg = "a duck"
                self.Ni += -1
        
        if self.state == 8:
            if msg == "a duck":
                rmsg = "does it quack"
                self.Ni = -1
    
        if self.state == 9:
            if msg == "does it quack":
                rmsg = "does it quack"
                self.Ni += -1
                
        if self.state == 10:
            if msg == "does it quack":
                rmsg = "yes it quacks"
                self.Ni = -1
        
        if self.state == 11:
            if msg == "yes it quacks":
                rmsg = "yes it quacks"
                self.Ni += -1
                
        if self.state == 12:
            if msg == "yes it quacks":
                rmsg = "ahh"
                self.Ni = -1
        
        return rmsg
    
    def stateNext(self):
        stateCh = self.state
        
        if self.Ni == -1:
            if self.hasDuck == True:
                self.state += 1
                if self.state == 11:
                    self.state = 0
                    self.hasDuck = False
            elif self.hasDuck == False:
                self.state += 1
                if self.state == 13:
                    self.state = 0
                    self.hasDuck = True
                    self.N += 1
                    self.nextDuck = True
        
        if self.N == 0:
            if self.hasDuck == True:
                if self.state in [1]:
                    self.state = 2
                if self.state in [3,4]:
                    self.state = 5
                if self.state in [6,7]:
                    self.state = 8
                if self.state in [9]:
                    self.state = 10     
         
            if self.hasDuck == False:
                if self.state in [1]:
                    self.state = 2
                if self.state in [3]:
                    self.state = 4
                if self.state in [5]:
                    self.state = 6
                if self.state in [7]:
                    self.state = 8
                if self.state in [9]:
                    self.state = 10
                if self.state in [11]:
                    self.state = 12
                    
        elif self.Ni == 0:
            if self.hasDuck == True:
                self.state += 1
            if self.hasDuck == False:
                self.state += 1
            
        if self.state != stateCh:
            self.Ni = self.N

    def reply(self, msgR):
        msg = msgR.lower()
        
        print("Input: " + str(msg))
        print("Has Duck: " + str(self.hasDuck))
        print("State: " + str(self.state))
        print("N: " + str(self.N))
        print("Ni: " + str(self.Ni))
        print()
        
        if self.hasDuck == True:
            rmsg = self.hasDuckReply(msg)
        
        if self.hasDuck == False:
            rmsg = self.noDuckReply(msg)
            
        self.stateNext()
    
        

    
        return rmsg,self.nextDuck

readAccount()

ListMsg = WebFace() 
Duck = Tracker()

rply = None
autoDuck = True

while True:  
       
    msg = ListMsg.GetMsg()
    try:
        msg = msg.lower()
    except AttributeError:
        pass
        
    if autoDuck == True:
        msg = Duck.nextRound()
        autoDuck = False
 
    if msg != None:
    
        rply, autoDuck = Duck.reply(msg) 
        
        if rply != None:
            ListMsg.Send(rply)
        
    time.sleep(.1)
 

                    
# for i in range (10):
    # messageBox.send_keys(" ")
    # messageBox.send_keys("a who?")
    # messageBox.send_keys(Keys.RETURN)
    # messageBox.clear()

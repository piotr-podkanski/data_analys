# Impotrtera moduler
# Codecs används föt att kunna öpna och koda CSV filen med svenska bokstäver
import csv
import os 
import pandas as pd
import numpy as np
import codecs

# Sätter en specifik seed för att kunna jobba med samma slumpade värden varje gång
# Kan komenteras ut
np.random.seed(1) 

# Deklarera variablet random som funktionen för att göra det snygarre 
random = np.random.randint

# En funktion som genererar vilket kön "deltageren" har och direkt returnera det
def generate_sex(): 
# Slumpar mellan 0 och 1 för att göra hälften av participanterna män och hälften kvinorna
    if random(2) == 1:
        return "Man"    
    else:
        return  "kvinna"
    
# En funktion som genererar hur gammal man är
def generate_age():
    
    # Skapar värde mellan 16 och 80(år) 64år
    #16 - 20, 10%
    #21 - 30, 28%
    #31 - 40, 26%
    #41 - 50, 21%
    #51 - 60, 8%
    #61 - 70, 5%
    #71- 80, 2%
    
    age = random(16,80) + 1
    
    # För att få värden se meer naturliga ut så minskar jag värden lite slumpmessigt så att värde 70 fram kommer mer sällan än värde 20
    if age > 70:
        #eftersom att det skulle vara väldigt få personer 1/3 av alla värden som är 70+ ska minskas med 1-20 år resten ska minskas med 20-40
        if random(3) == 1:
            age -= random(21)
        else:
            age -= random(21,41)
            
    # Minskning för 60 år          
    elif age > 60:
        if random(3) == 1:
            age -= random(16)
        else:
            age -= random(21,31)
            
    # Minskning för 50 år           
    elif age > 50:
        age -= random(16) 
        
    # Minsknign för 40 år   
    elif age > 40:
        age -= random(21)
        
    # Minskning för 30 år
    elif age > 30:
        age -= random(17)

    # Returnera värdet
    return age
    
# En funktion som genererar vilken krops typ man har
def generare_body():
    # Väljer 1 siffra mellan 0 och 3
    type_number = random(4) + 1
    
    # Chansen för varje ciffra är 25% medelsnitt (100%/4 = 25%)
    if type_number == 1:
        if random(2) == 1:
            return "Athletic" # 1/2 av 25% = 12.5% 
        else:
            return "Healthy" # 1/2 av 25% = 12.5% 
        
    # 25% medelsnit
    elif type_number == 2:
        if random(5) <= 1:
            return "Healthy" # 2/5 av 25% = 10%
        else: 
            return "Average" # 3/5 av 25% = 15%
        
    # 25% medelsnit
    elif type_number == 3:
        if random(8) <= 6:
            return "Average" # 7/8 av 25% = 21.875% 
        else:
            return "unhealthy" # 1/8 av 25% = 3.125%
    
    # 25% medelsnit
    else:
        return "Unhealthy" #25% 
    
    # Resultatet blir #Athletic = 12.5%. Healthy = 22.5%. Average = 36.875. Unhealthy = 28.125%.
   
# En funktion som generear hur många timmar i veckan man tränar
def generate_time(age,body):
  #Timmar ska  vara max 21timmar minst 0 timmar i veckan 
    chance = random(1000)+1
  
#Athletic ska ha generelt mellan 
  #0 - 2 - 2.5%
  #3 - 6 - 7.5%
  #11 - 14 - 20% 
  #15 - 18 - 15%
  #19 - 21 - 5%
    if "At" in body:
        if age > 0 and age <= 25:
            if chance <= 150: #150/1000 = 15%
                return random(3)
            
            elif chance <= 250: #100/1000 = 10%
                return random(3, 7)
            
            elif chance <= 650:#400/1000 = 40%
                return random(7,11)
            
            elif chance <= 800:#150/1000 = 15%
                return random(11,15)
            
            elif chance <= 950: #150/1000 = 15%
                return random(15,19)
            
            else: #50/1000 = 5%
                return random(19,22)
        
        elif age >25 and age <=40:
            if chance <= 225: #22.5/1000 = 22.5%
                return random(3)
            
            elif chance <= 475: #250/1000 = 25%
                return random(3, 7)
            
            elif chance <= 650:#175/1000 = 17.5%
                return random(7,11)
            
            elif chance <= 800:#150/1000 = 15%
                return random(11,15)
            
            elif chance <= 925: #125/1000 = 12.5%
                return random(15,19)
            
            else: #75/1000 = 7.5%
                return random(19,22)
            
        elif age >40 and age <50:
            if chance <= 100: #100/1000 = 10%
                return random(3)
            
            elif chance <= 300: #200/1000 = 20%
                return random(3, 7)
            
            elif chance <= 525:#225/1000 = 22.5%
                return random(7,11)
            
            elif chance <= 750:#225/1000 = 22.5%
                return random(11,15)
            
            elif chance <= 900: #150/1000 = 15%
                return random(15,19)
            
            else: #100/1000 = 10%
                return random(19,22)
            
                
        else: #50+
            pass
      
#helthy
  #0 - 2 - 10%
  #3 - 6 - 20%
  #7 - 10 - 50%
  #11 - 14 - 25% 
  #15 - 18 - 3%
  #18 - 21 2%
    if "He" in body:
        pass
      
#average
  #0 - 2 - 70%
  #3 - 6 - 24%
  #7 - 10 - 5%
  #11 - 14 - 0.5% 
  #15 - 18 - 0.3%
  #18 - 21 - 0.2% 
  
    if "Av" in body:
        pass
#Unhealthy
  #0 - 89%
  #1 - 2 - 5%
  #3 - 6 - 2.5%
  #7 - 10 - 2%
  #11 - 14 - 1% 
  #15 - 18 - 0.4%
  #18 - 21  0.1%
    if "Un" in body:
        pass
# En funktion som bestämmer vilken diet personen har 
    pass

#en  funktion för ens diet 
def generate_diet(age, body):
    diet = random(20) + 1  
    if age > 0 and age <= 25: 
        if body == "Athletic":
            if diet <= 8: # 8/20 == 40%
                return "Cc"
            
            elif diet <= 15: #7/20 == 35%
                return "H"
            
            elif diet <= 18:# 3/20 == 15%
                return "Np"          
            
            else: # 2/20 == 10%
                return "Nc"
                      
        if body == "Healthy":
            if diet <= 7: # 7/20 = 35%
                return "H"
            
            elif diet <= 13: # 6/20 = 30%
                return 'Cc'
            
            elif diet <= 17:# 4/20 = 20%
                return "np"
            
            else: # 3/20 = 15%
                return "Wl"
        
        if body == "Average":
            if diet <= 10: # 10/20 = 50%
                return "Np"
            
            elif diet <= 13: # 3/20 = 15%
                return "H"
            
            elif diet <= 18:# 5/20 = 25%
                return "Nc"
            
            else: # 2/20 = 10%
                return "Ff"
            
        if body == "Unhealthy":
            if diet <= 6: #6/20 = 30%
                return "Nc"
            
            elif diet <= 13: #7/20 = 35%
                return "Ff"
            
            elif diet <= 17: #4/20 = 20%
                return "Cc"
            
            elif diet <= 19: # 2/20 = 10%
                return "np"
            
            else: # 1/20 = 5%
                return "wl"
                       
    elif age > 25 and age <= 35:
        if body == "Athletic":
            if diet <= 8: # 8/20 == 40%
                return "Cc"
            
            elif diet <= 17: #9/20 == 45%
                return "H"
            
            elif diet <= 19:# 2/20 == 10%
                return "Np"          
            
            else: # 1/20 == 5%
                return "Nc"
        
        if body == "Healthy":
            if diet <= 11: # 11/20 = 55%
                return "H"
            
            elif diet <= 15: # 4/20 = 20%
                return 'Cc'
            
            elif diet <= 18:# 3/20 = 15%
                return "np"
            
            else: # 2/20 = 10%
                return "Wl"
               
        if body == "Average":
            if diet <= 12: # 12/20 = 60%
                return "Np"
            
            elif diet <= 16: # 4/20 = 20%
                return "H"
            
            elif diet <= 19:# 3/20 = 15%
                return "Nc"
            
            else: # 1/20 = 5%
                return "Ff"
            
        if body == "Unhealthy":
            if diet <= 6: #6/20 = 30%
                return "Nc"
            
            elif diet <= 10: #4/20 = 20%
                return "Ff"
            
            elif diet <= 14: #4/20 = 20%
                return "Cc"
            
            elif diet <= 17: # 3/20 = 15%
                return "np"
            
            else: # 3/20 = 15%
                return "wl"
              
    elif age > 35 and age <= 50:
        if body == "Athletic":
            if diet <= 6: # 6/20 == 30% 
                return "Cc"
            
            elif diet <= 18: #12/20 == 60%
                return "H"
            
            elif diet <= 19:# 1/20 == 5%
                return "Np"          
            
            else: # 1/20 == 5%
                return "Nc"
        
        if body == "Healthy":
            if diet <= 8: # 8/20 = 40%
                return "H"
            
            elif diet <= 12: # 4/20 = 20%
                return 'Cc'
            
            elif diet <= 16:# 4/20 = 20%
                return "np"
            
            else: # 4/20 = 20%
                return "Wl"
               
        if body == "Average":
            if diet <= 9: # 9/20 = 45%
                return "Np"
            
            elif diet <= 14: # 5/20 = 25%
                return "H"
            
            elif diet <= 18:# 4/20 = 20%
                return "Nc"
            
            else: # 2/20 = 10%
                return "Ff"
            
        if body == "Unhealthy":
            if diet <= 4: #4/20 = 20%
                return "Nc"
            
            elif diet <= 9: #5/20 = 25%
                return "Ff"
            
            elif diet <= 12: #3/20 = 15%
                return "Cc"
            
            elif diet <= 17: # 5/20 = 35%
                return "np"
            
            else: # 3/20 = 15%
                return "wl"
        
    elif age > 50:
        if body == "Athletic":
            if diet <= 2: # 2/20 == 10% 
                return "Cc"
            
            elif diet <= 12: #10/20 == 50%
                return "H"
            
            elif diet <= 17:# 5/20 == 25%
                return "Np"          
            
            else: # 3/20 == 15%
                return "Nc"
        
        if body == "Healthy":
            if diet <= 6: # 6/20 = 30%
                return "H"
            
            elif diet <= 9: # 3/20 = 15%
                return 'Cc'
            
            elif diet <= 13:# 4/20 = 20%
                return "np"
            
            else: # 7/20 = 35%
                return "Wl"
               
        if body == "Average":
            if diet <= 7: # 7/20 = 35%
                return "Np"
            
            elif diet <= 14: # 7/20 = 35%
                return "H"
            
            elif diet <= 18:# 4/20 = 25%
                return "Nc"
            
            else: # 1/20 = 5%
                return "Ff"
            
        if body == "Unhealthy":
            if diet <= 3: #3/20 = 15%
                return "Nc"
            
            elif diet <= 6: #3/20 = 15%
                return "Ff"
            
            elif diet <= 10: #4/20 = 20%
                return "Cc"
            
            elif diet <= 15: # 5/20 = 25%
                return "np"
            
            else: # 5/20 = 25%
                return "wl"
               
# En funktion för vikt för en peroson
def generate_weight(body,diet):
    weight = random(45,140)
    return weight


# Letar efter en fil och om den inte fins skapa och skriv
# Codecs används för att koda CSV med "åäö"
with codecs.open(os.path.join("data_analys","data_samling.csv"), encoding="utf-8",mode="w+") as file1:
    writer = csv.writer(file1)
    # Definerar första raden
    writer.writerow(["kön", " lder", " vikt", " timar per vecka", " krops-typ", " diet"])   
    
    # Börjar generera värden för CSV
    for i in range(1000000):
        
        # Dessa värden genereras av dessa funktioner 
        sex = generate_sex()
        age = generate_age()
        body = generare_body()
        time = generate_time(age, body)
        diet = generate_diet(age, body)
        #weight = generate_weight()
        print(i)

        # Skriver ner dassa värden
        writer.writerow([sex, age, None, None, body, diet])
  


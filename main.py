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
    
    age = random(16, 80) + 1
    
    # För att få värden se meer naturliga ut så minskar jag värden lite slumpmessigt så att värde 70 fram kommer mer sällan än värde 20
    if age > 70:
        #eftersom att det skulle vara väldigt få personer 1/3 av alla värden som är 70+ ska minskas med 1-20 år resten ska minskas med 20-40
        if random(3) == 1:
            age -= random(21)
        else:
            age -= random(21, 41)
            
    # Minskning för 60 år          
    elif age > 60:
        if random(3) == 1:
            age -= random(16)
        else:
            age -= random(21, 31)
            
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
def generate_time(age, body):
  #Timmar ska  vara max 21timmar minst 0 timmar i veckan 
    chance = random(1000)+1
    
    if body == "Athletic":
        if age > 0 and age <= 25:
            if chance <= 150: #150/1000 = 15%
                return random(3)
            
            elif chance <= 250: #100/1000 = 10%
                return random(3, 7)
            
            elif chance <= 650:#400/1000 = 40%
                return random(7, 11)
            
            elif chance <= 800:#150/1000 = 15%
                return random(11, 15)
            
            elif chance <= 950: #150/1000 = 15%
                return random(15, 19)
            
            else: #50/1000 = 5%
                return random(19, 22)
        
        elif age >25 and age <=40:
            if chance <= 225: #22.5/1000 = 22.5%
                return random(3)
            
            elif chance <= 475: #250/1000 = 25%
                return random(3, 7)
            
            elif chance <= 650:#175/1000 = 17.5%
                return random(7, 11)
            
            elif chance <= 800:#150/1000 = 15%
                return random(11, 15)
            
            elif chance <= 925: #125/1000 = 12.5%
                return random(15, 19)
            
            else: #75/1000 = 7.5%
                return random(19, 22)
            
        elif age >40 and age <=50:
            if chance <= 100: #100/1000 = 10%
                return random(3)
            
            elif chance <= 300: #200/1000 = 20%
                return random(3, 7)
            
            elif chance <= 525:#225/1000 = 22.5%
                return random(7, 11)
            
            elif chance <= 750:#225/1000 = 22.5%
                return random(11, 15)
            
            elif chance <= 900: #150/1000 = 15%
                return random(15, 19)
            
            else: #100/1000 = 10%
                return random(19, 22)
                      
        else: #50+
            if chance <= 200: #200/1000 = 20%
                return random(3)
            
            elif chance <= 300: #100/1000 = 10%
                return random(3, 7)
            
            elif chance <= 635:#335/1000 = 33.5%
                return random(7, 11)
            
            elif chance <= 8:#225/1000 = 22.5%
                return random(11, 15)
            
            elif chance <= 960: #100/1000 = 10%
                return random(15, 19)
            
            else: #40/1000 = 4%
                return random(19, 22)
      
    if body == "Healthy":
        if age > 0 and age <= 25:
            if chance <= 100: #100/1000 = 10%
                return random(3)
            
            elif chance <= 300: #200/1000 = 20%
                return random(3, 7)
            
            elif chance <= 700:#400/1000 = 40%
                return random(7, 11)
            
            elif chance <= 950:#250/1000 = 25%
                return random(11, 15)
            
            elif chance <= 980: #30/1000 = 3%
                return random(15, 19)
            
            else: #20/1000 = 2%
                return random(19, 22)
        
        elif age >25 and age <=40:
            if chance <= 175: #200/1000 = 17.5%
                return random(3)
            
            elif chance <= 350: #200/1000 = 17.5%
                return random(3, 7)
            
            elif chance <= 700:#400/1000 = 35%
                return random(7, 11)
            
            elif chance <= 950:#250/1000 = 25%
                return random(11, 15)
            
            elif chance <= 980: #30/1000 = 3%
                return random(15, 19)
            
            else: #20/1000 = 2%
                return random(19, 22)
            
        elif age >40 and age <=50:
            if chance <= 100: #100/1000 = 20%
                return random(3)
            
            elif chance <= 300: #200/1000 = 20%
                return random(3, 7)
            
            elif chance <= 525:#225/1000 = 20%
                return random(7, 11)
            
            elif chance <= 750:#225/1000 = 30%
                return random(11, 15)
            
            elif chance <= 900: #150/1000 = 5%
                return random(15, 19)
            
            else: #100/1000 = 5%
                return random(19, 22)
                      
        else: #50+
            if chance <= 400: #400/1000 = 40%
                return random(3)
            
            elif chance <= 500: #100/1000 = 10%
                return random(3, 7)
            
            elif chance <= 700:#200/1000 = 20%
                return random(7, 11)
            
            elif chance <= 850:#150/1000 = 15%
                return random(11, 15)
            
            elif chance <= 992: #142/1000 = 14.2%
                return random(15, 19)
            
            else: #8/1000 = 0.8%
                return random(19, 22)
            
    if body == "Average":
        if age > 0 and age <= 25:
            if chance <= 700: #700/1000 = 70%
                return random(3)
            
            elif chance <= 940: #240/1000 = 24%
                return random(3, 7)
            
            elif chance <= 990:#50/1000 = 5%
                return random(7, 11)
            
            elif chance <= 995:#5/1000 = 0.5%
                return random(11, 15)
            
            elif chance <= 998: #3/1000 = 0.3%
                return random(15, 19)
            
            else: #2/1000 = 0.2%
                return random(19, 22)
        
        elif age >25 and age <=40:
            if chance <= 600: #600/1000 = 60%
                return random(3)
            
            elif chance <= 840: #240/1000 = 24%
                return random(3, 7)
            
            elif chance <= 990:#150/1000 = 15%
                return random(7, 11)
            
            elif chance <= 995:#5/1000 = 0.5%
                return random(11, 15)
            
            elif chance <= 998: #3/1000 = 0.3%
                return random(15, 19)
            
            else: #20/1000 = 0.2%
                return random(19, 22)
            
        elif age >40 and age <=50:
            if chance <= 550: #550/1000 = 55%
                return random(3)
            
            elif chance <= 800: #250/1000 = 25%
                return random(3, 7)
            
            elif chance <= 980:#180/1000 = 18%
                return random(7, 11)
            
            elif chance <= 988:#8/1000 = 0.8%
                return random(11, 15)
            
            elif chance <= 995: #7/1000 = 0.7%
                return random(15, 19)
            
            else: #5/1000 = 0.5%
                return random(19, 22)
                      
        else: #50+
            if chance <= 400: #400/1000 = 40%
                return random(3)
            
            elif chance <= 600: #200/1000 = 20%
                return random(3, 7)
            
            elif chance <= 790:#190/1000 = 19%
                return random(7, 11)
            
            elif chance <= 890:#100/1000 = 10%
                return random(11, 15)
            
            elif chance <= 992: #102/1000 = 10.2%
                return random(15, 19)
            
            else: #8/1000 = 0.8%
                return random(19, 22)
      
    if body == "Unhealthy":
        if age > 0 and age <= 25:
            if chance <= 890: #890/1000 = 89%
                return 0
            
            elif chance <= 940: #50/1000 = 5%
                return random(3)
            
            elif chance <= 965: #25/1000 = 2.5%
                return random(3, 7)
            
            elif chance <= 985:#20/1000 = 2%
                return random(7, 11)
            
            elif chance <= 995:#10/1000 = 1%
                return random(11, 15)
            
            elif chance <= 999: #4/1000 = 0.4%
                return random(15, 19)
            
            else: #1/1000 = 0.1%
                return random(19, 22)
        
        elif age >25 and age <=40:
            if chance <= 790: #790/1000 = 79%
                return 0
            
            elif chance <= 890: #100/1000 = 10%
                return random(3)
            
            elif chance <= 965: #75/1000 = 7.5%
                return random(3, 7)
            
            elif chance <= 985:#20/1000 = 2%
                return random(7, 11)
            
            elif chance <= 995:#10/1000 = 1%
                return random(11, 15)
            
            elif chance <= 999: #4/1000 = 0.4%
                return random(15, 19)
            
            else: #1/1000 = 0.1%
                return random(19, 22)
            
        elif age >40 and age <=50:
            if chance <= 630: #630/1000 = 63%
                return 0
            
            elif chance <= 780: #150/1000 = 15%
                return random(3)
            
            elif chance <= 890: #110/1000 = 11%
                return random(3, 7)
            
            elif chance <= 960:#70/1000 = 7%
                return random(7, 11)
            
            elif chance <= 980:#20/1000 = 2%
                return random(11, 15)
            
            elif chance <= 996: #1.6/1000 = 1.6%
                return random(15, 19)
            
            else: #4/1000 = 0.4%
                return random(19, 22)
                      
        else: #50+
            if chance <= 600: #600/1000 = 60%
                return 0
            
            elif chance <= 750: #150/1000 = 15%
                return random(3)
            
            elif chance <= 870: #120/1000 = 12%
                return random(3, 7)
            
            elif chance <= 930:#60/1000 = 6%
                return random(7, 11)
            
            elif chance <= 970:#40/1000 = 4%
                return random(11, 15)
            
            elif chance <= 990: #20/1000 = 2%
                return random(15, 19)
            
            else: #10/1000 = 1%
                return random(19, 22) 
      
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
                return "Uh"
                      
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
                return "Uh"
            
            else: # 2/20 = 10%
                return "Ff"
            
        if body == "Unhealthy":
            if diet <= 6: #6/20 = 30%
                return "Uh"
            
            elif diet <= 13: #7/20 = 35%
                return "Ff"
            
            elif diet <= 17: #4/20 = 20%
                return "Cc"
            
            elif diet <= 19: # 2/20 = 10%
                return "Np"
            
            else: # 1/20 = 5%
                return "Wl"
                       
    elif age > 25 and age <= 35:
        if body == "Athletic":
            if diet <= 8: # 8/20 == 40%
                return "Cc"
            
            elif diet <= 17: #9/20 == 45%
                return "H"
            
            elif diet <= 19:# 2/20 == 10%
                return "Np"          
            
            else: # 1/20 == 5%
                return "Uh"
        
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
                return "Uh"
            
            else: # 1/20 = 5%
                return "Ff"
            
        if body == "Unhealthy":
            if diet <= 6: #6/20 = 30%
                return "Uh"
            
            elif diet <= 10: #4/20 = 20%
                return "Ff"
            
            elif diet <= 14: #4/20 = 20%
                return "Cc"
            
            elif diet <= 17: # 3/20 = 15%
                return "Np"
            
            else: # 3/20 = 15%
                return "Wl"
              
    elif age > 35 and age <= 50:
        if body == "Athletic":
            if diet <= 6: # 6/20 == 30% 
                return "Cc"
            
            elif diet <= 18: #12/20 == 60%
                return "H"
            
            elif diet <= 19:# 1/20 == 5%
                return "Np"          
            
            else: # 1/20 == 5%
                return "Uh"
        
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
                return "Uh"
            
            else: # 2/20 = 10%
                return "Ff"
            
        if body == "Unhealthy":
            if diet <= 4: #4/20 = 20%
                return "Uh"
            
            elif diet <= 9: #5/20 = 25%
                return "Ff"
            
            elif diet <= 12: #3/20 = 15%
                return "Cc"
            
            elif diet <= 17: # 5/20 = 35%
                return "Np"
            
            else: # 3/20 = 15%
                return "Wl"
        
    elif age > 50:
        if body == "Athletic":
            if diet <= 2: # 2/20 == 10% 
                return "Cc"
            
            elif diet <= 12: #10/20 == 50%
                return "H"
            
            elif diet <= 17:# 5/20 == 25%
                return "Np"          
            
            else: # 3/20 == 15%
                return "Uh"
        
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
                return "Uh"
            
            else: # 1/20 = 5%
                return "Ff"
            
        if body == "Unhealthy":
            if diet <= 3: #3/20 = 15%
                return "Uh"
            
            elif diet <= 6: #3/20 = 15%
                return "Ff"
            
            elif diet <= 10: #4/20 = 20%
                return "Cc"
            
            elif diet <= 15: # 5/20 = 25%
                return "Np"
            
            else: # 5/20 = 25%
                return "Wl"
               
# En funktion för vikt för en peroson

def generate_weight(body, diet):
    #Healthy - H
    #Counting calories - Cc
    #No particular - Np
    #Unhealthy- Un
    #Weight loss - Wl 
    #Ff - Fastfood
    chance = random(100)+1
    
    if body == "Athletic":
        if diet == "H":
            if chance <= 90: # 90/100 = 90% 60kg - 89kg 
                return random(60, 89)
            
            elif chance <= 97: #7/100 = 7% 90kg - 105kg
                return random(90, 106)
            
            else: # 3/100 = 3% 106 - 120kg
                return random(106, 121)
            
        if diet == "Cc":
            if chance <= 32: # 35/100 = 32% 60kg - 74kg 
                return random(60, 75)
            
            elif chance <= 50: #15/100 = 18% 75kg - 89kg
                return random(75, 90)
            
            elif chance <= 90: #40/100 = 40%% 90kg - 119kg
                return random(90, 120)
            
            else: # 10/100 = 10% 120kg - 150kg
                return random(120, 151)
            
        if diet == "Np":
            if chance <= 23: # 23/100 = 23% 60kg - 74kg 
                return random(60, 75)
            
            elif chance <= 75: #52/100 = 52% 75kg - 89kg
                return random(75, 90)
            
            elif chance <= 88: #13/100 = 13% 90kg - 99kg
                return random(90, 100)
            
            elif chance <= 96: #8/100 = 8%% 100kg - 135kg
                return random(100, 136)
            
            else: # 4/100 = 4% 135kg - 150kg
                return random(135, 151)
            
        if diet == "Un":
            if chance <= 16: # 16/100 = 16% 60kg - 74kg 
                return random(60, 75)
            
            elif chance <= 44: #28/100 = 28% 75kg - 89kg
                return random(75, 90)
            
            elif chance <= 76: #32/100 = 32% 90kg - 104kg
                return random(90, 105)
            
            elif chance <= 93: #17/100 = 17% 105kg - 120kg
                return random(105, 121)
            
            else: # 7/100 = 7% 120kg - 150kg
                return random(120, 151)
    
    if body == "Healthy":
        if diet == "H":
            if chance <= 25: # 25/100 = 25% 60kg - 69kg 
                return random(60, 70)
            
            elif chance <= 75: #50/100 = 50% 75kg - 84kg
                return random(75, 85)
            
            elif chance <= 97: #22/100 = 22% 85kg - 100kg
                return random(85, 100)
            
            else: # 3/100 = 3% 106kg - 120kg
                return random(100, 121)
            
        if diet == "Cc":
            if chance <= 35: # 35/100 = 35% 60kg - 70kg 
                return random(60, 70)
            
            elif chance <= 55: #20/100 =  20% 70kg - 79kg
                return random(70, 80)
            
            elif chance <= 90: #35/100 = 35% 80kg - 90kg
                return random(80, 91)
            
            else: # 10/100 = 10% 91kg - 120kg
                return random(91, 120)
            
        if diet == "Np":
            if chance <= 15: # 15/100 = 15% 60kg - 70kg 
                return random(60, 70)
            
            elif chance <= 54: #39/100 =  39% 70kg - 79kg
                return random(70, 80)
            
            elif chance <= 88: #34/100 = 34% 80kg - 90kg
                return random(80, 91)
            
            else: # 12/100 = 12% 91kg - 120kg
                return random(91, 120)
            
        if diet == "Wl":
            if chance <= 10: # 10/100 = 10% 60kg - 70kg 
                return random(60, 70)
            
            elif chance <= 35: #20/100 =  22% 70kg - 79kg
                return random(70, 80)
            
            elif chance <= 60: #25/100 = 27% 80kg - 90kg
                return random(80, 91)
            
            elif chance <= 80: #20/100 = 21% 90kg - 99kg
                return random(90,100)
            
            else: # 20/100 = 20% 91kg - 120kg
                return random(100, 120)
            
    if body == "Average":     
        if diet == "Np":
            if chance <= 13: # 13/100 = 13% 50kg - 59kg 
                return random(50, 60)
            
            elif chance <= 43: #30/100 = 30% 60kg - 69kg
                return random(60, 70)
            
            elif chance <= 93: #50/100 = 50% 70kg - 89kg
                return random(70, 90)
            
            else: # 7/100 = 7% 90kg - 105kg
                return random(90, 106)
            
        if diet == "H":
            if chance <= 22: # 22/100 = 22% 50kg - 59kg 
                return random(50, 60)
            
            elif chance <= 71: #49/100 = 49% 60kg - 79kg
                return random(60, 80)
            
            elif chance <= 95: #24/100 = 24% 80kg - 89kg
                return random(80, 90)
            
            else: # 5/100 = 5% 90kg - 105kg
                return random(90, 106)
            
        if diet == "Uh":
            if chance <= 30: # 30/100 = 30% 50kg - 59kg 
                return random(50, 60)
            
            elif chance <= 47: #17/100 = 17% 60kg - 69kg
                return random(60, 70)
            
            elif chance <= 90: #43/100 = 43% 80kg - 89kg
                return random(70, 90)
            
            else: # 10/100 = 10% 90kg - 105kg
                return random(90, 106)
            
        if diet == "Ff":
            if chance <= 12: # 10/100 = 12% 50kg - 59kg 
                return random(50, 60)
            
            elif chance <= 37: #25/100 = 25% 60kg - 69kg
                return random(60, 70)
            
            elif chance <= 87: #50/100 = 50% 80kg - 89kg
                return random(70, 90)
            
            else: # 13/100 = 13% 90kg - 105kg
                return random(90, 106)
            
    
    if body == "Unhealthy":
        #40 - 120+
        #Uh 90 
        #Ff 90 120, 
        #Cc between 40 - 50  some heigher 
        #Np 80 - 90 lean 100 
        #Wl 80 - 100 range but a lot on higher 
        
        if diet == "Uh":
            if chance <= 11: # 11/100 = 11% 40kg - 59kg 
                return random(40, 60)
            
            elif chance <= 26: #15/100 = 15% 60kg - 69kg
                return random(60, 70)
            
            elif chance <= 71: #45/100 = 45% 80kg - 89kg
                return random(70, 90)
            
            elif chance <= 94: # 23/100 = 23% 90kg - 109kg
                return random(90, 110)
            
            else: #6/100 = 6% 110 - 120 
                return random(110-121)
            
        if diet == "Ff":
            if chance <= 5: # 5/100 = 5% 40kg - 59kg 
                return random(40, 60)
            
            elif chance <= 15: #10/100 = 10% 60kg - 69kg
                return random(60, 70)
            
            elif chance <= 60: #35/100 = 35% 80kg - 89kg
                return random(70, 90)
            
            elif chance <= 86: # 36/100 = 36% 90kg - 109kg
                return random(90, 110)
            
            else: #14/100 = 14% 110 - 120 
                return random(110-121)
            
        if diet == "Cc":
            if chance <= 40: # 40/100 = 30% 40kg - 49kg 
                return random(40, 50)
            
            elif chance <= 70: #30/100 = 40% 50kg - 69kg
                return random(50, 70)
            
            elif chance <= 84: #14/100 = 14% 80kg - 89kg
                return random(70, 90)
            
            elif chance <= 94: # 10/100 = 10% 90kg - 109kg
                return random(90, 110)
            
            else: #6/100 = 6% 110 - 120 
                return random(110-121)
            
        if diet == "Np":
            if chance <= 10: # 10/100 = 10% 40kg - 49kg 
                return random(40, 50)
            
            elif chance <= 28: #18/100 = 18% 50kg - 69kg
                return random(50, 70)
            
            elif chance <= 65: #37/100 = 37% 80kg - 89kg
                return random(70, 90)
            
            elif chance <= 92: #27/100 = 27% 90kg - 109kg
                return random(90, 110)
            
            else: #8/100 = 8% 110 - 120 
                return random(110-121)
            
        if diet == "Wl":
            if chance <= 12: # 12/100 = 12% 40kg - 59kg 
                return random(40, 60)
            
            elif chance <= 35: #23/100 = 23% 60kg - 79kg
                return random(60, 80)
            
            elif chance <= 65: #35/100 = 35% 80kg - 99kg
                return random(80, 100)
            
            else: #8/100 = 30% 100 - 120 
                return random(100-121)
    
    return weight


# Letar efter en fil och om den inte fins skapa och skriv
# Codecs används för att koda CSV med "åäö"
with codecs.open(os.path.join("data_analys", "data_samling.csv"), encoding="utf-8", mode="w+") as file1:
    writer = csv.writer(file1)
    # Definerar första raden
    writer.writerow(["Kön", " Ålder", " Vikt", " Timar/Vecka", " Krops-typ", " Diet"])   
    
    # Börjar generera värden för CSV
    for i in range(1000000):
        
        # Dessa värden genereras av dessa funktioner 
        sex = generate_sex()
        age = generate_age()
        body = generare_body()
        time = generate_time(age, body)
        diet = generate_diet(age, body)
        weight = generate_weight(body, diet)
        print(i)

        # Skriver ner dassa värden
        writer.writerow([sex, age, weight, time, body, diet])
  


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pygame
import os

pygame.init()
pygame.font.init()
#--------------------------------------------------------------PyGame_Interface----------------------------------------------------------------------#
objects = []

#----------------------------------------------Skapa en klass för knappar-----------------------------------------------#
class button():
    def __init__(self, x, y, width, height, color, color_hover, text=None, on_click=None, button_value=-1, font_size=22, font_color=(0, 0, 0)):
        #-------------------------------------------skapar objektet---------------------------------------#
        surface = pygame.Surface((width, height)) 
        rect_object = pygame.Rect(x, y, width, height)  
        surface.fill(color) 

        #------------------------------------Visar upp objektet på skärmen--------------------------------#
        def blit():
            # Om det finns en text som ska visas lägger den till den.
            if text is not None:
                font = pygame.font.SysFont('comicsans', font_size)
                temp = font.render(text, 1, font_color)  

                # Centrerar texten på knappen
                surface.blit(temp, [
                    rect_object.width / 2 - surface.get_rect().width / 2 + 10,
                    rect_object.height / 2 - font_size / 2 - 5])
            
            # Lägger till knappen i objektslistan
            objects.append(self)
            # Ritar knappen på skärmen med ytan och rektangeln
            window.blit(surface, rect_object)  

        #----------------------------------------funktion för knappen-------------------------------------#
        def process():
            # Hämtar musens position
            mousePos = pygame.mouse.get_pos()  

            # Kollar om musens position överlappar med rektangeln för knappen
            if rect_object.collidepoint(mousePos):
                surface.fill(color_hover)

                # Kollar om någon musknapp trycks ned
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # Anropar klickhändelsen med det angivna knappvärdet
                        if button_value != -1:
                            pygame.event.wait()
                            on_click(button_value)
                            # Anropar klickhändelsen utan knappvärde  
                        else:
                            on_click()  

        process() 
        blit()  
#---------------------------------------------------------------------------------Funktioner-------------------------------------------------------------------------------------#
#------------Funktion för att skriva text----------------------#
def text(msg, x, y, font_size=30, color=(0,0,0), font_name=None):
    font = pygame.font.Font(font_name, font_size)
    
    # Renderar texten med färgen
    text_surface = font.render(msg, True, color)  
    text_rect = text_surface.get_rect()
    # Positionerar texten på skärmen och lägger den på
    text_rect.topleft = (x, y)
    window.blit(text_surface, text_rect)  

#---------------Function för att skapa en bild----------------#
def load_image(image_path, image_name, pos, resize=0, size=None):
    # Laddar in bilden från den angivna sökvägen och filnamnet
    image = pygame.image.load(os.path.join(image_path, image_name))
    
    if resize != 0: 
        # Ändrar storleken på bilden om 'resize' inte är noll
        image = pygame.transform.scale(image, size)
    
    # Ritar bilden på skärmen på den angivna positionen
    window.blit(image, pos)
    
#---- En funktion för att ändra vilket fönster som ska användas---#
def window_change(window_number):
    global win

    # Ändrar värdet av den globala variabeln 'win' till det angivna fönsternumret
    win = window_number
    
# ------ En funktion som startar om alla värden--------------#
def value_reset():
    global amount, data_group, compare
    global value1, value2, value3, value4
    global save
    
    # Återställer värdena av olika variabler till None eller False
    amount, data_group, compare = None, None, None
    value1, value2, value3, value4 = None, None, None, None
    save = False
    
# ---------En funktion som hjälper knapparna att ändra värden som ska användas-------#
def return_value(group):
    global amount, data_group, compare
    global value1, value2, value3, value4
    global save
    
    if group[0] == 'amount':
        # Om det första elementet i gruppen är 'amount', sätter vi variabeln 'amount' till det andra elementet i gruppen
        amount = group[1]
    if group[0] == 'data_group':
        # Om det första elementet i gruppen är 'data_group', sätter vi variabeln 'data_group' till det andra elementet i gruppen
        data_group = group[1]
        
        # Ser till att med data gruppen 'kön' så kan amount inte vara mer än 2
        try:
            if data_group == 'Kön' and amount > 2:
                amount = 2
        except:
            pass
        
        # Om data gruppen ändras så återställs värdena till None
        value1, value2, value3, value4 = None, None, None, None
        
    if group[0] == 'compare':
        compare = group[1]
    if group[0] == 'value1':
        value1 = group[1]
    if group[0] == 'value2':
        value2 = group[1]
    if group[0] == 'value3':
        value3 = group[1]
    if group[0] == 'value4':
        value4 = group[1]
    if group[0] == 'save':
        save = group[1]

#-----------------------------------------------------Main loopen för pygame-----------------------------------------------#      

window_color = (30,130,180)
amount, data_group, compare = None, None, None
value1, value2, value3, value4 = None, None, None, None

save = False

def start():
    # Globala värden för att enklare kunna byta genom fönster
    global win, window_Size, window
    run = True
    win = 0
    # Storleken kommer ändras men detta determinerar vart fönstret först börjar
    window_Size = [1000, 700]
   
    while run == True:
        # Skapar fönstret
        window = pygame.display.set_mode(window_Size)
        pygame.display.set_caption('Välkomen')
        
        clock = pygame.time.Clock()
        
        # Visar olika fönster beroende på värdet av 'win'
        if win == 0:
            win0()
            
        elif win == 'start':
            starting_window()
            value_reset()

        elif win == 'histogram window':
            histogram_window()
            
        elif win == 'multi-histogram':
            multi_histogram_window()
        
        for event in pygame.event.get():
            # I fall man trycker på korset så stänger programmet av sig
            
            if event.type == pygame.QUIT:
                run = False
            
        pygame.display.update()
        clock.tick(20)

#------------------------------------------------------skapar alla fönster--------------------------------------------------#
# Fönster där programmet startar
def win0():
    global window_Size
    window_Size = [900, 400]
    window.fill(window_color)
    
    text('Hello, welcome to my program', 10, 10, 40)
    
    # Information
    text('NOTE!!!', 15, 60, 40)
    text('- You can navigate by using buttons on the screen', 30, 100)
    text('- The red "back" button will always take you back to the main screen', 30, 130)
    text('- Remember to read instructions before plotting', 30, 160)
    
    button(700, 300, 180, 80, (50,100,50), (40,80,40), 'Continue', window_change, 'start', 30, (255,255,255))

# Hufvud menyn            
def starting_window():
    global window_Size
    
    window_Size = [900, 600]
    window.fill(window_color)
    
    # Text
    text('Start', 20, 20, 50)
    text('Welcome to the starting page, ', 30, 70)
    text('here you can choose what type of action you want to do', 30, 95 )
    
    text('Histogram plotting:', 40, 150 )
    button(42, 182, 186, 76, (250,240,70), (200,190,60), 'Continue', window_change, 'histogram window', 35, (0,0,0))   
             
def histogram_window():
    global window_Size
    
    window_Size = [1250, 700] 
            
    window.fill(window_color)
    #-----------------Olika val för histogram-----------------#
    # Fler figur histograms
    text('Multiple histograms:', 15, 20, 35)
    text('Create one to four', 15, 50)
    text('histograms and', 15, 80)
    text('compare them to', 15, 110)
    text('eachother', 15, 140)
    
    # ladda in en bild
    load_image('data_analys/assets', 'histogram_example.png', (265,30), 1, (452,254))
    button(25, 200, 200, 84, (200,50,200), (180,30,180), 'continue' , window_change, 'multi-histogram', 35)
    
    
    #-----------------Tillbaka knappen-----------------#
    button(1120, -10, 140, 60, (220,10,30), (180,8,25), 'Back', window_change, 'start', 30)
            
def multi_histogram_window():
    global window_Size
    
    window_Size = [1250, 700] 
    window.fill(window_color)
    
    text('Multiple histograms plots', 40, 20, 60)
    
    
    #--------------Val av datagroup-----------------#
    text('What data group would you want to compare?*', 50, 100)
    button(50, 130, 60, 50, (255,0,127), (222,0,111), 'Kön', return_value, ('data_group', 'Kön'))
    button(120, 130, 80, 50, (255,0,127), (222,0,111), 'Kropp', return_value, ('data_group', 'Kropp'))
    button(210, 130, 65, 50, (255,0,127), (222,0,111), 'Diet', return_value, ('data_group', 'Diet'))
    text('your choice: '+str(data_group), 300, 150) 
    
    
    #--------------Val av amount--------------#
    if data_group != None:
        text('How many figures do you want to compare?*', 50, 200)
        button(50, 230, 50, 50, (255,0,127), (222,0,111), '1', return_value, ('amount', 1))
        button(110, 230, 50, 50, (255,0,127), (222,0,111), '2', return_value, ('amount', 2))
        if data_group != 'Kön':
            button(170, 230, 50, 50, (255,0,127), (222,0,111), '3', return_value, ('amount', 3)) 
            button(230, 230, 50, 50, (255,0,127), (222,0,111), '4', return_value, ('amount', 4))
            text('your choice: '+str(amount), 300, 250)
        else:
            text('your choice: '+str(amount), 170, 250)
    
    #--------------Val av vad man compare(gemför)--------------#
    if amount != None:
        if amount == 1:
            text('What would you want to see about "' + data_group +'"?*', 50, 300)
        else:
            text('What would you like to compare in "' + data_group +'"?*', 50, 300)
            
        button(50, 330, 70, 50, (255,0,127), (222,0,111), 'Ålder', return_value, ('compare', 'Ålder'))
        button(130, 330, 50, 50, (255,0,127), (222,0,111), 'Tid', return_value, ('compare', 'Tid'))
        button(190, 330, 60, 50, (255,0,127), (222,0,111), 'Vikt', return_value, ('compare', 'Vikt'))
        text('your choice: '+str(compare), 270, 350)
        
    #--------------Val av vilka värden man gemför--------------#
    if compare != None:
        if amount == 1:
            text('What do you want to look at?*', 50, 400)
        else:
            text('What do you want to compare?*', 50, 400)
        
        # Skapar ett specifikt antall av knappar
        for i in range(amount):
            #För varje knapp ska det finnas en text med ett värde, detta låter det ske
            if i  == 0:
                what_value = value1
            elif i == 1:
                what_value = value2
            elif i == 2:
                what_value = value3
            elif i== 3:
                what_value = value4
                
            # Hur ska frågan ska se ut om data_group värdet är kön 
            if data_group == 'Kön':
                button(50, 430 + (60*i), 60, 50, (255,0,127), (222,0,111), 'Man', return_value, ('value' + str(i+1), 'Man'))
                button(120, 430 + (60*i), 90, 50, (255,0,127), (222,0,111), 'Kvinna', return_value, ('value' + str(i+1), 'Kvinna'))
                text('your choice: ' + str(what_value), 220, 450+(60*i))

            # Hur ska frågan ska se ut om data_group värdet är Kropp
            if data_group == 'Kropp':
                button(50, 430 + (60*i), 110, 50, (255,0,127), (222,0,111), 'Athletic', return_value, ('value' + str(i+1), 'Athletic'))
                button(170, 430 + (60*i), 110, 50, (255,0,127), (222,0,111), 'Average', return_value, ('value' + str(i+1), 'Average'))
                button(290, 430 + (60*i), 110, 50, (255,0,127), (222,0,111), 'Healthy', return_value, ('value' + str(i+1), 'Healthy'))
                button(410, 430 + (60*i), 120, 50, (255,0,127), (222,0,111), 'Unhealthy', return_value, ('value' + str(i+1), 'Unhealthy'))  
                text('your choice: ' + str(what_value), 540, 450+(60*i))
                
            if data_group == 'Diet':
                button(50, 430 + (60*i), 50, 50, (255,0,127), (222,0,111), 'Np', return_value, ('value' + str(i+1), 'Np'))
                button(110, 430 + (60*i), 50, 50, (255,0,127), (222,0,111), 'Nc', return_value, ('value' + str(i+1), 'Nc'))
                button(170, 430 + (60*i), 50, 50, (255,0,127), (222,0,111), 'H', return_value, ('value' + str(i+1), 'H'))
                button(230, 430 + (60*i), 50, 50, (255,0,127), (222,0,111), 'Uh', return_value, ('value' + str(i+1), 'Uh'))
                button(290, 430 + (60*i), 50, 50, (255,0,127), (222,0,111), 'Ff', return_value, ('value' + str(i+1), 'Ff'))
                button(350, 430 + (60*i), 50, 50, (255,0,127), (222,0,111), 'Wl', return_value, ('value' + str(i+1), 'Wl'))
                text('your choice: ' + str(what_value), 410, 450+(60*i))
        
    
    #---------------Note!!!--------------------#

    if compare != None:
        text('Note!!!', 650, 65, 40)
        
        text('-Plot the figure/figures by pressing the plot button', 660, 105)
        
        text("-If you want to save the figure you're about to plot,", 660, 135)
        text(' please click on save', 680, 165)
        
        text('-Ploting with no chosen values will result in empty figures', 660, 195)
        text('-The chosen amount will always determin amount of shown plots', 660, 225)
        
        text('-If you are comparing 2 figures, it is advised', 660, 255)
        text(' not to compare the same figures', 680, 285)
        
        #Text som ska visas när du väljder värden för diet
        if data_group == 'Diet':
            text('-The following shortenings stand for:', 660, 315)
            text(' Np: No particular, Nc: Not controlled, H: Healthy', 680, 345)
            text(' Uh: Unhealthy, Ff: Fast food and Wl: Weight loss', 680, 375)
       
    
        #-------------- plotta och spara --------------#
        text('Plot and save:', 750, 500)
        # Knappen ska ändrras beroende på värdet save
        if save == False:
            button(755, 530, 140, 80, (255,0,127), (222,0,111), '  Save?', return_value,('save', True),25)
            
        else:
            button(755, 530, 140, 80, (222,0,111), (255,0,127) , ' Saveing', return_value,('save', False),25)
        
        button(955, 530, 100, 80, (255,0,127), (222,0,111), 'Plot', multi_histogram_plotting, 
               (amount, data_group, compare, value1, value2, value3, value4),25)
            
        
    
    #-----------------Tillbaka knappen-----------------#
    button(1120, -10, 140, 60, (220,10,30), (180,8,25), 'Back', window_change, 'start', 30)

#----------------------------------------------------------------------------Pandas och Plotting-----------------------------------------------------------------------------------#

# Skapar en data frame
gym_dataset = pd.read_csv(os.path.join('data_analys', 'data_samling.csv'))

# En funktion som sparar din plot
def saving():
    for i in range(101):
        # Definerar en dynamisk path som ändras för varje loop
        path = 'data_analys/images/mygraf' + str(i) + '.png'

        # Kollar om denna pathen fins vid denna loopen
        if os.path.exists(path) :
            # Om den finns så kommer den säga till dig och gå till nästa loop
            print('Image ' + str(i) + ' exists')
            # Om alla 101 bilder är upptagna så säger den till dig att du inte kan ta bort mer
            if i == 100:
                print('you have too many saved grafs, remove or move them')
                break
        # Om den inte finns så kommer en ny bild skapas på en specifik plats
        else:
            print('iamge saved as "image'+str(i)+'"')
            plt.savefig(os.path.join('data_analys/images', 'mygraf'+str(i)+'.png'), dpi=500 )

            break
        
def multi_histogram_plotting(values):
    global save
    
    # Definerar ett värde ur en lista pga knapparna
    amount = values[0]
    data_group = values[1]
    compare = values[2]
    value1 = values[3]
    value2= values[4]
    value3= values[5]
    value4= values[6]
    
    colors = ['#9F0606', '#B20E3A', '#EC6826', '#F7EB38']
    num_rows = (amount + 1) // 2

    # Skapar subplots baserat på antalet rader och kolumner
    if num_rows > 1:
        fig, axes = plt.subplots(num_rows, 2, figsize=(12, 6))
        axes = axes.flatten()  # Omvandlar den 2D-arrayen av axlar till en 1D-array
    else:
        fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        
    fig.subplots_adjust(hspace=0.5)  # Justerar vertikalt mellanrum mellan subplots

    group1 = gym_dataset.loc[gym_dataset[data_group] == value1]
    groups = [group1]

    # Lägger till ytterligare grupper baserat på värdena value2, value3 och value4 om de finns
    if value2 is not None:
        group2 = gym_dataset.loc[gym_dataset[data_group] == value2]
        groups.append(group2)

    if value3 is not None:
        group3 = gym_dataset.loc[gym_dataset[data_group] == value3]
        groups.append(group3)

    if value4 is not None:
        group4 = gym_dataset.loc[gym_dataset[data_group] == value4]
        groups.append(group4)

    # Beräknar histogramdata för varje grupp och kombinerar dem
    all_counts = np.concatenate([np.histogram(group[compare])[0] for group in groups])
    max_count = max(all_counts)

    # Loopar igenom varje grupp och skapar subplots för varje grupp
    for i, group in enumerate(groups[:amount]):

        # Väljer rätt label baserat på gruppens index
        if i + 1 == 1:
            label = value1
        elif i + 1 == 2:
            label = value2
        elif i + 1 == 3:
            label = value3
        elif i + 1 == 4:
            label = value4

        # Skapar histogram för gruppen och ställer in attribut för subplots
        axes[i].hist(group[compare], color=colors[i])
        axes[i].set_ylim((0, max_count))
        axes[i].set_title(label)
        #Namn på x och y axeln
        axes[i].set_ylabel('Personer')
        
        if compare == 'Ålder':  
            x_name = 'År'
        if compare == 'Vikt':  
            x_name = 'Kg'
        if compare == 'Tid':
            x_name = 'Timmar/Vecka'
        axes[i].set_xlabel(x_name)  
    


    # Döljer subplots som över stiger antalet som ska finnas
    for j in range(amount, len(axes)):
        fig.delaxes(axes[j])
    #Titel till ploten
    plt.suptitle(f'Hur många med specifik {compare} beroende på {data_group} ')
    
    if save == True:
        saving()
    
    plt.show()
    
#-----------------------------------------------------------------------startar PyGameLoopen, därmed programmet------------------------------------------------------------------------#

start()


from pyb import Timer, Pin
import time
import tm1637

class Note():
    def __init__(self,hauteur=float(),longueur=int(),nom=str()):
        self.hauteur=int() #int=nombre entier
        self.longueur=float() #float=nombre à virgule
        self.nom=str()
        
    def play(self):
        self.timer = Timer(5, freq=self.hauteur)
        self.channel = self.timer.channel(3, Timer.PWM, pin=Pin('X1'), pulse_width_percent=50)
        start=time.ticks_ms()  #duree de temps
        while True:
            duree=time.ticks_diff(time.ticks_ms(),start)
            if duree>self.longueur:
                break
            pyb.delay(10) #pause de 5ms
            
display = tm1637.TM1637(clk=pyb.Pin('X7'), dio=pyb.Pin('X6'))

dict_note={"do":Note(130,1000,"do"),"re":Note(147,1000,"re"),"mi":Note(165,1000,"mi")}

display.scroll("Hello Vic et Stef")
#ou alors à la place de scroll tu mets show
#(de préférence pour un mot à 4 lettres comme ça il y aura tout le mot)
            
#pour créer un objet Note pour le faire on a utilisé class.
#Donc un objet possède des attributs qui correspondent à l'objet qu'il permet de créer.
do=dict_note["do"]
re=dict_note["re"]
mi=dict_note["mi"]
#les [] sont pour chercher dans un dictionnaire (en gros : va dans le dictionnaire note et chercher do)
partition=[do,re,mi] #liste de note                               

for note in partition:
    note.play()
    display.show(note.nom)
    
    
    
    
    
    
    
    
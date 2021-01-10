from tkinter import *
import pygame
from PIL import ImageTk,Image

def startIspressed():
    root.destroy()
    import quiz2.py

WIDTH = 900
HEIGHT = 700
File = "MathEquations.png "
 
root = Tk()
root.title("QUIZ")
root.iconbitmap('Quiz_image.ico')
# CENTER THE WINDOW
#dimensions of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
#x,y coordinates in order to be exactly in the middle of the screen
x = (screen_width / 2) - (WIDTH / 2)
y = (screen_height / 2) - (HEIGHT / 2)
root.geometry(f"{WIDTH}x{HEIGHT}+{int(x)}+{int(y)}")
root.resizable(width = False, height = False)

                              #'Η Image.open(file)
bg_image = ImageTk.PhotoImage(file = "MathEquations.png")

#CREATE CANVAS(1)
canvas = Canvas(root,width = WIDTH,height = HEIGHT,bd = 0, highlightthickness = 0)  #Υπάρχει ενα άσπρο περίγραμμα,μπορώ να το βγάλω βάζοντας στον καμβά bd=0,highlightthickness = 0
canvas.grid(row = 1,column = 1)
canvas.create_image(0,0,image = bg_image , anchor = "nw")

#music Text(1)
canvas.create_text(115,16,text = "<<Press to play>>" , font =("Comic sans MS",12,"bold"),fill ="#A8080E")
#music Text(2)
canvas.create_text(115,53,text = "<<Press to mute>>" , font =("Comic sans MS",12,"bold"),fill ="#A8080E")

#open Music Image
music_foto = Image.open( "Music_Image.png")

#resize Music Image
resized = music_foto.resize((29,29), Image.ANTIALIAS)
new_music_foto = ImageTk.PhotoImage(resized)

#Turn on pygame
pygame.mixer.init()

def play():
    pygame.mixer.music.load("Music_for_quiz.mp3")
    pygame.mixer.music.play(loops = 1)

#create music button up left
music_btn = Button(root,image =new_music_foto,command = play, width = 30,height =0,fg = "#000000",bg ="#A13034",activebackground ="#A13034")
music_btn_window = canvas.create_window(37,18,anchor = "e",window = music_btn)


#open Mute Image
mute_foto = Image.open("Mute_image.png")
#resize Mute Image
resized = mute_foto.resize((29,29), Image.ANTIALIAS)
new_mute_foto = ImageTk.PhotoImage(resized)


def stop():
     pygame.mixer.music.stop()
    
#create mute music button up left
mute_btn = Button(root,image = new_mute_foto,command =stop,width = 30,height = 0,fg = "#000000",bg ="#A13034",activebackground ="#A13034")
mute_btn_window = canvas.create_window(37,53,anchor = "e",window = mute_btn)


#Open Image
image_button = Image.open("Start_image.png")
#Resize Image
resized = image_button.resize((238,58), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized)


#CREATE Image START Button
start_button = Button(root,command = startIspressed, image = new_image ,borderwidth = 0,activebackground = "#000000")
start_button_window = canvas.create_window(325,675,anchor ="sw",window = start_button)

#CREATE CANVAS(2)
canvas = Canvas(root, width = 700 ,height = 500,bg ="#36AAA0",bd = 0,highlightthickness = 0)                                            
canvas.grid(row = 1,column = 1)

#TEXT
canvas.create_text(350,40,text ="QUIZ GAME",font = ("Comic sans MS",40,"bold"),fill = "#A13034")
#TEXT 2
canvas.create_text(450,90,text =" για το μάθημα των Μαθηματικών",font = ("Comic sans MS",20,"bold"),fill = "#000000")
#TEXT 3
canvas.create_text(350,290,text ="Διαβάστε τις οδηγίες\n και όταν είστε έτοιμοι\n πατήστε το κουμπί <<Start>>\n για να ξεκινήσετε",font = ("Georgia",15,"bold"),fill = "#000000",justify = "center")

#create label
label = Label(root,width = 98,padx =5,pady =11,bg ="#000000",fg ="#A13034",
                 text ="Το  Quiz περιλαμβάνει  δέκα ερωτήσεις που αφορούν το μάθημα των μαθηματικών\nΠατώντας το κουμπί <<Επόμενο>>, πηγαίνετε σε επόμενη ερώτηση\nΟταν οι ερωτήσειες τελειώσουν θα εμφανιστεί το ποσοστό επιτυχίας\n σας και ο αριθμός των σωστών και λάθος απαντήσεων\nΚΑΛΗ ΕΠΙΤΥΧΙΑ!!! ",font =("Oswald",9,"bold"))                 
label_window = canvas.create_window(0,500,anchor ="sw",window = label)


#Open Quiz Image
quiz_foto = Image.open("Quiz_image.png")
#Resize Quiz_Image
resized = quiz_foto.resize((57,57), Image.ANTIALIAS)
new_quiz_foto= ImageTk.PhotoImage(resized)


#Custom Message Box
def destroy_ok():
    pop.destroy()
    
def popup_message():
    pop_width = 400
    pop_height = 280
    global pop
    pop = Toplevel(root)
    pop.title("Informations")
    pop.iconbitmap('info.ico')
    #CENTER POPUP WINDOW
    x = (screen_width / 2) - (pop_width / 2)
    y = (screen_height / 2) - (pop_height / 2)
    pop.geometry(f"{pop_width}x{pop_height}+{int(x)}+{int(y)}")
    pop.config(bg = "#ffffff")
    pop.resizable(0,0)
  
    #global quiz_foto
    
    pop_label = Label(pop,
                         text = "Το συγκεκριμένο Quiz αποτελεί \nένα διδακτικό βοήθημα των μαθημάτων\nτης Γραμμικής Άλγεβρας και του\nΛογισμού Συναρτήσεων Μίας  Μεταβλητής.\nΣκοπός αυτού τού Quiz παιχνιδιού είναι\n η όσο το δυνατό καλύτερη κατανόηση \nτων παραπάνω μαθημάτων μέσο διαδοχικών ερωτήσεων \nπου εξετάζουν ένα αρκετά μεγάλο κομμάτι της ύλης.",
                         justify = "center",
                         bg = "#ffffff",
                         fg = "#000000",
                         font = ("Sitca Small",10,"bold"))
    pop_label.pack(pady = 10)

    frame = Frame(pop,bg ="#ffffff")  #frame τριγύρω απο την foto quiz
    frame.pack(pady =5)

    quiz_foto_img = Label(frame,image = new_quiz_foto,borderwidth = 0)
    quiz_foto_img.grid(row = 0,column = 1,padx = 10,pady = 10)
    
    #<Ok> button
    ok_btn = Button(frame,text ="OK",command =destroy_ok,font = ("Sitca Small",10,"bold") ,bg = "#ECECEC",fg = "black",width = 10,activebackground = "#8B69DB",activeforeground ="white")#command =destroy_ok
    ok_btn.grid(row = 1,column =1)
                        
#create info button down left
info_btn = Button(root,text = "Info",command = popup_message,font =("Comic sans MS",10,"bold"),width = 6,height =0,fg = "#000000",bg ="#A13034",border = 1,activebackground ="#36AAA0")
info_btn_window = canvas.create_window(58,483,anchor = "e",window = info_btn)

root.mainloop()



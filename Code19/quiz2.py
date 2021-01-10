from tkinter import messagebox as mb
from tkinter import *
import pygame
import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
filepath = "quiz.json"
abs_file_path = os.path.join(script_dir, filepath)

root = Tk()
root.title("Ερωτηματολόγιο")
root.iconbitmap('Quiz_image.ico')
WIDTH = 1024
HEIGHT = 768

# CENTER THE WINDOW
#dimensions of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
#x,y coordinates in order to be exactly in the middle of the screen
x = (screen_width / 2) - (WIDTH / 2)
y = (screen_height / 2) - (HEIGHT / 2)
root.geometry(f"{WIDTH}x{HEIGHT}+{int(x)}+{int(y)}")

root.configure(bg="#36AAA0")
root.resizable(width = False, height = False)
my_fonts = "Helvetica"


with open(abs_file_path,encoding="utf8") as f:
    obj = json.load(f)

questions = (obj['ques'])
options = (obj['options'])
answers = (obj['ans'])


class Quiz:
    def __init__(self):
        self.qn = 0
        self.ques = self.question(self.qn)
        self.opt_selected = IntVar()
        self.opts = self.radiobtns()
        self.display_options(self.qn)
        self.buttons()
        self.correct = 0
        

    def question(self, qn):
        
        
        t = Label(root, text="QUIZ ΕΡΩΤΗΣΕΩΝ ΣΤΑ ΜΑΘΗΜΑΤΙΚΑ",font = ("Comic sans MS",26,"bold"), justify='center', bg="#A13034", fg="white")
        t.place(height=50, width=1024, x=0, y=0)
        
        t.config()
        t1x = 0
        t1y = 3 

        l = t1y + 2 
        qn = Label(root, text=questions[qn], bg="#000000", fg="white",  font=(my_fonts, 16, "bold"))
        
        qn.place(height=120, width=1024, x=0, y=50)
        qn.config()
        self.l2 = 1 + 50
        
        return qn
    
    def radiobtns(self):
        val = 0
        b = []
        l3 = self.l2 + 30
        print (l3)
        yp = l3

        while val < 4:
            
            btn = Radiobutton(root, text=" ", fg="black",bg="#36AAA0"  ,width=90,  variable=self.opt_selected, value=val + 1, bd=0, relief=GROOVE, font=(my_fonts,16))
            b.append(btn)
            #btn.place(x=100, y=yp+80)
            btn.pack_propagate(0)
            btn.place(height=100, width=1024, x=0, y=80 + yp)
            
            
            #btn.config()
            val += 1
            yp += 80
                 
        return b

    
    def display_options(self, qn):
        val = 0
        self.opt_selected.set(0)
        self.ques['text'] = questions[qn]
        for op in options[qn]:
              self.opts[val]['text'] = op
              val += 1
              
    #Turn on pygame
    pygame.mixer.init()


    def music_final_stop(self):
        pygame.mixer.music.stop()
        root.destroy()
        
    def play(self):
        pygame.mixer.music.load("Music_for_quiz.mp3")
        pygame.mixer.music.play(loops = 1)

    def stop(self):
         pygame.mixer.music.stop()
            

    def buttons(self):
        nbutton = Button(root,text='Επόμενο',command=self.nextbtn, width=20,bg="#000000",fg="white", activebackground = "#A13034",font=(my_fonts,16,"bold"))
        nbutton.place(x=200,y=600)
        quitbutton = Button(root,text='Έξοδος', command=self.music_final_stop,width=20,bg="#A13034",fg="black",activebackground = "#000000",activeforeground ="white", font=(my_fonts,16,"bold"))
        quitbutton.place(x=600,y=600)
        musicbutton = Button(root,text = "MUSIC",font = ("Comic sans MS",8,"bold"),command = self.play, width = 7,height =0,fg = "#000000",bg ="#A13034",activebackground ="white",activeforeground ="#000000")
        musicbutton.place(x = 0,y =0)
        mutebutton = Button(root,text ="MUTE",font = ("Comic sans MS",8,"bold"),command =self.stop,width = 7,height = 0,fg = "#000000",bg ="#A13034",activebackground ="white",activeforeground ="#000000")
        mutebutton.place(x = 0,y =27)


    def checkans(self, qn):
        if self.opt_selected.get() == answers[qn]:
             return True
        
    def nextbtn(self):
        if self.checkans(self.qn):
            self.correct += 1
        self.qn += 1
        if self.qn == len(questions):
            self.display_result()
        else:
            self.display_options(self.qn)       
        

    def display_result(self):
        score = int(self.correct / len(questions) * 100)
        result = "Score: " + str(score) + "%"
        wc = len(questions) - self.correct
        correct = "No. of correct answers: " + str(self.correct)
        wrong = "No. of wrong answers: " + str(wc)
        mb.showinfo("Result", "\n".join([result, correct, wrong]))

quiz=Quiz()
root.mainloop()





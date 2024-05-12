from tkinter import *
from PIL import Image,ImageTk
import random 

#main window
frame=Tk()
frame.title("Rock Paper Scissor")
frame.configure(background="#15f2fd")

#picture
rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissor.png"))
rock_comp_img = ImageTk.PhotoImage(Image.open("rock_comp.png"))
paper_comp_img = ImageTk.PhotoImage(Image.open("paper_comp.png"))
scissor_comp_img = ImageTk.PhotoImage(Image.open("scissor_comp.png"))

#insert picture
user_label=Label(frame,image=rock_img,bg="#15f2fd")
comp_label=Label(frame,image=rock_comp_img,bg="#15f2fd")
user_label.grid(row=1,column=1)
comp_label.grid(row=1,column=10) 

#scores
playerscore=Label(frame,text=0,font=("Times new Roman",15, "bold"),bg="#15f2fd",fg="white")
compscore=Label(frame,text=0,font=("Times new Roman",15, "bold"),bg="#15f2fd",fg="white")
playerscore.grid(row=1,column=2)
compscore.grid(row=1,column=4)

#buttons
rock=Button(frame,width=18,height=2,text="ROCK",font=25,bg="#FF3E4D",fg="white",command=lambda:updatechoice("rock")).grid(row=2,column=2)
paper=Button(frame,width=18,height=2,text="PAPER",font=25,bg="#FF3E4D",fg="white",command=lambda:updatechoice("paper")).grid(row=2,column=3)
scissor=Button(frame,width=18,height=2,text="SCISSOR",font=25,bg="#FF3E4D",fg="white",command=lambda:updatechoice("scissor")).grid(row=2,column=4)

#Indicators
user_ind=Label(frame,font=("Times new Roman",15, "bold"),text="USER",bg="#15f2fd",fg="white")
comp_ind=Label(frame,font=("Times new Roman",15, "bold"),text="COMPUTER",bg="#15f2fd",fg="white")
user_ind.grid(row=0,column=2)
comp_ind.grid(row=0,column=4)

#message
msg=Label(frame,font=("Times new Roman",20, "bold"),bg="#15f2fd",fg="white")
msg.grid(row=4,column=3)

options=["rock","paper","scissor"]

#picture logic
def updatechoice(x):
    
    compchoice=random.choice(options)
    #for computer
    if compchoice=="rock":
        comp_label.configure(image=rock_comp_img)
    elif compchoice=="paper":
        comp_label.configure(image=paper_comp_img)
    else:
        comp_label.configure(image=scissor_comp_img) 
    # for user
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    judge(x,compchoice)

#updating scores
def UpdateUserScore():
    score=int(playerscore["text"])
    score+=1
    playerscore["text"]=str(score)

def UpdateCompScore():
    score=int(compscore["text"])
    score+=1
    compscore["text"]=str(score)

#update message
def updateMesaage(X):
    msg["text"]= X

#Check for Winner
def judge(player,computer):
    if player==computer:
        updateMesaage("It is a Tie")
    elif player=="rock" and computer == "scissor":
        updateMesaage("!! You Win !!")
        UpdateUserScore() 
    elif player=="paper" and computer=="rock":
        updateMesaage("!! You Win !!")
        UpdateUserScore()
    elif player=="scissor" and computer=="paper":
        updateMesaage("!! You Win !! ")
        UpdateUserScore()       
    else:
        updateMesaage("You Lose :(")
        UpdateCompScore()

frame.mainloop()
# the json module to work with json files 
import json
import tkinter
from tkinter import *
import random
from tkinter import messagebox



# questions = [
#     "How many Keywords are there in C Programming language ?",
#     "Which of the maximum possible length of an identifier ?",
#     "In which year was the Python language developed ?",
#     "In which language is Python written ?",
#     "Which of the following is not a keyword in Python language ?",
#     "The append Method adds value to the list at the  ?",
#     "What is called when a function is defined inside a class ?",
#     "Which of The following is executed in browser(client side) ?",
#     "Which of the following keyword is used to create a function in Python ?",
#     "To Declare a Global variable in python we use the keyword ?",
# ]

# answers_choice = [
#     ["23","32","33","43",],
#     ["16","32","64","None of the above",],
#     ["1995","1972","1981","1989",],
#     ["English","PHP","C","All of the above",],
#     ["val","raise","try","with",],
#     ["custom location","end","center","beginning",],
#     ["Module","Class","Another Function","Method",],
#     ["perl","css","python","java",],
#     ["function","void","fun","def",],
#     ["all","var","let","global",],
# ] 


##Coding done by Nabin Chakraborty

# load questions and answer choices from json file instead of the file
with open('./data.json', encoding="utf8") as f:
    data = json.load(f)

# convert the dictionary in lists of questions and answers_choice 
questions = [v for v in data[0].values()]
answers_choice = [v for v in data[1].values()]

answers = [1,3,3,2,0,1,3,1,3,3] 

user_answer = []

indexes = []
def gen():
    global indexes
    while(len(indexes) < 5):
        x = random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background = "#ffffff",
        border = 0,
    )
    labelimage.pack(pady=(50,30))
    labelresulttext = Label(
        root,
        font = ("Consolas",20),
        background = "#ffffff",
    )
    labelresulttext.pack()
    if score >= 20:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Excellent !!")
    elif (score >= 10 and score < 20):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Can Do Better !!")
    else:
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Should Work Hard !!")


def calc():
    global indexes,user_answer,answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    print(score)
    showresult(score)


ques = 1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblQuestion.config(text= questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        # print(indexes)
        # print(user_answer)
        # these two lines were just developement code
        # we don't need them
        calc()
    



##Coding done by Subhesh Kumar

def startquiz():
    global lblQuestion,r1,r2,r3,r4
    lblQuestion = Label(
        root,
        text = questions[indexes[0]],
        font = ("Consolas", 30),
        width = 1500,
        justify = "center",
        wraplength = 800,
        background = "#ffffff",
    )
    lblQuestion.pack(pady=(100,40))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][0],
        font = ("Times", 20),
        value = 0,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][1],
        font = ("Times", 20),
        value = 1,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][2],
        font = ("Times", 20),
        value = 2,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][3],
        font = ("Times", 20),
        value = 3,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r4.pack(pady=5)


def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    btnStart.destroy()
    btnrules.destroy()
    gen()
    startquiz()


def popup():
    messagebox.showinfo("Rules","This quiz contains 10 questions\nYou will get 20 seconds to solve a question\nOnce you select a radio button that will be a final choice\nhence think before you select")

root = tkinter.Tk()
root.title("Quiz Master")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable()


img1 = PhotoImage(file="quiz.png")

labelimage = Label(
    root,
    image = img1,
    background = "#ffffff",
)
labelimage.pack(pady=(40,0))

labeltext = Label(
    root,
    text = "Quiz Master",
    font = ("Comic sans MS",40,"bold"),
    background = "#ffffff",
)
labeltext.pack(pady=(0,35))

img2 = PhotoImage(file="start.png")

btnStart = Button(
    root,
    image = img2,
    relief = FLAT,
    border = 0,
    command = startIspressed,
    background="#ffffff",
)
btnStart.pack()

pic = PhotoImage(file="rules.png")
btnrules = Button(
    root, 
    image=pic, 
    command=popup,
    relief = FLAT,
    background="#ffffff")
btnrules.pack(side=RIGHT, pady=(0,0))


lblInstruction = Label(
    root,
    text = "Read The Rules And\nClick Start Once You Are ready",
    background = "#ffffff",
    font = ("Consolas",14),
    justify = "center",
)

lblInstruction.pack(pady=(0,0), side=LEFT)



root.mainloop()
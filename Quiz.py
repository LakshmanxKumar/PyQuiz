import random
from tkinter import *
front = Tk()
front.geometry("950x500+155+60")
front.title("Python Quiz")
front.resizable(height=FALSE, width=FALSE)
front.config(bg="#ffffff")

pframe = Frame(front, bg="#FFFFFF")
pframe.pack(side=LEFT)
bframe = Frame(front, bg="#FFFFFF")
bframe.pack(side=RIGHT)


global markstoshow, namestoshow
markstoshow = []
namestoshow = []


def exit():
    front.destroy()


def opener():

    root = Toplevel(front)
    root.geometry("950x500+155+60")
    root.resizable(height=FALSE, width=FALSE)
    root.config(bg="#F0F0F2")
    root.title("Quiz")

    global n, timer, opt, marks

    n = 0
    timer = 30

    questions = {
        1:  " In Python 3, the maximum value for an integer is ?",
        2:  " How do you insert COMMENTS in Python code ?",
        3:  " Which one is NOT a legal variable name ?",
        4:  " What is the correct file extension for Python files ?",
        5:  " What is the correct syntax to output the type of a variable or object in Python ?",
        6:  " What is the correct way to create a function in Python ?",
        7:  " Which built-in function can be used to calculate the\nlength of any iterable object in Python ?",
        8:  " Which method can be used to return a string in upper case letters ?",
        9:  " Which method can be used to replace parts of a string ?",
        10: " Which operator is used to multiply numbers ?",
        11: " Which operator can be used to compare two values ?",
        12: " Which of these collections defines a LIST ?",
        13: " Which of these collections defines a TUPLE ?",
        14: " Which of these collections defines a SET ?",
        15: " Which collection is ordered, changeable, and allows duplicate members ?",
        16: " Which collection does not allow duplicate members ?",
        17: " What is output for − 'raining'. find('z') ?",
        18: " What is output for − 2 * 2 **3 ?",
        19: " What command is used to insert 6 in a list \"L\" at 3rd position ?",
        20: " Which of the following data types is not supported in python?",
        21: " What is the output of print str[0] if str = 'Hello World!'?",
        22: " What is the output of print list if tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )?",
        23: " Which operator is overloaded by the or() function?",
        24: " Which function overloads the >> operator?",
        25: " What is called when a function is defined inside a class?"

    }

    options = {
        1:
        {
            'A':		"2^63 – 1",
            'B':		"2^63 + 1",
            'C':		"–(2^63 1 1)",
            'D':   	"No limit"

        },
        2:
        {
            'A':		"// this is a comment",
            'B':		"/* this is a comment*/",
            'C':		"#  This is comment",
            'D':		"* This is a comment*"

        },
        3:
        {
            'A': 		"my-var",
            'B':    	"My_var",
            'C':    	"Myvar",
            'D':   	 "_Myvar"

        },
        4:
        {
            'A':		"Python",
            'B':		"Pyh",
            'C':		"Ptx",
            'D':		"Py"

        },
        5:
        {
            "A":	"print(typeof(x))",
            "B":    	"print(type(x))",
            "C":    	"print(typeOf(x))",
            "D":	"none of the above"

        },
        6:
        {
            "A":	"generate myFunction():",
            "B": 	"def myFunction():",
            "C": 	"create myFuntion():",
            "D": 	"function myfucntion():"

        },
        7:
        {
            "A":	"Ptrim()",
            "B":	"trim()",
            "C":	"strip()",
            "D":	"len()"

        },
        8:
        {
            "A": 	"uppercase()",
            "B": 	"upper()",
            "C": 	"touppercase()",
            "D": 	"UpperCase()"

        },
        9:
        {
            "A":	"switch()",
            "B":	"repl()",
            "C":	"replace()",
            "D":	"replacestring()"
        },
        10:
        {
            "A":	"X",
            "B":	"%",
            "C":	"*",
            "D":	"**"

        },
        11:
        {
            "A":	"=",
            "B":	"==",
            "C":	"><",
            "D":	"<>"

        },
        12:
        {
            "A": 	"[“apple”,”banana”,”cherry”]",
            "B":	"{ “apple”,”banana”,”cherry”}",
            "C": 	"(“apple”,”banana”,”cherry”)",
            "D": 	"none of the above"
        },
        13:
        {
            "A": 	"[“apple”,”banana”,”cherry”]",
            "B":	"{ “apple”,”banana”,”cherry”}",
            "C": 	"(“apple”,”banana”,”cherry”)",
            "D": 	"none of the above"
        },
        14:
        {
            "A": 	"[“apple”,”banana”,”cherry”]",
            "B": 	"{ “apple”,”banana”,”cherry”}",
            "C": 	"(“apple”,”banana”,”cherry”)",
            "D": 	"none of the above"
        },
        15:
        {
            "A":	"list",
            "B":	"set",
            "C":	"dictionary",
            "D":	"tuple"

        },
        16:
        {
            "A":	"list",
            "B":	"set",
            "C":	"dictionary",
            "D":	"tuple"
        },
        17:
        {
            "A": 	"Type error",
            "B": 	" ",
            "C": 	"-1",
            "D": 	"Not found"
        },
        18:
        {
            "A": 	"12",
            "B": 	"64",
            "C": 	"16",
            "D": 	"36"

        },
        19:
        {
            "A":	"L.insert(2,6)",
            "B": 	"L.insert(3,6)",
            "C": 	"L.add(3,6)",
            "D": 	"L.append(2,6)"

        },
        20:
        {
            "A": 	"Numbers",
            "B": 	"String",
            "C": 	"List",
            "D": 	"Option A and B"

        },
        21:
        {
            "A": 	"Hello World!",
            "B": 	"H",
            "C": 	"ello World!",
            "D": 	"None of the above."

        },
        22:
        {
            "A":	"( 'abcd', 786 , 2.23, 'john', 70.2 )",
            "B": 	"tuple",
            "C": 	"Error",
            "D": 	"None of the above"

        },
        23:
        {
            "A": 	"||",
            "B": 	"|",
            "C": 	"//",
            "D": 	"/"

        },
        24:
        {
            "A": 	"__more__()",
            "B": 	"__gt__()",
            "C": 	"__ge__()",
            "D": 	"None of the above"

        },
        25:
        {
            "A": 	"Module",
            "B": 	"Class",
            "C": 	"Another Function",
            "D": 	"Method"

        }

    }

    answerkey = {
        1: "D",
        2: "C",
        3: "A",
        4: "D",
        5: "B",
        6: "B",
        7: "D",
        8: "B",
        9: "C",
        10: "C",
        11: "B",
        12: "B",
        13: "C",
        14: "A",
        15: "A",
        16: "B",
        17: "C",
        18: "C",
        19: "A",
        20: "D",
        21: "B",
        22: "A",
        23: "B",
        24: "D",
        25: "D"

    }

    marks = 0
    opt = StringVar()
    randomlist = random.sample(range(1, 26), 10)

    def starting():

        global quelabel, nextbutton, option1, option2, option3, option4, finished_times, optionframe, countdown

        quelabel = Label(root, text="Q"+str(n+1)+"."+questions[randomlist[n]], font=(
            "Open sans", 18, "normal"), fg="black", bg="#F0F0F2", pady=30)
        quelabel.pack(side=TOP)

        optionframe = Frame(root, bg="#F0F0F2")
        optionframe.pack()
        option1 = Radiobutton(optionframe, text="A.    "+options[randomlist[n]]['A'], variable=opt, value="A", font=(
            "Open sans", 17, "normal"), tristatevalue=0, fg="black", bg="#F0F0F2")
        option1.grid(row=0, column=0, sticky=W)

        option2 = Radiobutton(optionframe, text="B.    "+options[randomlist[n]]['B'], variable=opt, value="B", font=(
            "Open sans", 17, "normal"), tristatevalue=0, fg="black", bg="#F0F0F2")
        option2.grid(row=1, column=0, sticky=W)

        option3 = Radiobutton(optionframe, text="C.    "+options[randomlist[n]]['C'], variable=opt, value="C", font=(
            "Open sans", 17, "normal"), tristatevalue=0, fg="black", bg="#F0F0F2")
        option3.grid(row=2, column=0, sticky=W)

        option4 = Radiobutton(optionframe, text="D.    "+options[randomlist[n]]['D'], variable=opt, value="D", font=(
            "Open sans", 17, "normal"), tristatevalue=0, fg="black", bg="#F0F0F2")
        option4.grid(row=3, column=0, sticky=W)

        root.config(bg="#F0F0F2")

        nextbutton = Button(root, text="Next", font=("Cinzel", 16, "bold"),
                            bg="#F0F0F2", fg="#194159", border=0, command=nextquestion)
        nextbutton.pack(anchor=E, side=BOTTOM, padx=(10), pady=5)

        countdown = Label(root, text=timer, font=(
            "Open sans", 16, "bold"), fg="#D9BD32", bg="#F0F0F2",)
        countdown.pack(anchor=W, side=BOTTOM, padx=35, pady=0)

        timecount()

        savebutton.destroy()
        x.destroy()
        global savename
        savename = name.get()
        name.destroy()

    def reseting():
        global timer
        timer = 30

    def timecount():
        global timer
        if (timer > 0):
            timer = timer-1
            countdown.config(text=timer)
            
            countdown.after(1000, timecount)
        else:

            nextquestion()
            timecount()

    def nextquestion():
        global quelabel, finished_times, n, option1, option2, option3, option4, marks, markstoshow, namestoshow
        x = opt.get()
        if x == answerkey[randomlist[n]]:
            marks = marks+1
        n = n+1

        if n < 10:
            quelabel.config(text="Q"+str(n+1)+"."+questions[randomlist[n]])

            option1.config(text="A.    "+options[randomlist[n]]['A'])
            option1.deselect()
            option2.config(text="B.    "+options[randomlist[n]]['B'])
            option2.deselect()
            option3.config(text="C.    "+options[randomlist[n]]['C'])
            option3.deselect()
            option4.config(text="D.    "+options[randomlist[n]]['D'])
            option4.deselect()
            reseting()

        else:
            optionframe.destroy()
            quelabel.destroy()
            nextbutton.destroy()
            countdown.destroy()
            s = Label(root, text=savename.title()+" Your score is %d.       " %
                      marks, bg="#F0F0F2", font=("Open sans", 20, "bold"))
            s.pack(padx=0, pady=(200, 0))

            markstoshow.append(marks)
            namestoshow.append(savename.title())
            if (len(markstoshow) > 9):
                markstoshow.remove(markstoshow[0])
                namestoshow.remove(namestoshow[0])

            root.after(2500, root.destroy)

    x = Label(root, text="Enter your name :", bg=(
        "#F0F0F2"), font=("Open Sans", 14, "bold"))
    x.pack(side=TOP, pady=(100, 0))
    name = Entry(root, width=30, bg="#ADD8E6", font=("Open Sans", 14))
    name.pack(pady=20)
    savebutton = Button(root, text="Save", font=(
        "Cinzel", 18, "bold"), bg="#F0F0F2", fg="#194159", border=0, command=starting)
    savebutton.pack(side=BOTTOM, pady=(0, 15))


def feedback():
    bframe.pack_forget()
    pframe.pack_forget()
    global feed1, zzz, ok
    feed1 = Text(front, width=100, height=10,
                 font=("Open Sans", 12), bg="#D8F0F2")
    feed1.pack()

    def okkk():
        with open(r'feedback.txt', 'a')as file:
            file.writelines(feed1.get(1.0, END))
        feed1.delete(1.0, END)

    ok = Button(front, text='Submit feedback', command=okkk, font=(
        "Cinzel", 18, "bold"), bg="#FFFFFF", fg="#194159", border=0)
    ok.pack(pady=30)

    back_button.pack(side=BOTTOM, pady=15)
    zzz = "feedback"


def scores():
    bframe.pack_forget()
    pframe.pack_forget()

    global showmarks, showname, scoreframe

    scoreframe = Frame(front, bg="#ffffff")
    scoreframe.pack()
    nnn = Label(scoreframe, text="Name", bg="#ffffff",
                fg="black", font=("Open sans", 17, "bold"))
    nnn.grid(row=0, column=0, padx=150)
    sss = Label(scoreframe, text="Score", bg="#ffffff",
                fg="black", font=("Open sans", 17, "bold"))
    sss.grid(row=0, column=1, padx=150)
    for scoreno in range(len(markstoshow)):

        showname = Label(scoreframe, text=namestoshow[scoreno], bg="#ffffff", fg="black", font=(
            "Open Sans", 16, "normal"))
        showname.grid(row=scoreno+1, column=0, padx=150)
        showmarks = Label(scoreframe, text=markstoshow[scoreno], bg="#ffffff", fg="black", font=(
            "Open Sans", 16, "normal"))
        showmarks.grid(row=scoreno+1, column=1, padx=150)

    global zzz
    zzz = "scores"
    back_button.pack(side=BOTTOM, pady=15)


def rules():
    bframe.pack_forget()
    pframe.pack_forget()
    global rule_Label, zzz
    rule_Label = Label(front, justify=LEFT, text="There are a total of 10 questions.\nEach question carries 1 mark, for every correct answer.\nThere is no negative marking.\nThere is a 30 second time limit on every question.", font=(
        "Open Sans", 20, "normal"), bg="#ffffff", fg="#194159", pady=70)
    rule_Label.pack()
    back_button.pack(side=BOTTOM, pady=15)
    zzz = "rules"


def backbutton():
    back_button.pack_forget()
    bframe.pack(side=RIGHT)
    pframe.pack(side=LEFT)
    if (zzz == "feedback"):
        feed1.pack_forget()
        ok.pack_forget()
    elif(zzz == "rules"):
        rule_Label.pack_forget()
    elif(zzz == "scores"):
        scoreframe.pack_forget()


back_button = Button(front, text="back", font=(
    "Cinzel", 18, "bold"), command=backbutton, border=0, fg="#194159", bg="#ffffff")

img = PhotoImage(file="Front Pic.png")
pic = Label(pframe, image=img, background="#ffffff")
pic.pack(side=LEFT)
bt1 = Button(bframe, text="Start", bg="#ffffff", fg="#194159", border=0,
             padx=(50), pady=5, font=("Cinzel", 20, "bold"), command=opener)
bt1.grid(row=0, column=1)

bt2 = Button(bframe, text="Rules", bg="#ffffff", fg="#194159",
             border=0, padx=(50), pady=5, font=("Cinzel", 20, "bold"), command=rules)
bt2.grid(row=1, column=1)

bt3 = Button(bframe, text="Scores", bg="#ffffff", fg="#194159",
             border=0, padx=(50), pady=5, font=("Cinzel", 20, "bold"), command=scores)
bt3.grid(row=2, column=1)

bt4 = Button(bframe, text="Feedback", bg="#ffffff", fg="#194159",
             border=0, padx=(50), pady=5, font=("Cinzel", 20, "bold"), command=feedback)
bt4.grid(row=3, column=1)

bt5 = Button(bframe, text="Exit", bg="#ffffff", fg="#194159",
             border=0, padx=(50), pady=5, font=("Cinzel", 20, "bold"), command=exit)
bt5.grid(row=4, column=1)

mainloop()
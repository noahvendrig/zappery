import tkinter as tk
from tkinter import filedialog, Text, Image
import os

root = tk.Tk()

canvas = tk.Canvas(root, height=450, width=800, bg="#fcff38")
canvas.pack()

FirstName = "1"
SubjectCountDigit = "2"

class App():
    def __init__(self):
        self.FirstName = "1"
        self.SubjectCountDigit = "2"
    def Clear(self):
        canvas.delete("all");
    def HomeScreen(self):
        foo.Clear()

        CreateProfileLabel = tk.Label(root, text="{Create Profile}", font=('VCR OSD MONO', 50), bg="#fcff38", fg="black")
        canvas.create_window(400, 80, window=CreateProfileLabel)
        canvas.pack()

        self.NameEntry = tk.Entry(root, width=10, font=('VCR OSD MONO', 24))
        canvas.create_window(550, 200,  window=self.NameEntry)
        canvas.pack()

        NameLabel = tk.Label(root, text="First Name:", font=('VCR OSD MONO', 24), bg="#fcff38")
        canvas.create_window(250, 200, window=NameLabel)
        canvas.pack()

        self.SubjectCountEntry = tk.Entry(root, width=10, font=('VCR OSD MONO', 24))
        canvas.create_window(550, 280,  window=self.SubjectCountEntry)
        canvas.pack()

        SubjectCountLabel = tk.Label(root, text="Subject Count:", font=('VCR OSD MONO', 24), bg="#fcff38")
        canvas.create_window(250, 280, window=SubjectCountLabel)
        canvas.pack()

        ProfileCompleteButton = tk.Button(root, width=10, font=('VCR OSD MONO', 16), text="Next", command=self.HomeScreenTest) # command=self.HomeScreenTest not command=self.HomeScreenTest()
        canvas.create_window(400, 370, window=ProfileCompleteButton)
        canvas.pack()
        #def RetrieveInputSubjectCount():
        #    SubjectCountStr = self.self.NameEntry.get("1.0", "end-1c")

        #def RetrieveInputName():
        #    NameStr = self.self.NameEntry.get("1.0", "end-1c")

    def HomeScreenTest(self): 
    #    RetrieveInputSubjectCount()
    #    RetrieveInputName()
        SubjectCountStr = self.SubjectCountEntry.get()
        
        if SubjectCountStr.isdigit():
            print("digit")
            self.SubjectCountDigit = int(self.SubjectCountEntry.get()) # originally a str from input, so make it int
            self.FirstName=self.NameEntry.get()
            for i in range(self.SubjectCountDigit):
                self.SubjectSelection(i)
            #next screen goes here
        else:
            print("not digit")
            canvas.delete("CreateProfileLabel")
            CreateProfileLabel = tk.Label(root, text="{Create Profile}", font=('VCR OSD MONO', 50), bg="#fcff38",
                                            fg="red")
            canvas.create_window(400, 80, window=CreateProfileLabel)
            canvas.pack()
            CreateProfileLabel = tk.Label(root, text="Number of Subjects must be a Number.", font=('VCR OSD MONO', 20), bg="#fcff38",
                                            fg="red")
            canvas.create_window(400, 130, window=CreateProfileLabel)
            canvas.pack()

        

    def SubjectSelection(self, i):
        self.Clear()
        Subjects = []
        # [[name, colour], ]
        #
        ChooseYourSubjects = tk.Label(root, text="{Choose your}\n{subjects}", font=('VCR OSD MONO', 50), bg="#fcff38")
        canvas.create_window(400, 80, window=ChooseYourSubjects)
        canvas.pack()

        SubjectInput = tk.Entry(root, width=10, font=('VCR OSD MONO', 24))
        canvas.create_window(500, 200, window=SubjectInput)
        canvas.pack()

        SubjectChoice = tk.Label(root, text="Subject:", font=('VCR OSD MONO', 24), bg="#fcff38")
        canvas.create_window(300, 200, window=SubjectChoice)
        canvas.pack()

        clicked = tk.StringVar()
        clicked.set("Red")

        Colours = [
            "Red",
            "Orange",
            "Yellow",
            "Green",
            "Blue",
            "Pink",
            "Purple",
            "Brown",
            "Gray"
        ]

        ColourSelect = tk.OptionMenu(root, clicked, *Colours)
        ColourSelect.config(width=8, font=('VCR OSD MONO', 24), bg="#fcff38")
        canvas.create_window(500, 280, window=ColourSelect)
        canvas.pack()

        ColourLabel = tk.Label(root, text="Colour:", font=('VCR OSD MONO', 24), bg="#fcff38")
        canvas.create_window(300, 280, window=ColourLabel)
        canvas.pack()

        class Subject:
            def __init__(self, SubjectName, SubjectColour):
                self.SubjectName = SubjectName
                self.SubjectColour = SubjectColour

        def SubjectSubmission(self):
            SubjectStr = SubjectInput.get()
            ColourStr = clicked.get()
            NewSubject = Subject(SubjectStr, ColourStr)
            Subjects.append(NewSubject)

            print(Subjects)

        NextSubjectButton = tk.Button(root, width=16, font=('VCR OSD MONO', 16), text="Next Subject", command=SubjectSubmission(self))
        canvas.create_window(400, 370, window=NextSubjectButton)
        canvas.pack()


foo = App()
foo.Clear()
foo.HomeScreen()

#AgeEntry = tk.Entry(root, width=10, font=('VCR OSD MONO', 24))
#canvas.create_window(450, 350,  window=AgeEntry)
#canvas.pack()

#AgeLabel = tk.Label(root, text="Age", font=('VCR OSD MONO', 24), bg="#fcff38")
#canvas.create_window(250, 350, window=AgeLabel)
#canvas.pack()

#GenderEntry = tk.Entry(root, width=10, font=('VCR OSD MONO', 24))
#canvas.create_window(450, 450,  window=GenderEntry)
#canvas.pack()

#GenderLabel = tk.Label(root, text="Gender", font=('VCR OSD MONO', 24), bg="#fcff38")
#canvas.create_window(250, 450, window=GenderLabel)
#canvas.pack()

#clicked = StringVar()

#drop = GenderOptions(root, clicked, "Male", "Female", "Non Binary", )
#drop.pack()
#canvas.pack()

root.mainloop()
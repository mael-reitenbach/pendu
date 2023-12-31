from tkinter import *
import time
import random
from functools import partial
import re

root = Tk()

#hangman steps
step0 = " +---+\n |     |\n       |\n       |\n       |\n       |\n========="
step1 = " +---+\n |     |\n O     |\n       |\n       |\n       |\n========="
step2 = " +---+\n |     |\n O     |\n |     |\n       |\n       |\n========="
step3 = " +---+\n |     |\n O     |\n/|     |\n       |\n       |\n========="
step4 = " +---+\n |     |\n O     |\n/|\    |\n       |\n       |\n========="
step5 = " +---+\n |     |\n O     |\n/|\    |\n/      |\n       |\n========="
step6 = " +---+\n |     |\n O     |\n/|\    |\n/ \    |\n       |\n========="
steps = [step0, step1, step2, step3, step4, step5, step6]


#functions
def validation():
    mot_a_test = str(word_input.get())
    if mot_a_test.isalpha() == False:
        explanation_text.config(text="Pas d'accents, de chiffres, ou de charactères spéciaux!")
        print("Pas alpha")
    else:
        mooot = mot_a_test.lower()
        test_mooot = mooot + "\n"
        with open('mots.txt', 'r') as f:
            lines = f.readlines()
            print(lines)
            if test_mooot in lines:
                print("le mot existe deja")
                add_click()
            else:
                with open("mots.txt", "a") as f:
                    f.write(f"{mooot}\n")
        

def valider():
    global n
    global list_lettres
    global phrase_presentation
    lettre_a_test = str(lettre_input.get())
    if len(lettre_a_test) > 1:
        explication_text.config(text = "Écrivez ->UNE<- lettre :")
    if lettre_a_test.isalpha() == False:
        explication_text.config(text = "Écrivez une ->LETTRE<- :")
    if lettre_a_test.lower() in word:
        print("Bien ouej")
        

        def findOccurrences(s, ch):
            return [i for i, letter in enumerate(s) if letter == ch]
        
        emplacement_lettres = findOccurrences(word, lettre_a_test)
        print(emplacement_lettres)

        for i in emplacement_lettres:
            if i == 0:
                tem_lis = list(phrase_presentation)
                tem_lis[0] = lettre_a_test.upper()
                phrase_presentation = ''.join(tem_lis)
            else:
                g = i*2
                tem_list = list(phrase_presentation)
                tem_list[g] = lettre_a_test.upper()
                phrase_presentation = ''.join(tem_list)
        
        guess.config(text=phrase_presentation)
        if phrase_presentation.find("_") == -1 :
            explication_text.config(text = "BRAVO !")
            valid_button.grid_remove()
            lettre_input.grid_remove()
            play_button.config(text="Play Again", padx=100, pady=50)
            play_button.grid(row=3, column=1)
      

    else:
        n += 1
        if n > 6:
            explication_text.config(text= "T'A PERDU CHEH")
            pendu.grid_forget()
            valid_button.grid_remove()
            lettre_input.grid_remove()
            guess.grid_remove()
            print("perdu")
            n = 0
            play_button.config(text="Play Again", padx=100, pady=50)
            play_button.grid(row=3, column=1)
            #time.sleep(10)
            #exit()

            
        pendu.config(text=steps[n])
        print("non deso")
    print(word)
    print(lettre_a_test)
    

def play_click():
    global phrase_presentation
    explication_text.config(text="Écrivez une lettre :")
    play_button.grid_remove()
    add_button.grid_remove()
    pad1.grid_remove()
    pad2.grid_remove()
    pad3.grid_remove()
    pad4.grid_remove()
    pad5.grid_remove()
    with open('mots.txt', 'r') as f:
        global word
        global phrase_presentation
        lines = f.readlines()
        d = len(lines) - 2
        select = random.randint(0,d)
        word = str(lines[select])
        print(word)
        e = len(word) - 1
        phrase_presentation = "_ "*e
        guess.config(text=phrase_presentation)
        pendu.grid(row=0, column=1)
        guess.grid(row=1, column=1)
        
        #padding
        pad1.grid(row=0, column=0)
        pad2.grid(row=0, column=2)
        pad6.grid(row=1, column=0)
        pad7.grid(row=1,column=2)
        pad8.grid(row=2, column=0)
        pad9.grid(row=2, column=2)
        pad10.grid(row=3, column=0)

        explication_text.grid(row=2, column=1, pady=10)
        lettre_input.grid(row=3, column=1)
        valid_button.grid(row=3, column=2)
        print("ca continue")
        


def add_click():
    global phrase_presentation
    explanation_text.config(text="Écrivez une lettre :")
    play_button.grid_remove()
    add_button.grid_remove()
    pad1.grid_remove()
    pad2.grid_remove()
    pad3.grid_remove()
    pad4.grid_remove()
    pad5.grid_remove()
    word_input.grid(row=1, column=0)
    explanation_text.grid(row=0, column=0)
    valid_input.grid(row=1, column=1)



#Padding Widgets
pad1 = Label(root, text=" ")
pad2 = Label(root, text=" ")
pad3 = Label(root, text="  ")
pad4 = Label(root, text="  ")
pad5 = Label(root, text="  ")
pad6 = Label(root, text=" ")
pad7 = Label(root, text=" ")
pad8 = Label(root, text=" ")
pad9 = Label(root, text=" ")
pad10 = Label(root, text=" ")
pad11 = Label(root, text=" ")
pad12 = Label(root, text=" ")
pad13 = Label(root, text=" ")
pad14 = Label(root, text=" ")


#Necessary widgets
n = 0

phrase_presentation = ""

list_lettres = []

emplacement_lettres = []

play_button = Button(root, text="Play", command=play_click, padx=200, pady=100)

add_button = Button(root, text="Add a word", command=add_click, padx=200, pady=100)

menu_button = Button(root, text="Back to menu")

valid_button = Button(root, text="Valider", command= lambda: valider())

lettre_input = Entry(root, width=-10)

word_input = Entry(root)

valid_input = Button(root, text="Valider", command=validation)

explication_text = Label(root, text="Écrivez une lettre :")

explanation_text = Label(root, text="Écrivez un mot (sans accents)")

pendu = Label(root, text=steps[n])

guess = Label(root, text="")

#Appear on screen
play_button.grid(row=3, column=1)

add_button.grid(row=3, column=3)

#Padding on screen
pad1.grid(row=1, column=1)
pad2.grid(row=4, column=1)
pad3.grid(row=3, column=0)
pad4.grid(row=3, column=2)
pad5.grid(row=3, column=4)


root.mainloop()
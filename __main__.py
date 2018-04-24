from tkinter import *
from tkinter import ttk
import sys, random
from tkinter import  messagebox

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    myMessage = vv.get()
    myKey = 'HWERTUYIOPQSDFGAJKLZXCVBNM'
    myMode = v.get()

    if myMode == 'mode22':
        translated = encryptMessage(myKey, myMessage)
        vvv.set(translated)
    elif myMode == 'mode23':
        translated = decryptMessage(myKey, myMessage)
        vvv.set(translated)
    else:
        messagebox.showerror(title='Warning', message='Please select the encryption type')

    checkValidKey(myKey)


def checkValidKey(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        sys.exit('There is an error in the key or symbol set.')

def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA

    # loop through each symbol in the message
    for symbol in message:
        if symbol.upper() in charsA:
            # encrypt/decrypt the symbol
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # symbol is not in LETTERS, just add it
            translated += symbol

    return translated


def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


def close():
    exit()

window = Tk()
window.title("Encrypt Messages")
window.configure(background="#006266")
window.geometry("600x470+380+150")
style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', background="#bdc3c7", foreground="#2c3e50", )


Label(window, text="Select encryption type", bg="#006266", fg="white", pady=12).pack()
v = StringVar()
mode = Entry(window, width=20, textvariable=v,).pack()

Label(window, text="Selet Your Message", bg="#006266", fg="white", pady=12).pack()
vv = StringVar()
messageBox = Entry(window, width=40, textvariable=vv).pack(ipady=30)

ttk.Button(window, text="Enceypet", command = main , ).pack(pady=12)

Label(window, text="This is Your Message", bg="#006266", fg="white", pady=12).pack()
vvv = StringVar()
outbput = Entry(window, width=40, textvariable=vvv).pack(ipady=30)

ttk.Button(window, text="Exit", command = close  ).pack(pady=12)

window.mainloop()
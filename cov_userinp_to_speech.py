from gtts import gTTS
import os

from tkinter import *

root = Tk()
root.title("Rahul speech converter")
canvas = Canvas(root, width=400, height=300)
canvas.pack()


heading = Label(text="Text to Speech Converter", font=("Arial", 14))
canvas.create_window(200, 50, window=heading)


def texttospeech():
    text = entry.get()
    output = gTTS(text=text, lang="en", slow=False)
    output.save("output1.mp3")
    os.system("start output1.mp3")


entry = Entry(root, width=50, font=("Arial", 12), justify=CENTER)
canvas.create_window(200, 180, window=entry, height=80)

button = Button(text="Enter", command=texttospeech)
canvas.create_window(200, 270, window=button)

root.mainloop()

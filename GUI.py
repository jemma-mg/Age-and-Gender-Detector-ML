# Importing necessary libraries

from keras.models import load_model
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np

# Loading the Model
model = load_model("Age_Gender_Detection.h5")

# Initializing the GUI
top = tk.Tk()
top.geometry("800x600")
top.title("Age and Gender Detector")
top.configure(background="#CDCDCD")

# Initilalizing the labels for age and gender
label1 = Label(top, background="#CDCDCD", font=("arial", 15, "bold"))
label2 = Label(top, background="#CDCDCD", font=("arial", 15, "bold"))
sign_image = Label(top)

# Defining detect function which detects the age and gender of person in image using the model


def detect(file_path):
    global Label_packed
    image = Image.open(file_path)
    image = image.resize((48, 48))
    image = np.expand_dims(image, axis=0)
    image = np.array(image)
    image = np.delete(image, 0, 1)
    image = np.resize(image, (48, 48, 3))
    print(image.shape)
    genders = ["Male", "Female"]
    image = np.array([image])/255
    pred = model.predict(image)
    age = int(np.round(pred[1][0]))
    gender = int(np.round(pred[0][0]))
    print("Predicted Age is "+str(age))
    print("Predicted Gender is "+genders[gender])
    label1.configure(foreground="#011638", text=age)
    label2.configure(foreground="#011638", text=genders[gender])

# Defining show detect button function


def show_detect(file_path):
    detect_btn = Button(top, text="Detect Image",
                        command=lambda: detect(file_path), padx=10, pady=5)
    detect_btn.configure(background="#364156",
                         foreground='white', font=("arial", 10, "bold"))
    detect_btn.place(relx=0.79, rely=0.46)

# Defining upload image function


def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(
            ((top.winfo_width()/2.25), (top.winfo_height()/2.25)))
        img = ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=img)
        sign_image.image = img
        label1.configure(text='')
        label2.configure(text='')
        show_detect(file_path)

    except:
        label1.configure(foreground="#011638",
                         text="Oops!, file upload failed")
        print("Oops!, file upload failed")


upload_btn = Button(top, text="Upload an Image",
                    command=upload_image(), padx=10, pady=5)
upload_btn.configure(background="#364156", foreground="white",
                     font=("arial", 10, "bold"))
upload_btn.pack(side="bottom", pady=50)
sign_image.pack(side="bottom", expand=True)
label1.pack(side="bottom", expand=True)
label2.pack(side="bottom", expand=True)
heading = Label(top, text="Age and Gender Detector",
                pady=20, font=("arial", 30, "bold"))
heading.configure(background="#CDCDCD", foreground="#364156")
heading.pack()
top.mainloop()

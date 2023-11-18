import tkinter as tk
from datetime import datetime
import time
import csv
import random 
from jokes import chuck_norris_jokes as default_jokes

now = datetime.now()
nums = ["1", "2", "3", "4", "5"]

def get_date():
    return now.strftime("%d-%b"),now.time().strftime("%I:%M")

def submit(button,selected_value):
    button.config(state=tk.DISABLED)
    value = selected_value.get()
    mood = ["Very Bad","Bad","Neutral","Good","Very Good"]
    if value not in nums:
        pass
    else:
        date,time=get_date()
        mood =mood[int(value)-1]
        joke = joke_of_the_day()
        query_complete(date,time, mood,joke)

def gui():
    
    root = tk.Tk()
    root.geometry("300x400")
    root.title("H.A.Y bot")
    


    selected_value = tk.StringVar()

    label = tk.Label(root, text="How are you from a scale of one to five?").pack()

    radio_button_1 = tk.Radiobutton(root, text="1. Very Bad", variable=selected_value, value="1").pack(anchor=tk.W)
    radio_button_2 = tk.Radiobutton(root, text="2. Bad", variable=selected_value, value="2").pack(anchor=tk.W)
    radio_button_3 = tk.Radiobutton(root, text="3. Neutral", variable=selected_value, value="3").pack(anchor=tk.W)
    radio_button_4 = tk.Radiobutton(root, text="4. Good", variable=selected_value, value="4").pack(anchor=tk.W)
    radio_button_5 = tk.Radiobutton(root, text="5. Very Good", variable=selected_value, value="5").pack(anchor=tk.W)
    button = tk.Button(root, text="Submit", command=lambda: submit(button,selected_value))
    button.pack()

    root.mainloop()

def joke_of_the_day():
    import tkinter.messagebox
    palceholder_joke = random.choice(default_jokes)
    tkinter.messagebox.showinfo('Joke of the Day',palceholder_joke )
    return palceholder_joke 


def query_complete(date,time, mood,joke):
    with open("logs.csv", "a", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([date,time, mood,joke])
    program_exit()
    
def program_exit():
    time.sleep(2)
    exit()

if __name__ == "__main__":
    gui()

from tkinter import *
from timeit import default_timer as timer
import random

root = Tk()
root.geometry("450x200")
counter = 0

def game_session():
    global counter
    if counter == 0:
        root.destroy()
        counter += 1

    def validate_input():
        if input_field.get() == word_list[word_index]:
            end_time = timer()
            elapsed_time = end_time - start_time
            print(f"Elapsed time: {elapsed_time:.2f} seconds")
        else:
            print("Incorrect input")

    word_list = ['different', 'multiplication', 'algorithm', 'codewithrashel', 'python', 'intern']

    word_index = random.randint(0, len(word_list) - 1)
    start_time = timer()
    game_window = Tk()
    game_window.geometry("450x200")

    word_label = Label(game_window, text=word_list[word_index], font="times 20")
    word_label.place(x=150, y=10)

    instruction_label = Label(game_window, text="Start Typing", font="times 20")
    instruction_label.place(x=10, y=50)

    input_field = Entry(game_window)
    input_field.place(x=280, y=55)

    submit_button = Button(game_window, text="Done", command=validate_input, width=12, bg='pink')
    submit_button.place(x=150, y=100)

    retry_button = Button(game_window, text="Try Again", command=game_session, width=12,bg='pink')
    retry_button.place(x=250, y=100)

    game_window.mainloop()

start_label = Label(root, text="Let's begin the challenge..", font="times 20")
start_label.place(x=10, y=50)

start_button = Button(root, text="Start", command=game_session, width=12, bg='pink')
start_button.place(x=150, y=100)

root.mainloop()

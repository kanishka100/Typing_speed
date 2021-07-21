import math
import random
import timeit
import tkinter as tk
from tkinter import messagebox


class Front_Page:
    def __init__(self):
        self.top = tk.Tk()
        self.top.config(bg='black')
        self.top.geometry('400x280')
        self.top.title('Typing Speed Calculator')
        welcome = tk.Label(self.top, text='Welcome', font=('FreeMono', 30), fg='yellow', bg='black')
        welcome.pack(pady=20)
        label1 = tk.Label(self.top, text='Please type for at least 1 minute to get accurate results\n\n'
                                         'Note:\n'
                                         'Gross speed = Total no.of words typed/Time taken\n'
                                         'Net speed = Correct words/Time taken'
                          , wraplength=350,
                          font=('FreeMono', 11), fg='white', bg='black')
        label1.pack()
        btn = tk.Button(self.top, text='Go', width=15, font=('Times of roman', 10),
                        fg='white', bg='blue', command=self.go)
        btn.pack(pady=20)
        self.top.mainloop()

    def go(self):
        self.top.destroy()
        obj = Main_Page()


class Main_Page:

    def __init__(self):

        self.correct_word = 0
        self.incorrect_word = 0
        self.time_list = []
        self.begin = 0
        self.root = tk.Tk()
        self.root.after(1, lambda: self.root.focus_force())

        self.root.config(bg='black', pady=20)
        self.root.geometry('350x260')
        self.root.title('Typing Speed Calculator')
        self.words = ['spiked', 'green', 'support', 'iguana', 'church', 'happy', 'corona', 'spectrum', 'lasting',
                      'sometimes', 'cheating', 'think', 'paint', 'dries', 'quicker', 'paint', 'handsome', 'anime',
                      'noticed', 'could', 'water', 'change', 'temperature', 'movies', 'dramas', 'joyful', 'celebrate',
                      'chocolate', 'flavor', 'lucifer', 'surprise', 'amount', 'death', 'valley',
                      'country', 'father', 'winter', 'secret', 'created', 'sense', 'insist', 'clean', 'closet',
                      'drive', 'encounter', 'disneyland', 'maize', 'first', 'experience', 'money', 'eyeing',
                      'raised', 'crackers', 'marriage', 'shoulders',
                      'excess', 'peanut', 'butter', 'crowds', 'mother', 'gloves',
                      'tsunami', 'rabbit', 'depths', 'library', 'pizza', 'hardship']

        self.random_word = (random.choice(self.words))

        # word label
        self.label = tk.Label(self.root, text=self.random_word,
                              font=('Times of roman', 20, 'bold'), fg='cyan', bg='black')
        self.label.pack(pady=10)
        self.text = tk.StringVar()

        self.ent1 = tk.Entry(self.root, width=17, textvariable=self.text,
                             bg='white', font=('Times of roman', 12, 'normal'))
        self.ent1.focus_set()
        self.ent1.pack(pady=10)

        self.begin = timeit.default_timer()
        self.root.bind('<Return>', self.show)
        stop_button = tk.Button(self.root, text='Stop Typing',
                                bg='blue', fg='white', command=self.stop_typing, width=20)
        stop_button.pack(pady=10)

        self.results = tk.Label(self.root, text=" ", bg='black', fg='white',
                                font=('Times of roman', 10))
        self.results.pack(pady=10)

        self.root.mainloop()

    def refresh(self):
        random.shuffle(self.words)
        self.random_word = random.choice(self.words)
        self.label.config(text=self.random_word)
        self.ent1.delete(0, tk.END)
        self.text.set("")
        self.begin = timeit.default_timer()

    def show(self, event):
        sentence = self.text.get()
        if self.text.get() == "":
            messagebox.showerror('Typing Speed', 'Please enter the word')
            timer = 0
        elif sentence == self.random_word:
            self.correct_word += 1
            self.time_list.append(round(timeit.default_timer() - self.begin, 4))
            self.refresh()
        else:
            self.incorrect_word += 1
            self.time_list.append(round(timeit.default_timer() - self.begin, 4))
            self.ent1.delete(0, tk.END)
            self.refresh()

    def stop_typing(self):
        self.begin = 0

        total = self.correct_word + self.incorrect_word
        time_in_minutes = sum(self.time_list) / 60
        try:
            gross_wpm = total / time_in_minutes
            net_speed = (total - self.incorrect_word) / time_in_minutes
            accuracy = (net_speed / gross_wpm) * 100
        except ZeroDivisionError:
            messagebox.showinfo('Speed Typing', 'Timer stopped')

        else:
            self.results.config(text=f'Gross Speed in WPM :{math.floor(gross_wpm)} WPM\n'
                                     f'Net speed in WPM: {math.floor(net_speed)} WPM\n'
                                     f'Accuracy: {round(accuracy, 2)}% ⌨')


obj = Front_Page()

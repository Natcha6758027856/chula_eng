Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import tkinter as tk
import random

# Thai consonants and their names
thai_consonants = [
...     ("ก", "gor kai"), ("\u0e02", "khor khai"), ("\u0e03", "khor khuad"),
...     ("\u0e04", "khor khwai"), ("\u0e05", "khor khon"), ("\u0e06", "khor rakhang"),
...     ("\u0e07", "ngor ngu"), ("\u0e08", "jor jan"), ("\u0e09", "chor ching"),
...     ("\u0e0a", "chor chang"), ("\u0e0b", "sor so"), ("\u0e0c", "chor cher"),
... ]
... 
... class FlashcardApp:
...     def __init__(self, root):
...         self.root = root
...         self.root.title("Thai Consonant Flashcards")
...         
...         self.current_card = None
...         
...         self.label = tk.Label(root, text="", font=("Arial", 100))
...         self.label.pack(pady=50)
...         
...         self.flip_button = tk.Button(root, text="Flip", command=self.flip_card, font=("Arial", 14))
...         self.flip_button.pack()
...         
...         self.next_button = tk.Button(root, text="Next", command=self.next_card, font=("Arial", 14))
...         self.next_button.pack()
...         
...         self.next_card()
...     
...     def next_card(self):
...         self.current_card = random.choice(thai_consonants)
...         self.label.config(text=self.current_card[0])
...     
...     def flip_card(self):
...         if self.current_card:
...             self.label.config(text=self.current_card[1])
... 
... if __name__ == "__main__":
...     root = tk.Tk()
...     app = FlashcardApp(root)
...     root.mainloop()

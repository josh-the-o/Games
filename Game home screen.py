import tkinter as tk

root = tk.Tk()
root.title("Main Menu")
root.geometry("1000x800")
root.configure(bg="#9c3ddb")

label = tk.Label(root, text="Main Menu", bg="#164980", fg="#3ac990", font=("Calibri", 100, "bold"))
label.pack(pady=20)



def play():
    print("Play button")
    class VendingMachine:
        def __init__(self):
            self.balance = 10.0
            self.snacks = {
                "Ramen1": 3,
                "Ramen2": 4,
                "Ramen3": 2,
                "Ramen4": 5,
                "Ramen5": 3
            }










def restore():
    print("Restore button")

def quit_game():
    root.destroy()

button1= tk.Button(root, text="Play", command=play, bg="gray", fg="#3ac990", font=("Calibri", 70))
button1.pack(pady=10)

button2 = tk.Button(root, text="Restore", command=restore, bg="gray", fg="#3ac990", font=("Arial", 70))
button2.pack(pady=10)

button3 = tk.Button(root, text="Quit", command=quit_game, bg="gray", fg="#3ac990", font=("Arial", 70))
button3.pack(pady=10)

root.mainloop()
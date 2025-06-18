import tkinter as tk
from tkinter import messagebox

class VendingMachine:
    def __init__(self, master):
        self.master = master
        self.ramen = {
            "Plain Ramen Base": 3.00,
            "Carbonara Ramen Base": 3.00,
            "Spicy Ramen Base": 3.00,
            "EXTREME! Heat Ramen Base": 3.00
        }
        
        self.toppings = {
            "Chili Oil": 1.50,
            "Fried Egg": 1.50,
            "Kimchi": 1.00,
            "Steak": 3.50,
            "Pork": 3.50
        }
        
        self.balance = 0
        self.ramen_purchased = False  # Flag to check if ramen base is purchased

        # Create GUI components
        self.balance_label = tk.Label(master, text="Balance: $0.00", font=("Calibri", 30))
        self.balance_label1 = tk.Label(master, text="""\f
         / \ / \ / \ / \ / \   / \ / \ / \ / \ / \ 
        ( R | a | m | m | y ) ( V | e | n | d | i )
        \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/

                                                                          """)
        self.balance_label1.pack()
        self.balance_label.pack()

        self.ramen_frame = tk.Frame(master)
        self.ramen_frame.pack()
        
        self.toppings_frame = tk.Frame(master)
        self.toppings_frame.pack()

        self.ramen_buttons = []
        for i, (ramen, price) in enumerate(self.ramen.items()):
            button = tk.Button(self.ramen_frame, text=f"{ramen} - ${price:.2f}", command=lambda ramen=ramen, price=price: self.select_ramen(ramen, price))
            button.grid(row=i, column=0)
            self.ramen_buttons.append(button)
            button.config(bg='lightcoral')
            
        self.toppings_buttons = []
        for i, (toppings, price) in enumerate(self.toppings.items()):
            button = tk.Button(self.toppings_frame, text=f"{toppings} - ${price:.2f}", command=lambda toppings=toppings, price=price: self.select_toppings(toppings, price))
            button.grid(row=i, column=0)
            self.toppings_buttons.append(button)
            button.config(bg='lightcoral')

        self.insert_money_entry = tk.Entry(master, width=10)
        self.insert_money_entry.pack()

        self.insert_money_button = tk.Button(master, text="Insert Money", command=self.insert_money)
        self.insert_money_button.pack()

        self.refund_button = tk.Button(master, text="Refund", command=self.refund)
        self.refund_button.pack()

    def insert_money(self):
        try:
            amount = float(self.insert_money_entry.get())
            if amount <= 0:
                messagebox.showerror("Error", "Invalid amount. Please enter a positive value.")
            else:
                self.balance += amount
                self.balance_label.config(text=f"Balance: ${self.balance:.2f}")
                self.insert_money_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid amount.")

    def select_toppings(self, toppings, price):
        if not self.ramen_purchased:
            messagebox.showerror("Error", "Please select a ramen base first!")
            return
        if self.balance >= price:
            self.balance -= price
            self.balance_label.config(text=f"Balance: ${self.balance:.2f}")
            messagebox.showinfo("Success", f"Dispensing {toppings}. Enjoy!")
        else:
            messagebox.showerror("Error", "Insufficient balance. Please insert more money.")
    
    def select_ramen(self, ramen, price):
        if self.balance >= price:
            self.balance -= price
            self.balance_label.config(text=f"Balance: ${self.balance:.2f}")
            messagebox.showinfo("Success", f"Dispensing {ramen}. Enjoy!")
            self.ramen_purchased = True  # Set flag to True when ramen is purchased
        else:
            messagebox.showerror("Error", "Insufficient balance. Please insert more money.")
            

    def refund(self):
        if self.balance > 0:
            messagebox.showinfo("Success", f"Refunding ${self.balance:.2f}.")
            self.balance = 0
            self.balance_label.config(text="Balance: $0.00")
        else:
            messagebox.showerror("Error", "No balance to refund.")
        self.ramen_purchased = False  # Reset ramen purchased flag on refund

root = tk.Tk()
root.geometry('500x900')
root.title("Vending Machine")
vending_machine = VendingMachine(root)
root.configure(bg='pink')
root.mainloop()

import tkinter as tk
from tkinter import messagebox

class QuickEatsApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quick Eats")
        
        # Initialize variables
        self.burger_menu_number = tk.StringVar()
        self.delivery_address = tk.StringVar()
        
        # Create widgets
        self.label1 = tk.Label(master, text="Select Burger Menu Number:")
        self.label2 = tk.Label(master, text="Enter Delivery Address:")
        self.entry1 = tk.Entry(master, textvariable=self.burger_menu_number)
        self.entry2 = tk.Entry(master, textvariable=self.delivery_address)
        self.button_order = tk.Button(master, text="Place Order", command=self.place_order)
        self.button_exit = tk.Button(master, text="Exit", command=master.destroy)
        
        # Layout widgets
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        self.entry1.grid(row=0, column=1, padx=10, pady=10)
        self.label2.grid(row=1, column=0, padx=10, pady=10)
        self.entry2.grid(row=1, column=1, padx=10, pady=10)
        self.button_order.grid(row=2, column=0, columnspan=2, pady=10)
        self.button_exit.grid(row=3, column=0, columnspan=2, pady=10)
    
    def place_order(self):
        burger_menu_number = self.burger_menu_number.get()
        delivery_address = self.delivery_address.get()
        
        if burger_menu_number and delivery_address:
            # Implement order processing logic here
            # Display order confirmation, send to the kitchen, etc.
            messagebox.showinfo("Order Placed", f"Order for Burger #{burger_menu_number} will be delivered to {delivery_address}.")
        else:
            messagebox.showerror("Error", "Please fill in all the details.")

# Create the main window
root = tk.Tk()
app = QuickEatsApp(root)

# Start the GUI event loop
root.mainloop()

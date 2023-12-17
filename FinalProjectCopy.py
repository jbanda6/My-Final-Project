import tkinter as tk
from tkinter import messagebox

class QuickEatsApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quick Eats")

        # Load images
        self.burger_image = tk.PhotoImage(file="burger2.gif")
        self.delivery_image = tk.PhotoImage(file="map2.gif")

        # Load images for the second window
        self.menu_image1 = tk.PhotoImage(file="BurgerMeal1.gif")
        self.menu_image2 = tk.PhotoImage(file="BurgerMeal2.gif")

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
        self.button_show_second_window = tk.Button(master, text="Show Menu", command=self.show_menu)

        # Display images
        self.label_burger_image = tk.Label(master, image=self.burger_image)
        self.label_delivery_image = tk.Label(master, image=self.delivery_image)

        # Layout widgets
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        self.entry1.grid(row=0, column=1, padx=10, pady=10)
        self.label_burger_image.grid(row=0, column=2, padx=10, pady=10)
        
        self.label2.grid(row=1, column=0, padx=10, pady=10)
        self.entry2.grid(row=1, column=1, padx=10, pady=10)
        self.label_delivery_image.grid(row=1, column=2, padx=10, pady=10)
        
        self.button_order.grid(row=2, column=0, columnspan=2, pady=10)
        self.button_show_second_window.grid(row=3, column=0, columnspan=2, pady=10)
        self.button_exit.grid(row=4, column=0, columnspan=2, pady=10)

    def place_order(self):
        burger_menu_number = self.burger_menu_number.get()
        delivery_address = self.delivery_address.get()

        if burger_menu_number and delivery_address:
            # Implement order processing logic here
            # Display order confirmation, send to the kitchen, etc.
            self.show_order_confirmation(burger_menu_number, delivery_address)
        else:
            messagebox.showerror("Error", "Please fill in all the details.")

    def show_order_confirmation(self, burger_menu_number, delivery_address):
        
        confirmation_message = f"Order for Burger #{burger_menu_number} will be delivered to {delivery_address}."
        messagebox.showinfo("Order Placed", confirmation_message)

    def show_menu(self):
        menu_window = tk.Toplevel(self.master)
        menu_window.title("Menu")

        # Display images in the second window
        label_image1 = tk.Label(menu_window, image=self.menu_image1)
        label_image2 = tk.Label(menu_window, image=self.menu_image2)

        # Layout images
        label_image1.grid(row=0, column=0, pady=10)
        label_image2.grid(row=1, column=0, pady=10)

# Create the main window
root = tk.Tk()
app = QuickEatsApp(root)

# Start the GUI event loop
root.mainloop()


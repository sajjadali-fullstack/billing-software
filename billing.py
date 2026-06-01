from tkinter import *

#                            1. Window Set-Up

root = Tk()  # main window
root.title("Welcome to Billing Software")  # Title Software name
root.geometry("400x500")
root.config(bg="#5E91F7")

#                            2. Text & Entry Boxes [user Input fields]

# Items Label
Label(root, text="Items Name", bg="lightblue").pack()
item_entry = Entry(root)
item_entry.pack()

# Qty Label
Label(root, text="Quantity", bg="lightblue").pack()
quantity_entry = Entry(root)
quantity_entry.pack()

# price Label
Label(root, text="Price", bg="lightblue").pack()
price_entry = Entry(root)
price_entry.pack()

# Discount Label
Label(root, text="Discount", bg="lightblue").pack()
discount_price = Entry(root)
discount_price.pack()

# GST Label
Label(root, text="GST", bg="lightblue").pack()
gst_discount = Entry(root)
gst_discount.pack()


#                            3. Billing calculation logic
def calculate_bill():
    quantity = int(quantity_entry.get())
    price = float(price_entry.get())
    gst = float(gst_discount.get())
    discount = float(discount_price.get())

    total = quantity * price  # 2 items * 100 = 200
    discount_amount = total * discount / 100  # 200 ka 10% = 20
    total_after_discount = total - discount_amount  # 200 - 20 = 180
    gst_amount = total_after_discount * gst / 100  # 180 ka 18% = 32.4
    final_bill = total_after_discount + gst_amount  # 180 + 32.4 = 212.4

    result_label.config(text=f"Total Bill Is : {final_bill:.2f}")


#                                4. Buttons & Output Labels

Button(root, text="Calculate Bill", command=calculate_bill, bg="green", fg="white").pack(pady=12)
result_label = Label(root, text="", bg="#5E91F7", font=("Arial", 12, "bold"))
result_label.pack()


def clear_data():
    item_entry.delete(0, END)
    quantity_entry.delete(0, END)
    price_entry.delete(0, END)
    discount_price.delete(0, END)
    gst_discount.delete(0, END)
    result_label.config(text='')


Button(root, text="clear", command=clear_data, bg="red", fg="white").pack(pady=5)


def backspace():
    widget = root.focus_get()
    if isinstance(widget, Entry):
        widget.delete(len(widget.get()) - 1, END)


Button(root, text="Backspace", command=backspace, bg='orange').pack(pady=5)


mainloop()  # Window ko run karta hai

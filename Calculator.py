import customtkinter as ctk
from tkinter import messagebox
import math

root = ctk.CTk()
root.title("Calculator")
root.geometry("620x580") 
root.configure(fg_color="#242424")

history_list = []

def add_to_box(char):
    my_box.insert(ctk.END, char)

def calculate_result():
    try:
        original = my_box.get()
        content = original.replace('π', str(math.pi))
        content = content.replace('SIN', 'math.sin').replace('COS', 'math.cos').replace('TAN', 'math.tan')
        
        result = eval(content)
        final_res = str(round(result, 8))
        
        my_box.delete(0, ctk.END)
        my_box.insert(ctk.END, final_res)
        
   
        history_list.append(f"{original} = {final_res}")
        update_history()
    except Exception:
        messagebox.showerror("Error", "Invalid Expression")

def update_history():
    history_box.configure(state="normal")
    history_box.delete("1.0", ctk.END)
    for entry in reversed(history_list):
        history_box.insert(ctk.END, entry + "\n" + "-"*15 + "\n")
    history_box.configure(state="disabled")

def toggle_sign():
    content = my_box.get()
    if not content: return
    if content.startswith('-'):
        my_box.delete(0)
    else:
        my_box.insert(0, '-')

def clear():
    my_box.delete(0, ctk.END)


my_box = ctk.CTkEntry(root, width=280, height=50, font=("Arial", 24), justify="right", corner_radius=10)
my_box.place(x=25, y=50)


ctk.CTkLabel(root, text="HISTORY", font=("Arial", 14, "bold"), text_color="orange").place(x=340, y=20)
history_box = ctk.CTkTextbox(root, width=240, height=480, corner_radius=10, fg_color="#1a1a1a", state="disabled")
history_box.place(x=340, y=50)


btn_p = {"width": 60, "height": 60, "corner_radius": 30, "font": ("Arial", 14, "bold")}


button_sin = ctk.CTkButton(root, text="SIN", fg_color="#D4D4D2", text_color="black", command=lambda: add_to_box("SIN("), **btn_p)
button_sin.place(x=25, y=140)
button_cos = ctk.CTkButton(root, text="COS", fg_color="#D4D4D2", text_color="black", command=lambda: add_to_box("COS("), **btn_p)
button_cos.place(x=95, y=140)
button_tan = ctk.CTkButton(root, text="TAN", fg_color="#D4D4D2", text_color="black", command=lambda: add_to_box("TAN("), **btn_p)
button_tan.place(x=165, y=140)
button_π = ctk.CTkButton(root, text="π", fg_color="#D4D4D2", text_color="black", command=lambda: add_to_box("π"), **btn_p)
button_π.place(x=235, y=140)


button1 = ctk.CTkButton(root, text="1", fg_color="#505050", text_color="white", command=lambda: add_to_box("1"), **btn_p)
button1.place(x=25, y=210)
button2 = ctk.CTkButton(root, text="2", fg_color="#505050", text_color="white", command=lambda: add_to_box("2"), **btn_p)
button2.place(x=95, y=210)
button3 = ctk.CTkButton(root, text="3", fg_color="#505050", text_color="white", command=lambda: add_to_box("3"), **btn_p)
button3.place(x=165, y=210)
button_clear = ctk.CTkButton(root, text="C", fg_color="#FF9500", text_color="white", command=clear, **btn_p)
button_clear.place(x=235, y=210)


button4 = ctk.CTkButton(root, text="4", fg_color="#505050", text_color="white", command=lambda: add_to_box("4"), **btn_p)
button4.place(x=25, y=280)
button5 = ctk.CTkButton(root, text="5", fg_color="#505050", text_color="white", command=lambda: add_to_box("5"), **btn_p)
button5.place(x=95, y=280)
button6 = ctk.CTkButton(root, text="6", fg_color="#505050", text_color="white", command=lambda: add_to_box("6"), **btn_p)
button6.place(x=165, y=280)
button_plus = ctk.CTkButton(root, text="+", fg_color="#FF9500", text_color="white", command=lambda: add_to_box("+"), **btn_p)
button_plus.place(x=235, y=280)


button7 = ctk.CTkButton(root, text="7", fg_color="#505050", text_color="white", command=lambda: add_to_box("7"), **btn_p)
button7.place(x=25, y=350)
button8 = ctk.CTkButton(root, text="8", fg_color="#505050", text_color="white", command=lambda: add_to_box("8"), **btn_p)
button8.place(x=95, y=350)
button9 = ctk.CTkButton(root, text="9", fg_color="#505050", text_color="white", command=lambda: add_to_box("9"), **btn_p)
button9.place(x=165, y=350)
button_minus = ctk.CTkButton(root, text="-", fg_color="#FF9500", text_color="white", command=lambda: add_to_box("-"), **btn_p)
button_minus.place(x=235, y=350)


button_pm = ctk.CTkButton(root, text="+/-", fg_color="#505050", text_color="white", command=toggle_sign, **btn_p)
button_pm.place(x=25, y=420)
button0 = ctk.CTkButton(root, text="0", fg_color="#505050", text_color="white", command=lambda: add_to_box("0"), **btn_p)
button0.place(x=95, y=420)
button_equal = ctk.CTkButton(root, text="=", fg_color="#FF9500", text_color="white", command=calculate_result, **btn_p)
button_equal.place(x=165, y=420)
button_multiply = ctk.CTkButton(root, text="*", fg_color="#FF9500", text_color="white", command=lambda: add_to_box("*"), **btn_p)
button_multiply.place(x=235, y=420)


button_open = ctk.CTkButton(root, text="(", fg_color="#D4D4D2", text_color="black", command=lambda: add_to_box("("), **btn_p)
button_open.place(x=25, y=490)
button_close = ctk.CTkButton(root, text=")", fg_color="#D4D4D2", text_color="black", command=lambda: add_to_box(")"), **btn_p)
button_close.place(x=95, y=490)
button_dot = ctk.CTkButton(root, text=".", fg_color="#505050", text_color="white", command=lambda: add_to_box("."), **btn_p)
button_dot.place(x=165, y=490)
button_divide = ctk.CTkButton(root, text="/", fg_color="#FF9500", text_color="white", command=lambda: add_to_box("/"), **btn_p)
button_divide.place(x=235, y=490)

root.mainloop()

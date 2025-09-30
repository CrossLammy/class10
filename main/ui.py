import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()
window.title('Login')
window.geometry('600x500+500+150')  
window.resizable(False, False)

# store Variable
gender = tk.StringVar()
weight = tk.StringVar() 
height = tk.StringVar()
age = tk.StringVar()
activity = tk.StringVar()




# function

# def btn_submit():
#     result_text = f"Gender: {Gender}\nWeight: {Weight} kg\nHeight: {Height} cm\nAge: {Age}\nActivity: {Activity}"
#     output_label.config(text=result_text)

def btn_submit():
    try:
        g = gender.get()
        w = int(weight.get())
        h = int(height.get())
        a = int(age.get())
        print(g,w,h,a)
    except ValueError:
        messagebox.showerror("Data Error", "ผู้ใช้ต้องใส่ตัวเลข")


# main frame
form = ttk.Frame(window)
form.pack(padx=20, pady=20, expand=True)

# left module (gender + activity)
left_frame = ttk.Frame(form)
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky='n')

ttk.Label(left_frame, text="Gender").grid(row=0, column=0, sticky='w')
tk.Radiobutton(left_frame, text="Men", variable=gender, value='mem').grid(row=1, column=0, sticky='w')
tk.Radiobutton(left_frame, text="Women", variable=gender, value='women').grid(row=2, column=0, sticky='w')
gender.set(1)

ttk.Label(left_frame, text="Activity Level").grid(row=3, column=0, pady=(10, 0), sticky='w')
ttk.Combobox(left_frame, textvariable=activity, values=[
    "Sedentary", "Lightly active", "Moderately active", "Very active", "Super active"
]).grid(row=4, column=0, sticky='w')

# right module (weight, height, age)
right_frame = ttk.Frame(form)
right_frame.grid(row=0, column=1, padx=10, pady=10, sticky='n')

ttk.Label(right_frame, text="Weight (kg)").grid(row=0, column=0, sticky='w')
tk.Entry(right_frame, textvariable=weight).grid(row=1, column=0, sticky='w')

ttk.Label(right_frame, text="Height (cm)").grid(row=2, column=0, sticky='w')
tk.Entry(right_frame, textvariable=height).grid(row=3, column=0, sticky='w')

ttk.Label(right_frame, text="Age").grid(row=4, column=0, sticky='w')
tk.Entry(right_frame, textvariable=age).grid(row=5, column=0, sticky='w')

# submit button
ttk.Button(form, command=btn_submit, text="Submit").grid(row=1, column=0, columnspan=2, pady=10)

# output label
output_label = tk.Label(window, text="XXX", font=('Arial', 12), justify='left', fg='blue')
output_label.pack(pady=10)

window.mainloop()

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()
window.title('BMR & TDEE Calculator')
window.geometry('650x520+500+150')
window.resizable(False, False)

# Style
style = ttk.Style()
style.configure('TLabel', font=('Arial', 11))
style.configure('TButton', font=('Arial', 11), padding=6)
style.configure('TCombobox', font=('Arial', 11))

# Variables
gender = tk.StringVar()
weight = tk.StringVar()
height = tk.StringVar()
age = tk.StringVar()
activity = tk.StringVar()
goal = tk.StringVar()

# Functions
def btn_submit():
    try:
        g = gender.get()
        w = int(weight.get())
        h = int(height.get())
        a = int(age.get())
        bmr = BMR(g, w, h, a)
        tdee = cal_tdee(bmr)
        target_tdee = goal_cal(tdee)
        
        try:
            if w <= 0 or h <= 0 or a <= 0:
                raise ValueError("น้ำหนัก ส่วนสูง และอายุ ต้องเป็นค่าบวกเท่านั้น")
            elif tdee < 1000:
                raise ValueError("TDEE ต่ำเกินไป เป็นไปไม่ได้")
            elif tdee > 7000:
                raise ValueError("TDEE สูงเกินไป เป็นไปไม่ได้")
        except ValueError as e:
            messagebox.showerror("TDEE Error", str(e))
            return  # หยุดการทำงานต่อ
        
        result_text = (
            f'💪 BMR = {int(bmr)} kcal\n'
            f'🔥 TDEE = {int(tdee)} kcal\n'
            f'🎯 Goal ({goal.get()}) = {int(target_tdee)} kcal'
        )
        output_label.config(text=result_text)
    except ValueError:
        messagebox.showerror("Data Error", "กรุณาใส่ตัวเลขให้ถูกต้อง")

def goal_cal(tdee):
    g_choice = goal.get().lower()
    if g_choice == "gain weight":
        target_cal = tdee + 500
        return target_cal
    elif g_choice == "lose weight":
        target_cal = tdee - 500
        return target_cal
    else:
        target_cal = tdee
        return target_cal
    


def BMR(g, w, h, a):
    if g.lower() == 'men':
        return (10 * w) + (6.25 * h) - (5 * a) + 5
    elif g.lower() == 'women':
        return (10 * w) + (6.25 * h) - (5 * a) - 161
    else:
        return 0

def cal_tdee(bmr):
    act = activity.get().lower()
    if act == 'sedentary':
        return bmr * 1.2
    elif act == 'lightly active':
        return bmr * 1.375
    elif act == 'moderately active':
        return bmr * 1.55
    elif act == 'very active':
        return bmr * 1.725
    elif act == 'super active':
        return bmr * 1.9
    return bmr

# Main Frame
form = ttk.Frame(window)
form.pack(padx=20, pady=20, expand=True)

# Left Frame (Gender + Activity)
left_frame = ttk.LabelFrame(form, text="ข้อมูลทั่วไป")
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky='n')

ttk.Label(left_frame, text="Gender").grid(row=0, column=0, sticky='w')
tk.Radiobutton(left_frame, text="Men", variable=gender, value='men').grid(row=1, column=0, sticky='w')
tk.Radiobutton(left_frame, text="Women", variable=gender, value='women').grid(row=2, column=0, sticky='w')
gender.set('men')

ttk.Label(left_frame, text="Activity Level").grid(row=3, column=0, pady=(10, 0), sticky='w')
ttk.Combobox(left_frame, textvariable=activity, values=[
    "Sedentary", "Lightly active", "Moderately active", "Very active", "Super active"
], state='readonly').grid(row=4, column=0, sticky='w')
activity.set('Sedentary')

# Center Frame (Goal)
center_frame = ttk.LabelFrame(form, text="เป้าหมาย")
center_frame.grid(row=0, column=1, padx=10, pady=10, sticky='n')

ttk.Label(center_frame, text="Goal").grid(row=0, column=0, pady=(10, 0), sticky='w')
ttk.Combobox(center_frame, textvariable=goal, values=[
    "Maintain weight", "Gain weight", "Lose weight"
], state='readonly').grid(row=1, column=0, sticky='w')
goal.set("Maintain weight")

# Right Frame (Weight, Height, Age)
right_frame = ttk.LabelFrame(form, text="ข้อมูลร่างกาย")
right_frame.grid(row=0, column=2, padx=10, pady=10, sticky='n')

ttk.Label(right_frame, text="Weight (kg)").grid(row=0, column=0, sticky='w')
tk.Entry(right_frame, textvariable=weight, font=('Arial', 11)).grid(row=1, column=0, sticky='w')

ttk.Label(right_frame, text="Height (cm)").grid(row=2, column=0, sticky='w')
tk.Entry(right_frame, textvariable=height, font=('Arial', 11)).grid(row=3, column=0, sticky='w')

ttk.Label(right_frame, text="Age").grid(row=4, column=0, sticky='w')
tk.Entry(right_frame, textvariable=age, font=('Arial', 11)).grid(row=5, column=0, sticky='w')

# Submit Button
ttk.Button(form, command=btn_submit, text="คำนวณ").grid(row=1, column=0, columnspan=3, pady=15)

# Output Label
output_label = tk.Label(form, text="💪 BMR = ? kcal\n🔥 TDEE = ? kcal\n🎯 Goal = ? kcal",
font=('Arial', 12), justify='left', fg='blue')
output_label.grid(row=2, column=0, columnspan=3)

window.mainloop()

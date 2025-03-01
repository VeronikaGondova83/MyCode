import tkinter as tk
from tkinter import messagebox, ttk

#temy na zmenu dizajnu
color_themes= {
    "Pink": ("#FFB6C1", "#FFB6C1"), 
    "Red": ("#f81515", "#ed6a6a"),
    "Yellow": ("#ede36a", "#f1f80d"), 
    "Green": ("#0df82d", "#73de81"), 
    "Turquoise": ("#bffaed", "#0af99c"), 
    "LightBlue": ("#b1f6f7", "#07c7ca"),
    "DarkBlue": ("#3f4af5", "#08108c"),
    "Purple": ("#7c53e1", "#30059b"),
    "Cyclamin": ("#e759fb", "#a707bd")
}

current_theme = "Turquoise"
tasks = []

#pridanie novej ulohy
def add_tasks():
    task_text = task_entry.get().strip()
    if task_text:
        var = tk.IntVar()
        tasks.append((task_text, var))
        render_tasks()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("POZOR", "Úloha nemôže byť prázdna!")
        
#obnovenie zoznamu uloh
def render_tasks():
    for widget in task_frame.winfo_children():
        widget.destroy()
        
    for task, var in tasks:
        task_row = tk.Frame(task_frame)
        task_row.pack(fill = "x", pady = 2, padx = 5)
        
        check = tk.Checkbutton(task_row, variable = var)
        check.pack(side = "left")
        
        label = tk.Label(task_row, text = task, font = ("Arial", 12))
        label.pack(side = "left", padx = 5)

#ZMENA FAREBNEJ TEMY
def change_theme(theme):
    global current_theme
    current_theme = theme
    bg_color,_= color_themes[theme]
    
    root.configure(bg = bg_color)
    frame.configure(bg = bg_color)
    task_entry.configure(bg = "white")
    task_frame.configure(bg = bg_color)

#GUI Aplikacie
root = tk.Tk()
root.title("To-Do Aplikacia")
root.geometry("400x400")

#hlavne menu
menu_bar = tk.Menu(root)
theme_menu = tk.Menu(menu_bar, tearoff = 0)

for theme in color_themes.keys():
    theme_menu.add_command(label = theme, command = lambda t = theme:change_theme(t))

menu_bar.add_cascade(label = "Tema", menu=theme_menu)
root.config(menu = menu_bar)

#hlavny ramik
frame = tk.Frame(root)
frame.pack(pady = 10)

#VSTUPNE POLE
task_entry = tk.Entry(frame, width = 40, font= ("Arial", 12))
task_entry.pack(side = tk.LEFT, padx = 5)

#tlacidlo na pridanie ulohy
add_button = ttk.Button(frame, text = "Pridat", command = add_tasks)
add_button.pack(side = tk.LEFT)

#ramik pre zoznam uloh
task_frame = tk.Frame(root)
task_frame.pack(pady = 10)

change_theme(current_theme)

root.mainloop()

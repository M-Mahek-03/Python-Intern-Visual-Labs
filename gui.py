import tkinter as tk

def getName():
    name = entry.get()
    label1.config(text="Your name is " + name)
    label2.config(text="Your name is " + name)

window = tk.Tk()
window.geometry("500x500")

canvas = tk.Canvas(window, height=500, width=500)
canvas.create_line(0, 0, 500, 500, fill="green")
canvas.create_line(500, 0, 0, 500, fill="green")
canvas.create_oval(80, 30, 140, 150, fill="green")
canvas.create_arc(180, 150, 80, 210, start=0, extent=220, fill="red")
canvas.pack()

label1 = tk.Label(window, text="Your name is ", font="Arial 20", fg="green")
label1.place(x=120, y=200)

label2 = tk.Label(window, text="Your name is ", font="Arial 25", fg="blue")
label2.place(x=140, y=20)

name = tk.StringVar()
entry = tk.Entry(window, borderwidth=3, width=20, font="Arial 20")
entry.place(x=120, y=80)

submit_button = tk.Button(window, text="Submit", font="Arial 15", width=10, command=getName, bg="lightgreen")
submit_button.place(x=200, y=150)

window.mainloop()

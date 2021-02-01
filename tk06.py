import tkinter as tk

def action_btn_press():
    print('Button was pressed!')

root = tk.Tk()
root.title('Widget creation')
root.geometry("450x150")
lb = tk.Label(text="LABEL-1")
bt = tk.Button(text="BUTTON-1",command=action_btn_press)
lb.pack()
bt.pack()
root.mainloop()
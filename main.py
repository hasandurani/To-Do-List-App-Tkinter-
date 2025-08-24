import tkinter as tk
root = tk.Tk()
root.geometry("400x500")
root.title("To Do List")
entry=tk.Entry(root,font=("Arial",14),borderwidth=4,width=50)
entry.pack()
btn=tk.Button(root,text=('Add Task'),font=("Arial",14),borderwidth=5,fg='white',bg='green')
btn.pack()
lst=tk.Listbox(root,font=("Arial",14),borderwidth=5,bg='black',fg='white')
lst.pack()
dlt=tk.Button(root,text=('Delete'),font=("Arial",14),borderwidth=5,fg='black',bg='yellow')
dlt.pack()
clr=tk.Button(root,text=('Clear All'),font=("Arial",14),borderwidth=5,fg='white',bg='Red')
clr.pack()
def btn_click():
    value=entry.get()
    if value!='':
        entry.delete(0,tk.END)
        lst.insert(tk.END,value)
btn.config(command=btn_click)
def delete():
    lst.delete(tk.ANCHOR)
def clear():
    lst.delete(0,tk.END)
dlt.config(command=delete)
clr.config(command=clear)
root.mainloop() 

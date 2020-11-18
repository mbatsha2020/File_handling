from tkinter import *

def create():

txt_entry_info = txt_entry_info.get("1.0" , END)

print(txt_entry_info)

file = open("my_weekend_activities_txt", 'w')

file.write('My weekend activities')

file.write(txt_entry_info)

file.close()

def display():

    reader = open('my_weekend_activities_txt', 'r')

activities = reader.read()

txt_entry_info.insert(END,activities)

reader.close()

def append():

    reader = open('my_weekend_activities_txt', 'w')

    reader.write(txt_entry_info.get(1.0, END))

def clear():

    reader = open('my_weekend_activities_txt','r+')

    reader.truncate(0)

txt_entry_info.delete(1.0, END)

def exit_():
    window.destroy()

window = Tk()
window.title("Text File")
window.geometry('500x500')

weekend_label = Label(window, text = 'My weekend activities',bg='grey',fg='black',font=10,width=20,height=3)
weekend_label.pack()


txt_entry = Text(window, width = 40, height = 10)
txt_entry.pack(pady=20)

creat_btn = Button(window, text='Create textfile', command=create())
creat_btn.pack(pady=20)

dsp_btn = Button(window, text='Display',command=display)
dsp_btn.pack(padx=20)

appnd_btn = Button(window, text='Append Data',command=append)
appnd_btn.pack(padx=20)

clear_btn = Button(window, text = "Clear" , command=clear)
clear_btn.pack(pady=20)

exit_btn = Button(window, text = "Exit" , command=exit_)
exit_btn.pack(pady=20)

window.mainloop()

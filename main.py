import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Button

def button_clicked():
    print("I got clicked")
    input_text = input.get()
    my_label.config(text=input_text)

button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry
input = tkinter.Entry(width=10)
input.grid(column=1, row=0)
print(input.get())
input.grid(column=3, row=2)




window.mainloop()
import customtkinter as ctk
from problema_9 import problema9

ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.geometry("1000x600")
root.title("Tema laborator 3")

frame = ctk.CTkFrame(master=root)
frame.pack(padx=60, pady=20, fill="both", expand=True)

filler_label = ctk.CTkLabel(master=frame, text = "")
filler_label.grid(row=0, column=0, padx=150)

button_1 = ctk.CTkButton(master=frame, text="Problema 9", command=problema9)
button_1.grid(row=0, column=1, padx=10, pady=(40, 40))


root.mainloop()

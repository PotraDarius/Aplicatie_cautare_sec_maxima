import customtkinter as ctk
from problema_9 import main9
from problema_10 import main10
from problema_16 import main16

ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.geometry("1000x600")
root.title("Tema laborator 3")


def iesire():
    root.destroy()


frame = ctk.CTkFrame(master=root)
frame.pack(padx=60, pady=20, fill="both", expand=True)

filler_label = ctk.CTkLabel(master=frame, text="")
filler_label.grid(row=0, column=0, padx=150)

button_1 = ctk.CTkButton(master=frame, text="Problema 9", command=main9)
button_1.grid(row=0, column=1, padx=10, pady=(40, 40))

button_2 = ctk.CTkButton(master=frame, text="Problema 10", command=main10)
button_2.grid(row=1, column=1, padx=10, pady=(40, 40))

button_3 = ctk.CTkButton(master=frame, text="Problema 16", command=main16)
button_3.grid(row=2, column=1, padx=10, pady=(40, 40))

exit_button = ctk.CTkButton(master=frame, text="Iesire", command=iesire)
exit_button.grid(row=3, column=1, padx=10, pady=(40, 40))

root.mainloop()

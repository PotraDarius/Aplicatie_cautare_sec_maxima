import customtkinter as ctk


def main10():
    def min_max(a, b, c):  # Verifica daca elementul din mijloc dintre 3 elemente este maximul sau minimul
        if a != b and b != c:
            lista_aux = [a, b, c]
            if min(lista_aux) == b:
                return True
            if max(lista_aux) == b:
                return True
        return False

    def min_max_local(n, lista):
        if n <= 2:
            result_label.configure(text="Lista este prea mica pentru a gasi o astfel de secventa!")
        else:
            start_sec = 0
            lungime = 0

            lungime_aux = 0
            start_sec_aux = 0
            for i in range(0, n-2):
                if min_max(lista[i], lista[i+1], lista[i+2]) is True:
                    if lungime_aux == 0:
                        start_sec_aux = i
                        lungime_aux = 3
                    else:
                        lungime_aux += 1
                    if lungime_aux > lungime:
                        lungime = lungime_aux
                        start_sec = start_sec_aux
                else:
                    start_sec_aux = 0
                    lungime_aux = 0
            if not lungime:
                result_label.configure(text="Nu s-a gasit o astfel de secventa!")
            else:
                text_1 = "Lungimea secventei: " + str(lungime)
                text_2 = "Secventa: " + str(lista[start_sec:start_sec+lungime])
                result_label.configure(text=text_1 + '\n' + text_2)

    def handle_button_click():
        input_1 = entry_1.get()
        input_2 = entry_2.get()

        try:
            nr = int(input_1)
            lista = [int(item.strip()) for item in input_2.split(",")]  # Convertire in int al inputului
            min_max_local(nr, lista)
        except ValueError:
            result_label.configure(text="Datele nu au fost introduse corect")

    def iesire():
        root2.destroy()

    ctk.set_appearance_mode("dark")
    root2 = ctk.CTk()
    root2.geometry("1000x600")
    root2.title("Problema 10")

    frame = ctk.CTkFrame(master=root2)
    frame.pack(padx=60, pady=20, fill="both", expand=True)

    fill = "Secventa de lungime maxima cu p=1 sau diferentele (x[j+1]-x[j]) si (x[j+2]-x[j+1]) au semne contrare, j=i..i+p-2"
    filler_label = ctk.CTkLabel(master=frame, text=fill, font=('Helvetica', 17))
    filler_label.grid(row=0, column=0, padx=10)

    exec_button = ctk.CTkButton(master=frame, text="Exceturare", command=handle_button_click)
    exec_button.grid(row=1, column=0, pady=(40, 40), padx=10)

    entry_1 = ctk.CTkEntry(master=frame, placeholder_text="Dati un numar")
    entry_1.grid(row=2, column=0, pady=(40, 40), padx=10)

    entry_2 = ctk.CTkEntry(master=frame, placeholder_text="Dati sirul de numere")
    entry_2.grid(row=3, column=0, pady=(40, 40), padx=10)

    result_label = ctk.CTkLabel(master=frame, text=" ")
    result_label.grid(row=4, column=0, pady=(0, 40), padx=10)

    exit_button = ctk.CTkButton(master=frame, text="Iesire", command=iesire)
    exit_button.grid(row=5, column=0, pady=(0, 40), padx=10)

    root2.mainloop()

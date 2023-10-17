import customtkinter as ctk


def main16():
    def aceleasi_cifre(n, m):
        if n < 0:
            n = -n
        if m < 0:
            m = -m

        cifre_n = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        while n:
            cifre_n[n % 10] = 1
            n = int(n / 10)

        cifre_m = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        while m:
            cifre_m[m % 10] = 1
            m = int(m / 10)
        if not cifre_m == cifre_n:
            return False
        return True

    def functie_test():
        nr = 5
        lista_test = [23, 32, -78, 877, 77]
        assert sec_max(nr, lista_test) == (0, 2)
        return True

    def sec_max(n, lista):
        if n <= 1:
            result_label.configure(text="Lista este prea mica pentru a gasi o astfel de secventa!")
            return -1
        else:
            start_sec = 0
            lungime = 0

            lungime_aux = 0
            start_sec_aux = 0
            for i in range(0, n - 1):
                if aceleasi_cifre(lista[i], lista[i + 1]) is True:
                    if lungime_aux == 0:
                        start_sec_aux = i
                        lungime_aux = 2
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
                return -2
            else:
                text_1 = "Lungimea secventei: " + str(lungime)
                text_2 = "Secventa: " + str(lista[start_sec:start_sec + lungime])
                result_label.configure(text=text_1 + '\n' + text_2)
                return start_sec, lungime

    def handle_button_click():
        input_1 = entry_1.get()
        input_2 = entry_2.get()

        try:
            nr = int(input_1)
            lista = [int(item.strip()) for item in input_2.split(",")]  # Convertire in int al inputului
            sec_max(nr, lista)
        except ValueError:
            result_label.configure(text="Datele nu au fost introduse corect")

    def iesire():
        root2.destroy()

    ctk.set_appearance_mode("dark")
    root2 = ctk.CTk()
    root2.geometry("1000x600")
    root2.title("Problema 16")

    frame = ctk.CTkFrame(master=root2)
    frame.pack(padx=60, pady=20, fill="both", expand=True)

    fill = "Secventa de lungime maxima cu numere care scrierea lor in baza 10 foloseste aceleasi cifre"
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

    test_button = ctk.CTkButton(master=frame, text="Testare", command=functie_test)
    test_button.grid(row=0, column=1, padx=10, pady=(40, 40))

    exit_button = ctk.CTkButton(master=frame, text="Iesire", command=iesire)
    exit_button.grid(row=5, column=0, pady=(0, 40), padx=10)

    root2.mainloop()

from main import ctk


def problema9():
    ctk.set_appearance_mode("dark")

    root1 = ctk.CTk()
    root1.geometry("1000x600")
    root1.title("Problema 9")

    def sec_3numere_consec(n, lista):
        if n <= 2:
            output_label.configure(text="Sirul dat este prea scurt pentru o astfel de secventa!")
        else:
            lungime = 0
            start_sec = 0
            # Cele doua variabile de mai sus vor retine lungimea si inceputu secventei maxime la final
            lungime_aux = 0
            start_sec_aux = 0
            # Cele doua variabile auxiliare de mai sus vor ajuta la determinarea secventelor pe parcurs
            for i in range(0, n - 2):
                if lista[i] == lista[i + 1] or lista[i] == lista[i + 2]:  # Conditia de aparteneta la secventa cautata
                    if not lungime_aux:  # Aici se creeaza inceputu unei secvente
                        lungime_aux = 3  # Lungimea de inceput a unei secvente va fi 3 pentru a include si urmatoarele doua pozitii fata de prima
                        start_sec_aux = i  # Se reseteaza inceputul secventei la pozitia curenta
                    else:
                        lungime_aux += 1
                    if lungime_aux > lungime:
                        lungime = lungime_aux  # In cazul in care s-a gasit o secventa cu o lungime mai mare, lungimea finala si inceputul secventei finale se modifica
                        start_sec = start_sec_aux
                else:
                    lungime_aux = 0  # Variabilele auxiliare se reseteasa pentru gasirea unei secvente
                    start_sec_aux = 0
            if lungime == 0:
                output_label.configure(text="Nu s-a gasit o astfel de secventa")
            else:
                text1 = "Lungime: " + str(lungime)
                text2 = "Secventa: " + str(lista[start_sec:start_sec + lungime])
                output_label.configure(text=text1 + '\n' + text2)

    def handle_button_click():
        input_text1 = entry_1.get()
        input_text2 = entry_2.get()
        try:
            sir_numere = [int(item.strip()) for item in input_text2.split(
                ",")]  # sirul de numere trebuie dat cu virgule intre numere, fara spatiu la final
        except ValueError:
            output_label.configure(text="Datele nu sunt introduse corect!")
        try:
            nr = int(input_text1)
        except ValueError:
            output_label.configure(text="Datele nu sunt introduse corect!")
        sec_3numere_consec(nr, sir_numere)

    def iesire():
        root1.destroy()

    frame = ctk.CTkFrame(master=root1)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    fill_label = ctk.CTkLabel(master=frame, text="")
    fill_label.grid(row=0, column=0, padx=160, pady=10)

    button = ctk.CTkButton(master=frame, text="Execute", command=handle_button_click)
    button.grid(row=0, column=1, padx=10, pady=(40, 40))

    button_exit = ctk.CTkButton(master=frame, text="Iesire", command=iesire)
    button_exit.grid(row=4, column=1, padx=10, pady=40)

    entry_1 = ctk.CTkEntry(master=frame, placeholder_text="Dati o valoare")
    entry_1.grid(row=1, column=1, padx=10, pady=40)

    entry_2 = ctk.CTkEntry(master=frame, placeholder_text="Dati elementele sirului")
    entry_2.grid(row=2, column=1, padx=10, pady=40)

    output_label = ctk.CTkLabel(master=frame, text="")
    output_label.grid(row=3, column=1, padx=10, pady=40)

    # DE TERMINAT DE ADAUGAT LABEL PENTRU AFISARE REZULTATE + FUNCTIONALITATE BUTON IMPLEMENTATA

    root1.mainloop()



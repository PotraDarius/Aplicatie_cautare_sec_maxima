import customtkinter
"""
root = customtkinter.CTk()

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)



root.mainloop()"""


def citire(n, lista):
    for i in range(0, n):
        el = int(input())
        lista.append(el)


def sec_3numere_consec(n, lista):
    if n <= 2:
        print("Sirul dat este prea scurt pentru o astfel de secventa!")
    else:
        lungime = 0
        start_sec = 0
        # Cele doua variabile de mai sus vor retine lungimea si inceputu secventei maxime la final
        lungime_aux = 0
        start_sec_aux = 0
        # Cele doua variabile auxiliare de mai sus vor ajuta la determinarea secventelor pe parcurs
        for i in range(0, n-2):
            if lista[i] == lista[i+1] or lista[i] == lista[i+2]:  # Conditia de aparteneta la secventa cautata
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
            print("Nu s-a gasit o astfel de secventa")
        else:
            print("Lungime: " + str(lungime))
            print("Secventa: " + str(lista[start_sec:start_sec+lungime]))


nr = int(input())
lista = []
citire(nr, lista)
sec_3numere_consec(nr, lista)


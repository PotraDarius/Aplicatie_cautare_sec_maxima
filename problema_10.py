from main import ctk


def min_max(a, b, c):
    if a != b and b!= c:
        lista_aux = [a, b, c]
        if min(lista_aux) == b:
            return True
        if max(lista_aux) == b:
            return True
    return False


def min_max_local(n, lista):
    if n <= 2:
        print("Lista este prea mica pentru a gasi o astfel de secventa!")
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
            print("Nu s-a gasit o astfel de secventa!")
        else:
            text_1 = "Lungimea secventei: " + str(lungime)
            text_2 = "Secventa: " + str(lista[start_sec:start_sec+lungime])
            print(text_1 + '\n' + text_2)

# --- Leccion4 - BPP - TorresEspinosa ---

numeros = [3, 7, 4, 8, 5, 20, 19, 5, 22, 13]

def primo(n):
    primo = True
    for i in range(2, n):
        if(n%i == 0):
            primo = False
    if primo:
        return n

new = list(filter(primo, numeros))

print(new)
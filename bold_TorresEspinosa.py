# --- Leccion4 - BPP - TorresEspinosa ---
import pdb
# pdb.set_trace()

BOLD = "\033[1m"
END = "\033[0m"

numeros = [[2, 4, 1],[1, 2, 3, 4, 5, 6, 7, 8],[100, 250, 43]]
new = []

# MEDIANTE LISTAS ANIDADAS
# for l in numeros:
#     l_new = []
#     for n in l:
#         if n is max(l):
#             l_new.append(BOLD + str(n) + END)
#         else:
#             l_new.append(n)
#     new.append(l_new)

# Compresion listas anidadas
new = [[(BOLD + str(num) + END) if num is max(line) else str(num) for num in line] for line in numeros]

print(numeros)
print(new)

# --- Para que se aprecie la negrita ---
def imprimir(new):
    for l in new:
        for n in l:
            print(n, end=' ')
        print(', ')

imprimir(new)
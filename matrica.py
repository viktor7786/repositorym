# Korisnik unosi matricu.Napraviti funkciju koja dobija originalnu matricu i koja vraca novu matricu u kojoj su sve kolone obrnutim redosledom
# Primer:      8632                    Rezultat:     2368
#              6533                                  3356
#              8978                                  8798


def obrni_matricu(matrica):
    nova_matrica = []
    for red in matrica:
        nova_matrica.append(red[::-1])

    return nova_matrica

originalna_matrica = [
    [23, 45, 26, 98],
    [98, 58, 53, 30],
    [39, 94, 43, 10]
]

rezultat = obrni_matricu(originalna_matrica)
for red in rezultat:
    print(red) 


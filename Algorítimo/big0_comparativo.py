def encontrar_pares_bruto(lista: list[int], alvo: int) -> list[tuple[int, int]]:
    """Solução Força Bruta - Complexidade de Tempo: O(n²) | Espaço: O(1)"""
    lista_alvo = []
    tamanho = len(lista)
    for i in range(tamanho):
        for j in range(i + 1, tamanho):
            if lista[i] + lista[j] == alvo:
                lista_alvo.append((lista[i], lista[j]))
    return lista_alvo


def encontrar_pares_otimizado(lista: list[int], alvo: int) -> list[tuple[int, int]]:
    """Solução Otimizada com Hash Set - Complexidade de Tempo: O(n) | Espaço: O(n)"""
    vistos = set()
    pares = []
    for numero in lista:
        complemento = alvo - numero
        if complemento in vistos:
            pares.append((complemento, numero))
        vistos.add(numero)
    return pares


    
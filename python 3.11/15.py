def najdluzszy_wspolny_podciag(s1, s2):
    m = len(s1)
    n = len(s2)

    tabela = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                tabela[i][j] = tabela[i - 1][j - 1] + 1
            else:
                tabela[i][j] = max(tabela[i - 1][j], tabela[i][j - 1])

    wynik = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            wynik.append(s1[i - 1])
            i -= 1
            j -= 1
        elif tabela[i - 1][j] > tabela[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(wynik))


print(najdluzszy_wspolny_podciag("abcdfg", "abdfg"))  # "abdfg"

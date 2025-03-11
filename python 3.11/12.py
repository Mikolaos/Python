def czy_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    return sorted(s1) == sorted(s2)


print(czy_anagram("Quid est veritas", "Vir est qui adest"))
print(czy_anagram("hello", "world"))
print(czy_anagram("Anagram", "nagaram"))
print(czy_anagram("Julian Tuwim", "Lutni ujaw mi"))

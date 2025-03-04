def readability_score(text: str) -> float:
    sentences = text.split('.') + text.split('!') + text.split('?')
    sentences = [s.strip() for s in sentences if s.strip()]
    words = text.split()
    syllables = sum(sum(1 for char in word if char in 'aeiouAEIOU') for word in words)
    return len(words) / len(sentences) + syllables / len(words)

print(readability_score('Siała baba mak? Nie wiedziała jak!'))
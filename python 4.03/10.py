def group_words_by_length(words: list[str]) -> dict:
    grouped = {}
    for word in words:
        grouped.setdefault(len(word), []).append(word)
    return grouped

print(group_words_by_length(["hello", "world", "python"]))
from collections import Counter
def most_frequent_element(data: list):
    count = Counter(data)
    return max(count, key=count.get)

print(most_frequent_element(['a', 'b', 'c', 'd', 'e','b']))
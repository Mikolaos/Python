def longest_increasing_subsequence(sequence: list[int]):
    longest_subsequence = 0
    counter = 1
    bucket = sequence[0]
    for i in range(1, len(sequence)):
        if sequence[i] > bucket:
            counter += 1
        else:
            longest_subsequence = counter
            counter = 0
        bucket = sequence[i]
    longest_subsequence = max(longest_subsequence, counter)
    return longest_subsequence


print(longest_increasing_subsequence([1, 3, 5, 7, 9, 11]))
print(longest_increasing_subsequence([1, 3, 2, 7, 9, 11]))

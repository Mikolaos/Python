
def round_numbers(numbers: list[int], threshgold:int):
    for i in range(len(numbers)):
        if numbers[i] < threshgold:
            numbers[i]=round(numbers[i]/10)*10
        elif numbers[i] >= threshgold:
            if numbers[i]%10>0:
                numbers[i]=round(numbers[i]/10)*10+10
    return numbers


print(round_numbers(numbers=[21,22,23,24,25,26,27,28,29,30], threshgold=25))
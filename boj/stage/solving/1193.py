X = int(input())

fractions = [-1]

numerator = 1
dominator = 1
fractions.append(str(numerator) + '/' + str(dominator))

numerator += 1
fractions.append(str(numerator) + '/' + str(dominator))

while len(fractions) < X + 1:
    if dominator == 1:
        _ = 0
        while _ < numerator:
            numerator -= 1
            dominator += 1
            fractions.append(str(numerator) + '/' + str(dominator))
            _ += 1
    
    elif numerator == 1:
        _ = 0
        while _ < dominator:
            numerator += 1
            dominator -= 1
            fractions.append(str(numerator) + '/' + str(dominator))
            _ += 1

  

print(fractions)



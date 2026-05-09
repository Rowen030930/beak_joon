stairs = []

sum_list = []

N = int(input())

i = 0
while i < N:
    a_stair = int(input())
    stairs.append(str(a_stair))

    i += 1

sum_list.append(stairs[N -1])
sum_list.append(stairs[0])
sum list.append()

i = N - 1 
while i > 0:

    first_sum = stairs[N] + stairs[N - 1]
    second_sum = stairs[N] + stairs[N - 2]

    if first_sum > second_sum:
        sum_list.append(stairs[N - 1])
    elif first_sum < second_sum:
        sum_list.append(stairs[N - 2])
    i -= 2

print(sum(sum_list))


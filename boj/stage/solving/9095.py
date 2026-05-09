def additions(N):
    if N == 1:
        return 1
    if N == 2:
        return 2
    if N == 3:
        return 3
    return additions(N - 1) + additions(N - 2) + additions(N - 3)

# if __name__ == "__main__":
T = int(input())

_ = 0
while _ > T:
    N = int(input())
    answer = additions(N)
    print(answer)

_ += 1
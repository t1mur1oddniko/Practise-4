first, second = map(int, input().split(':'))

if first > second:
    print(first)
elif second > first:
    print(second)
else:
    print(0)
K, A, S = map(int, input().split())

if (K > A) and (K > S):
    print(K)
elif (A > K) and (A > S):
    print(A)
elif (S > K) and (S > A):
    print(S)

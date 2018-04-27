def scalar_mult(v,A):
    n = len(A)
    soma = A
    n = n - 1
    while n >= 0:
        soma[n] = v*A[n]
        n = n - 1
    return soma
def test(case):
    print(case)

test(scalar_mult(5, [1, 2]) == [5, 10])
test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])

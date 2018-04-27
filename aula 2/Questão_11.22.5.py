def add_vectors(v,A):
    n = len(v)
    soma = v
    n = n - 1
    while n >= 0:
        soma[n] = soma[n] + A[n]
        n = n - 1
    return soma
def test(case):
    print(case)

test(add_vectors([1, 1], [1, 1]) == [2, 2])
test(add_vectors([1, 2], [1, 4]) == [2, 6])
test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])

"""Verify three GF(4) Hermitian LCD constructions from Lu--Li--Ren (2024)."""

from itertools import product


# Elements are 0,1,w,w+1 encoded by 0,1,2,3.  Addition is XOR.
def mul(a, b):
    answer = 0
    while b:
        if b & 1:
            answer ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7              # w^2 = w+1
    return answer


def rank(matrix):
    matrix = [row[:] for row in matrix]
    pivot_row = 0
    for column in range(len(matrix[0])):
        pivot = next((r for r in range(pivot_row, len(matrix)) if matrix[r][column]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        inverse = (0, 1, 3, 2)[matrix[pivot_row][column]]
        matrix[pivot_row] = [mul(inverse, x) for x in matrix[pivot_row]]
        for r, row in enumerate(matrix):
            if r != pivot_row and row[column]:
                factor = row[column]
                matrix[r] = [x ^ mul(factor, y) for x, y in zip(row, matrix[pivot_row])]
        pivot_row += 1
    return pivot_row


def verify(rows, distance):
    generator = [[int(x) for x in row] for row in rows]
    n, k = len(generator[0]), len(generator)
    gram = []
    for a in generator:
        gram_row = []
        for b in generator:
            inner_product = 0
            for x, y in zip(a, b):
                inner_product ^= mul(x, mul(y, y))
            gram_row.append(inner_product)
        gram.append(gram_row)
    distribution = [0] * (n + 1)
    for coefficients in product(range(4), repeat=k):
        word = [0] * n
        for coefficient, row in zip(coefficients, generator):
            word = [x ^ mul(coefficient, y) for x, y in zip(word, row)]
        distribution[sum(x != 0 for x in word)] += 1
    observed_distance = next(i for i, count in enumerate(distribution) if i and count)
    assert rank(generator) == k
    assert rank(gram) == k, "Hermitian Gram matrix must be nonsingular"
    assert observed_distance == distance
    assert sum(distribution) == 4**k
    print(f"[{n},{k},{distance}]_4: rank={k}, Hermitian Gram rank={k}")
    print("  weight distribution:", distribution)


if __name__ == "__main__":
    g19 = [
        "1130121231010000000", "0133203320031200000", "0303332320310100000",
        "0131030320010011000", "0130001110020230300", "0301202120000230010",
        "0302110010030220003",
    ]
    g20 = [
        "11011111101000000011", "11120323003110000012", "30132223011030000020",
        "11202023001001100001", "11000132002013010001", "30220233000013001003",
        "30313002003012000101",
    ]
    # The [18,7,9] matrix is obtained by puncturing coordinate 1 of g19.
    verify([row[1:] for row in g19], 9)
    verify(g19, 9)
    verify(g20, 10)

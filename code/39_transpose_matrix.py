def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    print("Original Matrix:", matrix)
    print("Transpose Matrix:", transpose_matrix(matrix))
#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for i in range(len(line)):
            if i < len(line) - 1:
                print("{:d}".format(line[i]), end=" ")
            else:
                print("{:d}".format(line[i]), end="")
            print()

if __name__ == "__main__":
    matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

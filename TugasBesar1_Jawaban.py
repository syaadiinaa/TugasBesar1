import re

def decode_matrix_script(n, m, matrix):
    decoded_matrix = []
    for row in matrix:
        decoded_row = re.sub(r'[^\w\s]', '', row)
        decoded_row = ' '.join(decoded_row.split())
        decoded_matrix.append(decoded_row)

    for row in decoded_matrix:
        print(row)

if __name__ == "__main__":
    with open("Matrix.txt", "r") as file:
        input_values = list(map(int, file.readline().strip().split()))
        n, m = input_values
        matrix = [line.strip() for line in file.readlines()]
    decode_matrix_script(n, m, matrix)
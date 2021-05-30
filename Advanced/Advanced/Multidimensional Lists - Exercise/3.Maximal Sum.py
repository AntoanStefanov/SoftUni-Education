rows, columns = [int(x) for x in input().split()]

matrix = []


for r in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

# It gave 80/100 if you assign 0 as submatrix_sum !! So it means there were negative nums
submatrix_sum = None
submatrix = []

for n_row in range(rows - 2):
    for n_col in range(columns - 2):

        # first row
        current_value = matrix[n_row][n_col]
        second_value = matrix[n_row][n_col + 1]
        third_value = matrix[n_row][n_col + 2]

        first_row = [current_value, second_value, third_value]
        # second row
        second_row_current_value = matrix[n_row + 1][n_col]
        second_row_second_value = matrix[n_row + 1][n_col + 1]
        second_row_third_value = matrix[n_row + 1][n_col + 2]

        second_row = [second_row_current_value,
                      second_row_second_value, second_row_third_value]
        # third row
        third_row_current_value = matrix[n_row + 2][n_col]
        third_row_second_value = matrix[n_row + 2][n_col + 1]
        third_row_third_value = matrix[n_row + 2][n_col + 2]

        third_row = [third_row_current_value,
                     third_row_second_value, third_row_third_value]

        first_second_rows_sum = sum(first_row) + sum(second_row)
        total_current_sum = first_second_rows_sum + sum(third_row)

        if submatrix_sum is None or total_current_sum > submatrix_sum:

            submatrix_sum = total_current_sum
            submatrix = [
                first_row,
                second_row,
                third_row,
            ]

print(f'Sum = {submatrix_sum}')
for row in submatrix:
    print(*row)

# Second Time #

rows, columns = [int(x) for x in input().split()]
matrix = []
for r in range(rows):
    matrix.append([int(x) for x in input().split()])


matrix_max_sum = None


# -2 Защото квадрата си е 3х3 и няма смисъл да чеквам последните 2 реда защото излизат от матрицата
for row in range(rows - 2):
    # -2 Защото квадрата си е 3х3 и няма смисъл да чеквам последните 2 колони защото излизат от матрицата
    for column in range(columns - 2):
        first_row = [matrix[row][column], matrix[row]
                     [column + 1], matrix[row][column + 2]]
        second_row = [matrix[row + 1][column], matrix[row + 1]
                      [column + 1], matrix[row + 1][column + 2]]
        third_row = [matrix[row + 2][column], matrix[row + 2]
                     [column + 1], matrix[row + 2][column + 2]]

        current_matrix_sum = sum(first_row) + sum(second_row) + sum(third_row)
        if matrix_max_sum == None or current_matrix_sum > matrix_max_sum:
            matrix_max_sum = current_matrix_sum
            best_matrix = [first_row, second_row, third_row]

print(f'Sum = {matrix_max_sum}')
for row in best_matrix:
    print(' '.join([str(n) for n in row]))

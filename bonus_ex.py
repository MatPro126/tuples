# Matrix 3x3
# 1  4  7
# 3  5  2
# 8  0  6

matrix = ((1, 4, 7, 5), (3, 5, 2, 1), (8, 0, 6, 7))

def transpose_matrix(m):
    rows = len(m)
    cols = len(m[0])

    # the rows bcome columns and vice versa
    # start with an empty tuple
    ret_mat = ()
    for col in range(cols):
        n_row = ()
        for row in range(rows):
            n_row = n_row + (m[row][col],)
        ret_mat = ret_mat + (n_row,)
    return ret_mat

print(transpose_matrix(matrix))
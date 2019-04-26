# Magic squares are made of 3 numbers a, b, c such that

# 0 < a < b < c - a and b != 2a

# the square itself is 

# c − b	      c + (a + b)	c − a
# c − (a − b)	  c	            c + (a − b)
# c + a	      c − (a + b)	c + b

# This is Édouard Lucas's Method

def generate_base_numbers(r_min, r_max):
    abc_possibilities = []
    c = r_max
    while c > r_min:
        a = r_min
        while (a + 1) < (c - a):
            for b in range(a + 1, c - a):
                if b != 2 * a:
                    if 1 <= (a + b + c) <= 9:
                        if 1 <= (c - a - b) <= 9:
                            abc_possibilities.append([a, b, c])
            a += 1
        c -= 1
    return abc_possibilities

def magic_square(base):
    a, b, c = base
    row1 = [(c - b), c + (a + b), (c - a)]
    row2 = [c - (a - b), c, c + (a - b)]
    row3 = [(c + a), c - (a + b), c + b]
    return [row1, row2, row3]

def rotate_right(square):
    rotated_square_row1 = [square[2][0], square[1][0], square[0][0]]
    rotated_square_row2 = [square[2][1], square[1][1], square[0][1]]
    rotated_square_row3 = [square[2][2], square[1][2], square[0][2]]
    return [rotated_square_row1, rotated_square_row2, rotated_square_row3]

def transpose(square):
    t_square_row1 = [square[0][0], square[1][0], square[2][0]]
    t_square_row2 = [square[0][1], square[1][1], square[2][1]]
    t_square_row3 = [square[0][2], square[1][2], square[2][2]]
    return [t_square_row1, t_square_row2, t_square_row3]

def all_rotations_and_reflections(square):
    squares = []
    squares.append(square)
    squares.append(transpose(square))
    for i in range(3):
        square = rotate_right(square)
        squares.append(square)
        squares.append(transpose(square))
    return squares

def get_magic_squares(verbose = False):
    base = generate_base_numbers(1,9)
    m_square = magic_square(base[0])
    magic_squares = all_rotations_and_reflections(m_square)
    if verbose:
        print("valid base numbers are",base)
        print("the resulting magic square is:")
        for row in m_square:
            print(row)
        print("All magic squares:")
        for num, square in enumerate(magic_squares):
            print("---Square", num + 1, "---")
            for row in square:
                print(row)
            print("---------------")
    return magic_squares

def min_distance(square, magic_squares):
    distances = []
    for magic_square in magic_squares:
        distance = 0
        for square_row, magic_row in zip(square, magic_square):
            for square_element, magic_element in zip(square_row, magic_row):
                distance += abs(square_element - magic_element)
        distances.append(distance)
    return min(distances)

if __name__ == '__main__':
    magic_squares = get_magic_squares(False)
    random_square = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
    print(min_distance(random_square, magic_squares))
    random_square = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]
    print(min_distance(random_square, magic_squares))
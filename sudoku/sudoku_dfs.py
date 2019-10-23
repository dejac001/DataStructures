import copy


def getGroups(mat):
    pass


def reduceGroup(groups):
    """return True if can reduce group and False if not"""
    pass


def reduce(matrix):
    changed = True
    groups = getGroups(matrix)

    while changed:
        changed = reduceGroups(groups)


def solutionViable(matrix):
    """Check that no set is empty"""
    for i in range(9):
        for j in range(9):
            if len(matrix[i][j]) == 0:
                return False

    return True


def solve(matrix):
    reduce(matrix)

    if not solutionViable(matrix):
        return None

    if solutionOK(matrix):
        return matrix

    print('Searching...')
    for i in range(9):
        for j in range(9):
            if len(matrix[i][j]) > 1:
                for k in matrix[i][j]:
                    mcopy = copy.deepcopy(matrix)
                    mcopy[i][j] = {k}

                    result = solve(mcopy)

                    if result is not None:
                        return result

    return None


def read_file(f):
    matrix = []
    for line in open(f):
        print(line)
        columns = []
        for col in line.rstrip('\n').split():
            if not col.isdigit():
                columns.append(set())
            else:
                columns.append(int(col))
        matrix.append(columns)
    return matrix


def main():
    input_file = input('Please enter a Sudoku puzzle file name:')
    matrix = read_file(input_file)


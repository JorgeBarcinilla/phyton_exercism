class Matrix:
   
    def __init__(self, matrix_string):
        for row in matrix_string.split('/n'):
            self.matrix = [[int(index) for index in row.split()] for row in matrix_string.split("\n")]

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [row[index-1] for row in self.matrix]

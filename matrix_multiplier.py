# 2018 Douglas Berdeaux (C) GNU
# WeakNetLabs@Gmail.com
# Matrix Multiplication with Python
import sys  # for exit()


class Matrix:  # initialization:
    def __init__(self):
        self.matrix = []

    # Setters for data:
    def setDimensions(self,dimensions):
        dimList=dimensions.split(",")
        self.rowCount=int(dimList[0])
        self.columnCount=int(dimList[1])
    def setRow(self,rowString):
        self.matrix.append(rowString.split(","))

    # Getters of data:
    def getRowCount(self):
        return self.rowCount
    def getColumnCount(self):
        return self.columnCount


m1 = Matrix()  # build our two matrices to the Matrix() blue print
m2 = Matrix()  # This is fun! :)
# Get the sizes of the matrices: TODO add error handling
m1.setDimensions(input("Enter the FIRST matrix's dimensions (rows,columns): "))
m2.setDimensions(input("Enter the SECOND matrix's dimensions (rows,columns): "))

if m1.getColumnCount() != m2.getRowCount():
    print("These matrices cannot be multiplied.")
    sys.exit(9)

# build Matrices in Matrix objects:
print("MATRIX 1:")
for row in range(0,m1.getRowCount()):
    m1.setRow(input("Enter entire matrix row as CSV row=("+str(row)+"): "))
print("MATRIX 2:")
for row in range(0,m2.getRowCount()):
    m2.setRow(input("Enter entire matrix row as CSV row=("+str(row)+"): "))

# Multiply matrices in Matrix objects:
answerMatrix = []  # placeholder for the answer, a 2d array.
for row in range(len(m1.matrix)): # m1 rows = 0,1
    tmpAnsArray = []  # Build the nested array and .append() later
    for colCount in range(m2.getColumnCount()): # m2 cols = 0,1
        tmpAnsElement = 0  # reset
        for m1Col in range(len(m1.matrix[row])): # 0,1,2
            tmpAnsElement += int(m1.matrix[row][m1Col]) * int(m2.matrix[m1Col][colCount])
        tmpAnsArray.append(tmpAnsElement)
    answerMatrix.append(tmpAnsArray) # push in the array to answer.

print("----------------------------\nAnswer Matrix: ")
for row in answerMatrix:
    print(row)

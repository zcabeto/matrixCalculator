def unsparse(array):
    dArr = {}
    for i in range(len(array)):
        if (array[i] != 0):
            dArr[i] = array[i]
    return dArr
            
def addRow(fakeArray,arr):
    fakeArray.append(unsparse(arr))

def createMatrix():
    arr = []
    print(" -- Enter by space delimination --")
    while True:
        nextRow = input(">")
        if (nextRow == ''):
            break
        else:
            nextRow = nextRow.split()
            for i in range(len(nextRow)):
                nextRow[i] = int(nextRow[i])
            addRow(arr,nextRow)
    return arr

def mSum(m1,m2):
    if (len(m1) != len(m2)):
        return
    result = m1
    for row in range(len(m2)):
        for col in range(len(m2[row])):
            if (col in m1[row]):
                print(row,col)
                result[row][col] = m1[row][col] + m2[row][col]
            else:
                result[row][col] = m2[row][col]
    return result

def linear_product(row1,row2):
    result = 0
    for col in range(len(row1)):
        if ((col in row1) and (col in row2)):
            result += row1[col] * row2[col]
    return result

def rotate(matrix,index):
    result = {}
    for row in range(len(matrix)):
        if (index in matrix[row]):
            result[row] = matrix[row][index]
    return result
            
def mProduct(m1,m2):
    if (len(m1) != len(m2)):
        return
    result = []
    max_cols = 0
    for row in range(len(m1)):
        max_cols = max(len(m1[row]),len(m2[row]),max_cols)
    for row in range(len(m1)):
        result_row = {}
        for col in range(max_cols):
            result_row[col] = linear_product(m1[row],rotate(m2,col))
        result.append(unsparse(result_row))
    return result

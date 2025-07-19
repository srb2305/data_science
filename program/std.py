import program.numpyProgram as np

data = [1,2,3,4,5]

#calculation standard deviation
std = np.std(data)

print("Standard Deviation:", std)


arr =  np.array([1,2,3,4,5])
print("SUM:", np.sum(arr))
print("MEAN:", np.mean(arr))
print("Stadard Deviation:", np.std(arr))

#create 2d Array
a = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)
b = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)

print("Matrix Multiplication:  ")
print(np.matmul(a,b))

# Triangular
n = int(input("Masukkan angka: "))
a = [[1], [1, 1]]


for i in range(n-2):
    newlane = [1]

    for j in range(len(a[-1]) - 1):
        newlane.append(a[-1][j] + a[-1][j+1])
        
    newlane.append(1)
    
    a.append(newlane)


lastlane = list(map(str, a[-1]))
nl = len(" ".join(lastlane))

for row in a:
    row = list(map(str, row))
    row = " ".join(row)
    
    print(row.center(nl))
A, B = str(input()).split()
L = []
L.append(A[::-1])
L.append(B[::-1])
print(max(L))
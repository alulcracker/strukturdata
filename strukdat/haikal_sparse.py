# Sparse
from scipy import sparse

data = [4,5,7,9]
col = [0,3,1,2]
row = [0,3,1,0]

a = sparse.coo_matrix((data,(row, col)),shape=(4,4)) 
a, a.data

print(a.toarray())


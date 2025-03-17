import galois
GF = galois.GF(2**6,repr = 'power')
a = (GF.repr_table())
print(GF.repr_table())
x = GF(9)
y = GF(7)
z = x+y
print(x)
print(y)
print(z)
print(a[205])
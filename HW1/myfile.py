### Code to find one pair of Ramanujan numbers which are A^3 + B^3 = C^3 + D^3

def find_number():

    for i in range(1,1000):
        for j in range (1, 1000):
            for k in range (1, 1000):
                for m in range(1,1000):
                    if i!= j and j!=k and k!=m and m!=i and i!=k and i*i*i + j*j*j == k*k*k + m*m*m:
                        return (i, j, k, m)             

print(find_number())

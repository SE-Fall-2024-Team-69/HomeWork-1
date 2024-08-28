### Code to find one pair Ramanujan numbers which are A3 + B3 = C3 + D3

flag = False

for i in range(1,1000):
    if (flag):
        break
    for j in range (1, 1000):
        if (flag):
            break
        for k in range (1, 1000):
            if (flag):
                break
            for m in range(1,1000):
                if (flag):
                    break
                if i!= j and j!=k and k!=m and m!=i and i!=k and i*i*i + j*j*j == k*k*k + m*m*m:
                    print (i, j, k, m)
                    flag = True

for i in range(5):
    for j in range(1,10):
        if j%2==0:
            break
        print(j)

for i in range(5):
    for j in range(1,11):
        if j%2==0:
            continue
        print(j,end='\t')
    print()
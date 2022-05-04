l=int(input("enter number"))

for i in range(2,l+1):
    if(l%i==0):
        flag=0
        for j in range(2,(i//2+1)):
            if(i%j==0):
                flag=1
                break

        if flag==0:
                    print(i)

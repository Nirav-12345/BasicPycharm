import random
Head=0
Tail=0

HeadCount=0
TailCount=0
flips=int(input("Enter Flips"))
a = random.randrange(0,2)
x=a




if(flips > 0):
    while (flips < flips):
        flips = flips + 1




    if (x == 1):

        Head=1
        HeadCount=HeadCount+Head
        #HeadPercentage = HeadCount * 100 / flips
        #print(HeadPercentage)

    elif(x==0):
        Tail = 1
        TailCount = TailCount + Tail
        #TailPercentage = TailCount * 100 / flips
        #print(TailPercentage)


    HeadPercentage = (HeadCount/flips)*100
    TailPercentage=(TailCount/flips)*100
    print(HeadPercentage)
    print(TailPercentage)

else:

        print("Enter Positive Integer")









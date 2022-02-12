T=int(input())
for i in range(T):
    num=int(input())
    if(num<0):
        print("Invalid numeber")
        break
    if(num%2==0):
        print(num,"is an even number")
    else:
        print(num,"is a odd number")

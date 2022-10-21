def prime1(a):
    global i

    if a > 1:

     for i in range(2, a):

      if (a % i) == 0:

         print(a, "is NOT a prime number")

         break
    else:

     print(a, "is a PRIME number")
     if a == 0 or 1:
      print(a, "is a neither prime NOR composite number")
     else:
        print(a, "is NOT a prime number it is a COMPOSITE number")
def prime2 (a):
    # define a flag variable
    flag = False

    # prime numbers are greater than 1
    if a> 1:
        # check for factors
        for i in range(2, a):
            if (a % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

    # check if flag is True
    if flag:
        print(a, "is not a prime number")
    else:
        print(a, "is a prime number")
def prime3 (a):
    flag = True
    if a > 1:
        for i in range(2, a // 2 + 1):
            if a % i == 0:
                flag = False
                break
        if flag:
            print("prime")
        else:
            print("Not Prime")
    else:
        print("Not Prime")
def prime4 (a):
    if a > 1:
        for i in range(2, a // 2):
            if (a % i) == 0:
             print(a, "is not a prime number")
             break
    else:
     print(a, "is a prime number")
a=int(input("enter any number"))
c=int(input("enter any choice from 1 to 4"))
if c==1:
    print (prime1(a))
elif c==2:
    print(prime2(a))
elif c==3:
    print(prime3(a))
elif c==4:
    print(prime4(a))












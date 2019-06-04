# for reading user input as integer

num = int(input("enter a number to check:"))

# checking for even num

if num % 2 == 0:

    #checking for num in range 2,5

    if num < 5:
        print("not wired:")

    #checking for num in range 6,20

    elif num < 20:
        print("wired:")

    #remaning all conditions

    else:
        print("not wired:")

    # if num is odd

else:
    print("wired:")



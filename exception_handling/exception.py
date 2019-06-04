x = input("enter a number:")
y = input("enter a number:")
try:
    z = int(x) / (y)
except ZeroDivisionError as e:
    print ("Zero division error occured:", e)
    z = None
except TypeError as f:
    print ("type error occured:", f)
    z = None
except Exception as e:
    print ("Exception type is:", type(e).__name__)    #to know the which type of error
    z = None

else:
    print ("i am in else block:")

finally:
    print ("division:", z)


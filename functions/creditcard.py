n = (input("enter   number:"))
def credit():


    if len(n) == 16:
        if n[0] == "4" or n[0] == "5" or n[0] == "6":
            for i in n:
                k = n.count(i)
                if k > 4:
                    print("third type failure:")
                    break
                else:
                    pass
        else:
            print("second type failure:")
    else:
        print("entered more or less than 16 numbers:")


credit()



def varargs(a,b,*args):
    print(a)
    print(b)
    print(args)
varargs(10,20,"vinod",45,"kumar")

def keywards(**kwargs):
    print(kwargs)
keywards(name="vinod",place="ramadurgam")

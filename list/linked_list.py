"""l = [1,2,3,4,6,7,8]

choice = 0
while choice < 5:
    print("LINKED_LIST OPERATIONS:")

    print("1. ADD ELEMENTS TO LIST:")

    print("2. REMOVE ELEMENTS FROM LIST:")

    print("3. INSERT ELEMENTS TO LIST:")

    print("4. SEARCH ELEMENTS IN LIST:")

    print("5.EXIT:")

    choice = int(input("ENTER YOUR CHOICE:"))

    if choice == 1:
        element = input("enter a element to add list:")
        l.append(element)
        print(l)
        break
    elif choice == 2:
        try:
            element = input("enter a element to remove from list:")
            l.remove(element)
            print(l)
            break
        except:
            print("element not found in list:")
            print(l)
            break
    elif choice == 3:
        element = input("enter a element to isert  into list:")
        position = int(input("enter a position value:"))
        l.insert(position,element)
        print(l)
        break
    elif choice == 4:
        element = int(input("enter a element to search in list:"))

        try:
            position = l.index(element)
            print("element found at position :",position)
            break
        except:
            print("element not found in list:")
            break

    else:
        break"""

import urllib.parse

url = "http://tpwms-dev2-app.jdadelivers.com/"

tp1 = urllib.parse.urlparse(url)

print(tp1)

print(tp1.netloc)










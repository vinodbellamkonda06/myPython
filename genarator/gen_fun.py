import random

names = ["vinod", "manoj", "madhu", "sreenu", "manju", "ashok", "ravi", "sreekanth"]
intrests = ["maths", "science", "physics", "chemistry", "social", "organic_chemistry", "psycology"]


def people_list(num):
    result = []
    for i in range(num):
        person = {
                    "id": i,
                    "name": random.choice(names),
                    "intrest": random.choice(intrests),
        }
        result.append(person)
    return result


a = people_list(10)

print(a)


def people_genarator(num):
    for i in range(num):
        person = {
            "id": i,
            "name": random.choice(names),
            "intrest": random.choice(intrests),
        }
        yield person


k = people_genarator(10)
print(next(k))
print(next(k))
print(next(k))


names.sort(key=lambda x:len(x), reverse=True)
print(names)
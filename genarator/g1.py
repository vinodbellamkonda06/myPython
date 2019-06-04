def gen():
    yield "python"
    yield "java"
    yield "c++"

print(next(gen()))
print(set(gen()))


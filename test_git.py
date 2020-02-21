
def adding(a, b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a, b):
    return a*b


if __name__=="__main__":
    print("hi this works")
    print("I added this extra code")
    x = 5
    y = 3

    print(adding(x,y))
    print(subtract(x,y))
    x = [1,2,3,4,5]
    for i in range(5):
        x[i]+=1
        print(i)
    print(x)

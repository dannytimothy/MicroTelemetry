
x = input("Give a starting number") #5
y = input("Give an ending number") #10

def modfunction( integer ):
    if (count % 3) == 0 and (count % 5) == 0:
        print(count," - both")
    elif (count) % 3) == 0:
        print(count," - 3")
    elif (count % 5) == 0:
        print(count," - 5")

count = x
while count < y + 1:
    modfunction(count)
    count+
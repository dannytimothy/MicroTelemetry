def modulo(number):
    if (number % 3 == 0 and number % 5 == 0):
        print( " -- Both")
    elif number % 3 == 0:
        print (" -- 3")
    elif number % 5 == 0:
        print ("-- 5")

start = int(input("Please enter starting value: "))
end = int(input("Please enter ending value: "))

for number in range (start, end + 1):
    value = modulo(number)
    print (number, value)
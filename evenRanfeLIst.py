'''for num in range(4,15,2):
    print(num)'''

start = int(input("enetr the start range : "))
end = int(input("end of range : "))

for num in range(start, end+1):

    if num % 2 == 0:
        print(num,end=" ")
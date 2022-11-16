number_1 = int(input("Enter the number = "))
number_2 = int(input("Enter the number = "))
count_odd = 0
count_even = 0
for i in range(number_1 , number_2):
    if not i % 2 == 0 :
        count_even+=1
    else:
        count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)

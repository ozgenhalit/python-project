num = int(input(Enter a number....:))
if num == 0 :
    num = 1
elif num < 0 :
    num = num * -1
sum_div = 0
for i in range(1,num+1) :
    if num % i == 0 :
        sum_div += i 
print(sum_div,= The sum of the divisors of {} including itself.format(num))
print(sum_div - num,= Its value is the sum of the divisors of {} excluding itself..format(num))
if sum_div == num * 2 :
    print(Perfect Number)
else :
    print(Not a Perfect Number)

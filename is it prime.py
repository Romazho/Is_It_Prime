
print('Enter your number:')
number = int(input())

isPrime = True
for i in range(2, number):
    # print(i)
    if number % i == 0:
        print("Not prime, divisible by " + str(i))
        isPrime = False
        break

if isPrime:
    print("Your number (" + str(number) + ") is prime.")

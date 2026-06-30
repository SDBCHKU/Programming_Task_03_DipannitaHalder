n = int(input("Enter a number: "))

sum_n = 0
even_count = 0
odd_count = 0

for i in range(1, n + 1):
    sum_n += i
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Sum =", sum_n)
print("Even Numbers =", even_count)
print("Odd Numbers =", odd_count)
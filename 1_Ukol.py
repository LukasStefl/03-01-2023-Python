def find_divisors(n):
  divisors = []
  for i in range(1, n+1):
    if n % i == 0:
      divisors.append(i)
  return divisors

print(find_divisors(10))  # [1, 2, 5, 10]
print(find_divisors(15))  # [1, 3, 5, 15]
print(find_divisors(20))  # [1, 2, 4, 5, 10, 20]

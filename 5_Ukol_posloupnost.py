def sum_sequence(a1, d, n):
  a_n = a1 + (n-1) * d
  return (n/2) * (a1 + a_n)
n = int(input("Enter the highest sequence: "))
print(sum_sequence(1, 2, n)) 
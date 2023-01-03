def sum_n_terms(a1, d, n):
  a_n = a1 + (n-1) * d
  return (n/2) * (a1 + a_n)

print(sum_n_terms(1, 1, 50))  # 1275

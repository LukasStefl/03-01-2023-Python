def arithmetic_sequence(initial, common_difference, n):
  sequence = []
  current = initial
  for i in range(n):
    sequence.append(current)
    current += common_difference
  return sequence

print(arithmetic_sequence(1, 1, 5))  # [1, 2, 3, 4, 5]
print(arithmetic_sequence(1, 2, 5))  # [1, 3, 5, 7, 9]
print(arithmetic_sequence(5, -1, 5))  # [5, 4, 3, 2, 1]
print(arithmetic_sequence(0, 3, 5))  # [0, 3, 6, 9, 12]

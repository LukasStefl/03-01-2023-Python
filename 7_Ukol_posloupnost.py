def fibonacci(n):
  sequence = [0, 1]
  for i in range(2, n):
    sequence.append(sequence[i-1] + sequence[i-2])
  return sequence

# Generate the first 10 terms of the Fibonacci sequence
print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Generate the first 20 terms of the Fibonacci sequence
print(fibonacci(20))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

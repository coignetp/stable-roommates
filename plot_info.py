import matplotlib.pyplot as plt
import math


def number_of_k_partitions(n, k):
  return math.factorial(n) / ((math.factorial(k) ** (n / k)) * math.factorial(n // k)) 

if __name__ == "__main__":
  n = 120
  x = list(range(1, n + 1))
  k_part = [math.log(number_of_k_partitions(n, k)) for k in x]

  plt.plot(x, k_part)
  plt.show()
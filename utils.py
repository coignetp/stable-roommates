from math import inf
from random import shuffle

def compute_score(preferences, solution):
  """ Compute the score of a solution.
  A little score is a good solution. """
  score = 0
  visited = [False] * len(preferences)

  for group in solution:
    for i in range(len(group)):
      # Already attributed
      if visited[group[i]]:
        return inf
      visited[group[i]] = True
      for j in range(len(group)):
        if i != j:
          score += preferences[group[i]].index(group[j])
  
  if False in visited:
    return inf

  return score
  

def compute_score_att(preferences, solution, group_sizes):
  """ Compute the score of a solution with different
  group sizes. A little score is a good solution. """
  score = 0
  i = 0

  for group in group_sizes:
    for j in range(group):
      for k in range(group):
        if j != k:
          score += preferences[solution[i + j]].index(solution[i + k])
    i += group
  
  return score

def get_preferences(filename):
  with open(filename, "r") as file:
    n = int(file.readline())
    m = file.readline().split(' ')
    m_min = int(m[0])
    m_max = int(m[1])
    preferences = [[] for _ in range(n)]

    for i in range(n):
      line = file.readline()
      preferences[i] = [int(data) for data in line.split()]

    return n, m_min, m_max, preferences


def save_solution(filename, solution):
  with open(filename, "w") as file:
    for group in solution:
      for elt in group:
        file.write(f"{elt},")
      file.write("\n")


def save_solution_att(filename, solution, group_sizes):
  with open(filename, "w") as file:
    i = 0
    for group in group_sizes:
      for j in range(group):
        file.write(f"{solution[i + j]},")
      file.write("\n")
    
      i += group

##########################################
# Generate data with the ampl solver format
##########################################
def generate_random_table(n):
  table = [[i for i in range(1, n)] for _ in range(n)]

  for i in range(len(table)):
    shuffle(table[i])
    table[i].insert(i, 0)

  return table

def generate_ampl_dat(filename, n, k1, k2, table=None):
  if table is None:
    table = generate_random_table(n)

  with open(filename, "w") as file:
    file.write(f"param N := {n};\n")
    file.write(f"param K1 := {k1};\n")
    file.write(f"param K2 := {k2};\n")
    file.write("\nparam Preferences: ")

    for i in range(1, n+1):
      file.write(f"{i} ")
    
    file.write(":=")

    for i in range(n):
      file.write(f"\n\t{i + 1}\t")

      for j in range(n):
        file.write(f"{table[i][j]} ")
    file.write(";")

def generate_python_dat(filename, n, k1, k2, table=None):
  if table is None:
    table = generate_random_table(n)

  with open(filename, "w") as file:
    file.write(f"{n}\n")
    file.write(f"{k1} {k2}\n")

    for i in range(n):
      for j in range(1, n):
        ind = table[i].index(j)
        file.write(f"{ind} ")
      file.write("\n")


if __name__ == '__main__':
  n = 100
  k1 = 2
  k2 = 2
  table = generate_random_table(n)
  generate_ampl_dat("ampl/n-100.dat", n, k1, k2, table)
  generate_python_dat("data/sample_100.txt", n, k1, k2, table)

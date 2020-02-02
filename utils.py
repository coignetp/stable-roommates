from math import inf

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
      preferences[i] = [int(data) for data in line.split(' ')]

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
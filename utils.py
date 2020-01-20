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
  

def get_preferences(filename):
  with open(filename, "r") as file:
    n = int(file.readline())
    m = int(file.readline())
    preferences = [[] for _ in range(n)]

    for i in range(n):
      line = file.readline()
      preferences[i] = [int(data) for data in line.split(' ')]

    return n, m, preferences


def save_solution(filename, solution):
  with open(filename, "w") as file:
    for group in solution:
      for elt in group:
        file.write(f"{elt},")
      file.write("\n")
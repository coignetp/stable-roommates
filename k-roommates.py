import utils
from random import randint, shuffle

def solve_m_roommates(n, m, preferences):
  """ Group the n people by m.
  Start by a random solution and make some 2-permutations. """
 
  start = list(range(n))
  shuffle(start)
  solution = [[start[i + j] for j in range(0, m)] for i in range(0, n, m)]
  min_score = utils.compute_score(preferences, solution)
  print(f"Basic solution: {min_score}")
  no_progress_round = 0

  while no_progress_round < 30:
    a1 = randint(0, n - 1)
    a2 = randint(0, n - 1)

    solution[a1 // m][a1 % m], solution[a2 // m][a2 % m] = solution[a2 // m][a2 % m], solution[a1 // m][a1 % m]
    
    new_score = utils.compute_score(preferences, solution)

    if new_score < min_score:
      no_progress_round = 0
      min_score = new_score
    else:
      solution[a1 // m][a1 % m], solution[a2 // m][a2 % m] = solution[a2 // m][a2 % m], solution[a1 // m][a1 % m]
      no_progress_round += 1

  return solution


if __name__ == "__main__":
  n, m, preferences = utils.get_preferences("data/sample_2.txt")

  assert n % m == 0

  solution = solve_m_roommates(n, m, preferences)
  score = utils.compute_score(preferences, solution)

  print(f"Found a solution with a score of {score}")

  utils.save_solution("output/solution_" + str(score) + ".txt", solution)
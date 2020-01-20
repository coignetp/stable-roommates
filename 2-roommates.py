import utils
from random import randint, shuffle

def solve_2_roommates(n, m, preferences):
  """ Start from a random solution and make 2-permutation to have a better score """
  start = list(range(n))
  shuffle(start)
  solution = [[start[i], start[i + 1]] for i in range(0, n, 2)]
  min_score = utils.compute_score(preferences, solution)
  print(f"Basic solution: {min_score}")
  no_progress_round = 0

  while no_progress_round < 30:
    a1 = randint(0, n - 1)
    a2 = randint(0, n - 1)

    solution[a1 // 2][a1 % 2], solution[a2 // 2][a2 % 2] = solution[a2 // 2][a2 % 2], solution[a1 // 2][a1 % 2]
    
    new_score = utils.compute_score(preferences, solution)

    if new_score < min_score:
      no_progress_round = 0
      min_score = new_score
    else:
      solution[a1 // 2][a1 % 2], solution[a2 // 2][a2 % 2] = solution[a2 // 2][a2 % 2], solution[a1 // 2][a1 % 2]
      no_progress_round += 1

  return solution


if __name__ == "__main__":
  n, m, preferences = utils.get_preferences("data/sample_2.txt")

  assert n % 2 == 0

  solution = solve_2_roommates(n, m, preferences)
  score = utils.compute_score(preferences, solution)

  print(f"Found a solution with a score of {score}")

  utils.save_solution("output/solution_" + str(score) + ".txt", solution)
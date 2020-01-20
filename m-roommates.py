import utils
from random import randint, shuffle

def solve_m_roommates(n, m, preferences):
  """ Group the n people by m.
  Start by a random """ 


if __name__ == "__main__":
  n, m, preferences = utils.get_preferences("data/sample_2.txt")

  assert n % m == 0

  solution = solve_m_roommates(n, m, preferences)
  score = utils.compute_score(preferences, solution)

  print(f"Found a solution with a score of {score}")

  utils.save_solution("output/solution_" + str(score) + ".txt", solution)
import utils
from random import randint, shuffle

def solve_2_roommates_greedy(n, m, preferences):
  """ Try a greedy algorithm. Sort the people from the 
  most prefered person to the least one. Then, we combine
  them 2 by 2 in that order. """
  prefered_people = [[i, 0] for i in range(n)]

  for i in range(n):
    for j in range(n - 1):
      prefered_people[preferences[i][j]][1] += j
  
  prefered_people.sort(key = lambda tup : tup[1])

  return [[prefered_people[i][0], prefered_people[i + 1][0]] for i in range(0, n, 2)]


def solve_2_roommates_conv(n, m, preferences):
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
  n, m, _, preferences = utils.get_preferences("data/sample_2.txt")

  assert n % 2 == 0

  solution = solve_2_roommates_greedy(n, m, preferences)
  score = utils.compute_score(preferences, solution)
  print(f"Found a solution with a greedy algorithm of score {score}\n")
  utils.save_solution("output/solution_" + str(score) + ".txt", solution)

  solution = solve_2_roommates_conv(n, m, preferences)
  score = utils.compute_score(preferences, solution)

  print(f"Found a solution with a score of {score}")

  utils.save_solution("output/solution_" + str(score) + ".txt", solution)
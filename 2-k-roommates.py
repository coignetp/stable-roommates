import utils
from random import randint, shuffle


def generate_group_sizes(n, m_min, m_max):
  """ Generate different group sizes g1 .. gq between m_min
  and m_max where g1 + .. + gq = n """

  if m_min == m_max:
    if n % m_min == 0:
      return [m_min] * (n // m_min)
    else:
      return None
  
  if n < m_min:
    return None

  l = list(range(m_min, m_max + 1))
  shuffle(l)

  while len(l) > 0:
    group_size = l.pop()
    attribution = generate_group_sizes(n - group_size, m_min, min(m_max, group_size))

    if attribution is not None:
      return [group_size] + attribution

  return None


def create_solution(n, preferences, group_sizes):
  """ Create a solution from the preferences and the group sizes given.
  Start from a random solution and do 2-permutation until no 2-permutation
  can improve the score. Then do a 3-permutation to keep on improving the score. """

  solution = list(range(0, n))
  shuffle(solution)
  actual_score = utils.compute_score_att(preferences, solution, group_sizes)

  no_chgt = 0
  no_chgt_3_switch = 0

  while no_chgt_3_switch < 200:
    while no_chgt < 200:
      a1 = randint(0, n - 1)
      a2 = randint(0, n - 1)

      solution[a1], solution[a2] = solution[a2], solution[a1]
      new_score = utils.compute_score_att(preferences, solution, group_sizes)

      if new_score < actual_score:
        no_chgt = 0
        actual_score = new_score
      else:
        no_chgt += 1
        solution[a1], solution[a2] = solution[a2], solution[a1]
    
    no_chgt_3_switch += 1
    b1 = randint(0, n - 1)
    b2 = randint(0, n - 1)
    b3 = randint(0, n - 1)

    temp_var = solution[b1]
    solution[b1] = solution[b2]
    solution[b2] = solution[b3]
    solution[b3] = temp_var

    new_score = utils.compute_score_att(preferences, solution, group_sizes)

    if new_score < actual_score:
      no_chgt_3_switch = 0
      actual_score = new_score
    else:
      temp_var = solution[b3]
      solution[b3] = solution[b2]
      solution[b2] = solution[b1]
      solution[b1] = temp_var

  
  return solution, actual_score


def solve_m_roommates(n, m_min, m_max, preferences):
  """ Group the n people by m1 to m2.
  Start by a random solution and make some 2-permutations. """
  
  group_sizes = generate_group_sizes(n, m_min, m_max)
  solution = list(range(0, n))
  shuffle(solution)
  actual_score = utils.compute_score_att(preferences, solution, group_sizes)
  
  no_chgt = 0
  no_chgt_group_size = 0

  while no_chgt_group_size < 200:
    new_group_size = generate_group_sizes(n, m_min, m_max)
    no_chgt_group_size += 1

    while no_chgt < 200:
      new_solution, new_score = create_solution(n, preferences, new_group_size)
      no_chgt += 1

      if new_score < actual_score:
        actual_score = new_score
        solution = new_solution
        group_sizes = new_group_size
        no_chgt = 0
        no_chgt_group_size = 0

  return solution, group_sizes


if __name__ == "__main__":
  n, m_min, m_max, preferences = utils.get_preferences("data/sample_2.txt")

  solution, group_sizes = solve_m_roommates(n, m_min, m_max, preferences)
  score = utils.compute_score_att(preferences, solution, group_sizes)

  print(f"Found a solution with a score of {score}")

  utils.save_solution_att("output/solution_" + str(m_min) + "_" + str(m_max) + "_" + str(score) + ".txt", solution, group_sizes)
import utils
import sys

if __name__ == "__main__":
  filename = sys.argv[1]
  preferences = sys.argv[2]

  with open(filename) as file:
    header = file.readline()
    
    N = header.rstrip("\n").split("=")[1]

    n, m, _, preferences = utils.get_preferences(preferences)

    placed = [False for _ in range(n)]
    solution = []

    line = file.readline().rstrip("\n").split()
    for i in range(n):      
      if not placed[i]:
        solution.append([])
        for j in range(n):
          if line[(i * n) + j] == '1' and not placed[j]:
            print(f"Placing {j} in {solution[-1]} ({(i*n)+j})")
            placed[j] = True
            solution[-1].append(j)

    print(solution)

    score = utils.compute_score(preferences, solution)

    print(f"Ampl score: {score}")
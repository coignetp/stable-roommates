import utils
import sys

if __name__ == "__main__":
  filename = sys.argv[1]
  preferences = sys.argv[2]

  with open(filename) as file:
    header = file.readline()
    
    N = header.rstrip("\n").split("=")[1]

    n, m, _, preferences = utils.get_preferences(preferences)

    # useless lines
    _ = file.readline()
    _ = file.readline()

    placed = [False for _ in range(n)]
    solution = []

    for i in range(n):
      line = file.readline().rstrip("\n").split()
      
      if not placed[i]:
        solution.append([])
        for j in range(n):
          if line[j + 1] == '1':
            placed[j] = True
            solution[-1].append(j)

    print(solution)

    score = utils.compute_score(preferences, solution)

    print(f"Ampl score: {score}")
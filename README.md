# stable-roommates
Algorithm to solve the stable roommates problem for groups of k roommates with n participants

# Complexity
The number of possibility to group n people in k-sized group is n!/((k!)^(n/k) * (n/k)!. We cannot do all the possibilities, so we will go for a random start algorithm with permutations. 
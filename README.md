# Description
## Initial problem
We have `n` different people who have different affinities between each other. They want to be grouped in order to be roommates. However, they cannot `n` in the same appartment due to physical constraint. They can only be between `k1` and `k2`, where `0 < k1 <= k2`. This is a generalization of the stable roommates problem. 

This problem can also be seen as finding the best partition of a set with `n` elements where all the subset have between `k1` and `k2` elements. 

The sample data were generated randomly. `sample_1.txt` is a data sample with 10 people, and `sample_2.txt` is a sample with 100 people.

## Simplified problems
In order to make thing easier, we will also consider 2 problem.

The 2-roommates problem, where `k1 = k2 = 2`.

The k-roommates problem, where `k1 = k2` (generalization of 2-roommates).

# Complexity
For the k-roommates problem, the number of possibility to group n people in k-sized group is `n!/((k!)^(n/k) * (n/k)!)` (considering n = kq). We cannot do all the possibilities, so we will have to find another way.

# Possible solution
## Greedy algorithm for 2-roommates
I tried a greedy algorithm for the 2-roommates problem. The idea is to order the people from the most prefered person to the least one. Once its done, we just group the 2 most prefered people together, then the 2 next one, etc..  
The issue with this problem is that the score is not really better than a completely random algorithm.

I didn't really have any better idea for a greedy algorithm, so I did a random optimisation algorithm.

## Random algorithm for 2-roommates and k-roommates
The goal is to start from a completly random attribution and then do 2-permutation until we cannot improve the solution. The score is way better than a full random algorithm, and we can still run the algorithm again if we don't like the local optimum. We reach a local optimum in less than 0.2s with a common computer for `n=100`.

## Algorithm for the k1-k2-roommates
In this problem, we have to decide the size of the groups and the attribution of the solution. The first part here is to randomly choose group sizes with `generate_group_sizes`. Then we take a random solution, and we try to reach the local optimum thanks to 2-permutation and 3-permutation. In order to have a better solution, we try multiple random solution for the same group sizes and we try multiple random group sizes until we cannot do better. We reach a local optimum in about a minute.
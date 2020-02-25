param N;
param K1;
param K2;

set Length := 1 .. N;

param Preferences {Length cross Length};

var attributions {Length cross Length} >= 0, <= 1, integer;

minimize Objective:
  sum{(i,j) in Length cross Length} attributions[i, j] * Preferences[i, j];

subject to sym {(i,j) in Length cross Length}: attributions[i, j] == attributions[j, i];
subject to self_roommates {i in Length}: attributions[i, i] == 1;
subject to k_roommates {i in Length}: sum{j in Length} attributions[i, j] == 2; # 2 roommates
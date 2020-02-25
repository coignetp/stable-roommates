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
subject to k1_roommates {i in Length}: sum{j in Length} attributions[i, j] >= K1;
subject to k2_roommates {i in Length}: sum{j in Length} attributions[i, j] <= K2;

subject to standardize_roommates {(i,j) in Length cross Length, v in Length}:
  if attributions[i,j] == attributions[i,v] and attributions[i,j] == 1 
    then attributions[j,v] == 1;
;
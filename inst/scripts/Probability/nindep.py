import numpy as np
from itertools import combinations

P = 0
while np.any(P == 0):
  P = np.round(np.random.uniform(size=8), 1)
  P = P / P.sum()

# probabilistic weights

print(P)
if abs(P.sum() - 1) > 0.01:
  raise ValueError("Error in P")

vec = np.arange(1, len(P)+1)
AllSets = [comb for i in vec for comb in combinations(vec, i)]

Nindep = 0
for i, event1 in enumerate(AllSets[:-1]):
  for j, event2 in enumerate(AllSets[i+1:]):
    Inters = set(event1).intersection(event2)
    Inters = [i for i in Inters if i < len(P)]
    if len(Inters) > 0:
        event1 = [i for i in event1 if i < len(P)]
        P1 = P[np.ix_(event1)].sum()
        event2 = [i for i in event2 if i < len(P)]
        P2 = P[np.ix_(event2)].sum()
        PI = sum(P[list(Inters)])
        if PI == P1 * P2:
            print(f"E1={event1} E2={event2} P1={P1} P2={P2} PI={PI}")
            Nindep += 1

print(P)
print(f"The number of independent events is {Nindep}")
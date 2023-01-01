import pandas as pd

def P(model, **kwargs):
    M = pd.DataFrame(model)
    query = ' and '.join([f"{k} == {v}" for k, v in kwargs.items()])
    return M.query(query).p.sum()

# Define the data frame 'Model'
Model = pd.DataFrame({'z1': ['CLEAR', 'CLEAR', 'CLEAR', 'CLEAR', 'CLOUDY', 'CLOUDY', 'CLOUDY', 'CLOUDY'],
                      'z2': ['RISING', 'RISING', 'FALLING', 'FALLING', 'RISING', 'RISING', 'FALLING', 'FALLING'],
                      'z3': ['DRY', 'WET', 'DRY', 'WET', 'DRY', 'WET', 'DRY', 'WET'],
                      'p': [0.4, 0.07, 0.08, 0.1, 0.09, 0.11, 0.03, 0.12]})

# P(CLEAR, RISING)
print(P(Model, z1=['CLEAR'], z2=['RISING']))

# P(CLOUDY)
print(P(Model, z1=['CLOUDY']))

# P(DRY | CLEAR, RISING)
print(P(Model, z1=['CLEAR'], z2=['RISING'], z3=['DRY']) / P(Model, z1=['CLEAR'], z2=['RISING']))

# P(CLOUDY, RISING) + P(CLOUDY, FALLING)
print(P(Model, z1=['CLOUDY'], z2=['RISING']) + P(Model, z1=['CLOUDY'], z2=['FALLING']))

# P(CLEAR, FALLING) / P(CLEAR)
print(P(Model, z1=['CLEAR'], z2=['FALLING']) / P(Model, z1=['CLEAR']))

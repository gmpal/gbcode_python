import pandas as pd


def P(model, **kwargs):
    M = pd.DataFrame(model)
    query = ' and '.join([f"{k} == {v}" for k, v in kwargs.items()])
    return M.query(query).p.sum()

Model = {
    'owner': ['IT', 'BE', 'IT', 'BE', 'IT', 'BE', 'IT', 'BE'],
    'cook': ['IT', 'IT', 'BE', 'BE', 'IT', 'IT', 'BE', 'BE'],
    'pizza': ['GOOD', 'GOOD', 'GOOD', 'GOOD', 'BAD', 'BAD', 'BAD', 'BAD'],
    'p': [0.378, 0.168, 0.012, 0.032, 0.162, 0.072, 0.048, 0.128]
}

print(P(Model, pizza=['GOOD']))
print(P(Model, pizza=['GOOD'], owner=['IT']) / P(Model, owner=['IT']))
print(P(Model, pizza=['GOOD'], owner=['BE']) / P(Model, owner=['BE']))

print(P(Model, pizza=['GOOD'], cook=['IT'], owner=['IT']) / P(Model, cook=['IT'], owner=['IT']))
print(P(Model, pizza=['GOOD'], cook=['IT']) / P(Model, cook=['IT']))
print(P(Model, pizza=['GOOD'], cook=['IT'], owner=['BE']) / P(Model, cook=['IT'], owner=['BE']))

print(P(Model, pizza=['GOOD'], cook=['BE'], owner=['IT']) / P(Model, cook=['BE'], owner=['IT']))
print(P(Model, pizza=['GOOD'], cook=['BE']) / P(Model, cook=['BE']))
print(P(Model, pizza=['GOOD'], cook=['BE'], owner=['BE']) / P(Model, cook=['BE'], owner=['BE']))
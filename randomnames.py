randomnames.py

import random

def get_random_nickname():
    adjvs = ['golden', 'ruby', 'fuzzy', 'liquid', 'sour', 'snowy', 'blazing']
    nouns = ['shores', 'keys', 'peaks', 'smiles', 'jungles', 'skies', 'forests']

    return random.choice(adjvs) + ' ' + random.choice(nouns)
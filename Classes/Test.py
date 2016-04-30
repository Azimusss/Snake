import json, os


def form(name, score):
    sym = 30 - len(name)
    return name, ' '*sym, score

DIR = '..'
lol = []

top = json.load(open(os.path.join(DIR, 'Top_Records.json'), 'r'))

l = []
for player in top:
    l.append('%s %s %s' % (form(player['name'], player['score'])))

print(l)
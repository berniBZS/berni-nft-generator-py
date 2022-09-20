import json
from prettyprinter import pprint
import pandas as pd

expected = json.load(open('expected-rarity.json'))
generated = json.load(open('all-rarity.json'))

traits_categs = []
traits_names = []
traits_expected = []
traits_generated = []
traits_diff = []



background_expected = expected[0]['Background']
background_generated = generated[0]['Background']
for k,v in background_expected.items():
    traits_categs.append('BACKGROUND')
    traits_names.append(k)
    traits_expected.append(v)
    traits_generated.append(background_generated[k])
    traits_diff.append(f'{int((background_generated[k]-v)*100/background_generated[k])}%')

body_expected = expected[1]['Body']
body_generated = generated[1]['Body']
for k,v in body_expected.items():
    traits_categs.append('BODY')
    traits_names.append(k)
    traits_expected.append(v)
    traits_generated.append(body_generated[k])
    traits_diff.append(f'{int((body_generated[k]-v)*100/body_generated[k])}%')

head_expected = expected[2]['Head']
head_generated = generated[2]['Head']
for k,v in head_expected.items():
    traits_categs.append('HEAD')
    traits_names.append(k)
    traits_expected.append(v)
    traits_generated.append(head_generated[k])
    traits_diff.append(f'{int((head_generated[k]-v)*100/head_generated[k])}%')

eyes_expected = expected[3]['Eyes']
eyes_generated = generated[3]['Eyes']
for k,v in eyes_expected.items():
    traits_categs.append('EYES')
    traits_names.append(k)
    traits_expected.append(v)
    traits_generated.append(eyes_generated[k])
    traits_diff.append(f'{int((eyes_generated[k]-v)*100/eyes_generated[k])}%')


rarity_comparative = pd.DataFrame(list(zip(traits_categs, traits_names, traits_expected, traits_generated, traits_diff)),
                                  columns = ['category', 'name', 'expected', 'generated', 'difference'])

rarity_comparative.to_csv('rarity_comparative.csv')
pprint(rarity_comparative)
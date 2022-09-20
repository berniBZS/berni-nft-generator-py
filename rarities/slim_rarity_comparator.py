import json

def check_loop(expected, generated):


    traits_diff = []

    background_expected = expected[0]['Background']
    background_generated = generated[0]['Background']
    for k,v in background_expected.items():
        traits_diff.append(int((background_generated[k]-v)*100/background_generated[k]))

    body_expected = expected[2]['Body']
    body_generated = generated[2]['Body']
    for k,v in body_expected.items():
        traits_diff.append(int((body_generated[k]-v)*100/body_generated[k]))

    head_expected = expected[1]['Head']
    head_generated = generated[1]['Head']
    for k,v in head_expected.items():
        traits_diff.append(int((head_generated[k]-v)*100/head_generated[k]))

    eyes_expected = expected[3]['Eyes']
    eyes_generated = generated[3]['Eyes']
    for k,v in eyes_expected.items():
        traits_diff.append(int((eyes_generated[k]-v)*100/eyes_generated[k]))


    discard_per_gold = body_generated['Gold'] > 33
    discard_per_diamond = body_generated['Diamond'] > 33
    discard_per_percentage = any(ele > 19 or ele < -20 for ele in traits_diff)

    if any((discard_per_gold, discard_per_diamond, discard_per_percentage)):
        discard = True
    else:
        discard = False

    status = f'Gold: {body_generated["Gold"]} | Diamond: {body_generated["Diamond"]} | Max %: {max(traits_diff)} | Min %: {min(traits_diff)}'
    return discard, status

import glob
import itertools
import os

# def get_filenames(exts):
#     fnames = [glob.glob(ext) for ext in exts]
#     fnames = list(itertools.chain.from_iterable(fnames))
#     return fnames
#
# def rename_file(before, after):
#     os.rename(before, after)
#
# exts = ["*.png","*/*.png"]
# res = get_filenames(exts)
#
# renamed = []
# for file in res:
#     after = f'{file.split("#")[0]}.png'
#     os.rename(file, after)
#     renamed.append(after)
#
# print(renamed)

all_traits =  [
    ['Berry.png', 'Yellow.png', 'Cyan.png', 'Wine Cosmos.png', 'Unlockd Universe.png', 'Archaic Binary.png', 'Fuchsia.png', 'Azure Lightning.png', 'Ancient Binary.png', 'Teal Scrapyard.png', 'Blue.png', 'Violet Factory.png', 'Plum Scrapyard.png', 'Sapphire Scrapyard.png', 'Lilac Lightning.png', 'Rusty Factory.png', 'Lavender Cosmos.png', 'Blood Cosmos.png'],
    ['Dumbfounded.png', 'Chill.png', 'Tilted.png', 'Evil.png', 'questionmark.png', 'Happy.png', 'Surprised.png', 'Baked.png', 'Mad.png', 'Outraged.png', 'Lifeline.png', 'Angry.png', 'Expectant.png'],
    ['Gold.png', 'Sentinel.png', 'Ancient.png', 'Freezer.png', 'Steampunk.png', 'ironclad.png', '0x220907.png', 'Guardian.png', 'Gadgeto.png', 'Assimov.png', 'Businessbot.png', 'Multitasker.png', 'Buzzer.png', 'Chunky.png', 'Pumpking.png', 'Turing.png', 'Diamond.png'],
    ['Golden Custodian.png', 'Golden Mastermind.png', 'Custodian.png', 'Golden Enlightened.png', 'Enlightened.png', 'Mastermind.png', 'Golden Operator.png', 'Operator.png']
]

for t in all_traits:
    values = []
    for i in t:
        value=i.split('.')[0]
        values.append(value)
    print(values)

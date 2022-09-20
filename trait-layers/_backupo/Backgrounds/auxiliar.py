import glob
import itertools
import os

def get_filenames(exts):
    fnames = [glob.glob(ext) for ext in exts]
    fnames = list(itertools.chain.from_iterable(fnames))
    return fnames

def rename_file(before, after):
    os.rename(before, after)

exts = ["*.png","*/*.png"]
res = get_filenames(exts)

renamed = []
for file in res:
    after = f'{file.split("#")[0]}.png'
    os.rename(file, after)
    renamed.append(after)

print(renamed)


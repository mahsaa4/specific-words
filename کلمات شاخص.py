import re
from collections import OrderedDict
SampleReport = input()
pat = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)
sentences = pat.findall(SampleReport)
count = 0
for sentence in sentences:
    splits = sentence.split()
    for index, split in enumerate(splits):
        count +=1
        if split.istitle() and index != 0:
            new_split = split.rstrip('.,')
            print(count , ':' , new_split)
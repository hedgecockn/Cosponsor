import re
import collections
from collections import defaultdict

text = open('Cosponsor.txt', 'r').read()
sponsors = re.findall(r'Sponsor:(.*?)\(', text)
sponsorCounts = collections.Counter(sponsors).most_common()

with open('Output.txt', 'w') as file_handler:
    for item in sponsorCounts:
        file_handler.write("{}\n".format(item))

print('Your rep cosponsored with' , len(sponsorCounts) , 'different reps')
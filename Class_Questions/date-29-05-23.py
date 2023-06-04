import sys
from collections import Counter

word_data = Counter()
for i in sys.stdin:
    word = i.strip().split()
    word_data.update(word)
print(word_data.most_common(1))

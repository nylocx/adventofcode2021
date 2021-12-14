#%% Initialize
from collections import Counter

#%% Read input
with open("day_14_input.txt") as f:
    template = f.readline().strip()
    f.readline()
    rules = dict(line.strip().split(" -> ") for line in f)


#%% Common
def apply_rules(bigrams, letters):
    for bigram, count in bigrams.copy().items():
        new_letter = rules[bigram]
        bigrams[bigram] -= count
        bigrams[bigram[0] + new_letter] += count
        bigrams[new_letter + bigram[1]] += count
        letters[new_letter] += count


#%% Part 1
letter_counter = Counter(template)
bigram_counter = Counter(template[i: i + 2] for i in range(len(template) - 1))
for i in range(10):
    apply_rules(bigram_counter, letter_counter)

most_common = letter_counter.most_common(len(letter_counter))

print(most_common[0][1] - most_common[-1][1])

# %% Part 2
letter_counter = Counter(template)
bigram_counter = Counter(template[i: i + 2] for i in range(len(template) - 1))
for i in range(40):
    apply_rules(bigram_counter, letter_counter)

most_common = letter_counter.most_common(len(letter_counter))

print(most_common[0][1] - most_common[-1][1])

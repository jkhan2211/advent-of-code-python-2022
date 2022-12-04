

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
import string
from collections import OrderedDict
lower_priorities = OrderedDict(zip(string.ascii_lowercase, range(1,27)))
upper_priorities = OrderedDict(zip(string.ascii_uppercase, range(27,53)))
score_card = []

with open("test.txt") as data:
    for line in data:
        x = len(line)
        string1 = slice(0, len(line) // 2)
        string2 = slice(len(line) // 2, len(line))
        string1_store = line[string1]
        string2_store = line[string2]

        commonChar = ''.join(
        set(string1_store).intersection(string2_store))

        if commonChar.islower():
            lower_value = lower_priorities[commonChar]
            score_card.append(lower_value)
        else:
            higher_value = upper_priorities[commonChar]
            score_card.append(higher_value)
    print(sum(score_card))
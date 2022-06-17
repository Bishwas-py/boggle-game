import random
import string

import numpy as np

a = ['cat', 'fat', 'rat', 'hat', 'echo']

newMat = list(list(''.join(a)))
print(newMat)
for i in range(16):
    print(i, len(newMat))
    if len(newMat) < 16:
        while True:
            character = random.choice(string.ascii_lowercase)
            if character not in newMat:
                newMat.append(character)
                break
    if len(newMat) == 16:
        break

print(newMat)

print(np.array(newMat).reshape(4, 4))

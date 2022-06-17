from numpy import array
import random

import data

randomInt = random.randrange(1, len(data.words))
print(randomInt)
wordsList = data.words[randomInt:randomInt + 3]
print(wordsList)
wordsMatrix = []

for word in wordsList:
    wordsMatrix.append(list(word))

cleanWordsLetterList = []
for wordsArray in wordsMatrix:
    for word in wordsArray:
        if word not in cleanWordsLetterList:
            cleanWordsLetterList.append(word)

print(cleanWordsLetterList)

# #User function Template for python3
#
# class Solution:
#     def wordBoggle(self,board,dictionary):
#         words = []
#         for wordsMatrix in board:
#             if all(isinstance(item, str) for item in wordsMatrix):
#                 words.append(wordsMatrix)
#         return words


# class Solution:
#     def wordBoggle(self,board,dictionary):
#         # return list of words(str) found in the board
[
    ['C', 'A', 'P'],
    ['A', 'N', 'D'],
    ['T', 'I', 'E']
]

vowels = ['a', 'e', 'i', 'o', 'u']


def main():
    wordToCheck = input("Word to check:  ")
    dissectedWord = list(wordToCheck)

    realWordProb = 0
    dissectedWord.sort()
    for letter in dissectedWord:
        for vowel in vowels:
            if vowel == letter:
                realWordProb += 1

    if 0 < realWordProb < 7:
        print(f"Yes, {wordToCheck} is a real word.")
        main()
    else:
        print(f"Sorry, {wordToCheck} is't a real word.")
    wannaContinue = input("Wanna continue? (enter/no):   ")
    if not wannaContinue.lower():
        main()

if __name__ == "__main__":
    main()
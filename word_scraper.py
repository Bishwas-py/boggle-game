import json

import requests

url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt?fbclid=IwAR12Yk9Od-tfuUktSPBUHhdunD2KbisXRV1XD55o4v4kRoTn1Wy81JMR1Ws"


def makeWords():
    requiredWords = []
    response = requests.get(url)
    if response.ok:
        textualWords = response.text
        for textualWord in textualWords.splitlines():
            if len(textualWord) >= 3:
                requiredWords.append(textualWord)
    data = {
        'words': requiredWords
    }

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    makeWords()

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseMap = {'a':".-",'b':"-...",'c':"-.-.",'d':"-..",
                    'e':".",'f':"..-.",'g':"--.",'h':"....",
                    'i':"..",'j':".---",'k':"-.-",'l':".-..",
                    'm':"--",'n':"-.",'o':"---",'p':".--.",
                    'q':"--.-",'r':".-.",'s':"...",'t':"-",
                    'u':"..-",'v':"...-",'w':".--",'x':"-..-",
                    'y':"-.--",'z':"--.."}
        result = []
        for item in words:
            itemResult = ''
            itemSplit = list(item)
            for letter in itemSplit:
                if letter in morseMap:
                    itemResult += morseMap[letter]
            result.append(itemResult)
        resultClean = set(result)
        return len(resultClean)

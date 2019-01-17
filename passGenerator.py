import itertools
import argparse

#TODO: Add File Export To Command Line
######################################################
# Generate all possible combinations of a passphrase #
######################################################
class PasswordGenerator:

    def __init__(self, passphrase):
        self.mapping = {
            "a" : ["a", "A", "@","^"], "b" : ["b","B"],"c" : ["c","C"], "d" : ["d","D"],
            "e" : ["e","E"], "f": ["f","F"], "g": ["g","G"], "h" : ["h", "H","#"], "i" : ["i","I","!","1"],
            "j" : ["j", "J"], "k": ["k","K"], "l": ["l","L"], "m": ["m","M"], "n" : ["n","N"], "o": ["o", "O","0"],
            "p" : ["p", "P"], "q" : ["q", "Q"] ,"r" : ["r", "R"] , "s" : ["s","S", "$","5"], "t" :["t","T"], "u": ["u","U"],
            "v" : ["v", "V","\/"], "w": ["w","W"],  "x": ["x","X"], "y": ["y","Y"], "z" : ["z","Z","2"]
        }
        self.allCombinations(passphrase)

    def allCombinations(self,string):
       com = map(''.join, itertools.product(*((self.mapping[c]) for c in string)))
       for x in com:
           print(x)

    def productOf(self, passphrase):
        letters = []
        for c in passphrase:
            letters.append(c)
            for x in self.mapping[c]:
                letters.append(x)
        x = itertools.permutations(letters,len(passphrase))
        for xx in x:
            print(''.join(xx))


    def characterMapping(self, passphrase):
        letters_used = []
        for c in passphrase:
            for x in self.mapping[c]:
                letters_used.append(x)
        return letters_used

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("string", help="String to display all possible combinations for")
    args = parser.parse_args()
    passphrase = args.string
    PasswordGenerator(passphrase.lower())

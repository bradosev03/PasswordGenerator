
import string
import itertools
class PasswordGenerator:

    def __init__(self, passphrase):
        self.mapping = {
            "a" : ["A", "@","^"], "b" : ["B"],"c" : ["C"],"d" : ["D"],
            "e" : ["E"], "f": ["F"], "g": ["G"],"h" : ["H","#"], "i" : ["I","!","1"],
            "j" : ["J"], "k": ["K"], "l": ["L"], "m": ["M"], "n" : ["N"], "o": ["O","0"],
            "p" : ["P"], "q" : ["Q"] ,"r" : ["R"] , "s" : ["S", "$"], "t" :["T"], "u": ["U"],
            "v" : ["V"], "w": ["W"],  "x": ["X"], "z" : ["Z"]
        }
        #p = self.characterMapping(passphrase)
        self.productOf(passphrase)

    def productOf(self, passphrase):
        letters = []
        for c in passphrase:
            letters.append(c)
            for x in self.mapping[c]:
                letters.append(x)
        x = itertools.permutations(letters,len(passphrase))
        for xx in x:
            print ''.join(xx)


    def characterMapping(self, passphrase):
        letters_used = []
        for c in passphrase:
            for x in self.mapping[c]:
                letters_used.append(x)

        return letters_used

if __name__ == "__main__":
    PasswordGenerator("ilikehotdogs")

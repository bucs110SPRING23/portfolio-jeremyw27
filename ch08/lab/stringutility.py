class StringUtility:

    def __init__(self, string=""):
        self.string = string
        
    def __str__(self):
        """
        Returns the unchanged internal string.
        args: none
        return: string
        """
        return self.string
    
    def vowels(self):
        """
        Counts the number of vowels in the string and returns the result as a string. If the count is less than 5, the string representation of the number is returned. If the count is 5 or more, the word "many" is returned instead.
        args: none
        return: string
        """
        return str(len([i for i in self.string if i in 'aeiou']) if len([i for i in self.string if i in 'aeiou']) < 5 else "many")

    def bothEnds(self):
        """
        Puts together the first 2 and last 2 characters of the original string if the original string length is greater than 2.
        args: none
        return: string
        """
        return self.string[0] + self.string[1] + self.string[-2] + self.string[-1] if len(self.string) > 2 else ''

    def fixStart(self):
        """
        Changes all occurrences of the first character to "*" except for the first character itself.
        args: none
        return: string
        """
        return (self.string[0] + "".join(['*' if i==self.string[0] else i for i in self.string[1:]])) if self.string else ''

    def asciiSum(self):
        """
        Sums up all the ascii values in the string.
        args: none
        return: int
        """
        return sum([ord(i) for i in self.string])

    def cipher(self):
        """
        Returns an encoded string by incrementing all letters by the length of the string itself. Does not change any characters that are not letters.
        args: none
        return: string
        """
        return "".join((chr((ord('a') + (ord(i) - ord('a') + len(self.string)) % 26))) if i.islower() else chr((ord('A') + (ord(i) - ord('A') + len(self.string)) % 26)) if i.isalpha() else " " for i in self.string)
    

    # attempts/work for cipher extra credit
    # "".join((list(chr((ord('a') + (ord(i) - ord('a') + len(self.string)) % 26)) if i.islower() else '' for i in self.string)) + (list(chr((ord('A') + (ord(i) - ord('A') + len(self.string)) % 26)) if i.isupper() else '' for i in self.string)))
    #(ord('A') + (ord(i) - ord('A') + len(self.string)) % 26) for  i in self.string]
    #[chr(ord('a') + (ord(i) - ord('a') + len(self.string)) % 26) for  i in self.string]
    # if lowercase: chr(ord('a') + ((ord(i) - ord('a') + len(self.string)) % 26) for i in self.string[:])
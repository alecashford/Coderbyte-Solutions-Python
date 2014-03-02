#Text of challenge: "Have the function VowelCount(str) take the str string
#parameter being passed and return the number of vowels the string contains
#(ie. "All cows eat grass" would return 5). Do not count y as a vowel for this challenge."


vowels = ["a", "e", "i", "o", "u"]

vowellist = []

def VowelCount(str):

    for i in str:
        if i in vowels:
            vowellist.append(i)
    
    vowelnum = len(vowellist)
    
    return vowelnum


print VowelCount(raw_input())

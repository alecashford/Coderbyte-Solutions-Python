#Text of challenge: "Have the function LongestWord(sen) take the sen parameter being passed
#and return the largest word in the string. If there are two or more words that are the
#same length, return the first word from the string with that length. Ignore punctuation
#and assume sen will not be empty."


punct = list(".,-_&/?!\"\'/")

def LongestWord(sen):
    for line in sen:
        if line in punct:
            sen = sen.replace(line, "")
    listed = sen.split(" ")
    return max(listed, key=len)


print LongestWord(raw_input())

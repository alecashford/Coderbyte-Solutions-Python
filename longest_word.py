punct = list(".,-_&/?!\"\'/")

def LongestWord(sen):
    for line in sen:
        if line in punct:
            sen = sen.replace(line, "")
    listed = sen.split(" ")
    return max(listed, key=len)


print LongestWord(raw_input())

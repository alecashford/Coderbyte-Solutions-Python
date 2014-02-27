def WordCount(str):

    wordsplit = str.split(" ")    
    answer = len(wordsplit)
    return answer

print WordCount(raw_input())

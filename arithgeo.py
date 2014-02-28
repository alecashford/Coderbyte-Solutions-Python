def ArithGeo(ar):

    arr = ar.split(",")
    if (int(arr[1]) - int(arr[0])) == (int(arr[len(arr) - 1])) - (int(arr[len(arr) - 2])):
        return "Arithmetic"
    elif (int(arr[1]) / int(arr[0])) == (int(arr[len(arr) - 1])) / (int(arr[len(arr) - 2])):
        return "Geometric"
    else:
        return "-1"

print ArithGeo(raw_input())

def ExOh(str):
    xs = 0
    os = 0
    for i in str:
        if i == "x":
            xs += 1
        elif i == "o":
            os += 1
    return xs == os



print ExOh(raw_input())

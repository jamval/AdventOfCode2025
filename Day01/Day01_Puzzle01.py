ExampleRotations = [
    ["L", 68],
    ["L", 30],
    ["R", 48],
    ["L", 5],
    ["R", 60],
    ["L", 55],
    ["L", 1],
    ["L", 99],
    ["R", 14],
    ["L", 82],
]

def TurnDial(startPos, direction, distance):
    if direction == "L":
        return (startPos - distance) % 100
    else:
        return (startPos + distance) % 100

def GetPassword(rotations):
    count = 0
    start = 50

    for rotation in rotations:
        start = TurnDial(start, rotation[0], rotation[1])
        if start == 0:
            count += 1

    return count

print(GetPassword(ExampleRotations))
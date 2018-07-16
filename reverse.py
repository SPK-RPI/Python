# Fucntion that reverSe uSerdefined value.

S = input("Enter Number to reverse: ")


def reverse(S):
    Str = ""
    for i in S:
        Str = i + Str
    return Str


print('The original String  is :', S)

print("The reveesed String is : ", reverse(S))

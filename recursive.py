def recure_factorial(n):
    if n == 1:
        return n
    else:
        return n*recure_factorial(n-1)


def main():
    num = input('Enter a number :-')
    if num.isalpha():
        print('You must enter a digit..')
        main()
    else:
        innum=int(num)
        if innum < 0:
            print('Sorry,Factorial does not exits for negtive numbers..')
        elif innum == 0:
            print('The factorial of zero is 1 ')

        else:
            print('The factorial of the number ',innum, 'is', recure_factorial(innum))


main()

# Python program to check if the number provided by the user is an Armstrong number or not
num = int(input("Enter a number: "))
def main():
    print('Select an option..')
    o=input('Armstrong:Palindrome (1:2)')
    if o in ('1'):
        arm()
        
    else:
        pal()


def arm():
    
    sum = 0
    order=len(str(num))

    temp = num
    while temp > 0:
       digit = temp % 10
       sum = sum+(digit ** order)
       temp = temp/10
    if num == sum:
       print(num,"is an Armstrong number")
    else:
       print(num,"is not an Armstrong number")

def pal():
    n = input('Enter Number to check for palindromee')
    m=n
    a = 0
    while(m!=0):
        a = m % 10 + a * 10
        m = m / 10
    if( n == a):
         print('%d is a palindrome number' %n)
    else:
         print('%d is not a palindrome number' %n)
main()           
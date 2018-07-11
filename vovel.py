def path():
    i=input('Do you want to try again (y/n): ')
    if (len(i)<=1):
        if i in ('y','Y'):
            getchar()
        else:
            print('Good bye')    

    else:
        print('Enter the correct option: ')
        path()




def getchar():
    i=input('Enter a charector ')
    if(len(i)<=2):
      if i[0] in ('a','e','i','o','u','A','E','I','O','U'):
        print('%s is an Vovel ',i[0])
        path()
      elif i[0] in ('1','2','3','4','5','6','7','8','9','0'):
            print('You have entered a digit enter a charector !!!!!')
            path()
      else:
          print('You have entered a consonent')
          path()
    else:
       print('Enter a charector not a string ...')
       path()       
getchar()    
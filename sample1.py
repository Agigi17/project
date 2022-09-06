print("Welcome to treasure island ")
choice01 = input ('Where to you want to go? type "greenline" or "redline".\n')

if choice01 == "greenline":
    choice02 = input('You\'ve come to greenflag. Type "love" or "bombing".\n').lower()
    if choice02 == "love":
        choice03 = input('You\'ve come to greenhouse. Just type "green", "purple", or "black". \n').lower()

        if choice03 == "green":
            print('you\'re in a right way')
        elif choice03 == "purple":
            print('you\'re in a wrong way!')
        elif choice03 == "black":
            print("Game over.")
        else: 
          print("You choose a wrong answer. Game over!")
    else:
         print("Game over!")
else:
    print("engkkk. Game over!")
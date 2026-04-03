#WAP of number which will keep adding a stream of number inputted by the uer . the adding stores as soon as user presses q key on the keyboard
sum = 0
while(True):
    number = (input("Enter the item price or press q to quit : \n"))
    if(number != 'q'):
        sum = sum + int(number)
        print(f"order total so far :{sum}")
        
    else: 
        print(f"You bill total is {sum}. Thanks for shopping with us")
        break   
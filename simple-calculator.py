def choose():
    arr = []
    def history():
        x = len(arr)
        if(x == 0):
            print("No past calculations to show")
        else:
            for x in arr:
                print(x)
    
    while True:
        print("Select operation.")
        print("1.Add      : + ")
        print("2.Subtract : - ")
        print("3.Multiply : * ")
        print("4.Divide   : / ")
        print("5.Power    : ^ ")
        print("6.Remainder: % ")
        print("7.Terminate: # ")
        print("8.Reset    : $ ")
        print("8.History  : ? ")
  # take input from the user
        choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
        print(choice)
        def select_op(choice):
            if(choice == '#'):
                return -1
            elif(choice=='+'):
                return 1
            elif(choice=='-'):
                return 2
            elif(choice=='*'):
                return 3
            elif(choice=='/'):
                return 4
            elif(choice=='^'):
                return 5
            elif(choice=='%'):
                return 6
            elif(choice=='?'):
                history()
                choose()
            else:
                return 0
  
        if(select_op(choice) == -1):
    #program ends here
            print("Done. Terminating")
            exit()
        elif(select_op(choice) >=1)and(select_op(choice) <=7):
 
            def check_user_input(input):
                try:
                    val = float(input)
                    return val
                except ValueError:
                    choose()
        
      
            num1 = input("Enter first number: ")
            print(num1)
            if(num1=='#'):
                print("Done. Terminating")
                exit()
            else:
                num1 = check_user_input(num1)
                
            num2 = input("Enter second number: ")
            print(num2)
            if(num2=='#'):
                print("Done. Terminating")
                exit()
            else:
                num2 = check_user_input(num2)
                
      
            if(select_op(choice) == 1):
                    ans = str(num1+num2)
                    display =str((str(num1)+" "+choice+" "+str(num2)+" = "+ans))
                    print(display)
                    arr.append(display)
            elif(select_op(choice) == 2):
                    ans = str(num1-num2)
                    display =str((str(num1)+" "+choice+" "+str(num2)+" = "+ans))
                    print(display)
                    arr.append(display)
            elif(select_op(choice) == 3):
                    ans = str(num1*num2)
                    display =str((str(num1)+" "+choice+" "+str(num2)+" = "+ans))
                    print(display)
                    arr.append(display)
            elif(select_op(choice) == 4):
                    if(num2==0):
                        print("float division by zero")
                        display =str((str(num1)+" "+choice+" "+str(num2)+" = "+"None"))
                        print(display)
                        arr.append(display)
                    else:
                        ans = str(num1/num2)
                        display =str((str(num1)+" "+choice+" "+str(num2)+" = "+ans))
                        print(display)
                        arr.append(display)
            elif(select_op(choice) == 5):
                    ans = str(num1**num2)
                    display =str((str(num1)+" "+choice+" "+str(num2)+" = "+ans))
                    print(display)
                    arr.append(display)
            elif(select_op(choice) == 6):
                    ans = str(num1%num2)
                    display =str((str(num1)+" "+choice+" "+str(num2)+" = "+ans))
                    print(display)
                    arr.append(display)
        else:
            print("Unrecognized operation")
  
choose()

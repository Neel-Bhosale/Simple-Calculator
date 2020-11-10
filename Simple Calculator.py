#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Simple CalculotorS

#SDefined Calculate function
def calculate():
    while True:
        operation=input('''Select Operation : 
                1. Addition
                2. Substration
                3. Multiplication
                4. Division
                5. Power
                6. Modulos
                ''')
        
        if operation in('1','2','3','4','5','6'):
            
            #Takes Integer Input from user
            num1=int(input("Enter First number : "))
            num2=int(input("Enter Second number : "))
    
            #ADDITION
            if operation == '1':
                print("{} + {} = ".format(num1,num2))
                print(num1 + num2)
    
            #SUBSTRACTION
            elif operation == '2':
                print("{} - {} = ".format(num1,num2))
                print(num1 - num2)
    
            #mULTIPLICATION
            elif operation == '3':
                print("{} * {} = ".format(num1,num2))
                print(num1 * num2)
    
            #DIVISION
            elif operation == '4':
                print("{} / {} = ".format(num1,num2))
                print(num1 / num2)
    
            #POWER
            elif operation == '5':
                print("{} ** {} = ".format(num1,num2))
                print(num1 ** num2)
    
            #MODULOS
            elif operation == '6':
                print("{} % {} = ".format(num1,num2))
                print(num1 % num2)
            break
        else:
            print("You have choosen Wrong operation ! ")
        
    #'AGAIN' fuction is defined to ask whether to use calculator again or not    
    def again():
        cal_again= input('''
        Do you want to use calculator again ? 
        Type 'Y' for YES and 'N' for NO
        ''')
        
        #if 'YES',goes to 'calculate' function
        if cal_again.upper() == 'Y':
            calculate()
        
        #if 'NO',exits the calculator
        elif cal_again.upper() == 'N':
            print('''See You Later ,Bye !''')
            
        else:
            again()
    
    #'again' function is called
    again()

#'calculate' function is called    
calculate()


# In[ ]:





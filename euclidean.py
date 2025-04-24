

#“I confirm that this assignment is my own work.  
#Where I/we have referred to academic sources, I have provided in-text 
#citations and included the sources in the final reference list. “


class EuclideanAlgorithm:
    
    def __init__(self, a, b):
        #two positive integers stored as private attributes _a and _b
        
        if not self._is_positive_integer(a) or not self._is_positive_integer(b):
            self._a= None   #set _a to None to indicate invalid input
            self._b= None   #set _b to None to indicate invalid input
            self._valid= False   #set _valid to False to indicate invalid input
        else:
            self._a=a   #store first integer
            self._b=b   #store second integer
            self._valid= True   #set _valid to True to indicate valid input
        self._gcd= None   #initialize _gcd to None, indicating that the GCD
                          #has not yet been calculated
        
    def _is_positive_integer(self,n):
        #checks if a given number is a positive integer
        #check if n is of type int and greater than 0
        return type(n) ==int and n>0   
    
    def is_valid(self):
        #true if the object was initialized with valid positive integers
        
        return self._valid   #returns the value of the _valid attribute
    
    def caculate_gcd(self):
        #calculates the GCD of the two integers stored in the object using the Euclidean Algorithm
        if not self._valid:
            return None   #return None if the object is not valid
        
        A=self._a   #make it a variable
        B=self._b   #make it a variable
     
        while B!=0:  
            R=A%B   #use modolus to find the remainder
            A=B   #the new A is the old B
            B=R   #the new B is the remainder
            self._gcd=A
        return self._gcd   #when B=0, A holds the GCD

        
    
    def get_gcd(self):
        if not self._valid: 
           return None   #return None if the object is not valid
        if self._gcd is None:
           self.caculate_gcd()   ##calculate the GCD if it hasn't been already
           return self._gcd
       
def get_valid_integer_input(prompt):
    while True:
        user_input=input(prompt)   #get input from the user
        if not user_input or ' ' in user_input:
            print('Invalid input: Please enter a single number without spaces.')
            continue   #go back to the beginning of the loop
           
        is_digit_string=True
        for char in user_input:
            if not ('0' <= char <= '9'):
                is_digit_string=False
                break
            
            if is_digit_string:
                number= int(user_input)   #convert the input string to an integer
                if number>0:
                    return number   #return the positive integer
                else:
                    print('invalid input: Please enter a positive integer.')
            else:
                print('Invalid input: Please enter an integer.')
                
if __name__ =='__main__':
    print('Welcome to the Euclidean Algorithm GCD caculator!')
        
    while True:
        A= get_valid_integer_input('Enter your first positive integer number: ')
        if A is None:
            continue   #go back to the beginning of the loop if input is invalid
        B= get_valid_integer_input('Enter your second positive integer number: ')
        if B is None:
            continue   #go back to the beginning of the loop if input is invalid
            
        solve=EuclideanAlgorithm(A, B)   #create an instance of the EuclideanAlgorithm class
        if solve.is_valid():
            gcd_result=solve.get_gcd()   #get the GCD
            print(f'GCD({A},{B})={gcd_result}')   
            break   #exit the loop after successful calculation
        else:
            print("Error: Invalid input provided. Please try again.")
        
                
                
                   
         
        

  


#“I confirm that this assignment is my own work.  
#Where I/we have referred to academic sources, I have provided in-text 
#citations and included the sources in the final reference list. “


class EuclideanAlgorithm:
    
    def __init__(self, a, b):
        #two positive integers stored as private attributes _a and _b
        
        if not self._is_positive_integer(a) or not self._is_positive_integer(b):
            self._a= None
            self._b= None
            self._valid= False
        else:
            self._a=a
            self._b=b
            self._valid= True
        self._gcd= None
        
    def _is_positive_integer(self,n):
        return type(n) ==int and n>0
    
    def is_valid(self):
        return self._valid
    
    def caculate_gcd(self):
        if not self._valid:
            return None
        
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
           return None
        if self._gcd is None:
           self.caculate_gcd()
           return self._gcd
       
def get_valid_integer_input(prompt):
    while True:
        user_input=input(prompt)
        if not user_input or ' ' in user_input:
            print('Invalid input: Please enter a single number without spaces.')
            continue
           
        is_digit_string=True
        for char in user_input:
            if not ('0' <= char <= '9'):
                is_digit_string=False
                break
            
            if is_digit_string:
                number= int(user_input)
                if number>0:
                    return number
                else:
                    print('invalid input: Please enter a positive integer.')
            else:
                print('Invalid input: Please enter an integer.')
                
if __name__ =='__main__':
    print('Welcome to the Euclidean Algorithm GCD caculator!')
        
    while True:
        A= get_valid_integer_input('Enter your first positive integer number: ')
        if A is None:
            continue
        B= get_valid_integer_input('Enter your second positive integer number: ')
        if B is None:
            continue
            
        solve=EuclideanAlgorithm(A, B)
        if solve.is_valid():
            gcd_result=solve.get_gcd()
            print(f'GCD({A},{B})={gcd_result}')
            break
        else:
            print("Error: Invalid input provided. Please try again.")
        
                
                
                   
         
        

  
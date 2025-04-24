

#“I confirm that this assignment is my own work.  
#Where I/we have referred to academic sources, I have provided in-text 
#citations and included the sources in the final reference list. “


class EuclideanAlgorithm:
    
    def __init__(self, a, b):
        #two positive integers stored as private attributes _a and _b
        self._a=a
        self._b=b
    
    def get_gcd(self):
        
        A=self._a   #make it a variable
        B=self._b   #make it a variable
        
        while B!=0:  
            R=A%B   #use modolus to find the remainder
            A=B   #the new A is the old B
            B=R   #the new B is the remainder
        return A   #when B=0, A holds the GCD

input_a=270
input_b=192       


example=EuclideanAlgorithm(input_a, input_b)   
gcd_result=example.get_gcd()
print(f"GCD({input_a}, {input_b})={gcd_result}")     
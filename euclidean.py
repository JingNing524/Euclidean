

#“I confirm that this assignment is my own work.  
#Where I/we have referred to academic sources, I have provided in-text 
#citations and included the sources in the final reference list. “


initial_A=270
initial_B=192

A=initial_A 
B=initial_B 

while B != 0:
    R = A % B  #use modolus to find the remainder
    A = B  #the new A is the old B
    B = R  #the new B is the remainder

result = A  #the GCD is the final value of A when B becomes 0

output = f"GCD({initial_A}, {initial_B}) = {result}"
print(output)
    
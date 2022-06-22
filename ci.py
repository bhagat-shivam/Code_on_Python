def compound(p,r,t):
 
 

 a = p*(pow((1+r/100), t))
 ci = a-p
 print("the compund interest is :", ci)

compound(1000, 10, 5)
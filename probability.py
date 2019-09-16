x1 = list(range(1,7))
x2 = list(range(1,7))
x3 = list(range(1,7))

exp1 = 0
for a in x1:
    for b in x2:
        for c in x3:
            exp1 += (a*b*b*c)/(6**3)
print(exp1)

exp2 = 0
for a in x1:
    for b in x2:
        exp2 += a*b/36
        
exp3 = 0 
for a in x2:
    for b in x3:
        exp3 += a*b/36
        
print(exp2*exp3)

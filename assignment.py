#  given data  
# two die are thrown randaom then sample 
            # '''
S={(1,1),(1,2),(1,3),(1,4),(1,5),(1,6), 
            (2,1),(2,2),(2,3),(2,4),(2,5),(2,6), 
            (3,1),(3,2),(3,3),(3,4),(3,5),(3,6), 
            (4,1),(4,2),(4,3),(4,4),(4,5),(4,6),
            (5,1),(5,2),(5,3),(5,4),(5,5),(5,6),
            (6,1),(6,2),(6,3),(6,4),(6,5),(6,6)}
# A is obating sum greater than 9 
A={(4,6),(5,5),(5,6),(6,4),(6,5),(6,6)}

# B is getting 5 on balck die
B={(5,1),(5,2),(5,3),(5,4),(5,5),(5,6)}

# let C is intersection of A and B
C=A & B
prob_A=float(len(A)/len(S))
prob_B=float(len(B)/len(S))
prob_C=float(len(C)/len(S))

# let D is probabilty of A givan B
# D =P(A/B)
D=float(prob_C/prob_B)

# (ii)
# A be the event of obtaining a sum 8 and B be the
# event of ’getting a number less than 4 on red die
A ={(2,6),(3,5),(4,4),
(5,3),(6,2) }
B= {(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),
(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),
(1,3),(2,3),(3,3),(4,3),(5,3),(6,3)}
#  let C be the intersectio of A and B
C=A & B
prob_A=float(len(A)/len(S))
prob_B=float(len(B)/len(S))
prob_C=float(len(C)/len(S))
# let D is probabilty of A givan B
# D=P(A/B)
D=float(prob_C/prob_B)













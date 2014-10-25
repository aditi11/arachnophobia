import nltk	

l = nltk.LogicParser()

#parsing the predicates using LogicParser object
c1 = l.parse('ton(sachin)')
c2 = l.parse('all x. ((ton(x) | fwhaul(x) )-> momatch(x))')
c3 = l.parse('momatch(sachin)')

#using object of Prover9 to prove query (c3) , given list of assumptions (c1, c2)
gd =  nltk.Prover9().prove(c3, [c1, c2])

print gd

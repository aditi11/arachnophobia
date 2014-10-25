import nltk	

l = nltk.LogicParser()

####################
#	Assuming we are given the predicates: ton(sachin), ton(rahul), momatch(sachin).
#	Now we have the query: For all players, ton implies man of match award ( which is - (all x. (ton(x) -> momatch(x))))
#####################


####################
# 	The string var_pair has to be constructed from the predicates, to build the model 
###################
var_pair  = """ 
sachin => s
rahul => r
momatch => {s} 
ton => {r, s}
"""

#getting the values and domain of var_pair
val = nltk.parse_valuation(var_pair)
dom = val.domain
#print val


# creating a mapping from individual variables to entities in domain
g = nltk.Assignment(dom, [])


##################
#	 Building the model
###################
m = nltk.Model(dom , val)

print "************************"
print m.evaluate('all x. (ton(x) -> momatch(x))', g)
print "************************"

####################
#	Now finding the values x, for which ton(x) -> mom(x)
###################
c1 = l.parse('(ton(x) -> momatch(x))')
print m.satisfiers(c1, 'x', g)


#################
#	Please look at http://www.nltk.org/book/ch10.html for syntax and reference.
#################


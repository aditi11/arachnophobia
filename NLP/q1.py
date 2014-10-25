
import nltk
import sys
import os

def make_model_and_answer1(s,query,players):
	val=nltk.parse_valuation(s)
	dom=val.domain

	m=nltk.Model(dom,val)
	g=nltk.Assignment(dom,[])
	print ''
	print 'Q1. Player of match is given to player of winning team'
	print m.evaluate(query,g)
	x=nltk.LogicParser()
	c1=x.parse('(match(x)) & (exists y.((team(y)) & (winplayerteam(x,y) & winteam(x,y))))')
	varnames=m.satisfiers(c1,'x',g)
	for i in varnames:
		print i

def make_model_and_answer2(s,query):
	#print s
	val=nltk.parse_valuation(s)
	dom=val.domain
	m=nltk.Model(dom,val)
	g=nltk.Assignment(dom,[])
	print ''
	print 'Q2. At least one duck for losing team'
	print m.evaluate(query,g)
	x=nltk.LogicParser()
	c1=x.parse('(match(x)) & (exists y.((team(y)) & losingteam(x,y) & ducks(x,y)))')
	varnames=m.satisfiers(c1,'x',g)
	for i in varnames:
		print i

def make_model_and_answer3(s,query):
	#print s
	val=nltk.parse_valuation(s)
	dom=val.domain
	m=nltk.Model(dom,val)
	g=nltk.Assignment(dom,[])
	print ''
	print 'Q3. Strike rate more than 200 means more sixes than fours'
	print m.evaluate(query,g)
	x=nltk.LogicParser()
	c1=x.parse('(match(x)) & (exists y.((player(y)) & (strikerate(x,y) -> more6than4(x,y))))')
	varnames=m.satisfiers(c1,'x',g)
	for i in varnames:
		print i

def make_model_and_answer4(s,query):
	#print s
	val=nltk.parse_valuation(s)
	dom=val.domain
	m=nltk.Model(dom,val)
	g=nltk.Assignment(dom,[])
	print ''
	print 'Q4. For all matches, at least one player who hit at least one boundary but strike rate < 100'
	print m.evaluate(query,g)
	x=nltk.LogicParser()
	c1=x.parse('(player(y)) & (exists x.((match(x)) & atleast1four(x,y) & strikeratebelow(x,y)))')
	varnames=m.satisfiers(c1,'y',g)
	for i in varnames:
		print i

def make_model_and_answer5(s,query):
	#print s
	val=nltk.parse_valuation(s)
	dom=val.domain
	m=nltk.Model(dom,val)
	g=nltk.Assignment(dom,[])
	print ''
	print 'Q5. Player, who has scored at least 50 runs and taken at least 1 wicket in a match in the series'
	print m.evaluate(query,g)
	x=nltk.LogicParser()
	c1=x.parse('(player(y)) & (exists x.((match(x)) & morethan50(x,y) & atleast1w(x,y)))')
	varnames=m.satisfiers(c1,'y',g)
	for i in varnames:
		print i

def make_model_and_answer6(s,query):
	#print s
	val=nltk.parse_valuation(s)
	dom=val.domain
	m=nltk.Model(dom,val)
	g=nltk.Assignment(dom,[])
	print ''
	print 'Q6. Player, who has bowled more than 7 overs and not taken a single wicket in a match for all matches'
	print m.evaluate(query,g)
	x=nltk.LogicParser()
	c1=x.parse('(player(y)) & (exists x.((match(x)) & morethan7overs(x,y) & nowickets(x,y)))')
	varnames=m.satisfiers(c1,'y',g)
	for i in varnames:
		print i

def make_model_and_answer7(s,query):
	#print s
	#print query
	val=nltk.parse_valuation(s)
	dom=val.domain
	m=nltk.Model(dom,val)
	g=nltk.Assignment(dom,[])
	print ''
	print 'Q7. Player, who has given more than 8 runs per over and not taken a single wicket in a match for any match'
	print m.evaluate(query,g)
	x=nltk.LogicParser()
	c1=x.parse('(player(y)) & (exists x.((match(x)) & economy8(x,y) & nowickets(x,y)))')
	varnames=m.satisfiers(c1,'y',g)
	for i in varnames:
		print i

def make_model_and_answer8(s,query):
	#print s
	val=nltk.parse_valuation(s)
	dom=val.domain
	m=nltk.Model(dom,val)
	g=nltk.Assignment(dom,[])
	print ''
	print 'Q8. Player scored a century but team lost'
	print m.evaluate(query,g)
	x=nltk.LogicParser()
	c1=x.parse('(match(x)) & (exists y.((player(y)) & centurybutlost(x,y)))')
	varnames=m.satisfiers(c1,'x',g)
	for i in varnames:
		print i

def make_model_and_answer9(s,query):
	#print s
	val=nltk.parse_valuation(s)
	dom=val.domain
	m=nltk.Model(dom,val)
	g=nltk.Assignment(dom,[])
	#print m
	print ''
	print 'Q9. Right handed bowlers take more wickets than left handed ones'
	print m.evaluate(query,g)
	x=nltk.LogicParser()
	c1=x.parse('(match(x)) & rightmorethanleft(x) ')
	varnames=m.satisfiers(c1,'x',g)
	for i in varnames:
		print i

def make_model_and_answer10(s,query):
	#print s
	val=nltk.parse_valuation(s)
	dom=val.domain
	m=nltk.Model(dom,val)
	g=nltk.Assignment(dom,[])
	#print m
	print ''
	print 'Q10. There is a player, who is less than 26 years of age, has scored more than 250 runs in the series and not a single duck'
	print m.evaluate(query,g)
	x=nltk.LogicParser()
	c1=x.parse('(player(x)) & (-ducks(x)) & (morethan250(x))')
	varnames=m.satisfiers(c1,'x',g)
	for i in varnames:
		print i

def make_model_and_answer11(s,query):
	#print s
	val=nltk.parse_valuation(s)
	dom=val.domain
	m=nltk.Model(dom,val)
	g=nltk.Assignment(dom,[])
	#print m
	print ''
	print 'Q11. Players, who have played in all matches'
	#print m.evaluate(query,g)
	x=nltk.LogicParser()
	c1=x.parse('(player(x)) & (all y.((match(y) & pnm(y,x)) | (-match(y))))')
	varnames=m.satisfiers(c1,'x',g)
	for i in varnames:
		print i

def make_model_and_answer12(s,query):
	#print s
	val=nltk.parse_valuation(s)
	dom=val.domain
	m=nltk.Model(dom,val)
	g=nltk.Assignment(dom,[])
	#print m
	print ''
	print 'Q12. Ishant Sharma bowled more wides than Sir Jadeja'
	print m.evaluate(query,g)
	#x=nltk.LogicParser()
	#c1=x.parse('(player(x)) & (all y.((match(y) & pnm(y,x)) | (-match(y))))')
	#varnames=m.satisfiers(c1,'x',g)
	#for i in varnames:
	#		print i

def make_model_and_answer13(s,query):
	#print s
	val=nltk.parse_valuation(s)
	dom=val.domain
	m=nltk.Model(dom,val)
	g=nltk.Assignment(dom,[])
	#print m
	print ''
	print 'Q13. Southee took more catches than Ryder'
	print m.evaluate(query,g)
	#x=nltk.LogicParser()
	#c1=x.parse('(player(x)) & (all y.((match(y) & pnm(y,x)) | (-match(y))))')
	#varnames=m.satisfiers(c1,'x',g)
	#for i in varnames:
	#		print i

def make_model_and_answer14(s,query):
	#print s
	#print query
	val=nltk.parse_valuation(s)
	dom=val.domain
	m=nltk.Model(dom,val)
	g=nltk.Assignment(dom,[])
	#print m
	print ''
	print 'Q14. There is a player, who has been awarded player of match twice'
	print m.evaluate(query,g)
	x=nltk.LogicParser()
	c1=x.parse('(pom(x)) & (twice(x))')
	varnames=m.satisfiers(c1,'x',g)
	for i in varnames:
			print i

def make_model_and_answer15(s,query):
	#print s
	#print query
	val=nltk.parse_valuation(s)
	dom=val.domain
	m=nltk.Model(dom,val)
	g=nltk.Assignment(dom,[])
	#print m
	print ''
	print 'Q15. Did Sir Jadeja bowl better in innings 1 or 2'
	#print m.evaluate(query,g)
	x=nltk.LogicParser()
	c1=x.parse('(higher(x))')
	varnames=m.satisfiers(c1,'x',g)
	for i in varnames:
			print i

def make_model_and_answer16(s,query):
	#print s
	#print query
	val=nltk.parse_valuation(s)
	dom=val.domain
	m=nltk.Model(dom,val)
	g=nltk.Assignment(dom,[])
	#print m
	print ''
	print 'Q16. Is Dhoni a hard-hitting batsman?'
	print m.evaluate(query,g)
	x=nltk.LogicParser()
	c1=x.parse('(higher(x)) & (ans(x))')
	varnames=m.satisfiers(c1,'x',g)
	for i in varnames:
			print i

def make_model_and_answer17(s,query):
	#print s
	#print query
	val=nltk.parse_valuation(s)
	dom=val.domain
	m=nltk.Model(dom,val)
	g=nltk.Assignment(dom,[])
	#print m
	print ''
	print 'Q17. Who is the better bowler, I Sharma or RA Jadeja?'
	#print m.evaluate(query,g)
	x=nltk.LogicParser()
	c1=x.parse('(player(x)) & (better(x))')
	varnames=m.satisfiers(c1,'x',g)
	for i in varnames:
			print i

def make_model_and_answer19(s,query):
	#print s
	#print query
	val=nltk.parse_valuation(s)
	dom=val.domain
	m=nltk.Model(dom,val)
	g=nltk.Assignment(dom,[])
	#print m
	print ''
	print 'Q19. Do all teams that win the toss win the match?'
	print m.evaluate(query,g)
	x=nltk.LogicParser()
	c1=x.parse('(match(y)) & (all x.((team(x)) & ((toss(y,x)) -> (win(y,x)))))')
	varnames=m.satisfiers(c1,'y',g)
	for i in varnames:
			print i

def make_model_and_answer18(s,query):
	#print s
	#print query
	val=nltk.parse_valuation(s)
	dom=val.domain
	m=nltk.Model(dom,val)
	g=nltk.Assignment(dom,[])
	#print m
	print ''
	print 'Q18. Who performs better, opening batsmen or middle order batsmen?'
	#print m.evaluate(query,g)
	x=nltk.LogicParser()
	c1=x.parse('(set(x)) & (ans(x))')
	varnames=m.satisfiers(c1,'x',g)
	for i in varnames:
			print i

def make_model_and_answer20(s,query):
	#print s
	#print query
	val=nltk.parse_valuation(s)
	dom=val.domain
	m=nltk.Model(dom,val)
	g=nltk.Assignment(dom,[])
	#print m
	print ''
	print 'Q20. Which team will win the next match?'
	#print m.evaluate(query,g)
	x=nltk.LogicParser()
	c1=x.parse('(team(x)) & (ans(x))')
	varnames=m.satisfiers(c1,'x',g)
	for i in varnames:
			print i

def generate_and_solve_query1(l,players):
	a=''
	b=''
	c=''
	c+='New Zealand => r1\n'
	c+='India => r2\n'
	#c+='Match tied => {r1,r2}\n'
	a+='winteam => {'
	b+='winplayerteam => {'
	count=1
	mapping={}
	mapping['India']='r2'
	mapping['New Zealand']='r1'
	for i in range(0,len(l)-1,2):
		if l[i]=='Match tied':
			a+='(m'+str(count)+','+mapping[l[i+1]]+'),'
		else:
			a+='(m'+str(count)+','+mapping[l[i]]+'),'
		b+='(m'+str(count)+','+mapping[l[i+1]]+'),'
		count+=1
	a=a[:-1]
	b=b[:-1]
	a+='}\n'
	b+='}\n'
	d='match => {m1,m2,m3,m4,m5}\nteam => {r1,r2}\n'
	#print c
	#print a
	#print b
	query='all x.( ((match(x) & (exists y.(team(y) & (winplayerteam(x,y) -> winteam(x,y)))))  )  | (-match(x) ) ) '
	make_model_and_answer1(c+d+b+a,query,players)

def findducks(a):
	a=a[1:]
	count=0
	for i in range(len(a)-1):
		#print a[i]
		b=a[i].split(',')
		#print b[2]
		if b[2]=='0':
			if b[1].strip()=='not out':
				continue
			else:
				count+=1
	return count

def generate_and_solve_query2(l,l2):
	mapping={}
	mapping['India']='r2'
	mapping['New Zealand']='r1'
	a='India => r2\nNew Zealand => r1\nmatch => {m1,m2,m3,m4,m5}\nteam => {r1,r2}\n'
	b='losingteam => {'
	c='ducks => {'
	for i in range(len(l2)):
		if l[i]=='Match tied':
			continue
		if l[i]=='New Zealand':
			b+='(m'+str(i+1)+','+mapping['India']+'),'
		else:
			b+='(m'+str(i+1)+','+mapping['New Zealand']+'),'
		if l2[i]==0:
			continue
		if l[i]=='New Zealand':
			c+='(m'+str(i+1)+','+mapping['India']+'),'
		else:
			c+='(m'+str(i+1)+','+mapping['New Zealand']+'),'
	b=b[:-1]
	c=c[:-1]
	b+='}\n'
	c+='}\n'
	query='all x.((match(x) & (exists y.(team(y) & losingteam(x,y) & ducks(x,y)))) | (-match(x)))'
	make_model_and_answer2(a+b+c,query)

def strikerate(f1,f2,num):
	l=[]
	f=open(f1,'r')
	d=f.read()
	d=d.split('\n')
	d=d[1:]
	for i in range(len(d)-1):
		#print d[i]
		x=d[i].split(',')
		#print x[7]
		if float(x[7].strip())>num:
			l.append(x[0].strip())
	ff=open(f2,'r')
	d=ff.read()
	d=d.split('\n')
	d=d[1:]
	for i in range(len(d)-1):
		x=d[i].split(',')
		#print x[7]
		if float(x[7].strip())>num:
			l.append(x[0].strip())
	return l

def strikeratebelow(f1,f2,num,win):
	l=[]
	f=open(f1,'r')
	d=f.read()
	d=d.split('\n')
	#print d[0]
	if d[0]==win or d[0]=='Match tied':
		d=d[1:]
		for i in range(len(d)-1):
			#print d[i]
			x=d[i].split(',')
			#print x[7]
			if float(x[7].strip())<num:
				l.append(x[0].strip())
	if d[0]=='Match tied':
		ff=open(f2,'r')
		d=ff.read()
		d=d.split('\n')
		d=d[1:]
		for i in range(len(d)-1):
			x=d[i].split(',')
			#print x[7]
			if float(x[7].strip())<num:
				l.append(x[0].strip())
	elif d[0] is not win:
		ff=open(f2,'r')
		d=ff.read()
		d=d.split('\n')
		d=d[1:]
		for i in range(len(d)-1):
			x=d[i].split(',')
			#print x[7]
			if float(x[7].strip())<num:
				l.append(x[0].strip())

	return l

def lefthandedbowlersandwickets(f1,f2):
	total=0
	count=0	
	data=open(f1,'r').read()
	data=data.split('\n')
	if data[0]=='New Zealand':
		f=open('player_profile/indian_players_profile.txt','r')
	else:
		f=open('player_profile/nz_players_profile.txt','r')
	d=f.read()
	d=d.split('\n')
	data=data[1:]
	#print data
	#print d
	for i in range(len(data)):
		#print data[i]
	 	for j in range(len(d)-1):
	 		x=d[j].split('\t')
			y=data[i].split(',')
	 		if x[0].strip()==y[0].strip():
				total+=int(y[4])
				#z=x[7].split('-')
				#print z
				#print x[7]
				#print y
				if str(x[7]).find("left")!=-1 or str(x[7]).find("Left")!=-1:
					#print 'adding left'
					#print int(y[4])
					count+=int(y[4])
	data=open(f2,'r').read()
	data=data.split('\n')
	if data[0]=='New Zealand':
		f=open('player_profile/indian_players_profile.txt','r')
	else:
		f=open('player_profile/nz_players_profile.txt','r')
	d=f.read()
	d=d.split('\n')
	data=data[1:]
	for i in range(len(data)):
		#print data[i]
	 	for j in range(len(d)-1):
	 		x=d[j].split('\t')
			y=data[i].split(',')
	 		if x[0].strip()==y[0].strip():
				total+=int(y[4])
				#z=x[7].split('-')
				#print z
				#print x[7]
				#print y
				if str(x[7]).find("left")!=-1 or str(x[7]).find("Left")!=-1:
					#print 'adding left'
					#print int(y[4])
					count+=int(y[4])

	return count,total-count


def moresixesthanfours(f1,f2):
	l=[]
	f=open(f1,'r')
	d=f.read()
	d=d.split('\n')
	d=d[1:]
	for i in range(len(d)-1):
		x=d[i].split(',')
		if int(x[6])>int(x[5]):
			l.append(x[0].strip())
	f=open(f2,'r')
	d=f.read()
	d=d.split('\n')
	d=d[1:]
	for i in range(len(d)-1):
		x=d[i].split(',')
		if int(x[6])>int(x[5]):
			l.append(x[0].strip())
	return l

def atleast1four(f1,f2,win):
	l=[]
	f=open(f1,'r')
	d=f.read()
	d=d.split('\n')
	if d[0]==win or d[0]=='Match tied':
		d=d[1:]
		for i in range(len(d)-1):
			x=d[i].split(',')
			if int(x[5])>=1:
				l.append(x[0].strip())
	if d[0]=='Match tied':
		f=open(f2,'r')
		d=f.read()
		d=d.split('\n')
		d=d[1:]
		for i in range(len(d)-1):
			x=d[i].split(',')
			if int(x[5])>=1:
				l.append(x[0].strip())
	elif d[0] is not win:
		f=open(f2,'r')
		d=f.read()
		d=d.split('\n')
		d=d[1:]
		for i in range(len(d)-1):
			x=d[i].split(',')
			if int(x[5])>=1:
				l.append(x[0].strip())
	return l


def morethan50(f1,f2):
	l=[]
	runs=50
	f=open(f1,'r')
	d=f.read()
	d=d.split('\n')
	d=d[1:]
	for i in range(len(d)-1):
		x=d[i].split(',')
		if int(x[2])>runs:
			l.append(x[0].strip())
	f=open(f2,'r')
	d=f.read()
	d=d.split('\n')
	d=d[1:]
	for i in range(len(d)-1):
		x=d[i].split(',')
		if int(x[2])>runs:
			l.append(x[0].strip())
	return l

def morethan100(f1,f2,win):
	l=[]
	runs=100
	f=open(f1,'r')
	d=f.read()
	d=d.split('\n')
	if d[0] is not win:
		d=d[1:]
		for i in range(len(d)-1):
			x=d[i].split(',')
			if int(x[2])>runs:
				l.append(x[0].strip())
	elif d[0]=='Match tied' or d[0]==win:
		f=open(f2,'r')
		d=f.read()
		d=d.split('\n')
		d=d[1:]
		for i in range(len(d)-1):
			x=d[i].split(',')
			if int(x[2])>runs:
				l.append(x[0].strip())
	return l

def atleast1w(f1,f2):
	l=[]
	f=open(f1,'r')
	d=f.read()
	d=d.split('\n')
	d=d[1:]
	for i in range(len(d)-1):
		x=d[i].split(',')
		if int(x[4])>=1:
			#print 'appending'
			l.append(x[0].strip())
	f=open(f2,'r')
	d=f.read()
	d=d.split('\n')
	d=d[1:]
	for i in range(len(d)-1):
		x=d[i].split(',')
		if int(x[4])>=1:
			#print 'appending'
			l.append(x[0].strip())
	return l

def nowickets(f1,f2):
	l=[]
	f=open(f1,'r')
	d=f.read()
	d=d.split('\n')
	d=d[1:]
	for i in range(len(d)-1):
		x=d[i].split(',')
		if int(x[4])==0:
			#print 'appending'
			l.append(x[0].strip())
	f=open(f2,'r')
	d=f.read()
	d=d.split('\n')
	d=d[1:]
	for i in range(len(d)-1):
		x=d[i].split(',')
		if int(x[4])==0:
			#print 'appending'
			l.append(x[0].strip())
	return l

def economy8(f1,f2):
	l=[]
	f=open(f1,'r')
	d=f.read()
	d=d.split('\n')
	d=d[1:]
	for i in range(len(d)-1):
		x=d[i].split(',')
		if float(x[5])>8.0:
			#print 'appending'
			l.append(x[0].strip())
	f=open(f2,'r')
	d=f.read()
	d=d.split('\n')
	d=d[1:]
	for i in range(len(d)-1):
		x=d[i].split(',')
		if float(x[5])>8.0:
			#print 'appending'
			l.append(x[0].strip())
	return l

def morethan7overs(f1,f2):
	l=[]
	f=open(f1,'r')
	d=f.read()
	d=d.split('\n')
	d=d[1:]
	for i in range(len(d)-1):
		x=d[i].split(',')
		if float(x[1])>7.0:
			#print 'appending'
			l.append(x[0].strip())
	f=open(f2,'r')
	d=f.read()
	d=d.split('\n')
	d=d[1:]
	for i in range(len(d)-1):
		x=d[i].split(',')
		if float(x[1])>7.0:
			#print 'appending'
			l.append(x[0].strip())
	return l

def generate_and_solve_query6(l,l2):
	a='New Zealand => r1\nIndia => r2\nmatch => {m1,m2,m3,m4,m5}\n'
	b='morethan7overs => {'
	c='nowickets => {'
	d='player => {'
	players=[]
	#print l
	#print l2
	for i in l:
		for j in i:
			if j not in players:
				players.append(j)
	for i in l2:
		for j in i:
			if j not in players:
				players.append(j)
	for i in players:
		d+=i+','
	d=d[:-1]
	d+='}\n'
	count=1
	for i in l:
		for j in i:
			b+='(m'+str(count)+','+j+'),'
		count+=1
	count=1
	for i in l2:
		for j in i:
			c+='(m'+str(count)+','+j+'),'
	b=b[:-1]
	c=c[:-1]
	b+='}\n'
	c+='}\n'
	query='exists x.((match(x) & exists y.(player(y) & morethan7overs(x,y) & nowickets(x,y))) | (-match(x)))'
	make_model_and_answer6(a+d+b+c,query)

def generate_and_solve_query4(l,l2):
	a='New Zealand => r1\nIndia => r2\nmatch => {m1,m2,m3,m4,m5}\n'
	b='atleast1four => {'
	c='strikeratebelow => {'
	d='player => {'
	players=[]
	#print l
	#print l2
	for i in l:
		for j in i:
			if j not in players:
				players.append(j)
	for i in l2:
		for j in i:
			if j not in players:
				players.append(j)
	for i in players:
		d+=i+','
	d=d[:-1]
	d+='}\n'
	count=1
	for i in l:
		for j in i:
			b+='(m'+str(count)+','+j+'),'
		count+=1
	count=1
	for i in l2:
		for j in i:
			c+='(m'+str(count)+','+j+'),'
		count+=1
	b=b[:-1]
	c=c[:-1]
	b+='}\n'
	c+='}\n'
	#print b
	#print c
	query='all x.((match(x) & (exists y.(player(y) & atleast1four(x,y) & strikeratebelow(x,y)))) | (-match(x)))'
	make_model_and_answer4(a+d+b+c,query)

def generate_and_solve_query8(l):
	a='New Zealand => r1\nIndia => r2\nmatch => {m1,m2,m3,m4,m5}\n'
	b='centurybutlost => {'
	d='player => {'
	players=[]
	#print l
	#print l2
	for i in l:
		for j in i:
			if j not in players:
				players.append(j)
	for i in players:
		d+=i+','
	d=d[:-1]
	d+='}\n'
	count=1
	for i in l:
		for j in i:
			b+='(m'+str(count)+','+j+'),'
		count+=1
	b=b[:-1]
	b+='}\n'
	#print b
	#print c
	query='exists x.((match(x) & (exists y.(player(y) & centurybutlost(x,y)))) | (-match(x)))'
	make_model_and_answer8(a+d+b,query)

def generate_and_solve_query7(l,l2):
	a='New Zealand => r1\nIndia => r2\nmatch => {m1,m2,m3,m4,m5}\n'
	b='nowickets => {'
	c='economy8 => {'
	d='player => {'
	players=[]
	#print l
	#print l2
	for i in l:
		for j in i:
			if j not in players:
				players.append(j)
	for i in l2:
		for j in i:
			if j not in players:
				players.append(j)
	for i in players:
		d+=i+','
	d=d[:-1]
	d+='}\n'
	count=1
	for i in l:
		for j in i:
			b+='(m'+str(count)+','+j+'),'
		count+=1
	count=1
	for i in l2:
		for j in i:
			c+='(m'+str(count)+','+j+'),'
		count+=1
	b=b[:-1]
	c=c[:-1]
	b+='}\n'
	c+='}\n'
	#print b
	#print c
	query='exists x.((match(x) & (exists y.(player(y) & nowickets(x,y) & economy8(x,y)))))'
	make_model_and_answer7(a+d+b+c,query)



def generate_and_solve_query5(l,l2):
	a='New Zealand => r1\nIndia => r2\nmatch => {m1,m2,m3,m4,m5}\n'
	b='morethan50 => {'
	c='atleast1w => {'
	d='player => {'
	players=[]
	#print l
	#print l2
	for i in l:
		for j in i:
			if j not in players:
				players.append(j)
	for i in l2:
		for j in i:
			if j not in players:
				players.append(j)
	for i in players:
		d+=i+','
	d=d[:-1]
	d+='}\n'
	count=1
	for i in l:
		for j in i:
			b+='(m'+str(count)+','+j+'),'
		count+=1
	count=1
	for i in l2:
		for j in i:
			c+='(m'+str(count)+','+j+'),'
	b=b[:-1]
	c=c[:-1]
	b+='}\n'
	c+='}\n'
	query='exists x.(match(x) & exists y.(player(y) & morethan50(x,y) & atleast1w(x,y)))'
	make_model_and_answer5(a+d+b+c,query)

def generate_and_solve_query3(l,l2):
	count=1
	a='New Zealand => r1\nIndia =>r2\nmatch => {m1,m2,m3,m4,m5}\n'
	b='strikerate => {'
	c='more6than4 => {'
	d='player => {'
	players=[]
	for i in l:
		for j in i:
			if j not in players:
				players.append(j)
	for i in l2:
		for j in i:
			if j not in players:
				players.append(j)
	for i in players:
		d+=i+','
	d=d[:-1]
	d+='}\n'
	for i in l:
		for j in i:
			b+='(m'+str(count)+','+j+'),'
		count+=1
	count=1
	for i in l2:
		for j in i:
			c+='(m'+str(count)+','+j+'),'
		count+=1
	b=b[:-1]
	c=c[:-1]
	b+='}\n'
	c+='}\n'
	query='all x.((match(x) & exists y.(player(y) & (strikerate(x,y) -> more6than4(x,y)))) | (-match(x)))'
	make_model_and_answer3(a+d+b+c,query)

def generate_and_solve_query9(l):
	a='match => {m1,m2,m3,m4,m5}\nIndia => r2\nNew Zealand => r1\n'
	b='rightmorethanleft => {'
	for i in range(len(l)):
		b+='m'+str(l[i])+','
	if b[len(b)-1]==',':
		b=b[:-1]
	b+='}\n'
	query='all x.((match(x) & rightmorethanleft(x)) | (-match(x)))'
	make_model_and_answer9(a+b,query)

def generate_and_solve_query10(l,l2,players):
	a='player => {'
	b='ducks => {'
	c='morethan250 => {'
	for i in players:
		a+=i+','
	a=a[:-1]
	a+='}\n'
	for i in l:
		b+=i+','
	b=b[:-1]
	b+='}\n'
	for i in l2:
		c+=i+','
	c=c[:-1]
	c+='}\n'
	query='exists x.(player(x) & morethan250(x) & (-ducks(x)))'
	make_model_and_answer10(a+b+c,query)

def ducks(f1,f2,playername,teamname):
	f=open(f1,'r')
	d=f.read()
	d=d.split('\n')
	if d[0] is not teamname:
		f=open(f2,'r')
		d=f.read()
		d=d.split('\n')
	d=d[1:]
	for i in range(len(d)):
		x=d[i].split(',')
		if x[0].strip()==playername:
			if int(x[2])==0 and x[1].strip() is not 'not out':
				return 1
			else:
				return 0

def findruns(f1,f2,playername,teamname):
	f=open(f1,'r')
	d=f.read()
	d=d.split('\n')
	if d[0] is not teamname:
		f=open(f2,'r')
		d=f.read()
		d=d.split('\n')
	d=d[1:]
	for i in range(len(d)):
		x=d[i].split(',')
		if x[0].strip()==playername:
			return int(x[2])
	return 0

def getplayers(f1,f2,f3,f4):
	players=[]
	f=open(f1,'r')
	d=f.read()
	d=d.split('\n')
	d=d[1:]
	for i in range(len(d)):
		x=d[i].split(',')
		if x[0].strip() not in players:
			players.append(x[0].strip())
	f=open(f2,'r')
	d=f.read()
	d=d.split('\n')
	d=d[1:]
	for i in range(len(d)):
		x=d[i].split(',')
		if x[0].strip() not in players:
			players.append(x[0].strip())
	f=open(f3,'r')
	d=f.read()
	d=d.split('\n')
	d=d[1:]
	for i in range(len(d)):
		x=d[i].split(',')
		if x[0].strip() not in players:
			players.append(x[0].strip())
	f=open(f4,'r')
	d=f.read()
	d=d.split('\n')
	d=d[1:]
	for i in range(len(d)):
		x=d[i].split(',')
		if x[0].strip() not in players:
			players.append(x[0].strip())
	return players

def generate_and_solve_query11(l,players):
	a='match => {m1,m2,m3,m4,m5}\n'
	b='player => {'
	c='pnm => {'
	for i in players:
		b+=i+','
	b=b[:-1]
	b+='}\n'
	count=1
	for i in l:
		for j in i:
			if j is not '':
				c+='(m'+str(count)+','+j+'),'
		count+=1
	c=c[:-1]
	c+='}\n'
	query='exists x.(player(x) & (all y.((match(y) & pnm(y,x)) | (-match(y)))))'
	#print a+b+c
	make_model_and_answer11(a+b+c,query)

def findwides(f1,f2,playername):
	f=open(f1,'r')
	d=f.read()
	d=d.split('\n')
	if d[0] is not 'India':
		f=open(f1,'r')
		d=f.read()
		d=d.split('\n')
	d=d[1:]
	for i in range(len(d)):
		if d[i]=='':
			continue
		x=d[i].split(',')
		if x[0]==playername:
			if len(x)==8:
				y=x[6]
				if 'w' in y:
					y=y.split('w')
					if ' ' in y[0]:
						z=y[0].split(' ')
					else:
						z=y[0].split('(')
					return int(z[1])
	return 0

def findcatches(f1,f2,playername):
	catches=0
	f=open(f1,'r')
	d=f.read()
	d=d.split('\n')
	if d[0] is not 'India':
		f=open(f2,'r')
		d=f.read()
		d=d.split('\n')
	d=d[1:]
	for i in range(len(d)):
		if d[i]=='':
			continue
		x=d[i].split(',')
		y=x[1]
		if 'c' not in y:
			continue
		z=y.split('c')
		w=z[1].split('b')
		if w[0].strip()==playername:
			catches+=1
	return catches

def generate_and_solve_query12(iwides,jwides):
	a='I Sharma => i\nRA Jadeja => j\n'
	b='morewides => {'
	c='ans => {i}\n'
	if iwides>jwides:
		b+='i}\n'
	else:
		b+='j}\n'
	query='all x.((ans(x) & morewides(x)) | (-ans(x)))'
	make_model_and_answer12(a+b+c,query)

def generate_and_solve_query13(scatches,rcatches):
	a='Southee => s\nRyder => r\n'
	b='morecatches => {'
	c='ans => {s}\n'
	if scatches>rcatches:
		b+='s}\n'
	else:
		b+='r}\n'
	query='all x.((ans(x) & morecatches(x)) | (-ans(x)))'
	make_model_and_answer13(a+b+c,query)

def findbetterjadeja(f1):
	f=open(f1,'r')
	d=f.read()
	val=0
	d=d.split('\n')
	d=d[1:]
	for i in d:
		if i=='':
			continue
		x=i.split(',')
		if x[0]=='RA Jadeja':
			val+=int(x[2])+4*int(x[4])-3*float(x[5])
			if len(x)==8:
				y=x[6]
				if ',' in y:
					y=y.split(',')
					z=y[0].split('nb')
					z=z[0].split('(')
					val-=int(z[1].strip())
					z=y[1].split('w')
					z=z[0].strip()
					val-=int(z)
				elif 'nb' in y:
					y=y.split('nb')
					z=y[0].split('(')
					val-=int(z[1].strip())
				elif 'w' in y:
					y=y.split('w')
					z=y[0].split('(')
					val-=int(z[1].strip())
			break
	return val

def findbetter(f1,playername):
	f=open(f1,'r')
	d=f.read()
	val=0
	d=d.split('\n')
	d=d[1:]
	for i in d:
		if i=='':
			continue
		x=i.split(',')
		if x[0]==playername:
			val+=int(x[2])+4*int(x[4])-3*float(x[5])
			if len(x)==8:
				y=x[6]
				if ',' in y:
					y=y.split(',')
					z=y[0].split('nb')
					z=z[0].split('(')
					val-=int(z[1].strip())
					z=y[1].split('w')
					z=z[0].strip()
					val-=int(z)
				elif 'nb' in y:
					y=y.split('nb')
					z=y[0].split('(')
					val-=int(z[1].strip())
				elif 'w' in y:
					y=y.split('w')
					z=y[0].split('(')
					val-=int(z[1].strip())
			break
	return val


def finddhoni(f1):
	f=open(f1,'r')
	d=f.read()
	d=d.split('\n')
	d=d[1:]
	val=0
	for i in d:
		if i=='':
			continue
		x=i.split(',')
		if x[0]=='MS Dhoni':
			val+=3*int(x[5])+5*int(x[6])+3*float(x[7])
			break
	return val


def generate_and_solve_query14(l,l2):
	a='pom => {'
	b='twice => {'
	for i in l:
		a+=i+','
	a=a[:-1]
	a+='}\n'
	for i in l2:
		b+=i+','
	if b[len(b)-1]==',':
		b=b[:-1]
	b+='}\n'
	query='exists x.(pom(x) & twice(x))'
	make_model_and_answer14(a+b,query)

def generate_and_solve_query15(inn1,inn2):
	b='higher => {'
	if inn1>inn2:
		b+='innings1'
	else:
		b+='innings2'
	b+='}\n'
	query='exists x.(higher(x))'
	#print query
	make_model_and_answer15(b,query)

def generate_and_solve_query16(index):
	b='higher => {'
	c='ans => {Dhoni has index greater than 200}\n'
	if index>200:
		b+='Dhoni has index greater than 200'
	else:
		b+='Dhoni has index less than 200'
	b+='}\n'
	query='exists x.((higher(x)) & ans(x))'
	#print query
	#print b+c
	make_model_and_answer16(b+c,query)

def generate_and_solve_query17(v1,v2):
	a='player => {I Sharma,RA Jadeja}\n'
	b='better => {'
	if v1>v2:
		b+='I Sharma}\n'
	else:
		b+='RA Jadeja}\n'
	query='exists x.(player(x) & better(x))'
	make_model_and_answer17(a+b,query)

def generate_and_solve_query18(v1,v2):
	a='set => {opening,middle order}\n'
	b='ans => {'
	if v1>v2:
		b+='opening}\n'
	else:
		b+='middle order}\n'
	query='exists x.(set(x) & ans(x))'
	make_model_and_answer18(a+b,query)

def generate_and_solve_query19(l,l2):
	a='India => r2\nNew Zealand => r1\nteam => {r1,r2}\nmatch => {m1,m2,m3,m4,m5}\n'
	mapping={}
	mapping['India']='r2'
	mapping['New Zealand']='r1'
	b='toss => {'
	c='win => {'
	count=1
	for i in range(len(l)):
		b+='(m'+str(count)+','+mapping[l[i]]+'),'
	b=b[:-1]
	b+='}\n'
	count=1
	for i in range(len(l2)):
		if l2[i]=='Match tied':
			c+='(m'+str(count)+','+mapping[l[i]]+'),'
		else:
			c+='(m'+str(count)+','+mapping[l2[i]]+'),'
	c=c[:-1]
	c+='}\n'
	#print a+b+c
	query='all y.((match(y) & (all x.((team(x) & (toss(y,x) -> win(y,x))) ))) | (-match(y)))'
	make_model_and_answer19(a+b+c,query)

def findtop(f1):
	f=open(f1,'r')
	d=f.read()
	d=d.split('\n')
	d=d[1:]
	val=0
	x=d[0].split(',')
	val+=4*int(x[2])+2*int(x[4])+int(x[5])+2*float(x[6])
	x=d[1].split(',')
	val+=4*int(x[2])+2*int(x[4])+int(x[5])+2*float(x[6])
	return val/2

def findmiddle(f1):
	f=open(f1,'r')
	d=f.read()
	d=d.split('\n')
	d=d[1:]
	val=0
	count=0
	if len(d)>5:
		x=d[4].split(',')
		val+=4*int(x[2])+2*int(x[4])+int(x[5])+2*float(x[6])
		count+=1
	if len(d)>6:
		x=d[5].split(',')
		val+=4*int(x[2])+2*int(x[4])+int(x[5])+2*float(x[6])
		count+=1
	if len(d)>7:
		x=d[6].split(',')
		val+=4*int(x[2])+2*int(x[4])+int(x[5])+2*float(x[6])
		count+=1
	return val/count

def findinnscore(f1,f2):
	f=open(f1,'r')
	d=f.read()
	d=d.split('\n')
	a=d[0]
	d=d[1:]
	val=0
	for i in d:
		if i=='':
			continue
		x=i.split(',')
		val+=2*int(x[2])
	f=open(f2,'r')
	d=f.read()
	d=d.split('\n')
	d=d[1:]
	for i in d:
		if i=='':
			continue
		x=i.split(',')
		val+=int(x[4])
	return a,val

def generate_and_solve_query20(l,l2,l3,dictionary):
	count={}
	count['New Zealand']=0
	count['India']=0
	a='team => {India,New Zealand}\n'
	#b='predicted => {'
	mapping={}
	mapping['New Zealand']='r1'
	mapping['India']='r2'
	for i in range(1,len(l),2):
		if l[i]>l2[i]:
			count[l[i-1]]+=1
	#		b+=mapping[l[i-1]]+','
		else:
			count[l2[i-1]]+=1
	#		b+=mapping[l2[i-1]]+','
	for i in dictionary:
	 	count[i]+=dictionary[i]
	if count['New Zealand']>count['India']:
	 	c='ans => {New Zealand}\n'
	else:
		c='ans => {India}\n'
	query='exists x.(team(x) & ans(x))'
	make_model_and_answer20(a+c,query)

def main():
	f=open('winners.txt','r')
	data=f.read()
	d=data.split('\n')
	l=[]
	players=[]
	for i in range(0,len(d)-2,3):
		l.append(d[i])
		l.append(d[i+2])
		players.append(d[i+1])
	generate_and_solve_query1(l,players)
	l=[]
	f11='odi1_inn1_bat.txt'
	f12='odi1_inn2_bat.txt'
	f21='odi2_inn1_bat.txt'
	f22='odi2_inn2_bat.txt'
	f31='odi3_inn1_bat.txt'
	f32='odi3_inn2_bat.txt'
	f41='odi4_inn1_bat.txt'
	f42='odi4_inn2_bat.txt'
	f51='odi5_inn1_bat.txt'
	f52='odi5_inn2_bat.txt'
	f13='odi1_inn1_bowl.txt'
	f14='odi1_inn2_bowl.txt'
	f23='odi2_inn1_bowl.txt'
	f24='odi2_inn2_bowl.txt'
	f33='odi3_inn1_bowl.txt'
	f34='odi3_inn2_bowl.txt'
	f43='odi4_inn1_bowl.txt'
	f44='odi4_inn2_bowl.txt'
	f53='odi5_inn1_bowl.txt'
	f54='odi5_inn2_bowl.txt'
	for i in range(0,len(d)-2,3):
		l.append(d[i])
	l2=[]
	os.chdir('dataset')
	os.chdir('match1')
	a=open(f11,'r').read()
	a=a.split('\n')
	if a[0]==l[0]:
	 	a=open(f12,'r').read()
	 	a=a.split('\n')
	l2.append(findducks(a))
	os.chdir('../match2')
	a=open(f21,'r').read()
	a=a.split('\n')
	if a[0]==l[1]:
	 	a=open(f22,'r').read()
	 	a=a.split('\n')
	l2.append(findducks(a))
	os.chdir('../match3')
	a=open(f31,'r').read()
	a=a.split('\n')
	if a[0]==l[2]:
	 	a=open(f32,'r').read()
	 	a=a.split('\n')
	l2.append(findducks(a))
	os.chdir('../match4')
	a=open(f41,'r').read()
	a=a.split('\n')
	if a[0]==l[3]:
	 	a=open(f42,'r').read()
	 	a=a.split('\n')
	l2.append(findducks(a))
	os.chdir('../match5')
	a=open(f51,'r').read()
	a=a.split('\n')
	if a[0]==l[4]:
	 	a=open(f52,'r').read()
	 	a=a.split('\n')
	l2.append(findducks(a))
	generate_and_solve_query2(l,l2)
	l=[]
	os.chdir('..')
	l.append(strikerate('match1/'+f11,'match1/'+f12,200.0))
	l.append(strikerate('match2/'+f21,'match2/'+f22,200.0))
	l.append(strikerate('match3/'+f31,'match3/'+f32,200.0))
	l.append(strikerate('match4/'+f41,'match4/'+f42,200.0))
	l.append(strikerate('match5/'+f51,'match5/'+f52,200.0))
	l2=[]
	l2.append(moresixesthanfours('match1/'+f11,'match1/'+f12))
	l2.append(moresixesthanfours('match2/'+f21,'match2/'+f22))
	l2.append(moresixesthanfours('match3/'+f31,'match3/'+f32))
	l2.append(moresixesthanfours('match4/'+f41,'match4/'+f42))
	l2.append(moresixesthanfours('match5/'+f51,'match5/'+f52))
	generate_and_solve_query3(l,l2)
	l=[]
	l2=[]
	win=[]
	for i in range(0,len(d)-2,3):
		win.append(d[i])
	l.append(atleast1four('match1/'+f11,'match1/'+f12,win[0]))
	l.append(atleast1four('match2/'+f21,'match2/'+f22,win[1]))
	l.append(atleast1four('match3/'+f31,'match3/'+f32,win[2]))
	l.append(atleast1four('match4/'+f41,'match4/'+f42,win[3]))
	l.append(atleast1four('match5/'+f51,'match5/'+f52,win[4]))
	l2.append(strikeratebelow('match1/'+f11,'match1/'+f12,100.0,win[0]))
	l2.append(strikeratebelow('match2/'+f21,'match2/'+f22,100.0,win[1]))
	l2.append(strikeratebelow('match3/'+f31,'match3/'+f32,100.0,win[2]))
	l2.append(strikeratebelow('match4/'+f41,'match4/'+f42,100.0,win[3]))
	l2.append(strikeratebelow('match5/'+f51,'match5/'+f52,100.0,win[4]))
	generate_and_solve_query4(l,l2)
	l=[]
	l2=[]
	l.append(morethan50('match1/'+f11,'match1/'+f12))
	l.append(morethan50('match2/'+f21,'match2/'+f22))
	l.append(morethan50('match3/'+f31,'match3/'+f32))
	l.append(morethan50('match4/'+f41,'match4/'+f42))
	l.append(morethan50('match5/'+f51,'match5/'+f52))
	l2.append(atleast1w('match1/'+f13,'match1/'+f14))
	l2.append(atleast1w('match2/'+f23,'match2/'+f24))
	l2.append(atleast1w('match3/'+f33,'match3/'+f34))
	l2.append(atleast1w('match4/'+f43,'match4/'+f44))
	l2.append(atleast1w('match5/'+f53,'match5/'+f54))
	generate_and_solve_query5(l,l2)
	l=[]
	l2=[]
	l.append(morethan7overs('match1/'+f13,'match1/'+f14))
	l.append(morethan7overs('match2/'+f23,'match2/'+f24))
	l.append(morethan7overs('match3/'+f33,'match3/'+f34))
	l.append(morethan7overs('match4/'+f43,'match4/'+f44))
	l.append(morethan7overs('match5/'+f53,'match5/'+f54))
	l2.append(nowickets('match1/'+f13,'match1/'+f14))
	l2.append(nowickets('match2/'+f23,'match2/'+f24))
	l2.append(nowickets('match3/'+f33,'match3/'+f34))
	l2.append(nowickets('match4/'+f43,'match4/'+f44))
	l2.append(nowickets('match5/'+f53,'match5/'+f54))
	generate_and_solve_query6(l,l2)
	l=[]
	l2=[]
	l.append(nowickets('match1/'+f13,'match1/'+f14))
	l.append(nowickets('match2/'+f23,'match2/'+f24))
	l.append(nowickets('match3/'+f33,'match3/'+f34))
	l.append(nowickets('match4/'+f43,'match4/'+f44))
	l.append(nowickets('match5/'+f53,'match5/'+f54))
	l2.append(economy8('match1/'+f13,'match1/'+f14))
	l2.append(economy8('match2/'+f23,'match2/'+f24))
	l2.append(economy8('match3/'+f33,'match3/'+f34))
	l2.append(economy8('match4/'+f43,'match4/'+f44))
	l2.append(economy8('match5/'+f53,'match5/'+f54))
	#print l
	#print l2
	generate_and_solve_query7(l,l2)
	l=[]
	l2=[]
	l.append(morethan100('match1/'+f11,'match1/'+f12,win[0]))
	l.append(morethan100('match2/'+f21,'match2/'+f22,win[1]))
	l.append(morethan100('match3/'+f31,'match3/'+f32,win[2]))
	l.append(morethan100('match4/'+f41,'match4/'+f42,win[3]))
	l.append(morethan100('match5/'+f51,'match5/'+f52,win[4]))
	generate_and_solve_query8(l)
	l=[]
	r=[]
	a,b=lefthandedbowlersandwickets('match1/'+f13,'match1/'+f14)
	l.append(a)
	l2.append(b)
	a,b=lefthandedbowlersandwickets('match2/'+f23,'match2/'+f24)
	l.append(a)
	l2.append(b)
	a,b=lefthandedbowlersandwickets('match3/'+f33,'match3/'+f34)
	l.append(a)
	l2.append(b)
	a,b=lefthandedbowlersandwickets('match4/'+f43,'match4/'+f44)
	l.append(a)
	l2.append(b)
	a,b=lefthandedbowlersandwickets('match5/'+f53,'match5/'+f54)
	l.append(a)
	l2.append(b)
	#print l
	#print l2
	l3=[]
	for i in range(len(l)):
		if l[i]<l2[i]:
			l3.append(i+1)
	#print l3
	generate_and_solve_query9(l3)
	l=[]
	l2=[]
	playerslessthan26=[]
	teams=[]
	f=open('player_profile/indian_players_profile.txt','r')
	d=f.read()
	d=d.split('\n')
	for i in range(len(d)-1):
		x=d[i].split('\t')
		y=x[3].split('years')
		z=y[0].strip()
		if int(z)<26:
			playerslessthan26.append(x[0].strip())
			teams.append('India')
	f=open('player_profile/nz_players_profile.txt','r')
	d=f.read()
	d=d.split('\n')
	for i in range(len(d)-1):
		x=d[i].split('\t')
		y=x[3].split('years')
		z=y[0].strip()
		if int(z)<26:
			playerslessthan26.append(x[0].strip())
			teams.append('New Zealand')
	#print playerslessthan26
	#print teams
	for i in range(len(playerslessthan26)):
		a=ducks('match1/'+f11,'match1/'+f12,playerslessthan26[i],teams[i])
		if a==1:
			l.append(playerslessthan26[i])
			continue
		a=ducks('match2/'+f21,'match2/'+f22,playerslessthan26[i],teams[i])
		if a==1:
			l.append(playerslessthan26[i])
			continue
		a=ducks('match3/'+f31,'match3/'+f32,playerslessthan26[i],teams[i])
		if a==1:
			l.append(playerslessthan26[i])
			continue
		a=ducks('match4/'+f41,'match4/'+f42,playerslessthan26[i],teams[i])
		if a==1:
			l.append(playerslessthan26[i])
			continue
		a=ducks('match5/'+f51,'match5/'+f52,playerslessthan26[i],teams[i])
		if a==1:
			l.append(playerslessthan26[i])
			continue
	for i in range(len(playerslessthan26)):
		runs=0
		runs+=findruns('match1/'+f11,'match1/'+f12,playerslessthan26[i],teams[i])
		runs+=findruns('match2/'+f21,'match2/'+f22,playerslessthan26[i],teams[i])
		runs+=findruns('match3/'+f31,'match3/'+f32,playerslessthan26[i],teams[i])
		runs+=findruns('match4/'+f41,'match4/'+f42,playerslessthan26[i],teams[i])
		runs+=findruns('match5/'+f51,'match5/'+f52,playerslessthan26[i],teams[i])
		if runs>250:
			l2.append(playerslessthan26[i])
	generate_and_solve_query10(l,l2,playerslessthan26)
	l=[]
	l.append(getplayers('match1/'+f11,'match1/'+f12,'match1/'+f13,'match1/'+f14))
	l.append(getplayers('match2/'+f21,'match2/'+f22,'match2/'+f23,'match2/'+f24))
	l.append(getplayers('match3/'+f31,'match3/'+f32,'match3/'+f33,'match3/'+f34))
	l.append(getplayers('match4/'+f41,'match4/'+f42,'match4/'+f43,'match4/'+f44))
	l.append(getplayers('match5/'+f51,'match5/'+f52,'match5/'+f53,'match5/'+f54))
	players=[]
	#print l
	for i in l:
		for j in i:
			if j not in players:
				players.append(j)
	generate_and_solve_query11(l,players)
	iwides=0
	jwides=0
	iwides+=findwides('match1/'+f13,'match1/'+f14,'I Sharma')
	iwides+=findwides('match2/'+f23,'match2/'+f24,'I Sharma')
	iwides+=findwides('match3/'+f33,'match3/'+f34,'I Sharma')
	iwides+=findwides('match4/'+f43,'match4/'+f44,'I Sharma')
	iwides+=findwides('match5/'+f53,'match5/'+f54,'I Sharma')
	jwides+=findwides('match1/'+f13,'match1/'+f14,'RA Jadeja')
	jwides+=findwides('match2/'+f23,'match2/'+f24,'RA Jadeja')
	jwides+=findwides('match3/'+f33,'match3/'+f34,'RA Jadeja')
	jwides+=findwides('match4/'+f43,'match4/'+f44,'RA Jadeja')
	jwides+=findwides('match5/'+f53,'match5/'+f54,'RA Jadeja')
	#print iwides
	#print jwides
	generate_and_solve_query12(iwides,jwides)
	scatches=0
	rcatches=0
	scatches+=findcatches('match1/'+f11,'match1/'+f12,'Southee')
	scatches+=findcatches('match2/'+f21,'match2/'+f22,'Southee')
	scatches+=findcatches('match3/'+f31,'match3/'+f32,'Southee')
	scatches+=findcatches('match4/'+f41,'match4/'+f42,'Southee')
	scatches+=findcatches('match5/'+f51,'match5/'+f52,'Southee')
	rcatches+=findcatches('match1/'+f11,'match1/'+f12,'Ryder')
	rcatches+=findcatches('match2/'+f21,'match2/'+f22,'Ryder')
	rcatches+=findcatches('match3/'+f31,'match3/'+f32,'Ryder')
	rcatches+=findcatches('match4/'+f41,'match4/'+f42,'Ryder')
	rcatches+=findcatches('match5/'+f51,'match5/'+f52,'Ryder')
	#print scatches
	#print rcatches
	generate_and_solve_query13(scatches,rcatches)
	os.chdir('..')
	f=open('winners.txt','r')
	d=f.read()
	dictionary={}
	d=d.split('\n')
	for i in range(1,len(d)-1,3):
		if d[i] not in dictionary:
			dictionary[d[i]]=1
		else:
			dictionary[d[i]]+=1
	#print dictionary
	l=[]
	l2=[]
	for i in dictionary:
	 	l.append(i)
	 	if dictionary[i]==2:
	 		l2.append(i)
	#print l
	#print l2
	inn1=0
	inn2=0
	count1=0
	count2=0
	generate_and_solve_query14(l,l2)
	os.chdir('dataset/')
	f=open('match1/'+f13,'r')
	d=f.read()
	d=d.split('\n')
	if d[0]=='New Zealand':
		inn1+=findbetterjadeja('match1/'+f13)
		count1+=1
	else:
		inn2+=findbetterjadeja('match1/'+f14)
		count2+=1
	f=open('match2/'+f23,'r')
	d=f.read()
	d=d.split('\n')
	if d[0]=='New Zealand':
		inn1+=findbetterjadeja('match2/'+f23)
		count1+=1
	else:
		inn2+=findbetterjadeja('match2/'+f24)
		count2+=1
	f=open('match3/'+f33,'r')
	d=f.read()
	d=d.split('\n')
	if d[0]=='New Zealand':
		inn1+=findbetterjadeja('match3/'+f33)
		count1+=1
	else:
		inn2+=findbetterjadeja('match3/'+f34)
		count2+=1
	f=open('match4/'+f43,'r')
	d=f.read()
	d=d.split('\n')
	if d[0]=='New Zealand':
		inn1+=findbetterjadeja('match4/'+f43)
		count1+=1
	else:
		inn2+=findbetterjadeja('match4/'+f44)
		count2+=1
	f=open('match5/'+f53,'r')
	d=f.read()
	d=d.split('\n')
	if d[0]=='New Zealand':
		inn1+=findbetterjadeja('match5/'+f53)
		count1+=1
	else:
		inn2+=findbetterjadeja('match5/'+f54)
		count2+=1
	if count1 is not 0:
		inn1=inn1/count1
	if count2 is not 0:
		inn2=inn2/count2
	#print inn1
	#print inn2
	generate_and_solve_query15(inn1,inn2)
	f=open('match1/'+f11,'r')
	d=f.read()
	d=d.split('\n')
	if d[0]=='New Zealand':
		f=open('match1/'+f12,'r')
		d=f.read()
		d=d.split('\n')
	d=d[1:]
	index=0
	count=0
	if d[0]=='India':
		index+=finddhoni('match1/'+f11)
		count+=1
	else:
		index+=finddhoni('match1/'+f12)
		count+=1
	f=open('match2/'+f21,'r')
	d=f.read()
	d=d.split('\n')
	if d[0]=='New Zealand':
		f=open('match2/'+f22,'r')
		d=f.read()
		d=d.split('\n')
	d=d[1:]
	index=0
	count=0
	if d[0]=='India':
		index+=finddhoni('match2/'+f21)
		count+=1
	else:
		index+=finddhoni('match2/'+f22)
		count+=1
	f=open('match3/'+f31,'r')
	d=f.read()
	d=d.split('\n')
	if d[0]=='New Zealand':
		f=open('match3/'+f32,'r')
		d=f.read()
		d=d.split('\n')
	d=d[1:]
	index=0
	count=0
	if d[0]=='India':
		index+=finddhoni('match3/'+f31)
		count+=1
	else:
		index+=finddhoni('match3/'+f32)
		count+=1
	f=open('match4/'+f41,'r')
	d=f.read()
	d=d.split('\n')
	if d[0]=='New Zealand':
		f=open('match4/'+f42,'r')
		d=f.read()
		d=d.split('\n')
	d=d[1:]
	index=0
	count=0
	if d[0]=='India':
		index+=finddhoni('match4/'+f41)
		count+=1
	else:
		index+=finddhoni('match4/'+f42)
		count+=1
	f=open('match5/'+f51,'r')
	d=f.read()
	d=d.split('\n')
	if d[0]=='New Zealand':
		f=open('match5/'+f52,'r')
		d=f.read()
		d=d.split('\n')
	d=d[1:]
	index=0
	count=0
	if d[0]=='India':
		index+=finddhoni('match5/'+f51)
		count+=1
	else:
		index+=finddhoni('match5/'+f52)
		count+=1
	#print index/count
	generate_and_solve_query16(index/count)
	f=open('match1/'+f13,'r')
	d=f.read()
	d=d.split('\n')
	if d[0]=='India':
		f=open('match1/'+f14,'r')
		d=f.read()
		d=d.split('\n')
	d=d[1:]
	val1=0
	val2=0
	count1=0
	count2=0
	for i in d:
		if i=='':
			continue
		if d[0]=='New Zealand':
			val1+=findbetter('match1/'+f13,'I Sharma')
			if val1 is not 0:
				count1+=1
			val2+=findbetter('match1/'+f13,'RA Jadeja')
			if val2 is not 0:
				count2+=1
		else:
			val1+=findbetter('match1/'+f14,'I Sharma')
			if val1 is not 0:
				count1+=1
			val2+=findbetter('match1/'+f14,'RA Jadeja')
			if val2 is not 0:
				count2+=1
	f=open('match2/'+f23,'r')
	d=f.read()
	d=d.split('\n')
	if d[0]=='India':
		f=open('match2/'+f24,'r')
		d=f.read()
		d=d.split('\n')
	d=d[1:]
	val1=0
	val2=0
	for i in d:
		if i=='':
			continue
		if d[0]=='New Zealand':
			val1+=findbetter('match2/'+f23,'I Sharma')
			if val1 is not 0:
				count1+=1
			val2+=findbetter('match2/'+f23,'RA Jadeja')
			if val2 is not 0:
				count2+=1
		else:
			val1+=findbetter('match2/'+f24,'I Sharma')
			if val1 is not 0:
				count1+=1
			val2+=findbetter('match2/'+f24,'RA Jadeja')
			if val2 is not 0:
				count2+=1
	f=open('match3/'+f33,'r')
	d=f.read()
	d=d.split('\n')
	if d[0]=='India':
		f=open('match3/'+f34,'r')
		d=f.read()
		d=d.split('\n')
	d=d[1:]
	val1=0
	val2=0
	for i in d:
		if i=='':
			continue
		if d[0]=='New Zealand':
			val1+=findbetter('match3/'+f33,'I Sharma')
			if val1 is not 0:
				count1+=1
			val2+=findbetter('match3/'+f33,'RA Jadeja')
			if val2 is not 0:
				count2+=1
		else:
			val1+=findbetter('match3/'+f34,'I Sharma')
			if val1 is not 0:
				count1+=1
			val2+=findbetter('match3/'+f34,'RA Jadeja')
			if val2 is not 0:
				count2+=1
	f=open('match4/'+f43,'r')
	d=f.read()
	d=d.split('\n')
	if d[0]=='India':
		f=open('match4/'+f44,'r')
		d=f.read()
		d=d.split('\n')
	d=d[1:]
	val1=0
	val2=0
	for i in d:
		if i=='':
			continue
		if d[0]=='New Zealand':
			val1+=findbetter('match4/'+f43,'I Sharma')
			if val1 is not 0:
				count1+=1
			val2+=findbetter('match4/'+f43,'RA Jadeja')
			if val2 is not 0:
				count2+=1
		else:
			val1+=findbetter('match4/'+f44,'I Sharma')
			if val1 is not 0:
				count1+=1
			val2+=findbetter('match4/'+f44,'RA Jadeja')
			if val2 is not 0:
				count2+=1
	f=open('match5/'+f53,'r')
	d=f.read()
	d=d.split('\n')
	if d[0]=='India':
		f=open('match5/'+f54,'r')
		d=f.read()
		d=d.split('\n')
	d=d[1:]
	val1=0
	val2=0
	for i in d:
		if i=='':
			continue
		if d[0]=='New Zealand':
			val1+=findbetter('match5/'+f53,'I Sharma')
			if val1 is not 0:
				count1+=1
			val2+=findbetter('match5/'+f53,'RA Jadeja')
			if val2 is not 0:
				count2+=1
		else:
			val1+=findbetter('match5/'+f54,'I Sharma')
			if val1 is not 0:
				count1+=1
			val2+=findbetter('match5/'+f54,'RA Jadeja')
			if val2 is not 0:
				count2+=1
	generate_and_solve_query17(val1,val2)
	top=0
	middle=0
	top+=findtop('match1/'+f11)
	top+=findtop('match1/'+f12)
	top+=findtop('match2/'+f21)
	top+=findtop('match2/'+f22)
	top+=findtop('match3/'+f31)
	top+=findtop('match3/'+f32)
	top+=findtop('match4/'+f41)
	top+=findtop('match4/'+f42)
	top+=findtop('match5/'+f51)
	top+=findtop('match5/'+f52)
	middle+=findmiddle('match1/'+f11)
	middle+=findmiddle('match1/'+f12)
	middle+=findmiddle('match2/'+f21)
	middle+=findmiddle('match2/'+f22)
	middle+=findmiddle('match3/'+f31)
	middle+=findmiddle('match3/'+f32)
	middle+=findmiddle('match4/'+f41)
	middle+=findmiddle('match4/'+f42)
	middle+=findmiddle('match5/'+f51)
	middle+=findmiddle('match5/'+f52)
	generate_and_solve_query18(top,middle)
	l=[]
	l2=[]
	os.chdir('..')
	f=open('toss.txt','r')
	d=f.read()
	d=d.split('\n')
	for i in d:
		if i=='':
			continue
		l.append(i)
	f=open('winners.txt','r')
	d=f.read()
	d=d.split('\n')
	for i in range(0,len(d)-2,3):
		l2.append(d[i])
	generate_and_solve_query19(l,l2)
	l=[]
	l2=[]
	l3=[]
	os.chdir('dataset')
	a,b=findinnscore('match1/'+f11,'match1/'+f14)
	l.append(a)
	l.append(b)
	a,b=findinnscore('match1/'+f12,'match1/'+f13)
	l2.append(a)
	l2.append(b)
	a,b=findinnscore('match2/'+f21,'match2/'+f24)
	l.append(a)
	l.append(b)
	a,b=findinnscore('match2/'+f22,'match2/'+f23)
	l2.append(a)
	l2.append(b)
	a,b=findinnscore('match3/'+f31,'match3/'+f34)
	l.append(a)
	l.append(b)
	a,b=findinnscore('match3/'+f32,'match3/'+f33)
	l2.append(a)
	l2.append(b)
	a,b=findinnscore('match4/'+f41,'match4/'+f44)
	l.append(a)
	l.append(b)
	a,b=findinnscore('match4/'+f42,'match4/'+f43)
	l2.append(a)
	l2.append(b)
	a,b=findinnscore('match5/'+f51,'match5/'+f54)
	l.append(a)
	l.append(b)
	a,b=findinnscore('match5/'+f52,'match5/'+f53)
	l2.append(a)
	l2.append(b)

	dictionary={}
	dictionary['India']=0
	dictionary['New Zealand']=0
	for i in range(0,len(d)-2,3):
		l3.append(d[i])
		if d[i]=='Match tied':
			dictionary['India']+=0.5
			dictionary['New Zealand']+=0.5
		else:
			dictionary[d[i]]+=1
	generate_and_solve_query20(l,l2,l3,dictionary)

if __name__=='__main__':
	main()

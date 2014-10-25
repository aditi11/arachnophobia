import os
import nltk
import urllib
from bs4 import BeautifulSoup

url1="http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667641.html"
url2="http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667643.html"
url3="http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667645.html"
url4="http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667647.html"
url5="http://www.espncricinfo.com/new-zealand-v-india-2014/engine/match/667649.html"

id1='inningsBat1'
id2='inningsBowl1'
id3='inningsBat2'
id4='inningsBowl2'
writefile=open('winners.txt','w')
write2=open('toss.txt','w')

def parse(url,f,tid,inid):
	temp=urllib.urlopen(url)
	data=temp.read()
	soup=BeautifulSoup(data)
	a=soup.find('table',id=inid)
	row=a.find('tr',attrs={'class':'inningsHead'})
	tds=row.findAll('td')
	x=str(tds[1]).split('>')
	y=x[1].split('<')
	y=y[0].split('innings')
	y=y[0].strip()
	f.write(y)
	f.write('\n')
	a=soup.find('table',id=tid)
	rows=a.findAll('tr',attrs={'class':'inningsRow'})
	for i in rows:
		rows2=i.findAll('td')
		for j in range(1,len(rows2)):
			if rows2[j]=='':
				continue
			t=str(rows2[j]).split('<')
			#print t
			for k in range(len(t)):
				p=t[k].split('>')
				#print p
				if p[0] is not '':
					if p[1] is not None and p[1] is not '' and p[1] is not ' ':
						#print p[1]
						if p[1]=='Extras':
							return
						f.write(p[1])
						f.write(",")
						break
		f.write("\n")

def findwinners(url):
	temp=urllib.urlopen(url)
	data=temp.read()
	soup=BeautifulSoup(data)

	a=soup.find('p',attrs={'class':'statusText'})
	b=str(a).split('<')
	c=b[1].split('>')
	c=c[1].split('won')
	winnercountry=c[0].strip()
	writefile.write(winnercountry)
	writefile.write('\n')
	a=soup.find('table',attrs={'class':'notesTable'})
	rows=a.findAll('tr',attrs={'class':'notesRow'})
	b=rows[1].find('td')
	#print b
	b=str(b).split('match</b>')
	c=b[1].split('(')
	#print c[0].strip()
	writefile.write(c[0].strip())
	writefile.write('\n')
	win=c[1].split(')')
	#print win[0].strip()
	writefile.write(win[0].strip())
	writefile.write('\n')

def findtoss(url):
	temp=urllib.urlopen(url)
	data=temp.read()
	soup=BeautifulSoup(data)
	a=soup.find('table',attrs={'class':'notesTable'})
	b=a.find('tr',attrs={'class':'notesRow'})
	c=b.find('td')
	#print c
	x=str(c).split(',')
	y=x[0].split('>')
	write2.write(y[3].strip())
	write2.write('\n')
	
os.chdir('dataset')
if not os.path.exists('match1'):
	os.mkdir('match1');
os.chdir('match1');
inid1='inningsBat1'
inid3='inningsBat2'
f11=open('odi1_inn1_bat.txt','w')
parse(url1,f11,id1,inid1)
f12=open('odi1_inn1_bowl.txt','w')
parse(url1,f12,id2,inid1)
f13=open('odi1_inn2_bat.txt','w')
parse(url1,f13,id3,inid3)
f14=open('odi1_inn2_bowl.txt','w')
parse(url1,f14,id4,inid3)
os.chdir('..')
if not os.path.exists('match2'):
	os.mkdir('match2');
os.chdir('match2');
f21=open('odi2_inn1_bat.txt','w')
parse(url2,f21,id1,inid1)
f22=open('odi2_inn1_bowl.txt','w')
parse(url2,f22,id2,inid1)
f23=open('odi2_inn2_bat.txt','w')
parse(url2,f23,id3,inid3)
f24=open('odi2_inn2_bowl.txt','w')
parse(url2,f24,id4,inid3)
os.chdir('..')

if not os.path.exists('match3'):
	os.mkdir('match3')
os.chdir('match3')
f31=open('odi3_inn1_bat.txt','w')
parse(url3,f31,id1,inid1)
f32=open('odi3_inn1_bowl.txt','w')
parse(url3,f32,id2,inid1)
f33=open('odi3_inn2_bat.txt','w')
parse(url3,f33,id3,inid3)
f34=open('odi3_inn2_bowl.txt','w')
parse(url3,f34,id4,inid3)
os.chdir('..')
if not os.path.exists('match4'):
	os.mkdir('match4')
os.chdir('match4')
f41=open('odi4_inn1_bat.txt','w')
parse(url4,f41,id1,inid1)
f42=open('odi4_inn1_bowl.txt','w')
parse(url4,f42,id2,inid1)
f43=open('odi4_inn2_bat.txt','w')
parse(url4,f43,id3,inid3)
f44=open('odi4_inn2_bowl.txt','w')
parse(url4,f44,id4,inid3)
os.chdir('..')
if not os.path.exists('match5'):
	os.mkdir('match5')
os.chdir('match5')
f51=open('odi5_inn1_bat.txt','w')
parse(url5,f51,id1,inid1)
f52=open('odi5_inn1_bowl.txt','w')
parse(url5,f52,id2,inid1)
f53=open('odi5_inn2_bat.txt','w')
parse(url5,f53,id3,inid3)
f54=open('odi5_inn2_bowl.txt','w')
parse(url5,f54,id4,inid3)

findwinners(url1)
findwinners(url2)
findwinners(url3)
findwinners(url4)
findwinners(url5)

findtoss(url1)
findtoss(url2)
findtoss(url3)
findtoss(url4)
findtoss(url5)

f=open('dataset/player_profile/nz_players_profile.txt','r')
f2=open('dataset/player_profile/indian_players_profile.txt','r')
d=f.read()
d2=f2.read()
d=d.split('\n')
d2=d2.split('\n')
for i in range(len(d)-1):
	x=d[i].split('\t')
	print x[7]
for i in range(len(d2)-1):
	x=d2[i].split('\t')
	print x[7]

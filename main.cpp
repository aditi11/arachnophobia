#include<iostream>
#include<cmath>
#include<GL/glut.h>
using namespace std;
typedef struct position
{
	float x;
	float y;
}position;
position spiderpos[3];
#define PI 3.141592653589
#define DEG2RAD(deg)(deg*PI/180)

void drawScene();
void update(int value);
void drawBox(float len);
void drawBasket(float,float,int);
void drawGun();
void drawLaser();
void drawSpider();
void initRendering();
void handleResize(int w,int h);
void handleKeypress1(unsigned char key,int x,int y);
void handleKeypress2(int key,int x,int y);
void scoreDisplay(float,float,float,float);
void handleMouseClick(int button,int state,int x,int y);
void MouseMove(int x,int y);
void DisplayEnd(float,float,float,float);
void drawSmiley();

float box_len=4.0f;
float a=0.2f;
float b=0.1f;
int spidercolor[3]={0};
float spidera=0.07f;
float spiderb=0.15f;
float spiderhead=0.04f;
int spiderindex=0;
int spiderend=0;
float spidervel[3];
float minspeed=0.001f;
float maxspeed=0.008f;
float threshold=0.5f;
int controlflag;
float redbasketx=-1.5f;
float redbaskety=-1.5f;
float greenbasketx=1.5f;
float greenbaskety=-1.5f;
float guncenterx=0.0f;
float guncentery=-1.5f;
float guncenterside=0.25f;
float guntoplength=0.2f;
float guntopbreadth=0.1f;
float gunsidelength=0.1f;
float gunsidebreadth=0.1f;
float theta=10.0f;
float angle=0.0f;
int score;
int laserflag=0;
float lasercoord=guncenterside/2+guntoplength;
int lasertime=0;
float laservel=0.10f;
float init=lasercoord;
float dist=0.0f;
float lx=0.0f;
float ly=0.0f;
float ltheta;
int pausedflag=0;
float redleft=-2.0f;
float redright=2.0f;
float greenleft=-2.0f;
float greenright=2.0f;
float cannonleft=-2.0f;
float cannonright=2.0f;
float blockedx[1000];
float blockedcolor[1000];
int blockedindex=0;
int finishedflag=0;
float redshift=0.0f;
float greenshift=0.0f;
float gunshift=0.0f;
int shiftflag=0;
int mouseleftflag=0;
int mouserightflag=0;
float mousex=0.0f;
float mousey=0.0f;
float smileyx=-1.6f+(3.2f*(float)rand())/(float)RAND_MAX;
float smileyy=2.0f;
int smileytime=0;
int smileyflag=0;

int main(int argc,char **argv) 
{
	glutInit(&argc,argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	for(int i=0;i<3;i++)
	{
		spidervel[i]=minspeed+(maxspeed-minspeed)*(float)rand()/(float)RAND_MAX;
		spiderpos[i].x=-1.6f+(3.2f*(float)rand())/(float)RAND_MAX;
		spiderpos[i].y=2.0f;
//		srand(time(NULL));
//		spidercolor[i]=rand()%3;
	}
	int w=glutGet(GLUT_SCREEN_WIDTH);
	int h=glutGet(GLUT_SCREEN_HEIGHT);
	int windowWidth=w*2/3;
	int windowHeight=h*2/3;
	glutInitWindowSize(w,h);
	glutInitWindowPosition(0.0f,0.0f);
	glutCreateWindow("Arachnophobia");
	initRendering();
	glutDisplayFunc(drawScene);
	glutIdleFunc(drawScene);
	glutKeyboardFunc(handleKeypress1);
	glutSpecialFunc(handleKeypress2);
	glutReshapeFunc(handleResize);
	glutMouseFunc(handleMouseClick);
	glutMotionFunc(MouseMove);
	glutTimerFunc(10,update,0);
	glutMainLoop();
	return 0;
}
void drawScene() 
{
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	glPushMatrix();
	glTranslatef(0.0f,0.0f,-5.0f);
	glColor3f(1.0f,1.0f,1.0f);
	drawBox(box_len);
	glPushMatrix();
	glBegin(GL_LINES);
	glVertex2f(-2.0f,-1.5f);
	glVertex2f(2.0f,-1.5f);
	glEnd();
	glPopMatrix();
	glPushMatrix();
	glTranslatef(redbasketx,redbaskety,0.0f);
	glColor3f(1.0f,0.0f,0.0f);
	if(controlflag==1)
		drawBasket(a,b,1);
	else
		drawBasket(a,b,0);
	glPopMatrix();
	glPushMatrix();
	glTranslatef(greenbasketx,greenbaskety,0.0f);
	glColor3f(0.0f,1.0f,0.0f);
	if(controlflag==2)
		drawBasket(a,b,1);
	else
		drawBasket(a,b,0);
	glPopMatrix();
	glPushMatrix();
	glTranslatef(guncenterx,guncentery,0.0f);
	glRotatef(angle,0.0f,0.0f,1.0f);
	glColor3f(0.0f,0.0f,1.0f);
	drawGun();
	glPopMatrix();
	if(laserflag==1)
	{
		glPushMatrix();
		glTranslatef(lx,ly,0.0f);
		glRotatef(ltheta,0.0f,0.0f,1.0f);
		glColor3f(1.0f,1.0f,0.0f);
		drawLaser();
		glPopMatrix();
	}
	int i;
	for(i=0;i<3;i++)
	{
		if(spiderpos[i].y<1.6f)
		{
			glPushMatrix();
			glTranslatef(spiderpos[i].x,spiderpos[i].y,0.0f);
			if(spidercolor[i]==1)
				glColor3f(1.0f,0.0f,0.0f);
			else if(spidercolor[i]==2)
				glColor3f(0.0f,1.0f,0.0f);
			else
				glColor3f(0.0f,0.0f,1.0f);
			drawSpider();
			glPopMatrix();
		}
	}
	for(i=0;i<blockedindex;i++)
	{
		glPushMatrix();
		glTranslatef(blockedx[i],-1.5f,0.0f);
		if(blockedcolor[i]==1)
			glColor3f(1.0f,0.0f,0.0f);
		else if(blockedcolor[i]==2)
			glColor3f(0.0f,1.0f,0.0f);
		else
			glColor3f(0.0f,0.0f,1.0f);
		drawSpider();
		glPopMatrix();
	}
	if(smileyflag==1)
	{
		glPushMatrix();
		glTranslatef(smileyx,smileyy,0.0f);
		glColor3f(0.5f,0.5f,0.0f);
		drawSmiley();
		glPopMatrix();
	}
	scoreDisplay(3.0f,1.5f,0.0f,0.5f);
	if(finishedflag)
		DisplayEnd(1.0f,0.0f,0.0f,0.3f);
	glPopMatrix();
	glutSwapBuffers();
}
void update(int value) 
{
	int i;
	if(!finishedflag)
	{
	if(!pausedflag)
	{
		smileytime++;
		if(smileytime%600==0)
		{
			smileyflag=1;
		}
		if(smileyy<-1.5f)
		{
			smileyy=2.0f;
			smileyx=-1.6f+(3.2f*(float)rand())/(float)RAND_MAX;
			smileyflag=0;
		}
		if(lx-(0.4f+lasercoord-laservel)*sin(DEG2RAD(ltheta))<smileyx+0.1f && lx-(0.4f+lasercoord-laservel)*sin(DEG2RAD(ltheta))>smileyx-0.1f && ly+(0.4f+lasercoord-laservel)*cos(DEG2RAD(ltheta))<smileyy+0.1f && ly+(0.4f+lasercoord-laservel)*cos(DEG2RAD(ltheta))>smileyy-0.1f)
		{
			score+=10;
			smileyy=2.0f;
			smileyx=-1.6f+(3.2f*(float)rand())/(float)RAND_MAX;
			smileyflag=0;
		}
		if(smileyflag==1)
		{
			smileyy-=0.03f;
		}
		
		if(laserflag==1 && ((ltheta==0 && dist>=2.9f) || (ly+(0.4f+lasercoord-laservel)*cos(DEG2RAD(ltheta))>2.0f)))
		{
			laserflag=0;
			dist=0.0f;
			lasercoord=guncenterside/2+guntoplength;
		}
		else if(laserflag==1 && (lx-(0.4f+lasercoord-laservel)*sin(DEG2RAD(ltheta))>2.0f || lx-(0.4f+lasercoord-laservel)*sin(DEG2RAD(ltheta))<-2.0f))
		{
			lx=lx-(0.4f+lasercoord-laservel)*sin(DEG2RAD(ltheta));
			ltheta*=-1;
			ly=ly+(0.4f+lasercoord-laservel)*cos(DEG2RAD(ltheta));
			lasercoord=0.0f;
			dist=0.0f;
		}
		if(laserflag==1)
		{
			lasercoord+=laservel;
			dist+=laservel;
		}
		if(controlflag==3)
		{
			lasertime++;
			if(lasertime==100)
			{
				lasertime=0;
			}
		}
		//if(lasertime==1 && laserflag==1)
		//	system("aplay gunsound.mp3 &");
		for(i=0;i<3;i++)
		{
			if(spiderpos[i].x<guncenterx+guncenterside/2 && spiderpos[i].x>guncenterx-guncenterside/2 && spiderpos[i].y<guncentery+guncenterside/2+guntoplength && spiderpos[i].y>guncentery-guncenterside/2-guntoplength)
			{
				finishedflag=1;
			}
			if(spidercolor[i]==1)
			{
				if(spiderpos[i].x<redbasketx+a && spiderpos[i].x>redbasketx-a && spiderpos[i].y-spiderb-2*spiderhead>redbaskety && spiderpos[i].y-spiderb-2*spiderhead<redbaskety+0.1f)
				{
					srand(time(NULL));
					spidercolor[i]=rand()%3;
					spiderpos[i].x=-1.6f+(3.2f*(float)rand())/(float)RAND_MAX;
					spiderpos[i].y=2.0f;
					spidervel[i]=minspeed+(maxspeed-minspeed)*(float)rand()/(float)RAND_MAX;
					score++;
				}
				else if(spiderpos[i].x<greenbasketx+a && spiderpos[i].x>greenbasketx-a && spiderpos[i].y-spiderb-2*spiderhead>greenbaskety && spiderpos[i].y-spiderb-2*spiderhead<greenbaskety+0.1f)
				{
					srand(time(NULL));
					spidercolor[i]=rand()%3;
					spiderpos[i].x=-1.6f+(3.2f*(float)rand())/(float)RAND_MAX;
					spiderpos[i].y=2.0f;
					spidervel[i]=minspeed+(maxspeed-minspeed)*(float)rand()/(float)RAND_MAX;
					score--;
				}
				else if(laserflag==1 && lx-(0.4f+lasercoord-laservel)*sin(DEG2RAD(ltheta))<spiderpos[i].x+spidera && lx-(0.4f+lasercoord-laservel)*sin(DEG2RAD(ltheta))>spiderpos[i].x-spidera && ly+(0.4f+lasercoord-laservel)*cos(DEG2RAD(ltheta))<spiderpos[i].y+spiderb && ly+(0.4f+lasercoord-laservel)*cos(DEG2RAD(ltheta))>spiderpos[i].y-spiderb-2*spiderhead)
				{
					srand(time(NULL));
					spidercolor[i]=rand()%3;
					spiderpos[i].x=-1.6f+(3.2f*(float)rand())/(float)RAND_MAX;
					spiderpos[i].y=2.0f;
					spidervel[i]=minspeed+(maxspeed-minspeed)*(float)rand()/(float)RAND_MAX;
					score--;
					laserflag=0;
					lasertime=0;
				}
			}
			else if(spidercolor[i]==2)
			{
				if(spiderpos[i].x<greenbasketx+a && spiderpos[i].x>greenbasketx-a && spiderpos[i].y-spiderb-2*spiderhead>greenbaskety && spiderpos[i].y-spiderb-2*spiderhead<greenbaskety+0.1f)
				{
					srand(time(NULL));
					spidercolor[i]=rand()%3;
					spiderpos[i].x=-1.6f+(3.2f*(float)rand())/(float)RAND_MAX;
					spiderpos[i].y=2.0f;
					spidervel[i]=minspeed+(maxspeed-minspeed)*(float)rand()/(float)RAND_MAX;
					score++;
				}
				else if(spiderpos[i].x<redbasketx+a && spiderpos[i].x>redbasketx-a && spiderpos[i].y-spiderb>redbaskety && spiderpos[i].y-spiderb<redbaskety+0.1f)
				{
					srand(time(NULL));
					spidercolor[i]=rand()%3;
					spiderpos[i].x=-1.6f+(3.2f*(float)rand())/(float)RAND_MAX;
					spiderpos[i].y=2.0f;
					spidervel[i]=minspeed+(maxspeed-minspeed)*(float)rand()/(float)RAND_MAX;
					score--;
				}
				else if(laserflag==1 && lx-(0.4f+lasercoord-laservel)*sin(DEG2RAD(ltheta))<spiderpos[i].x+spidera && lx-(0.4f+lasercoord-laservel)*sin(DEG2RAD(ltheta))>spiderpos[i].x-spidera && ly+(0.4f+lasercoord-laservel)*cos(DEG2RAD(ltheta))<spiderpos[i].y+spiderb && ly+(0.4f+lasercoord-laservel)*cos(DEG2RAD(ltheta))>spiderpos[i].y-spiderb-2*spiderhead)
				{
					srand(time(NULL));
					spidercolor[i]=rand()%3;
					spiderpos[i].x=-1.6f+(3.2f*(float)rand())/(float)RAND_MAX;
					spiderpos[i].y=2.0f;
					spidervel[i]=minspeed+(maxspeed-minspeed)*(float)rand()/(float)RAND_MAX;
					score--;
					laserflag=0;
					lasertime=0;
				}
			}
			else
			{
				if(laserflag==1 && lx-(0.4f+lasercoord-laservel)*sin(DEG2RAD(ltheta))<spiderpos[i].x+spidera && lx-(0.4f+lasercoord-laservel)*sin(DEG2RAD(ltheta))>spiderpos[i].x-spidera && ly+(0.4f+lasercoord-laservel)*cos(DEG2RAD(ltheta))<spiderpos[i].y+spiderb && ly+(0.4f+lasercoord-laservel)*cos(DEG2RAD(ltheta))>spiderpos[i].y-spiderb-2*spiderhead)
				{
					srand(time(NULL));
					spidercolor[i]=rand()%3;
					spidervel[i]=minspeed+(maxspeed-minspeed)*(float)rand()/(float)RAND_MAX;
					spiderpos[i].x=-1.6f+(3.2f*(float)rand())/(float)RAND_MAX;
					spiderpos[i].y=2.0f;
					score++;
					laserflag=0;
					lasertime=0;
				}
				else if(spiderpos[i].x<greenbasketx+a && spiderpos[i].x>greenbasketx-a && spiderpos[i].y-spiderb-2*spiderhead>greenbaskety && spiderpos[i].y-spiderb-2*spiderhead<greenbaskety+0.1f)
				{
					srand(time(NULL));
					spidercolor[i]=rand()%3;
					spiderpos[i].x=-1.6f+(3.2f*(float)rand())/(float)RAND_MAX;
					spiderpos[i].y=2.0f;
					spidervel[i]=minspeed+(maxspeed-minspeed)*(float)rand()/(float)RAND_MAX;
					cout<<"yes";
					score--;
				}
				else if(spiderpos[i].x<redbasketx+a && spiderpos[i].x>redbasketx-a && spiderpos[i].y-spiderb-2*spiderhead>redbaskety && spiderpos[i].y-spiderb-2*spiderhead<redbaskety+0.1f)
				{
					srand(time(NULL));
					spidercolor[i]=rand()%3;
					spiderpos[i].x=-1.6f+(3.2f*(float)rand())/(float)RAND_MAX;
					spiderpos[i].y=2.0f;
					spidervel[i]=minspeed+(maxspeed-minspeed)*(float)rand()/(float)RAND_MAX;
					if(i==5)
						spiderindex=0;
					else
						spiderindex=i+1;
					score--;
				}
			}
		}
		for(i=0;i<3;i++)
		{
			if(spiderpos[i].y<-1.5f)
			{
				score-=5;
				blockedx[blockedindex]=spiderpos[i].x;
				blockedcolor[blockedindex]=spidercolor[i];
				blockedindex++;
				if(spiderpos[i].x>greenbasketx && spiderpos[i].x<greenright)
					greenright=spiderpos[i].x;
				else if(spiderpos[i].x<greenbasketx && spiderpos[i].x>greenleft)
					greenleft=spiderpos[i].x;
				if(spiderpos[i].x>redbasketx && spiderpos[i].x<redright)
					redright=spiderpos[i].x;
				else if(spiderpos[i].x<redbasketx && spiderpos[i].x>redleft)
					redleft=spiderpos[i].x;
				if(spiderpos[i].x>guncenterx && spiderpos[i].x<cannonright)
					cannonright=spiderpos[i].x;
				else if(spiderpos[i].x<guncenterx && spiderpos[i].x>cannonleft)
					cannonleft=spiderpos[i].x;
				spidervel[i]=minspeed+(maxspeed-minspeed)*(float)rand()/(float)RAND_MAX;
				spiderpos[i].x=-1.6f+(3.2f*(float)rand())/(float)RAND_MAX;
				spiderpos[i].y=2.0f;
				srand(time(NULL));
				spidercolor[i]=rand()%3;
			}
		}
		for(i=0;i<3;i++)
			spiderpos[i].y-=spidervel[i];
	}
	}
	glutTimerFunc(10,update,0);
}
void drawBox(float len) 
{
	glPolygonMode(GL_FRONT_AND_BACK,GL_LINE);
	glBegin(GL_QUADS);
	glVertex2f(-len/2,-len/2);
	glVertex2f(len/2,-len/2);
	glVertex2f(len/2,len/2);
	glVertex2f(-len/2,len/2);
	glEnd();
	glPolygonMode(GL_FRONT_AND_BACK,GL_FILL);
}
void initRendering()
{
	glEnable(GL_DEPTH_TEST);       
	glEnable(GL_COLOR_MATERIAL);
	glClearColor(0.0f,0.0f,0.0f,1.0f);
}
void handleResize(int w,int h)
{
	glViewport(0,0,w,h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluPerspective(45.0f,(float)w/(float)h,0.1f,200.0f);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
}
void handleKeypress1(unsigned char key, int x, int y)
{
	if (key==27 || key=='q')
	{
		if(finishedflag==0)
			finishedflag=1;
		else
			exit(0);
	}
	if(key=='r' || key=='R')
	{
		controlflag=1;
	}
	else if(key=='g' || key=='G')
	{
		controlflag=2;
	}
	else if(key=='b' || key=='B')
	{
		controlflag=3;
	}
	if(key==' ' && controlflag==3 && laserflag==0)
	{
		system("aplay gunsound2.wav &");
		laserflag=1;
		ltheta=angle;
		lx=guncenterx;
		ly=guncentery;
	}
	if(key=='p' || key=='P')
	{
		if(pausedflag)
			pausedflag=0;
		else
			pausedflag=1;
	}
}
void handleKeypress2(int key,int x,int y)
{
	if(controlflag==1)
	{
		if(key==GLUT_KEY_LEFT)
		{
			if(redbasketx-0.05f>redleft+a)
			{
				redbasketx-=0.05f;
			}
		}
		if(key==GLUT_KEY_RIGHT)
		{
			if(redbasketx+0.05f<redright-a)
			{
				redbasketx+=0.05f;
			}
		}
	}
	else if(controlflag==2)
	{
		if(key==GLUT_KEY_LEFT)
		{
			if(greenbasketx-0.05f>greenleft+a)
			{
				greenbasketx-=0.05f;
			}
		}
		if(key==GLUT_KEY_RIGHT)
		{
			if(greenbasketx+0.05f<greenright-a)
			{
				greenbasketx+=0.05f;
			}
		}
	}
	else if(controlflag==3)
	{
		if(key==GLUT_KEY_LEFT)
		{
			if(guncenterx-0.05f>cannonleft+gunsidebreadth+0.025+guncenterside/2)
			{
				guncenterx-=0.05f;
			}
		}
		if(key==GLUT_KEY_RIGHT)
		{
			if(guncenterx+0.05f<cannonright-gunsidebreadth-0.025-guncenterside/2)
			{
				guncenterx+=0.05f;
			}
		}
		if(key==GLUT_KEY_UP)
		{
			if(angle-theta>-90.0f)
			{
				angle-=theta;
			}
		}
		if(key==GLUT_KEY_DOWN)
		{
			if(angle+theta<90.0f)
			{
				angle+=theta;
			}
		}
	}
}
void MouseMove(int x,int y)
{
	mousex=x;
	mousey=y;
	int height=glutGet(GLUT_WINDOW_HEIGHT);
	int width=glutGet(GLUT_WINDOW_WIDTH);
	mousex=mousex-width/2;
	mousex=mousex*4/width;
	mousey=height/2-mousey;
	mousey=mousey*4.0f/height;
	if(mouseleftflag!=0)
	{
		if(controlflag==1)
		{
			if(mousex>redleft && mousex<redright)
			{
				if(redbasketx<mousex)
				{
					redbasketx=mousex-a;
				}
				else
				{
					redbasketx=mousex+a;
				}
			}
			else
			{
				if(redbasketx<mousex)
				{
					redbasketx=redright-a;
				}
				else
				{
					redbasketx=redleft+a;
				}
			}
		}
		else if(controlflag==2)
		{
			if(mousex>greenleft && mousex<greenright)
			{
				if(greenbasketx<mousex)
				{
					greenbasketx=mousex-a;
				}
				else
				{
					greenbasketx=mousex+a;
				}
			}
			else
			{
				if(greenbasketx<mousex)
				{
					greenbasketx=greenright-a;
				}
				else
				{
					greenbasketx=greenleft+a;
				}
			}
		}
		else if(controlflag==3)
		{
			if(mousex>cannonleft && mousex<cannonright)
			{
				if(guncenterx<mousex)
				{
					guncenterx=mousex-0.25f-gunsidebreadth-guncenterside/2;
				}
				else
				{
					guncenterx=mousex+0.25f+gunsidebreadth+guncenterside/2;
				}
			}
			else
			{
				if(guncenterx<mousex)
				{
					guncenterx=cannonright-0.25f-gunsidebreadth-guncenterside/2;
				}
				else
				{
					guncenterx=cannonleft+0.25f+gunsidebreadth+guncenterside/2;
				}
			}
		}
	}
	else if(mouserightflag!=0)
	{
		if(controlflag==3)
		{
			if(guncenterx<mousex)
			{
				if(angle>-87.0f)
					angle-=3.0f;
			}
			else
			{
				if(angle<87.0f)
					angle+=3.0f;
			}
		}
	}
}
void handleMouseClick(int button,int state,int x,int y)
{
	if(button==GLUT_LEFT_BUTTON)
	{
		if(state==GLUT_DOWN)
		{
			mouseleftflag=1;
			mouserightflag=0;
			if(mousex<redbasketx+a && mousex>redbasketx-a && mousey<redbaskety+b && mousey>redbaskety-0.35f)
			{
				controlflag=1;
			}
			else if(mousex<greenbasketx+a && mousex>greenbasketx-a && mousey<greenbaskety+b && mousey>greenbaskety-0.35f)
			{
				controlflag=2;
			}
			else if(mousex<guncenterx+guncenterside/2+0.25f+gunsidebreadth && mousex>guncenterx-guncenterside/2-0.25f-gunsidebreadth && mousey<guncentery+guntoplength+guncenterside/2 && mousey>guncentery-guncenterside/2)
			{
				controlflag=3;
			}
		}
		else
			mouseleftflag=0;
	}
	else if(button==GLUT_RIGHT_BUTTON)
	{
		if(state==GLUT_DOWN)
		{
			mouserightflag=1;
			mouseleftflag=0;
		}
		else
			mouserightflag=0;
	}
}
void drawBasket(float a,float b,int arg)
{
	if(arg==0)
		glBegin(GL_LINE_STRIP);
	else
		glBegin(GL_TRIANGLE_FAN);
	for(int i=0;i<360;i++)
	{
		glVertex2f(a*cos(DEG2RAD(i)),b*sin(DEG2RAD(i)));
	}
	glEnd();
	if(arg==0)
		glPolygonMode(GL_FRONT_AND_BACK,GL_LINE);
	else
		glPolygonMode(GL_FRONT_AND_BACK,GL_LINES);
	glBegin(GL_LINES);
	glVertex2f(-a,-0.35f);
	glVertex2f(a,-0.35f);
	glVertex2f(a,-0.35f);
	glVertex2f(a,0);
	glVertex2f(-a,0);
	glVertex2f(-a,-0.35f);
	glEnd();
	glPolygonMode(GL_FRONT_AND_BACK,GL_FILL);
}
void drawSpider()
{
	glBegin(GL_TRIANGLE_FAN);
	for(int i=0;i<360;i++)
	{
		glVertex2f(spidera*cos(DEG2RAD(i)),spiderb*sin(DEG2RAD(i)));
	}
	glEnd();
	glBegin(GL_TRIANGLE_FAN);
	for(int i=0;i<360;i++)
	{
		glVertex2f(spiderhead*cos(DEG2RAD(i)),-spiderb-spiderhead+spidera*sin(DEG2RAD(i)));
	}
	glEnd();
	glBegin(GL_LINES);
	glVertex2f(spidera-0.01f,0.01f);
	glVertex2f(spidera+0.1f,0.05f);
	glVertex2f(spidera+0.1f,0.05f);
	glVertex2f(spidera+0.2f,0.2f);
	
	glVertex2f(-spidera+0.01f,0.01f);
	glVertex2f(-spidera-0.1f,0.05f);
	glVertex2f(-spidera-0.1f,0.05f);
	glVertex2f(-spidera-0.2f,0.2f);
	
	glVertex2f(spidera-0.01f,-0.01f);
	glVertex2f(spidera+0.1f,-0.05f);
	glVertex2f(spidera+0.1f,-0.05f);
	glVertex2f(spidera+0.2f,-0.2f);
	
	glVertex2f(-spidera+0.01f,-0.01f);
	glVertex2f(-spidera-0.1f,-0.05f);
	glVertex2f(-spidera-0.1f,-0.05f);
	glVertex2f(-spidera-0.2f,-0.2f);
	glVertex2f(spidera-0.01f,0.1f);
	glVertex2f(spidera+0.06f,0.2f);
	glVertex2f(spidera+0.06f,0.2f);
	glVertex2f(spidera+0.09f,0.35f);

	glVertex2f(-spidera+0.01f,0.1f);
	glVertex2f(-spidera-0.06f,0.2f);
	glVertex2f(-spidera-0.06f,0.2f);
	glVertex2f(-spidera-0.09f,0.35f);

	glVertex2f(spidera-0.01f,-0.1f);
	glVertex2f(spidera+0.06f,-0.2f);
	glVertex2f(spidera+0.06f,-0.2f);
	glVertex2f(spidera+0.09f,-0.35f);

	glVertex2f(-spidera+0.01f,-0.1f);
	glVertex2f(-spidera-0.06f,-0.2f);
	glVertex2f(-spidera-0.06f,-0.2f);
	glVertex2f(-spidera-0.09f,-0.35f);
	glEnd();
}
void drawGun()
{
	if(controlflag!=3)
		glPolygonMode(GL_FRONT_AND_BACK,GL_LINE);
	else
		glPolygonMode(GL_FRONT_AND_BACK,GL_LINES);
	glBegin(GL_QUADS);
	glVertex2f(guncenterside/2,guncenterside/2);
	glVertex2f(guncenterside/2,-1.5*guncenterside/2);
	glVertex2f(-guncenterside/2,-1.5f*guncenterside/2);
	glVertex2f(-guncenterside/2,guncenterside/2);
	glEnd();
	glBegin(GL_QUADS);
	glVertex2f(guntopbreadth/2,guncenterside/2);
	glVertex2f(guntopbreadth/2,guncenterside/2+guntoplength);
	glVertex2f(-guntopbreadth/2,guncenterside/2+guntoplength);
	glVertex2f(-guntopbreadth/2,guncenterside/2);
	glEnd();
	glBegin(GL_QUADS);
	glVertex2f(-gunsidebreadth-0.025f-guncenterside/2,gunsidelength);
	glVertex2f(-gunsidebreadth-0.025f-guncenterside/2,-gunsidelength);
	glVertex2f(-0.025f-guncenterside/2,-gunsidelength);
	glVertex2f(-0.025f-guncenterside/2,gunsidelength);
	glEnd();
	glBegin(GL_LINES);
	glVertex2f(-guncenterside/2,0.05f);
	glVertex2f(-guncenterside/2-0.025f,0.05f);
	glVertex2f(-guncenterside/2,-0.05f);
	glVertex2f(-guncenterside/2-0.025f,-0.05f);
	glEnd();
	glBegin(GL_QUADS);
	glVertex2f(gunsidebreadth+0.025f+guncenterside/2,gunsidelength);
	glVertex2f(gunsidebreadth+0.025f+guncenterside/2,-gunsidelength);
	glVertex2f(0.025f+guncenterside/2,-gunsidelength);
	glVertex2f(0.025f+guncenterside/2,gunsidelength);
	glEnd();
	glBegin(GL_LINES);
	glVertex2f(guncenterside/2,0.05f);
	glVertex2f(guncenterside/2+0.025f,0.05f);
	glVertex2f(guncenterside/2,-0.05f);
	glVertex2f(guncenterside/2+0.025f,-0.05f);
	glEnd();
	glPolygonMode(GL_FRONT_AND_BACK,GL_FILL);
}
void drawLaser()
{
	float thickness=5.0f;
	glLineWidth(thickness);
	glPolygonMode(GL_FRONT_AND_BACK,GL_LINES);
	glBegin(GL_LINES);
	glVertex2f(0.0f,lasercoord);
	glVertex2f(0.0f,lasercoord+0.4f);
	glEnd();
	glLineWidth(0.1f);
	glPolygonMode(GL_FRONT_AND_BACK,GL_FILL);
}
void drawSmiley()
{
	glBegin(GL_TRIANGLE_FAN);
	for(int i=0;i<360;i++)
	{
		glVertex2f(0.1*cos(DEG2RAD(i)),0.1*sin(DEG2RAD(i)));
	}
	glEnd();
}
void scoreDisplay(float posx,float posy,float posz,float space_char)
{
	int j=0,p,k;
	GLvoid *font_style1=GLUT_BITMAP_TIMES_ROMAN_24;
	p=score;
	glColor3f(1.0f,1.0f,1.0f);
	int fl=0;
	if(p<0)
	{
		p*=-1;
		fl=1;
	}
	k=0;
	while(p>9)
	{
		k=p%10;
		glRasterPos3f((posx-(j*space_char)),posy,posz);   
		glutBitmapCharacter(font_style1,48+k);
		j++;
		p/=10;
	}
	glRasterPos3f((posx-(j*space_char)),posy,posz);   
	glutBitmapCharacter(font_style1,48+p);
	if(fl==1)
	{
		glRasterPos3f((posx-(j*space_char)-0.2f),posy,posz);   
		glutBitmapCharacter(font_style1,'-');
	}
}
void DisplayEnd(float posx,float posy,float posz,float space_char)
{
	GLvoid *font_style1=GLUT_BITMAP_HELVETICA_18;
	glColor3f(1.0f,1.0f,1.0f);
	glRasterPos3f(posx,posy,posz);
	glutBitmapCharacter(font_style1,'!');
	posx-=space_char;
	glRasterPos3f(posx,posy,posz);
	glutBitmapCharacter(font_style1,'M');
	posx-=space_char;
	glRasterPos3f(posx,posy,posz);
	glutBitmapCharacter(font_style1,'O');
	posx-=space_char;
	glRasterPos3f(posx,posy,posz);
	glutBitmapCharacter(font_style1,'O');
	posx-=space_char;
	glRasterPos3f(posx,posy,posz);
	glutBitmapCharacter(font_style1,'B');
}

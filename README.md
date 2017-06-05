# arachnophobia

Arachnophobia is a Graphics game, totally built in C++ using [GLUT](https://www.opengl.org/resources/libraries/glut/). 

## Game Rules

In this game, you should collect green and red spiders in their respective baskets and shoot the blue ones. But beware! If any spider reaches the base, it blocks that area and you lose 5 points. Also, there will be high speed coins falling towards the base. Shoot those coins for bonus points! 

## Playing

In order to move the green basket, type `g` and use the arrow keys for motion or the mouse. Similarly, use `r` for the red
basket and `b` for the gun. A plus point of the gun is that you can rotate it. Any spider collected in the wrong basket or shot 
if not a blue spider, will give you a negative point. 

To quit the game, press `q` or `Esc`. If a spider lands on your gun, GAME OVER!

## Dependencies

- GCC
- GLUT - The OpenGL Utility Toolkit

## How to run? 

 > Before executing the commands below, make sure that you have [GLUT](https://www.opengl.org/resources/libraries/glut/) installed. 

To play the game, simply type the following commands in the console: 

```bash
make
./main
```  

## License

MIT 

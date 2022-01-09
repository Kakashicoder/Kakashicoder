# IT IS OLD STYLE MEATHOD FRO SIMPLE AND EASY GAME   
import turtle



wn = turtle.Screen()
wn.title('Ping-pong')
wn.bgcolor('black')
wn.setup(width=800 ,height=600)
wn.tracer(0)   # WHAT THAT DOES IS IT ACTUALLY STOPS THE WINDOW FROM UPDATING.
               # AND ALSO SPEED-UP THE GAME QUIT BETTER.



#SCORE
score_a = 0
score_b = 0

# PADDLE A
paddle_a = turtle.Turtle()
paddle_a.speed(0)                                 # THIS IS NOT A SPEED OF PADDLE THIS SPEED FOR ANIMATION OF PADDLE.
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # WE CAN SEE THAT THE SQUARE IS NOT PERFECT OF THIS GAME SO WE USE STRECTH 
paddle_a.penup()                                  # WHAT THEY DO IS THEY DRAW A LINE AS THEY'RE MOVING, WE DON'T NEED TO DRAW LINE, BECAUSE THAT'S NOT WHAT THIS PROGRAM DOES. SO WE DO THE PENUP
paddle_a.goto(-350, 0)                            # IN THE GAME LEFT SIDE OF THE PADDLE -350 AND RIGHT SIDE OF THE PADDLE IS 350 LIKE INTEGER TABEL  


#COPY ALL THE STATEMENT TO PADDLE_A TO PADDLE_B BECAUSE BOTH PADDLE ARE THE SAME IN THIS GAME 

# PADDLE B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  
paddle_b.penup() 
paddle_b.goto(350, 0)   # IN THE GAME THE LEFT SIDE OF THE PADDEL HAS +350 


# PEN

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()  # this is use hide something we only want to see text.
pen.goto(0, 260)
pen.write('Player A: 0   Player B: 0', align='center', font=('Courier', 24, 'normal'))  # This is score board.




# BALL
ball = turtle.Turtle()
ball.speed(0)  
ball.shape("circle")
ball.color("white")  
ball.penup() 
ball.goto(0, 0)         
ball.dx = 0.4        # I WANT TO SEPRATE THE BALL IS I WANT TO SEPRATE THE BALLS MOVEMENT INTO TWO PARTS X AND Y MOVEMENT DX AND DY. D MEANS DELTA OR CHANGE.
ball.dy = -0.4            # THAT'S MEAN IS EVRY TIME OUR BALL MOVES, IT MOVES BY TWO PIXEL SO SINCE X IS POSITIVE, IT'S GOING TO MOVE TO THE RIGHT TWO AND SINCE Y IS POSITIVE 
                        # IT'S GOING TO MOVE UP TO SO IT'D BE KIND OF MOVING UP AND DIAGONALLY TO GET THAT WE GOT TO MAIN GAME LOOP.


# FUNTIONS

def paddle_a_up():      # THE OBJECT WE CREATED HERE, WE CALL IT PADDLE A AND .YCOR MEATHOD IS FROM THE TURTLE
    y = paddle_a.ycor() # THAT DOES IS IT RETURN THE Y COORDINATE AND SO WE'RE ASSIGNING THE VALUE TO A VARIBLE CALLED Y
    y += 20             # I AM GOING TO GO UP ON THE SCREEN SO WHY INCREASE AS WE GO UP, IT DECRESS AS WE GO DOWN.
    paddle_a.sety(y)    # WE'VE JUST CALCULATED THE Y'S, THEN WHAT WE ACTUALLY HAVE TO DO IS PADDLE A ST Y TO THE NEW Y AND WE HAVE CALL THE FUNTION YET
                        

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
 
# KEYBOAR BINDING
 
wn.listen()                          # THIS TELL ITS TO LISTEN FOR KEYBOARD INPUT
wn.onkeypress(paddle_a_up, "w")      # IT TELLS THE PROGRAM TO LISTEN FOR KEYBOARD INPUT. THIS LINE SAYS, WHEN THE USER PRESSES W, CALL THE FUNCTION PADDLE_A_UP,
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")     #IF YOU USE ARROW KEYS INSTEAD OF WORD THEN UPPER ARROW = UP AND LOWER ARROW = DOWN.
wn.onkeypress(paddle_b_down, "Down")  





# MAIN GAME LOOP
while True:
    wn.update() #THAT DOES IS EVERY TIME THE LOOP RUN ITS UPDDATES THE SCREEN.

       
    # MOVE THE BALL  //  # COMBING WHAT I DO IN FUNCTION IN SINGLE LINE

    ball.setx(ball.xcor() + ball.dx) # THE BALL STARTS AT 00 SO 0x THE FIRST TIME THROUGH THIS LOOP, IT'S GOING 2 GO TO AN X TIMESTHE LOOP IS GONNA 2.
    ball.sety(ball.ycor() + ball.dy) # SOMEBODY FACES AN ERROR BECAUSE OF I USE FOUR SPACES BUT HERE, IT IS A TAB OKAY, YOU GOY TO USE THE SAME THING EACH TIME SO, I GOONA GO WITH FOUR SPACES,THAT'S ACTUALLY THE PREFERRED MEATHOD.

# BORDER CHECKING  
# [UPPER OR RIGHT SIDE = IN +] AND [IN LOWER OR LEFT SIDE = IN -]

                   # THIS IS FOR UPPER

    if ball.ycor() > 290: # SO IF THE Y CURRENT Y CORDINATE IS GREATER THAN 290 COLON.
        ball.sety(290)    # WE SET IT BACK TO 290.
        ball.dy *= -1     # WHAT THAT DOES IT REVERSE THE DIRECTION THE BALL OKAY. IF DY MINUS NEGATIVE ONE IS NEGATIVE TWO 
        
                   # THIS IS FOR LOWER
    
    if ball.ycor() < -290:
         ball.sety(-290)
         ball.dy *= -1 
         
               
                   # THIS IS FOR RIGHT SIDE
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()   # THIS IS FOR WHEN SCOREBOARD UPDATE THEY DIDNOT WRITE IT'S OWN BODY THEY UPDATE WHEN PREVIOUS SCORE IS ERASED.
        pen.write('Player A: {}   Player B: {}'.format(score_a, score_b) , align='center', font=('Courier', 24, 'normal'))
       

                   # THIS IS FOR LEFT SIDE

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write('Player A: {}   Player B: {}'.format(score_a, score_b) , align='center', font=('Courier', 24, 'normal')) # this is for updatating the scoreboard
       


#PADDLE AND BALL COLLISSIONz
                       # IF THAT IS A CASE, BASCICALLY, WE JUST WANT THE DX, SAME THING WE DID AT THE TOP TIMES EQUALS ONE OF THOSE IS X NAUGHT  NEGATIVE ONE, 
                       # BALL X COORDINATE GREATER THAN 340. THAT MEANS THE EDGES ARE BASCICALLY TOUCHING. AND IS IT BETWEEN THE TOP OF THE PADDLE AND THE BUTTOM OF THE PADDLE ACTUALLY USED TO BE 40 BECAUSE OF HTE SIZE OF THE BALL IS PROBABLY
    
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1 


    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1 
    
           

    
import random, os

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BALL_SIZE = 25

local_data = os.path.dirname(os.path.realpath(__file__))

class Ball:
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed_x = 0
        self.speed_y = 0
        self.color = 0
 
    def make_ball():
        ball = Ball()
        ball.x = random.randrange(BALL_SIZE, WINDOW_WIDTH - BALL_SIZE)
        ball.y = random.randrange(BALL_SIZE, WINDOW_HEIGHT - BALL_SIZE)
        ball.speed_x = random.choice([-5, -1, 1, 5])
        ball.speed_y = random.choice([-5, -1, 1, 5])
        ball.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        return ball

    def mov_collisions(ball):
        ball.x += ball.speed_x
        ball.y += ball.speed_y
        
        ### Collisions ###
        if (ball.y > WINDOW_HEIGHT - BALL_SIZE) or (ball.y < BALL_SIZE):
            ball.speed_y *= -1
        if (ball.x > WINDOW_WIDTH - BALL_SIZE) or (ball.x < BALL_SIZE):
            ball.speed_x *= -1
        
        return ball

def spawn_server():
    os.system('python ' + '"' + str(os.path.join(local_data, 'client.py')) + '"')

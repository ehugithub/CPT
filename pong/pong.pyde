import random


def setup():
    size(1366, 700)
    background(255)

location = PVector(683.0, 350.0)
velocity = PVector(0.0, 0.0)
keypress = [False] * 4
left = rightscore = 0
difficulty = 0
left_pos = right_pos = 300.0
new_game = button = display_rules = True
single_player = no_players = scoreboard = False


#displays the rules and allows user to choose game modes
def start_game():
    global new_game, single_player, difficulty, leftscore, rightscore
    global no_players, button, display_rules, scoreboard
    leftscore = rightscore = 0
    strokeCap(ROUND)
    strokeWeight(10)
    stroke(0)
    background(255)
    if display_rules:
        fill(128)
        rect(300, 50, 900, 500)
        fill(0)
        textSize(50)
        text('Rules', 600, 150)
        textSize(25)
        text('W and D control the red paddle\'s movement and left and \nright arrow keys control the blue paddle\'s movement', 355, 250)
        text('When the ball goes off the screen, the other side receives a point', 355, 350)
        text('The first side to score 10 points wins', 355, 400)
        text('Click anywhere to continue', 550, 450)
        if mousePressed:
            button = False
            display_rules = False
    if not single_player and not display_rules and not scoreboard:
        fill(128)
        rect(40, 370, 300, 100)
        rect(540, 370, 300, 100)
        rect(540, 570, 300, 100)
        rect(1040, 370, 300, 100)
        textSize(40)
        fill(0)
        text('Single Player', 80, 440)
        text('Multiplayer', 600, 440)
        text('No Players', 1100, 440)
        text('Scoreboard', 600, 640)
        textSize(100)
        text('Select Mode', 350, 300)

        if mousePressed and button and 470> mouseY > 370 and 340> mouseX > 40:
            single_player = True
            button = False
            background(255)
            delay(10)
        elif mousePressed and button and 470> mouseY > 370 and 840 > mouseX > 540:
            new_game = button = False
            velocity.set([10.0, 10.0])
        elif mousePressed and button and 670 > mouseY > 570 and 840 > mouseX > 540:
            button = False
            scoreboard = True
        elif mousePressed and button and 470 > mouseY > 370 and 1340 > mouseX > 1040:
            no_players = True
            new_game = button = False
            velocity.set([10.0, 10.0])
    if scoreboard:
        background(255)
        fill(128)
        rect(100, 600, 300, 100)
        fill(0)
        textSize(40)
        text('Back', 200, 660)
        if mousePressed and button and 700 > mouseY > 600 and 400 > mouseX > 100:
            button = scoreboard = False
    #if the single player mode was chosen, display the difficulty level of the bot
    if single_player:
        fill(0)
        textSize(100)
        text('Select Difficulty', 350, 300)
        fill(128)
        rect(40, 370, 300, 100)
        rect(540, 370, 300, 100)
        rect(1040, 370, 300, 100)
        rect(540, 570, 300, 100)
        textSize(40)
        fill(0)
        text('Easy', 140, 420)
        text('Medium', 600, 420)
        text('Hard', 1140, 420)
        text('Impossible', 580, 630)
        if mousePressed and button and 470 > mouseY > 370 and 340 > mouseX > 40:
            difficulty = 1
            new_game = button = False
            velocity.set([10.0, 10.0])
        elif mousePressed and button and 470 > mouseY > 370 and 840 > mouseX > 540:
            difficulty = 2
            new_game = button = False
            velocity.set([10.0, 10.0])
        elif mousePressed and button and 470 > mouseY > 370 and 1340 > mouseX > 1040:
            difficulty = 3
            new_game = button = False
            velocity.set([10.0, 10.0])
        elif mousePressed and button and 670 > mouseY > 570 and 840 > mouseX > 540:
            difficulty = 10
            new_game = button = False
            velocity.set([10.0, 10.0])


def score_point():
    global location
    location = PVector(width / 2, height / 2)
    velocity.x = 10.0
    velocity.y = 10.0
    delay(300)


def draw():
    global left_pos, right_pos, leftscore, rightscore, difficulty, single_player, new_game, button
    frameRate(100)
    background(255)

    if new_game:
        start_game()

    if leftscore == 10:
        fill(255, 0, 0)
        textSize(80)
        text('Red wins! Click to play again', 150, 330)
        velocity.set([0.0, 0.0])
        single_player = False
        if mousePressed and button:
            button = False
            new_game = True
    elif rightscore == 10:
        fill(0, 0, 255)
        textSize(80)
        text('Blue wins! Click to play again', 150, 330)
        velocity.set([0.0, 0.0])
        single_player = False
        if mousePressed and button:
            button = False
            new_game = True

    if velocity.x != 0:
        fill(0)
        textSize(150)
        text('{}     {}'.format(leftscore, rightscore), 450, 200)
        noStroke()
        #ball
        ellipse(location.x, location.y, 40, 40)
    location.add(velocity)

    #prevents paddles from going off screen
    left_pos = constrain(left_pos, 0, 500)
    right_pos = constrain(right_pos, 0, 500)

    if location.y > height - 20 or location.y < 20:
        velocity.y *= -1
    if location.x > width + 50:
        leftscore += 1
        score_point()
        left_pos = right_pos = 300
    elif location.x < -50:
        rightscore += 1
        score_point()
        left_pos = right_pos = 300

    #Paddles
    noStroke()
    fill(255, 0, 0)
    rect(10, left_pos, 15, 200)
    fill(0, 0, 255)
    rect(1341, right_pos, 15, 200)

    # collision detection
    if location.x > 1331 and location.y > right_pos and location.y < right_pos + 200 or location.x < 40 and location.y > left_pos and location.y < left_pos + 200:
        #makes ball go faster
        if velocity.x > 0:
            velocity.x += 0.25
        elif velocity.x < 0:
            velocity.x -= 0.25
        if velocity.y > 0:
            velocity.y += 0.25
        elif velocity.y < 0:
            velocity.y -= 0.25
        velocity.x *= -(random.uniform(0.9, 1.1))
        if location.x > 1331:
            location.x = 1331
        else:
            location.x = 40

    #controls paddle movement
    if keypress[0]:
        left_pos -= 10
    if keypress[1]:
        left_pos += 10
    if keypress[2]:
        right_pos -= 10
    if keypress[3]:
        right_pos += 10

    if single_player:
        if location.y > left_pos + 150:
            left_pos += difficulty * 5
        elif location.y < left_pos + 150:
            left_pos -= difficulty * 5

    if no_players:
        if location.x < 683:
            if location.y > left_pos + 150:
                left_pos += 10
            elif location.y < left_pos + 150:
                left_pos -= 10
        elif location.x > 683:
            if location.y > right_pos + 150:
                right_pos += 10
            elif location.y < right_pos + 150:
                right_pos -= 10


def mouseReleased():
    global button
    button = True


def keyPressed():
    if key == 'a':
        keypress[0] = True
    elif key == 'd':
        keypress[1] = True
    elif keyCode == LEFT:
        keypress[2] = True
    elif keyCode == RIGHT:
        keypress[3] = True


def keyReleased():
    if key == 'a':
        keypress[0] = False
    elif key == 'd':
        keypress[1] = False
    elif keyCode == LEFT:
        keypress[2] = False
    elif keyCode == RIGHT:
        keypress[3] = False

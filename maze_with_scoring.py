# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Super Easy Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (13, 100, 132)

#Fonts
MY_FONT = pygame.font.Font(None, 60)


# make walls
wall1 = [300, 275, 200, 25]
wall2 = [400, 450, 200, 25]
wall3 = [100, 100, 25, 200]
wall4 = [700, 300, 25, 200]
wall5 = [50, 400, 200, 25]
wall6 = [50, 400, 25, 200]
wall7 = [500, 150, 200, 25]

walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7]

# Make coins
coin1 = [300, 500, 25, 25]
coin2 = [400, 200, 25, 25]
coin3 = [150, 150, 25, 25]
coin4 = [500, 300, 25, 25]
coin5 = [74.5, 350, 25, 25]
coin6= [98, 430, 25, 25]

coins = [coin1, coin2, coin3, coin4, coin5, coin6]


# Sound
coinsound = pygame.mixer.Sound("Sound(s)/coin_sound.ogg")
timersound = pygame.mixer.Sound("Sound(s)/timer_sound.ogg")


# stages
START = 0
PLAYING = 1
END = 2
PAUSE = 3


def setup():
    global player1, vel1, score1, player2, vel2, score2, player3, vel3, score3, coins, stage, time_remaining, ticks
    
    player1 = [200, 150, 25, 25]
    vel1 = [0, 0]
    score1 = 0

    player2 = [300, 400, 25, 25]
    vel2 = [0, 0]
    score2 = 0

    player3 = [657, 264, 25, 25]
    vel3 = [0, 0]
    score3 = 0

    coins = [coin1, coin2, coin3, coin4, coin5, coin6]
    
    stage= START
    time_remaining = 15
    ticks = 0


# Game loop
setup()
win = 0
done = False
timersound.play()

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:

            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
                    
            elif stage == PLAYING:
                if event.key == pygame.K_SPACE:
                    stage = PAUSE

            elif stage == PAUSE:
                if event.key == pygame.K_SPACE:
                    stage == PLAYING
                    
            elif stage == END:
                if event.key == pygame.K_SPACE:
                    setup()
                    


    if PLAYING:
        
        pressed = pygame.key.get_pressed()

        up1 = pressed[pygame.K_UP]
        down1 = pressed[pygame.K_DOWN]
        left1 = pressed[pygame.K_LEFT]
        right1 = pressed[pygame.K_RIGHT]
        
        if left1:
            vel2[0] = -5
        elif right1:
            vel2[0] =  5
        else:
            vel2[0] = 0
            
        if up1:
            vel2[1] = -5
        elif down1:
            vel2[1] = 5
        else:
            vel2[1] = 0


        up2 = pressed[pygame.K_w]
        down2 = pressed[pygame.K_s]
        left2 = pressed[pygame.K_a]
        right2 = pressed[pygame.K_d]

        if left2:
            vel1[0] = -5
        elif right2:
            vel1[0] = 5
        else:
            vel1[0] = 0
            
        if up2:
            vel1[1] = -5
        elif down2:
            vel1[1] = 5
        else:
            vel1[1] = 0


        up3 = pressed[pygame.K_KP8]
        down3 = pressed[pygame.K_KP2]
        left3 = pressed[pygame.K_KP4]
        right3 = pressed[pygame.K_KP6]
        222
        if left3:
            vel3[0] = -5
        elif right3:
            vel3[0] =  5
        else:
            vel3[0] = 0
            
        if up3:
            vel3[1] = -5
        elif down3:
            vel3[1] = 5
        else:
            vel3[1] = 0


    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''
    player1[0] += vel1[0]
    player2[0] += vel2[0]
    player3[0] += vel3[0]
            
    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player1, w):        
            if vel1[0] > 0:
                player1[0] = w[0] - player1[2]
            elif vel1[0] < 0:
                player1[0] = w[0] + w[2]

        if intersects.rect_rect(player2, w):        
            if vel2[0] > 0:
                player2[0] = w[0] - player2[2]
            elif vel2[0] < 0:
                player2[0] = w[0] + w[2]

        if intersects.rect_rect(player3, w):        
            if vel3[0] > 0:
                player3[0] = w[0] - player3[2]
            elif vel3[0] < 0:
                player3[0] = w[0] + w[2]

    ''' move the player in vertical direction '''
    player1[1] += vel1[1]
    player2[1] += vel2[1]
    player3[1] += vel3[1]
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player1, w):                    
            if vel1[1] > 0:
                player1[1] = w[1] - player1[3]
            if vel1[1]< 0:
                player1[1] = w[1] + w[3]

        if intersects.rect_rect(player2, w):                    
            if vel2[1] > 0:
                player2[1] = w[1] - player2[3]
            if vel2[1]< 0:
                player2[1] = w[1] + w[3]

        if intersects.rect_rect(player3, w):                    
            if vel3[1] > 0:
                player3[1] = w[1] - player3[3]
            if vel3[1]< 0:
                player3[1] = w[1] + w[3]


    ''' here is where you should resolve player collisions with screen edges '''
    if player1[1] < -(player1[3]):
        player1[1] = HEIGHT + 1
    if player1[1] > HEIGHT + 1:
        player1[1] = -(player1[3])

    if player1[0] < -(player1[2]):
        player1[0] = WIDTH + 1
    if player1[0] > WIDTH + 1:
        player1[0] = -(player1[2])


    if player2[1] < -(player2[3]):
        player2[1] = HEIGHT + 1
    if player2[1] > HEIGHT + 1:
        player2[1] = -(player2[3])

    if player2[0] < -(player2[2]):
        player2[0] = WIDTH + 1
    if player2[0] > WIDTH + 1:
        player2[0] = -(player2[2])

    if player3[1] < -(player3[3]):
        player3[1] = HEIGHT + 1
    if player3[1] > HEIGHT + 1:
        player3[1] = -(player3[3])

    if player3[0] < -(player3[2]):
        player3[0] = WIDTH + 1
    if player3[0] > WIDTH + 1:
        player3[0] = -(player3[2])


    ''' get the coins '''
    hit_list1 = []
    hit_list2 = []
    hit_list3 = []
    
    hit_list1 = [c for c in coins if intersects.rect_rect(player1, c)]
    
    for hit in hit_list1 :
        coins.remove(hit)
        score1 += 1
        coinsound.play()
        
    hit_list2 = [c for c in coins if intersects.rect_rect(player2, c)]

    for hit in hit_list2 :
        coins.remove(hit)
        score2 += 1
        coinsound.play()

    hit_list3 = [c for c in coins if intersects.rect_rect(player3, c)]
    
    for hit in hit_list3 :
        coins.remove(hit)
        score3 += 1
        coinsound.play()
        
    # Winning Situations
    if len (coins) == 0:
        if score1 > score2:
            win = 1
        elif score2 > score1:
            win = 2
        else:
            win = 3

        stage = END

    ''' timer stuff '''
    if stage == PLAYING:
        ticks += 1

        if ticks % refresh_rate == 0:
            time_remaining -= 1

        if time_remaining == 0:
            stage = END
            
        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, player1)
    
    pygame.draw.rect(screen, GREEN, player2)

    pygame.draw.rect(screen, BLUE, player3)

    
    for w in walls:
        pygame.draw.rect(screen, RED, w)

    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)

    if stage == END:
        font = pygame.font.Font(None, 48)
        
        if score1 > score2:
            text = font.render("Player 1 Wins!", True, WHITE)
            screen.blit(text, [300, 100])
                
        elif score2 > score1:
            text = font.render("Player 2 Wins!", True, GREEN)
            screen.blit(text, [300, 100])

        elif score3 > score1:
            text = font.render("Player 3 Wins!", True, BLUE)
            screen.blit(text, [300, 100])
            
        else:
            text = font.render("DRAW", 1, RED)
            screen.blit(text, [350, 100])


    # Score
    font = pygame.font.Font(None, 36)
    score_text1 = font.render("P1 Score: " + str(score1), 1, WHITE)
    screen.blit(score_text1, [10, 25])

    font = pygame.font.Font(None, 36)
    score_text2 = font.render("P2 Score: " + str(score2), 1, GREEN)
    screen.blit(score_text2, [650, 25])

    font = pygame.font.Font(None, 36)
    score_text3 = font.render("P3 Score: " + str(score3), 1, BLUE)
    screen.blit(score_text3, [350, 25])
    
    ''' timer text '''
    timer_text = MY_FONT.render(str(time_remaining), True, WHITE)
    screen.blit(timer_text, [50, 50])


    ''' begin game text '''
    if stage == START:
        text1 = MY_FONT.render("Block", True, WHITE)
        text2 = MY_FONT.render("(Press SPACE to play.)", True, WHITE)
        screen.blit(text1, [350, 150])
        screen.blit(text2, [225, 200])
        
    elif stage == END:
        text1 = MY_FONT.render("Game Over", True, WHITE)
        text2 = MY_FONT.render("(Press SPACE to restart.)", True, WHITE)
        screen.blit(text1, [310, 150])
        screen.blit(text2, [210, 200])
        
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()

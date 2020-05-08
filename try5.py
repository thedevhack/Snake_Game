import pygame
import random
import time

def basic_defaults():
    pygame.init()
    snake_x = 200
    snake_y = 175
    font_for_game_title = pygame.font.Font(None, 36)
    screen = pygame.display.set_mode((800, 600))  # Making Screen for the game
    screen.blit(font_for_game_title.render("Snake Game", True, (0, 255, 255)), (300, 10))  # Making title appear
    Clock = pygame.time.Clock()
    x = 2
    counter = 0
    score = 0
    coordins = []
    eaten = 0
    return screen, snake_x, snake_y, Clock, x, counter, score, coordins, eaten


def snake_movements(x):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                x = 1
            elif event.key == pygame.K_DOWN:
                x = 2
            elif event.key == pygame.K_LEFT:
                x = 3
            elif event.key == pygame.K_RIGHT:
                x = 4
            else:
                pass
    return x

def food():
    food_x = random.randint(20, 780)
    food_y = random.randint(20, 280)
    return food_x, food_y


def game_loop():
    screen, snake_x, snake_y, clocko, x, counter, score, coordins, eaten = basic_defaults()
    running = True
    while (running):

        # for moving of snake in the game [code starts]

        screen.fill((0, 0, 0))
        x = snake_movements(x)
        if x == 1:
            snake_y -= 20
        elif x == 2:
            snake_y += 20
        elif x == 3:
            snake_x -= 20
        elif x == 4:
            snake_x += 20
        pygame.draw.rect(screen, (102, 255, 51), (snake_x, snake_y, 10, 10), 0)

        # for moving of snake in the game [code ends]

        # for food appering and disappearing after certain amount of time[code starts]

        timesec = 35  # in secs
        if (counter) % timesec == 0:
            food_x, food_y = food()
        else:
            pass
        pygame.draw.rect(screen, (0, 255, 255), (food_x, food_y, 11, 11), 0)
        counter += 1

        # for food appering and disappearing after certain amount of time[code ends]

        # for detecting snake is eating food or not [code starts]

        if snake_x + 10 >= food_x and snake_x + 10 <= food_x + 10 and snake_y >= food_y and snake_y <= food_y + 10:
            food_x, food_y = food()
            counter = 1
            score += 1
            eaten = 1
        elif snake_x >= food_x and snake_x <= food_x + 10 and snake_y >= food_y and snake_y <= food_y + 10:
            food_x, food_y = food()
            counter = 1
            score += 1
            eaten = 1
        elif snake_x >= food_x and snake_x <= food_x + 10 and snake_y + 10 >= food_y and snake_y + 10 <= food_y + 10:
            food_x, food_y = food()
            counter = 1
            score += 1
            eaten = 1

        elif snake_x + 10 >= food_x and snake_x + 10 <= food_x + 10 and snake_y + 10 >= food_y and snake_y + 10 <= food_y + 10:
            food_x, food_y = food()
            counter = 1
            score += 1
            eaten = 1

        else:
            eaten = 0
            pass

        # for detecting snake is eating food or not [code ends]

        # to determine boundaries for snake to not go beyond [code starts]

        if snake_x > 790 or snake_x < 0:
            running = False
        if snake_y < 0 or snake_y > 590:
            running = False

        # to determine boundaries for snake to not go beyond [code ends]

        # code to calculate score [code starts]

        font_for_score = pygame.font.Font(None, 25)
        screen.blit(font_for_score.render("Score: ", True, (0, 147, 255)), (645, 10))
        screen.blit(font_for_score.render(str(score), True, (0, 147, 255)), (705, 10))

        # code to calculate score [code ends]

        # code to extend tail of snake [code starts]
        if eaten == 1:
            coordins = []
            for i in range(score + 1):
                coordins.append("None")
        if score > 0:
            rangers = score + 1
            pos = (counter - 1) % rangers
            coordins[pos] = [snake_x, snake_y]
            for i in coordins:
                if i == "None":
                    pass
                else:
                    snake_xo = i[0]
                    snake_yo = i[1]
                    pygame.draw.rect(screen, (102, 255, 51), (snake_xo, snake_yo, 10, 10), 0)

        # code to extend tail of snake [code ends]

        # code to derect a collisio of snake with its tail [code starts]

        if score == 1:
            if coordins[0] == coordins[1]:
                print("Collision 1")
                running = False
        else:
            for j in range(1, score):
                if coordins[j] == "None":
                    pass
                else:
                    if coordins [0] == coordins[j]:
                        print("Collision")
                        running = False
                    else:
                        pass

        # code to detect a collision of snake with its tail [code ends]

        pygame.display.update()
        time.sleep(1)
        clocko.tick(30)


game_loop()
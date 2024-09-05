import pygame as py
import os
import random as rd

py.init()

Width = 400
Height = 700

Screen = py.display.set_mode((Width, Height))

title_name  = 'Rocket'
py.display.set_caption(title_name)

icon_image = os.path.join('Asset', 'Picture', 'booster.png')
icon_image = py.image.load(icon_image)
py.display.set_icon(icon_image)

start_img = os.path.join('Asset', 'Picture', 'Play_Button.png')
start_img = py.image.load(start_img).convert_alpha()
start_img = py.transform.scale(start_img, (220, 105))

reset_img = os.path.join('Asset', 'Picture', 'Reset_Button.png')
reset_img = py.image.load(reset_img).convert_alpha()
reset_img = py.transform.scale(reset_img, (180, 80))

exit_img = os.path.join('Asset', 'Picture', 'Exit_Button.png')
exit_img = py.image.load(exit_img).convert_alpha()
exit_img = py.transform.scale(exit_img, (180, 80))

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw(self):
        action = False
        pos = py.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if py.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if py.mouse.get_pressed()[0] == 0:
            self.clicked = False
        Screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

start_button = Button(90, 350, start_img)
reset_button = Button(110, 350, reset_img)
exit_button = Button(110, 475, exit_img)

background_image = os.path.join('Asset', 'Picture', 'rocket_background.jpg')
background_image = py.image.load(background_image)
background_image = py.transform.scale(background_image, (Width, Height))

game_page_background = os.path.join('Asset', 'Picture', 'Game_Page.png')
game_page_background = py.image.load(game_page_background)
game_page_background = py.transform.scale(game_page_background, (Width, Height))

star_image = os.path.join('Asset', 'Picture', 'star.png')
star_image = py.image.load(star_image)
star_image = py.transform.scale(star_image, (40, 40))

meteor_image = os.path.join('Asset', 'Picture', 'meteor.png')
meteor_image = py.image.load(meteor_image)
meteor_image = py.transform.scale(meteor_image, (50, 50))
meteor_image = py.transform.rotate(meteor_image, 45)

rocket_image = os.path.join('Asset', 'Picture', 'rocket.png')
rocket_image = py.image.load(rocket_image)
rocket_image = py.transform.scale(rocket_image, (70, 70))
rocket_image = py.transform.rotate(rocket_image, 45)

background_sound = os.path.join('Asset', 'Music','Rocket_music.mp3')
py.mixer.music.load(background_sound)
py.mixer.music.set_volume(0.5)
py.mixer.music.play(-1)

star_effect = os.path.join('Asset', 'Music', 'star_effect.wav')
star_effect = py.mixer.Sound(star_effect)
star_effect.set_volume(1.0)

meteor_effect = os.path.join('Asset', 'Music', 'meteor_effect.wav')
meteor_effect = py.mixer.Sound(meteor_effect)
meteor_effect.set_volume(1.0)

star_xpos = rd.randint(20, 380)
star_ypos = rd.randint(-200, -100)

meteor_xpos = rd.randint(20, 380)
meteor_ypos = rd.randint(-200, -100)

rocket_xpos = 200
rocket_ypos = 575

FPS = 60
Clock = py.time.Clock()

Score = 0
Score_List = [0]

Time = 60 * FPS
Show_time = 5 * FPS

star_hit = 0
meteor_hit = 0

Running = True
game_page = True
indroduce_page = False
game_over = False

White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)

Font = py.font.SysFont('fredoka one', 30)
Font1 = py.font.SysFont('fredoka one', 50)
Font2 = py.font.SysFont('fredoka one', 75)
Font3 = py.font.SysFont('fredoka one', 100)

def Score_message(score, colour, xpos, ypos):
    font_text = Font.render(f'Score: {score}', True, colour)
    Font_Width = font_text.get_width()
    Screen.blit(font_text, [(xpos - Font_Width) / 2, ypos])

def Timer_message(time, colour, xpos, ypos):
    seconds = time // FPS
    font_text = Font.render(f'Time: {seconds}', True, colour)
    Font_Width = font_text.get_width()
    Screen.blit(font_text, [(xpos - Font_Width) / 2, ypos])

def Game_title(colour, xpos, ypos):
    font_text = Font2.render('Rocket Game', True, colour)
    Font_Width = font_text.get_width()
    Screen.blit(font_text, [(xpos - Font_Width) / 2, ypos])

def Game_over_message(colour, xpos, ypos):
    font_text = Font2.render('Game Over', True, colour)
    Font_Width = font_text.get_width()
    Screen.blit(font_text, [(xpos - Font_Width) / 2, ypos])

def Game_over_score(score, colour, xpos, ypos):
    font_text = Font1.render(f'Score: {score}', True, colour)
    Font_Width = font_text.get_width()
    Screen.blit(font_text, [(xpos - Font_Width) / 2, ypos])

def Show_score_message(score, colour, xpos, ypos):
    font_text = Font.render(f'+{score}', True, colour)
    Font_Width = font_text.get_width()
    Screen.blit(font_text, [xpos, ypos])

def High_score_screen (colour, score, xpos, ypos):
    font_text = Font1.render(f'New High Score: {score}!', True, colour)
    Font_Width = font_text.get_width()
    Screen.blit(font_text, [(xpos-Font_Width)/2, ypos])

def Old_high_score (colour, score, xpos, ypos):
    font_text = Font1.render(f'High Score: {score}', True, colour)
    Font_Width = font_text.get_width()
    Screen.blit(font_text, [(xpos-Font_Width)/2, ypos])

def Game_over_message1(colour, xpos, ypos):
    font_text = Font1.render('Game Over', True, colour)
    Font_Width = font_text.get_width()
    Screen.blit(font_text, [(xpos - Font_Width) / 2, ypos])

def Introduce_message(colour, xpos, ypos):
    font_text = Font2.render('How To Play', True, colour)
    Font_Width = font_text.get_width()
    Screen.blit(font_text, [(xpos - Font_Width) / 2, ypos])

def Introduce_message1(colour, xpos, ypos):
    font_text = Font.render('1. Use arrow LEFT and RIGHT to move', True, colour)
    Font_Width = font_text.get_width()
    Screen.blit(font_text, [(xpos - Font_Width) / 2, ypos])

def Introduce_message2(colour, xpos, ypos):
    font_text = Font.render('2. Get many star as possible', True, colour)
    Font_Width = font_text.get_width()
    Screen.blit(font_text, [(xpos - Font_Width) / 2, ypos])

def Introduce_message3(colour, xpos, ypos):
    font_text = Font.render('3. Dodge all the meteors', True, colour)
    Font_Width = font_text.get_width()
    Screen.blit(font_text, [(xpos - Font_Width) / 2, ypos])

def Introduce_message4(colour, xpos, ypos):
    font_text = Font1.render('Good Luck!', True, colour)
    Font_Width = font_text.get_width()
    Screen.blit(font_text, [(xpos - Font_Width) / 2, ypos])

def Countdown_message(count, colour, xpos, ypos):
    font_text = Font3.render(str(count), True, colour)
    Font_Width = font_text.get_width()
    Screen.blit(font_text, [(xpos - Font_Width) / 2, ypos])

last_hit_time = None
show_message_duration = 2 * FPS

countdown_time = 3

while Running:
    while game_page:
        Screen.blit(game_page_background, [0, 0])
        Game_title(White, Width, 150)
        if start_button.draw():
            game_page = False
            game_over = False
            indroduce_page = True
            Calculate_page = False
            High_score_page = False
            countdown_start_ticks = py.time.get_ticks()
        if exit_button.draw():
            Running = False
            game_page = False
        py.display.flip()

        for event in py.event.get():
            if event.type == py.QUIT:
                Running = False
                game_page = False
    
    while indroduce_page:
        Screen.blit(background_image, [0, 0])
        Introduce_message(White, Width, 100)
        Introduce_message1(White, Width, 300)
        Introduce_message2(White, Width, 350)
        Introduce_message3(White, Width, 400)
        Introduce_message4(White, Width, 500)   

        countdown_seconds = countdown_time - (py.time.get_ticks() - countdown_start_ticks) // 1000

        if countdown_seconds > 0:
            Countdown_message(countdown_seconds, Red, Width, 550)
        else:
            game_page = False
            game_over = False
            indroduce_page = False
            Calculate_page = False
            High_score_page = False
        py.display.flip()

        for event in py.event.get():
            if event.type == py.QUIT:
                Running = False
                indroduce_page = False

    while game_over:
        Screen.blit(game_page_background, [0, 0])
        Game_over_message(Red, Width, 150)
        Game_over_score(Score, Red, Width, 200)
        Old_high_score(Red, Score_List[0], Width, 240)
        if reset_button.draw():
            rocket_xpos = 200
            rocket_ypos = 575
            FPS = 60
            Score = 0
            Time = 60 * FPS
            Hit = 0
            Running = True
            game_page = False
            game_over = False
            indroduce_page = True
            Calculate_page = False
            High_score_page = False
            star_xpos = rd.randint(20, 380)
            star_ypos = rd.randint(-200, -150)
            meteor_xpos = rd.randint(20, 380)
            meteor_ypos = rd.randint(-200, -150)
            countdown_start_ticks = py.time.get_ticks()
        if exit_button.draw():
            Running = False
            game_over = False
        py.display.update()

        for event in py.event.get():
            if event.type == py.QUIT:
                Running = False
                game_page = False
                game_over = False
                indroduce_page = False
                Calculate_page = False
                High_score_page = False

    while High_score_page == True:
        Screen.blit(game_page_background, [0, 0])
        High_score_screen(Red, Score, Width, 150)
        Game_over_message1(Red, Width, 200)
        if reset_button.draw():
            rocket_xpos = 200
            rocket_ypos = 575
            FPS = 60
            Score = 0
            Time = 60 * FPS
            Hit = 0
            Running = True
            game_page = False
            game_over = False
            indroduce_page = True
            Calculate_page = False
            High_score_page = False
            star_xpos = rd.randint(20, 380)
            star_ypos = rd.randint(-200, -150)
            meteor_xpos = rd.randint(20, 380)
            meteor_ypos = rd.randint(-200, -150)
            countdown_start_ticks = py.time.get_ticks()
        if exit_button.draw():
            Running = False
            game_page = False
            game_over = False
            indroduce_page = False
            Calculate_page = False
            High_score_page = False
        py.display.update()

        for event in py.event.get():
            if event.type == py.QUIT:
                Running = False
                High_score_page = False

    while Calculate_page == True:
        High_score = Score_List[0]
        if Score > High_score:
            Calculate_page = False
            High_score_page = True
            Score_List[0] = Score
        else:
            Calculate_page = False
            game_over = True

    if Time > 0:
        star_hit = 0
        meteor_hit = 0
        keys = py.key.get_pressed()
        rocket_width = 70

        for event in py.event.get():
            if event.type == py.QUIT:
                Running = False
        
        if keys[py.K_a] or keys[py.K_LEFT]:
            rocket_xpos -= 8
            if rocket_xpos < 0:
                rocket_xpos = 0

        elif keys[py.K_d] or keys[py.K_RIGHT]:
            rocket_xpos += 8
            if rocket_xpos > Width - rocket_width:
                rocket_xpos = Width - rocket_width

        if star_ypos >= Height:
            star_ypos = rd.randint(-200, -150)
            star_xpos = rd.randint(40, 350)
        else:
            star_ypos += 10

        if meteor_ypos >= Height:
            meteor_ypos = rd.randint(-200, -150)
            meteor_xpos = rd.randint(40, 350)
        else:
            meteor_ypos += 10

        min_y = int(rocket_ypos)
        max_y = int(rocket_ypos + 60)

        min_x = int(rocket_xpos)
        max_x = int(rocket_xpos + 60)

        if star_ypos in range(min_y, max_y):
            if star_xpos in range(min_x, max_x):
                if star_hit == 0:
                    star_ypos = rd.randint(-200, -150)
                    star_xpos = rd.randint(40, 350)
                    Hit = 1
                    score = rd.randint(1, 6)
                    print(f'Add: {score}')
                    Score += score
                    last_hit_time = py.time.get_ticks()
                    star_effect.play()
                    print(f'Score: {Score}')

        if meteor_ypos in range(min_y, max_y):
            if meteor_xpos in range(min_x, max_x):
                meteor_effect.play()
                Calculate_page = True
                print('Game Over')

        Time -= 1

        Screen.blit(background_image, [0, 0])
        Screen.blit(meteor_image, [meteor_xpos, meteor_ypos])
        Screen.blit(star_image, [star_xpos, star_ypos])
        Screen.blit(rocket_image, [rocket_xpos, rocket_ypos])
        Score_message(Score, White, Width, 5)
        Timer_message(Time, White, Width, 35)


        if last_hit_time is not None:
            current_time = py.time.get_ticks()
            if current_time - last_hit_time < show_message_duration:
                Show_score_message(score, White, rocket_xpos, rocket_ypos - 40)
            else:
                last_hit_time = None

        Clock.tick(FPS)
        py.display.update()

    else:
        Calculate_page = True

py.quit()

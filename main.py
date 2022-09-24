class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(WINDOWGEOMETRY, pygame.SCALED)
        self.clock = pygame.time.Clock()
        self.player_data = open("assets\\data\\player.dat", "r")

        self.player = player["down"]
        self.player_size = self.player.get_rect().size
        self.player_width = self.player_size[0]
        self.player_height = self.player_size[1]
        self.player_x_pos = 38
        self.player_y_pos = 32

        self.player_light = player["light"]
        self.player_light_size = self.player_light.get_rect().size
        self.player_light_width = self.player_light_size[0]
        self.player_light_height = self.player_light_size[1]
        self.player_light_x_pos = -462
        self.player_light_y_pos = -231

        self.font = pygame.font.Font("assets\\fonts\\NeoDunggeunmoPro-Regular.ttf", 32)

        pygame.display.set_caption(WINDOWCAPTION)
        pygame.display.set_icon(WINDOWICON)

    def check_slide_map(self):
        if self.player_x_pos >= 390:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                self.to_x = 0
                self.screen_to_x -= 2
                if self.screen_to_x < -512:
                    self.to_x = 2
                    self.screen_to_x += 2
                if self.player_x_pos >= 458: # checking whether player is colliding to a wall.
                    self.to_x = 0
        if self.player_y_pos >= 170:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                self.to_y = 0
                self.screen_to_y -= 2
                if self.screen_to_y < -288:
                    self.to_y = 2
                    self.screen_to_y += 2
                if self.player_y_pos >= 201:
                    self.to_y = 0
        if self.player_y_pos <= 63:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.to_y = 0
                self.screen_to_y += 2
                if self.screen_to_y > 0:
                    self.to_y = -2
                    self.screen_to_y -= 2
                if self.player_y_pos <= 32:
                    self.to_y = 0
        if self.player_x_pos <= 100:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.to_x = 0
                self.screen_to_x += 2
                if self.screen_to_x > 0:
                    self.to_x = -2
                    self.screen_to_x -= 2
                if self.player_x_pos <= 32:
                    self.to_x = 0

    def draw_game_board_for_tutorial(self):
        self.time = int(pygame.time.get_ticks()/1000) # 나중에 시간 바꿀 것
        
        self.draw_time = self.font.render(str(self.time), True, (127, 127, 127))

    def ending(self):
        while True: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.blit(ui["ending"], (0, 0))

            click = pygame.mouse.get_pressed()
            mx, my = pygame.mouse.get_pos()

            if mx >= 184 and mx <= 333:
                if my >= 177 and my <= 208:
                    if click[0] == True:
                        pygame.quit()
                        sys.exit()

            self.clock.tick() / 1000

            pygame.display.update()

    def tutorial1(self):
        self.to_x = 0
        self.to_y = 0

        self.screen_to_x = 0
        self.screen_to_y = 0

        self.player_x_pos = 38
        self.player_y_pos = 32
        self.player_light_x_pos = -462
        self.player_light_y_pos = -231
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player = player["up"]
                        self.to_y -= 2
                    elif event.key == pygame.K_LEFT:
                        self.player = player["left"]
                        self.to_x -= 2
                    elif event.key == pygame.K_DOWN:
                        self.player = player["down"]
                        self.to_y += 2
                    elif event.key == pygame.K_RIGHT:
                        self.player = player["right"]
                        self.to_x += 2
                    elif event.key == pygame.K_1:
                        self.tutorial1()
                    elif event.key == pygame.K_2:
                        self.tutorial2()
                    elif event.key == pygame.K_3:
                        self.tutorial3()
                    elif event.key == pygame.K_4:
                        self.tutorial4()
                    elif event.key == pygame.K_5:
                        self.tutorial5()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.to_x = 0
                    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.to_y = 0

            self.check_slide_map()
            self.draw_game_board_for_tutorial()

            if self.player_x_pos >= 439:
                if self.player_y_pos >= 192:
                    sound = pygame.mixer.Sound("assets\\audios\\stage_up.wav")
                    sound.set_volume(0.3)
                    sound.play() 
                    self.tutorial2()

            self.player_x_pos += self.to_x
            self.player_y_pos += self.to_y
            self.player_light_x_pos += self.to_x
            self.player_light_y_pos += self.to_y

            self.screen.blit(level["tutorial"][1], (self.screen_to_x, self.screen_to_y))
            self.screen.blit(level["tutorial"]["wall"], (self.screen_to_x, self.screen_to_y))

            self.screen.blit(player["light"], (self.player_light_x_pos, self.player_light_y_pos)) 
            self.screen.blit(self.player, (self.player_x_pos, self.player_y_pos))

            self.screen.blit(ui["playing_screen"], (0, 0))
            self.screen.blit(self.draw_time, (290, 8))

            self.clock.tick() / 1000

            self.player_data.close()

            pygame.display.update()

    def tutorial2(self):
        self.to_x = 0
        self.to_y = 0

        self.screen_to_x = 0
        self.screen_to_y = 0

        self.player_x_pos = 38
        self.player_y_pos = 32
        self.player_light_x_pos = -462
        self.player_light_y_pos = -231
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player = player["up"]
                        self.to_y -= 2
                    elif event.key == pygame.K_LEFT:
                        self.player = player["left"]
                        self.to_x -= 2
                    elif event.key == pygame.K_DOWN:
                        self.player = player["down"]
                        self.to_y += 2
                    elif event.key == pygame.K_RIGHT:
                        self.player = player["right"]
                        self.to_x += 2
                    elif event.key == pygame.K_1:
                        self.tutorial1()
                    elif event.key == pygame.K_2:
                        self.tutorial2()
                    elif event.key == pygame.K_3:
                        self.tutorial3()
                    elif event.key == pygame.K_4:
                        self.tutorial4()
                    elif event.key == pygame.K_5:
                        self.tutorial5()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.to_x = 0
                    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.to_y = 0

            self.check_slide_map()
            self.draw_game_board_for_tutorial()

            if self.player_x_pos >= 439:
                if self.player_y_pos >= 192:
                    sound = pygame.mixer.Sound("assets\\audios\\stage_up.wav")
                    sound.set_volume(0.3)
                    sound.play()
                    self.tutorial3()

            self.player_x_pos += self.to_x
            self.player_y_pos += self.to_y
            self.player_light_x_pos += self.to_x
            self.player_light_y_pos += self.to_y

            self.screen.blit(level["tutorial"][2], (self.screen_to_x, self.screen_to_y))
            self.screen.blit(level["tutorial"]["wall"], (self.screen_to_x, self.screen_to_y))
            self.screen.blit(level["tutorial"]["2_wall"], (self.screen_to_x, self.screen_to_y))

            self.screen.blit(player["light"], (self.player_light_x_pos, self.player_light_y_pos)) 
            self.screen.blit(self.player, (self.player_x_pos, self.player_y_pos))

            self.screen.blit(ui["playing_screen"], (0, 0))
            self.screen.blit(self.draw_time, (290, 8))

            self.clock.tick() / 1000

            self.player_data.close()

            pygame.display.flip()

    def tutorial3(self):
        self.to_x = 0
        self.to_y = 0

        self.screen_to_x = 0
        self.screen_to_y = 0

        self.player_x_pos = 38
        self.player_y_pos = 32
        self.player_light_x_pos = -462
        self.player_light_y_pos = -231
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player = player["up"]
                        self.to_y -= 2
                    elif event.key == pygame.K_LEFT:
                        self.player = player["left"]
                        self.to_x -= 2
                    elif event.key == pygame.K_DOWN:
                        self.player = player["down"]
                        self.to_y += 2
                    elif event.key == pygame.K_RIGHT:
                        self.player = player["right"]
                        self.to_x += 2
                    elif event.key == pygame.K_1:
                        self.tutorial1()
                    elif event.key == pygame.K_2:
                        self.tutorial2()
                    elif event.key == pygame.K_3:
                        self.tutorial3()
                    elif event.key == pygame.K_4:
                        self.tutorial4()
                    elif event.key == pygame.K_5:
                        self.tutorial5()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.to_x = 0
                    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.to_y = 0

            self.check_slide_map()
            self.draw_game_board_for_tutorial()

            if self.player_x_pos >= 439:
                if self.player_y_pos >= 192:
                    sound = pygame.mixer.Sound("assets\\audios\\stage_up.wav")
                    sound.set_volume(0.3)
                    sound.play()
                    self.tutorial4()

            self.player_x_pos += self.to_x
            self.player_y_pos += self.to_y
            self.player_light_x_pos += self.to_x
            self.player_light_y_pos += self.to_y

            self.screen.blit(level["tutorial"][1], (self.screen_to_x, self.screen_to_y))
            self.screen.blit(level["tutorial"]["wall"], (self.screen_to_x, self.screen_to_y))
            self.screen.blit(level["tutorial"]["3_wall"], (self.screen_to_x, self.screen_to_y))

            self.screen.blit(player["light"], (self.player_light_x_pos, self.player_light_y_pos)) 
            self.screen.blit(self.player, (self.player_x_pos, self.player_y_pos))

            self.screen.blit(ui["playing_screen"], (0, 0))
            self.screen.blit(self.draw_time, (290, 8))

            self.clock.tick() / 1000

            self.player_data.close()

            pygame.display.flip()

    def tutorial4(self):
        self.to_x = 0
        self.to_y = 0

        self.screen_to_x = 0
        self.screen_to_y = 0

        self.player_x_pos = 38
        self.player_y_pos = 32
        self.player_light_x_pos = -462
        self.player_light_y_pos = -231
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player = player["up"]
                        self.to_y -= 2
                    elif event.key == pygame.K_LEFT:
                        self.player = player["left"]
                        self.to_x -= 2
                    elif event.key == pygame.K_DOWN:
                        self.player = player["down"]
                        self.to_y += 2
                    elif event.key == pygame.K_RIGHT:
                        self.player = player["right"]
                        self.to_x += 2
                    elif event.key == pygame.K_1:
                        self.tutorial1()
                    elif event.key == pygame.K_2:
                        self.tutorial2()
                    elif event.key == pygame.K_3:
                        self.tutorial3()
                    elif event.key == pygame.K_4:
                        self.tutorial4()
                    elif event.key == pygame.K_5:
                        self.tutorial5()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.to_x = 0
                    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.to_y = 0

            self.check_slide_map()
            self.draw_game_board_for_tutorial()

            if self.player_x_pos >= 439:
                if self.player_y_pos >= 192:
                    sound = pygame.mixer.Sound("assets\\audios\\stage_up.wav")
                    sound.set_volume(0.3)
                    sound.play()
                    self.tutorial5()

            self.player_x_pos += self.to_x
            self.player_y_pos += self.to_y
            self.player_light_x_pos += self.to_x
            self.player_light_y_pos += self.to_y

            self.screen.blit(level["tutorial"][2], (self.screen_to_x, self.screen_to_y))
            self.screen.blit(level["tutorial"]["wall"], (self.screen_to_x, self.screen_to_y))
            self.screen.blit(level["tutorial"]["4_wall"], (self.screen_to_x, self.screen_to_y))

            self.screen.blit(player["light"], (self.player_light_x_pos, self.player_light_y_pos)) 
            self.screen.blit(self.player, (self.player_x_pos, self.player_y_pos))

            self.screen.blit(ui["playing_screen"], (0, 0))
            self.screen.blit(self.draw_time, (290, 8))

            self.clock.tick() / 1000

            self.player_data.close()

            pygame.display.flip()

    def tutorial5(self):
        self.to_x = 0
        self.to_y = 0

        self.screen_to_x = 0
        self.screen_to_y = 0

        self.player_x_pos = 38
        self.player_y_pos = 32
        self.player_light_x_pos = -462
        self.player_light_y_pos = -231
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player = player["up"]
                        self.to_y -= 2
                    elif event.key == pygame.K_LEFT:
                        self.player = player["left"]
                        self.to_x -= 2
                    elif event.key == pygame.K_DOWN:
                        self.player = player["down"]
                        self.to_y += 2
                    elif event.key == pygame.K_RIGHT:
                        self.player = player["right"]
                        self.to_x += 2
                    elif event.key == pygame.K_1:
                        self.tutorial1()
                    elif event.key == pygame.K_2:
                        self.tutorial2()
                    elif event.key == pygame.K_3:
                        self.tutorial3()
                    elif event.key == pygame.K_4:
                        self.tutorial4()
                    elif event.key == pygame.K_5:
                        self.tutorial5()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.to_x = 0
                    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        self.to_y = 0

            self.check_slide_map()
            self.draw_game_board_for_tutorial()

            if self.player_x_pos >= 439:
                if self.player_y_pos >= 192:
                    sound = pygame.mixer.Sound("assets\\audios\\stage_up.wav")
                    sound.set_volume(0.3)
                    sound.play()
                    self.ending()

            self.player_x_pos += self.to_x
            self.player_y_pos += self.to_y
            self.player_light_x_pos += self.to_x
            self.player_light_y_pos += self.to_y

            self.screen.blit(level["tutorial"][1], (self.screen_to_x, self.screen_to_y))
            self.screen.blit(level["tutorial"]["wall"], (self.screen_to_x, self.screen_to_y))
            self.screen.blit(level["tutorial"]["5_wall"], (self.screen_to_x, self.screen_to_y))

            self.screen.blit(player["light"], (self.player_light_x_pos, self.player_light_y_pos)) 
            self.screen.blit(self.player, (self.player_x_pos, self.player_y_pos))

            self.screen.blit(ui["playing_screen"], (0, 0))
            self.screen.blit(self.draw_time, (290, 8))

            self.clock.tick() / 1000

            self.player_data.close()

            pygame.display.flip()

if __name__ == "__main__":
    import pygame
    import sys
    import time

    from config import *
    from image import *

    pygame.mixer.init()

    time.sleep(0.1)

    sound = pygame.mixer.Sound("assets\\audios\\stage_up.wav")
    sound.set_volume(0.3)
    sound.play()
    
    game = Game()
    game.tutorial5()

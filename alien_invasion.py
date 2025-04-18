import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal

class AlienInvasion:
    
    def __init__(self): 
        pygame.init()
        pygame.mixer.init()  
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h))
        
        pygame.display.set_caption(self.settings.name)  
        self.bg = pygame.image.load(self.settings.bg_file) 
        self.bg = pygame.transform.scale(self.bg, 
            (self.settings.screen_w, self.settings.screen_h)
        )
        self.running = True 
        self.clock = pygame.time.Clock()

        
        self.laser_sound = pygame.mixer.Sound('Assets/sound/laser.mp3')  

        self.ship = Ship(self, Arsenal(self))

    def run_game(self):
        while self.running:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit_game()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():  
                self.laser_sound.play()  
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()

    def _check_keyup_events(self, event):
        
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_screen(self):
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()
        pygame.display.flip()

    def _quit_game(self):
        self.running = False
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
   
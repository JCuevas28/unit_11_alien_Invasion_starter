import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal


class Ship:
    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal'):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image,
                                            (self.settings.ship_w, self.settings.ship_h))

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.boundaries.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)  # Add vertical position
        self.arsenal = arsenal
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        self._update_ship_movement()
        self.arsenal.update_arsenal()

        # Update the ship's rect for horizontal movement
        self.rect.x = self.x
        self.rect.y = self.y  # Update vertical position

    def _update_ship_movement(self):
        
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        elif self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        
        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= temp_speed
        elif self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += temp_speed

        
        if self.rect.left <= self.boundaries.left:  
            self.rect.centerx = self.boundaries.centerx
            self.image = pygame.transform.flip(self.image, True, False)  
        elif self.rect.right >= self.boundaries.right:  
            self.rect.centerx = self.boundaries.centerx
            self.image = pygame.transform.flip(self.image, True, False)  

    def draw(self):
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        return self.arsenal.fire_bullet()

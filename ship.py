import pygame
import sys

class Ship:
    """Manage spaceship."""
    def __init__(self):
        """Initialize the game, and create game resource."""
        pygame.init()

        # Screen Settings
        self.screen = pygame.display.set_mode((1200,600))
        self.screen_rect = self.screen.get_rect()
        self.bg_color = (32,32,32)
        pygame.display.set_caption("Space Fighter")

        # Load ship images  and get its rect.
        self.sprite_sheet = pygame.image.load('images//player_plane.png').convert()
        self.image = [self.get_image(0,0,64,64),self.get_image(64,0,64,64),self.get_image(0,64,64,64)]
        # self.new_image = pygame.transform.scale(self.image,(60,40))
        self.rect = self.image[0].get_rect()
        self.select_image = self.image[0]

        # Start each new ship at left-centered position.
        self.rect.midleft = self.screen_rect.midleft

        # Ship settings
        self.ship_speed = 1
        self.move_up = False
        self.move_down = False
        self.move_right = False
        self.move_left = False

    def get_image(self,x,y,width,height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """
        # Create a new blank image.
        image = pygame.Surface([width,height]).convert()
        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet,(0,0),(x,y,width,height))
        # Assuming black works as the transparent color.
        image.set_colorkey((0,0,0))
        return image

    def blitme(self,image):
        """Draw ship at its current location"""
        self.screen.blit(image, self.rect)

    def run_ship(self):
        """Start the main loop."""
        while True:
            self._check_events()
            self.ship_movement()
            # Update image on the screen, and filp to new screen.
            self.screen.fill(self.bg_color)
            self.blitme(self.select_image)
            pygame.display.flip()
        
    def _check_events(self):
        """Respond to keypresses and mouse event."""
         # Watch for the keyboard and mouse event.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)

    def _check_keydown(self,event):
        if event.key == pygame.K_UP:
            self.move_up = True
        elif event.key == pygame.K_DOWN:
            self.move_down = True
        elif event.key == pygame.K_RIGHT:
            self.move_right = True
        elif event.key == pygame.K_LEFT:
            self.move_left = True

    def _check_keyup(self,event):
        if event.key == pygame.K_UP:
            self.move_up = False
            self.select_image = self.image[0]
        elif event.key == pygame.K_DOWN:
            self.move_down = False
            self.select_image = self.image[0]
        elif event.key == pygame.K_RIGHT:
            self.move_right = False
        elif event.key == pygame.K_LEFT:
            self.move_left = False
    
    def ship_movement(self):
        if self.move_up and self.rect.top >= 0:
            self.rect.y -= self.ship_speed
            self.select_image = self.image[1]
        elif self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.ship_speed
            self.select_image = self.image[2]
        elif self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.ship_speed
        elif self.move_left and self.rect.left > 0:
            self.rect.x -= self.ship_speed
    



if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = Ship()
    ai.run_ship()
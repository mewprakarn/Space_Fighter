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
        self.image = self.get_image(0,0,64,64)
        # self.new_image = pygame.transform.scale(self.image,(60,40))
        self.rect = self.image.get_rect()

        # Start each new ship at left-centered position.
        self.rect.midleft = self.screen_rect.midleft

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

    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def run_ship(self):
        """Start the main loop."""
        while True:
            self._check_events()
            # Update image on the screen, and filp to new screen.
            self.screen.fill(self.bg_color)
            self.blitme()
            pygame.display.flip()
        
            

    def _check_events(self):
        """Respond to keypresses and mouse event."""
         # Watch for the keyboard and mouse event.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()



if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = Ship()
    ai.run_ship()
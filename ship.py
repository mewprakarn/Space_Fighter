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
        self.image = pygame.image.load('images//bird1.png')
        self.new_image = pygame.transform.scale(self.image,(60,40))
        self.rect = self.new_image.get_rect()

        # Start each new ship at left-centered position.
        self.rect.midleft = self.screen_rect.midleft

    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.new_image, self.rect)

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
import sys
import pygame 
from setting import Setting
from ship import Ship
import game_funtions as gf

def run_game():
    
    #Initialize pygame ,settings , and screen object.
    pygame.init()
    
    ai_setting=Setting()
    screen=pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    ship=Ship(screen)
    
    
    # Start the main loop for the game.

    while True:
        # Watch for keyboard and mouse events.
        gf.check_events()
        
        # Redraw the screen during each pass through the loop 
        screen.fill(ai_setting.bg_color)
        ship.blitme()
        # Make the most recently drawn screen visible
        pygame.display.flip()

run_game()


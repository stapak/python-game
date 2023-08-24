import sys
import pygame 

from setting import Setting

def run_game():
    
    #Initialize pygame ,settings , and screen object.
    pygame.init()
    
    ai_setting=Setting()
    screen=pygame.display.set_mode(ai_setting.screen_width,ai_setting.screen_height)
    pygame.display.set_caption("Alien Invasion")
    # Start the main loop for the game.

    while True:
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # Redraw the screen during each pass through the loop 
        screen.fill(ai_setting.bg_color)
        
        # Make the most recently drawn screen visible
        pygame.display.flip()

run_game()


import sys
import pygame 

def run_game():
    
    #Initialize game and create a screen object.

    pygame.init()
    screen=pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")

    #set backgroud color. Here we define the RGB value for the background color and store it in a 
    # variable
    bg_color=(230,230,230)

    # Start the main loop for the game.

    while True:
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # Redraw the screen during each pass through the loop, using fill command and predefined RGB
        # values.
        screen.fill(bg_color)
        
        # Make the most recently drawn screen visible
        pygame.display.flip()

run_game()


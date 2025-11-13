import pygame, cussbotbackend as back, sys

# Initialize Pygame
text = back.cuss()
print(text)
# Set window dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hello World")
# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
# Font settings
pygame.init()
font = pygame.font.Font(None, 18)  # Use default font, size 36

# Render the text

def display_text(text, screen=screen, font_size=10, font_color=(0, 0, 0), screen_width=800, screen_height=600):
    try:

        #font = pygame.font.Font("Consolas", font_size)  # Load Consolas font
        text_surface = font.render(text, True, font_color)  # Render the text
        text_rect = text_surface.get_rect()
        text_rect.center = (screen_width // 2, screen_height // 2)  # Center the text
        screen.blit(text_surface, text_rect)
    except pygame.error as e:
        print(f"Error rendering text: {e}")
rendered_text = font.render(text, True, white)
text_rect = rendered_text.get_rect()
text_rect.center = (width // 2, height // 2)  # Center the text
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Fill the screen with black
    screen.fill(black)

    # Draw the text
    display_text(text, screen)
    screen.blit(rendered_text, text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
sys.exit()

pygame.quit()

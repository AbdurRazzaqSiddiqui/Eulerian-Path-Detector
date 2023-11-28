import pygame
import sys

pygame.init()

# Set up display
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pygame Dropdown Menu')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)

# Fonts
font = pygame.font.Font(None, 36)

# Menu options
options = ['Option 1', 'Option 2', 'Option 3']
selected_option = None

# Dropdown menu properties
menu_rect = pygame.Rect(10, 10, 150, 40)
menu_expanded = False

# Main game loop
while True:
    screen.fill(white)

    # Draw menu button
    pygame.draw.rect(screen, gray, menu_rect)
    pygame.draw.rect(screen, black, menu_rect, 2)

    # Draw menu label
    menu_label = font.render('Menu', True, black)
    screen.blit(menu_label, (menu_rect.x + 10, menu_rect.y + 10))

    # Draw dropdown menu if expanded
    if menu_expanded:
        for i, option in enumerate(options):
            option_rect = pygame.Rect(menu_rect.x, menu_rect.y + (i + 1) * menu_rect.height, menu_rect.width, menu_rect.height)
            pygame.draw.rect(screen, gray, option_rect)
            pygame.draw.rect(screen, black, option_rect, 2)
            option_label = font.render(option, True, black)
            screen.blit(option_label, (option_rect.x + 10, option_rect.y + 10))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if menu_rect.collidepoint(event.pos):
                menu_expanded = not menu_expanded
            elif menu_expanded:
                for i, option in enumerate(options):
                    option_rect = pygame.Rect(menu_rect.x, menu_rect.y + (i + 1) * menu_rect.height, menu_rect.width, menu_rect.height)
                    if option_rect.collidepoint(event.pos):
                        selected_option = option
                        menu_expanded = False

    # Draw selected option
    if selected_option is not None:
        selected_label = font.render(f'Selected: {selected_option}', True, black)
        screen.blit(selected_label, (200, 100))

    pygame.display.flip()
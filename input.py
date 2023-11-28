import pygame
import pygame_gui

pygame.init()

window_size = (400, 300)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Input Example')

ui_manager = pygame_gui.UIManager(window_size)

def handle_button_click(event):
    if event.type == pygame_gui.UI_BUTTON_PRESSED:
        if event.ui_element == button:
            text_input = text_box.get_text()
            number_input = number_box.get_text()
            if number_input.isdigit():
                number_input = int(number_input)
                print(f"Text Input: {text_input}")
                print(f"Number Input: {number_input}")
            else:
                print("Please enter a valid number")

text_box = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((50, 50), (200, 30)),
    manager=ui_manager
)

number_box = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((50, 100), (200, 30)),
    manager=ui_manager
)

button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((50, 150), (100, 30)),
    text='Submit',
    manager=ui_manager
)

button_handler = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((50, 150), (100, 30)),
    text='Submit',
    manager=ui_manager
)

pygame.event.set_allowed([pygame.USEREVENT, pygame_gui.UI_BUTTON_PRESSED])

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        ui_manager.process_events(event)
        handle_button_click(event)

    ui_manager.update(time_delta)

    window.fill((255, 255, 255))

    ui_manager.draw_ui(window)

    pygame.display.flip()

pygame.quit()

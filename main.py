import pygame
import sys
import time
from pygame.locals import *
from eulerian import Euler_Graph
from hamiltonian import Hamilton_Graph

width, height = 960, 720
bg_img = pygame.image.load('image.jpg')
bg_img = pygame.transform.scale(bg_img,(width,height))
button_color = (127, 0, 255)
text_color = (255,255,255)
heading_color = (255,255,255)
button_border_color = (0, 0, 0)
button_width = 160
button_height = 30
button_margin = 15
point_color = (30, 0, 255)
point_bg_color = (255,255,255)
coord_color = (56, 0, 153)
line_color = (0,0,0)
line_width = 1
point_radius = 8
font_size = 24

pygame.init()
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 20)
menu_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Minimum Spanning Tree - Menu")

def draw_button(rect, text, callback):
    pygame.draw.rect(menu_screen, button_color, rect)
    pygame.draw.rect(menu_screen, button_border_color, rect, 5)  # Draw the border
    text_surface = small_font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    menu_screen.blit(text_surface, text_rect)
    if rect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            callback()

def draw_list(rect, text):
    pygame.draw.rect(menu_screen, button_color, rect)
    pygame.draw.rect(menu_screen, button_border_color, rect, 5)  # Draw the border
    text_surface = small_font.render(text, True, text_color)
    # coords_text = small_font.render(f'({x},{y})', True, coord_color)
    text_rect = text_surface.get_rect(center=rect.center)
    menu_screen.blit(text_surface, text_rect)
    if rect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            pass

def sub_menu():
    global screen  # Declare screen as a global variable
    screen = None  # Set the screen to None

    # Clear the main application screen
    menu_screen.blit(bg_img,(0,0))
    pygame.display.flip()  # Update the display

    # Main menu loop
    menu_running = True
    while menu_running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()  # Quit the program
                sys.exit()  # Exit the program

        # Set the background color
        menu_screen.blit(bg_img,(0,0))

        # Draw "Brute Force" button
        Eulerian_button_rect = pygame.Rect(width // 2 - button_width // 2, height // 2 - button_height // 2, button_width, button_height)
        Hamiltonian_button_rect = pygame.Rect(width // 2 - button_width // 2, height // 2 - button_height // 2 + 40, button_width, button_height)
        back_button_rect = pygame.Rect(width // 2 - button_width // 2, height // 2 - button_height // 2 + 200, button_width, button_height)

        draw_button(Eulerian_button_rect, "Eulerian's Algorithm", lambda: open_main_window(algorithm_no=1))
        draw_button(Hamiltonian_button_rect, "Hamiltonian's Algorithm", lambda: open_main_window(algorithm_no=2))         
        draw_button(back_button_rect, "Return to Main Menu", main_menu)      

        # Update the display
        pygame.display.flip()

def about():
    global screen  # Declare screen as a global variable
    screen = None  # Set the screen to None

    # Clear the main application screen
    menu_screen.blit(bg_img,(0,0))
    pygame.display.flip()  # Update the display

    # Main menu loop
    menu_running = True
    while menu_running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()  # Quit the program
                sys.exit()  # Exit the program

        # Set the background color
        menu_screen.blit(bg_img,(0,0))

        back_button_rect = pygame.Rect(width - button_width - button_margin, height - button_height - 15, button_width, button_height)
        draw_button(back_button_rect, "Return to Main Menu", main_menu) 

        # Load images
        image1 = pygame.image.load("p1.jpg")  
        image2 = pygame.image.load("p2.jpeg")  
        image3 = pygame.image.load("p3.jpeg")  

        # Scale the images to fit on the screen
        image1 = pygame.transform.scale(image1, (200, 200))
        image2 = pygame.transform.scale(image2, (200, 200))
        image3 = pygame.transform.scale(image3, (200, 200))

        # Fonts
        font = pygame.font.Font(None, 20)

        # Create text captions
        caption1 = font.render("K213330 Muneeb Ahmed", True, heading_color)
        caption2 = font.render("K213200 Abdur Razzaq", True, heading_color)
        caption3 = font.render("K213201 Arham Mehmood", True, heading_color)

        # Display images
        menu_screen.blit(image1, (width // 4 - 100, height // 2 - 100))
        menu_screen.blit(image2, (width // 2 - 100, height // 2 - 100))
        menu_screen.blit(image3, (3 * width // 4 - 100, height // 2 - 100))

        # Display captions
        menu_screen.blit(caption1, (width // 4 - 80, height // 2 + 110))
        menu_screen.blit(caption2, (width // 2 - 80, height // 2 + 110))
        menu_screen.blit(caption3, (3 * width // 4 - 80, height // 2 + 110))

        pygame.display.flip()

def open_main_window(algorithm_no):
    global screen,algo_title # Declare screen and algo title as a global variable
    if screen is not None:
        screen.blit(bg_img,(0,0))  # Clear the screen
        pygame.display.flip()  # Update the display

    screen = pygame.display.set_mode((width, height))
    if algorithm_no == 1:
        algo_title = "Eulerian's Algorithm"
    elif algorithm_no == 2:
        algo_title = "Hamiltonian's Algorithm"

    # List to store user-selected points
    points = []
    resultant_path = []
    points_dict = []
    vertex = 'A'
    all_edges = []
    edge_line = []
    edge_opt = False
    euler_opt = False
    hamiton_opt = False
    euler_path = []
    hamilton_path = []

    # Rectangles to define the button areas
    reset_button_rect = pygame.Rect(width - button_width - button_margin, button_margin, button_width, button_height)
    resultant_path_button_rect = pygame.Rect(width - button_width - button_margin, button_margin * 2 + button_height, button_width, button_height)
    back_button_rect = pygame.Rect(width - button_width - button_margin, height - button_height - button_margin, button_width, button_height)
    edge_rect = pygame.Rect(button_margin * 2 + 430, button_margin * 2 + 30, button_width, button_height)

    # Function to draw a point
    def draw_point(x, y, caption, color=point_color):
        pygame.draw.circle(screen, color, (x, y), point_radius)
        pygame.draw.circle(screen, point_bg_color, (x, y), point_radius-3)
        coords_text = small_font.render(f'{caption}', True, coord_color)
        screen.blit(coords_text, (x + 10, y - 20))

    # Function to find the convex hull
    def find_paths():
        if algorithm_no == 1:
            global eulerian_path_graph
            vertices = []
            eulerian_path_graph = Euler_Graph(len(points))
            for edge in all_edges:
                for point in points_dict:
                    if edge[0] == point['point']:
                        vertices.append(point['vertex'])
                        break
                for point in points_dict:
                    if edge[1] == point['point']:
                        vertices.append(point['vertex'])
                        break
                option = True
                for euler_vertex in euler_path:
                    if euler_vertex['u'] == vertices[0] and euler_vertex['v'] == vertices[1]:
                        option = False
                if option:
                    eulerian_path_graph.addEdge(vertices[0],vertices[1])
                    euler_path.append({'u':vertices[0],'v':vertices[1]})
                vertices.clear()
            eulerian_path_graph.printEulerTour()
            euler_opt = True

        elif algorithm_no == 2:
            global hamiltonian_path_graph
            vertices = []
            hamiltonian_path_graph = Hamilton_Graph(len(points))
            for edge in all_edges:
                for point in points_dict:
                    if edge[0] == point['point']:
                        vertices.append(point['vertex'])
                        break
                for point in points_dict:
                    if edge[1] == point['point']:
                        vertices.append(point['vertex'])
                        break
                option = True
                for hamilton_vertex in hamilton_path:
                    if hamilton_vertex['u'] == vertices[0] and hamilton_vertex['v'] == vertices[1]:
                        option = False
                if option:
                    hamiltonian_path_graph.addEdge(vertices[0],vertices[1])
                    hamilton_path.append({'u':vertices[0],'v':vertices[1]})
                vertices.clear()
            hamiltonian_path_graph.test()
            # print(f'Path {hamiltonian_path_graph.path}')
            # print(f'Path {hamilton_path}')
            hamilton_opt = True
    # Function to reset points and clear the convex hull
    def reset_points():
        nonlocal resultant_path
        points.clear()
        points_dict.clear()
        vertex = 'A'
        resultant_path.clear()
        edge_line.clear()
        edge_opt = False
        all_edges.clear()
        screen.blit(bg_img,(0,0))
        euler_opt = False
        hamilton_opt = False
        euler_path.clear()
        hamilton_path.clear()

    # Function to check if a point is inside a button, excluding the "Find Complexity" button
    def is_point_in_button(point):
        return reset_button_rect.collidepoint(point) or resultant_path_button_rect.collidepoint(point) or back_button_rect.collidepoint(point)

    def make_edge():
        for point in points_dict:
            if point['vertex'] == first_selection:
                point1 = point['point']
            if point['vertex'] == second_selection:
                point2 = point['point']
        # print(point1,point2)
        edge_line.append(point1)
        edge_line.append(point2)
        if (point1,point2) not in all_edges:
            all_edges.append((point1,point2))
        # for edge in all_edges:
        #     print(edge[0],edge[1])
        # edge_line.clear()
        edge_opt = True

    # Dropdown menu properties
    menu_1_expanded = False
    menu_1_options = []
    first_selection = None
    menu_2_expanded = False
    menu_2_options = []
    second_selection = None

    # Main loop for the main application window
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()  # Quit the program
                sys.exit()  # Exit the program
            # if event.type == MOUSEBUTTONDOWN:
            #     if len(points) < 50:
            #         point = event.pos
            #         if not (is_point_in_button(point)):
            #             points.append(point)
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu_1_options = [point['vertex'] for point in points_dict]
                menu_2_options = [point['vertex'] for point in points_dict]
                if menu_1_rect.collidepoint(event.pos):
                    menu_1_expanded = not menu_1_expanded
                elif menu_1_expanded:
                    for i, option in enumerate(menu_1_options):
                        option_rect = pygame.Rect(menu_1_rect.x, menu_1_rect.y + (i + 1) * menu_1_rect.height, menu_1_rect.width, menu_1_rect.height)
                        if option_rect.collidepoint(event.pos):
                            first_selection = option
                            menu_1_expanded = False
                elif menu_2_rect.collidepoint(event.pos):
                    menu_2_expanded = not menu_2_expanded
                elif menu_2_expanded:
                    for i, option in enumerate(menu_2_options):
                        option_rect = pygame.Rect(menu_2_rect.x, menu_2_rect.y + (i + 1) * menu_2_rect.height, menu_2_rect.width, menu_2_rect.height)
                        if option_rect.collidepoint(event.pos):
                            second_selection = option
                            menu_2_expanded = False
                elif edge_rect.collidepoint(event.pos):
                    edge_opt = True
                elif len(points) < 50:
                    point = event.pos
                    if not (is_point_in_button(point)):
                        points.append(point)
                        points_dict.append({'point':point,'vertex':vertex})
                        vertex = chr(ord(vertex) + 1)
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    reset_points()

        # Set the background color
        screen.blit(bg_img,(0,0))

        # Draw title
        title_text = font.render("Path Detector Application - " + algo_title, True, heading_color)
        title_rect = title_text.get_rect(center=(width // 3, 15 + title_text.get_height() // 2))
        screen.blit(title_text, title_rect)

        # Draw buttons
        draw_button(reset_button_rect, "Reset", reset_points)
        draw_button(resultant_path_button_rect, "Find Paths", find_paths)
        draw_button(edge_rect, "Make Edge", make_edge)
        draw_button(back_button_rect, "Back", sub_menu)

        # Dropdown
        menu_1_rect = pygame.Rect(button_margin * 2 + 30, button_margin * 2 + 30, button_width, button_height)
        # draw_list(menu_1_rect,'Vertex A')
        if first_selection is not None:
            draw_list(menu_1_rect,first_selection)
        else:
            draw_list(menu_1_rect,'Vertex A')
        if menu_1_expanded:
            for i, option in enumerate(menu_1_options):
                option_rect = pygame.Rect(menu_1_rect.x, menu_1_rect.y + (i + 1) * menu_1_rect.height, menu_1_rect.width, menu_1_rect.height)
                draw_list(option_rect,option)
        
        menu_2_rect = pygame.Rect(button_margin * 2 + 230, button_margin * 2 + 30, button_width, button_height)
        if second_selection is not None:
            draw_list(menu_2_rect,second_selection)
        else:
            draw_list(menu_2_rect,'Vertex B')
        if menu_2_expanded:
            for i, option in enumerate(menu_2_options):
                option_rect = pygame.Rect(menu_2_rect.x, menu_2_rect.y + (i + 1) * menu_2_rect.height, menu_2_rect.width, menu_2_rect.height)
                draw_list(option_rect,option)

        # Draw Edges
        if edge_opt:
            for i in range(0,len(edge_line),2):
                pygame.draw.lines(screen, line_color, True, (edge_line[i],edge_line[i+1]), 4)

        # Draw Euler Path
        if euler_path:
            euler_line = []
            for edge in eulerian_path_graph.path:
                for point in points_dict:
                    if point['vertex'] == edge[0]:
                        euler_line.append(point['point'])
                for point in points_dict:
                    if point['vertex'] == edge[1]:
                        euler_line.append(point['point'])
                pygame.draw.lines(screen, (250,0,0), True, (euler_line[0],euler_line[1]), 5)
                euler_line.clear()

        if hamilton_path:
            hamilton_line = []
            for i in range(len(hamiltonian_path_graph.result)):
                for point in points_dict:
                    if point['vertex'] == hamiltonian_path_graph.result[i]:
                        hamilton_line.append(point['point'])
            
            for i in range(len(hamilton_line)):
                print(i,len(hamilton_line))
                if i != (len(hamilton_line)-1):
                    pygame.draw.lines(screen, (250,0,0), True, (hamilton_line[i],hamilton_line[i+1]), 5)

        # Draw points and coordinates
        for point,caption in zip(points,points_dict):
            draw_point(point[0], point[1],caption['vertex'])

        # Update the display
        pygame.display.flip()

def main_menu():
    global screen  # Declare screen as a global variable
    screen = None  # Set the screen to None

    # Clear the main application screen
    menu_screen.blit(bg_img,(0,0))
    pygame.display.flip()  # Update the display

    # Main menu loop
    menu_running = True
    while menu_running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()  # Quit the program
                sys.exit()  # Exit the program

        # Set the background color
        menu_screen.blit(bg_img,(0,0))

        # Draw Title
        title_text = font.render("Graph Theory Project", True, heading_color)
        title_rect = title_text.get_rect(center=(width // 2, 15 + title_text.get_height() // 2))
        menu_screen.blit(title_text, title_rect)

        resultant_path_button_rect = pygame.Rect(width//2 - 80, height//2 - 100, 160, 40)  # Create the convex button rect
        draw_button(resultant_path_button_rect, "Path Detector", sub_menu)

        about_button_rect = pygame.Rect(width - button_width - button_margin, button_margin * 2 - 15, button_width, button_height)
        draw_button(about_button_rect, "About Us", about)
        pygame.display.flip()

# Call the function to display the main menu initially
main_menu()
sys.exit()

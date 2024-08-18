import pygame
import sys
from random import shuffle, randint, choice

# Variables
######
cell_size = 20  # Cell size
maze_length = 40 * cell_size + 1  # Maze length
maze_height = 30 * cell_size + 1  # Maze height
num_enemies = 10  # Number of enemies
######

# Colors
black = (0, 0, 0)
white = (245, 245, 245)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)
menu_background_color = (25, 25, 112)  # Midnight blue background for the menu
button_color = (255, 140, 0)  # Dark orange for buttons
button_text_color = (255, 255, 255)  # White text on buttons
outline_color = white  # Outline color for buttons

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((maze_length, maze_height))
clock = pygame.time.Clock()

# Fonts
font = pygame.font.Font(None, 74)
asian_font = pygame.font.Font('SEVESBRG.ttf', 80)  # Adjusted font size for the title
small_font = pygame.font.Font('go3v2.ttf', 48)  # Smaller font for menu buttons
rights_font = pygame.font.SysFont('timesnewroman', 24)  # Font for the "All rights reserved" text
anoofel_font = pygame.font.Font('SEVESBRG.ttf', 67)  # 1.5 times smaller font for "ANOOFEL GAMES"
year_font = pygame.font.Font('SEVESBRG.ttf', 150)  # Bigger font for "2024"
year_color = (255, 215, 0)  # Gold color for "2024"

# Emoji Font
emoji_font = pygame.font.SysFont('segoeuisymbol', 48)  # Or use 'Noto Color Emoji'

# Load and rotate Background Image
background_image = pygame.image.load('manokhashi.jpg')
background_image = pygame.transform.rotate(background_image, -90)

# Uncomment to use an emoji image instead of emoji font
# emoji_image = pygame.image.load('emoji.png')
# emoji_image = pygame.transform.scale(emoji_image, (48, 48))  # Adjust size as needed

# Music Playlist
song_list = [f'{i}.mp3' for i in range(1, 11)]
shuffle(song_list)  # Shuffle the playlist

# Initialize the mixer for music playback
pygame.mixer.init()

# Function to play a random song from the playlist
def play_random_song():
    global current_song
    current_song = randint(0, len(song_list) - 1)
    pygame.mixer.music.load(song_list[current_song])
    pygame.mixer.music.play()

# Set up the end of song event to trigger the next random song
pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)

# Start playing a random song at the beginning
play_random_song()

# Function Definitions for the Menu
def display_text(text, font, color, y_offset=0, x_offset=0):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, ((maze_length - text_surface.get_width()) // 2 + x_offset, 
                               (maze_height - text_surface.get_height()) // 2 + y_offset))

def display_anoofel_games():
    screen.fill(menu_background_color)
    
    # Add border
    pygame.draw.rect(screen, white, screen.get_rect(), 10)

    # Outline
    outline_offset = 3
    for dx in [-outline_offset, outline_offset]:
        for dy in [-outline_offset, outline_offset]:
            display_text('ANOOFEL GAMES', anoofel_font, outline_color, x_offset=dx, y_offset=dy)
    # Main text
    display_text('ANOOFEL GAMES', anoofel_font, black)
    pygame.display.flip()
    pygame.time.wait(2000)  # Display for 2 seconds

def display_license():
    # Set the background image
    screen.blit(pygame.transform.scale(background_image, (maze_length, maze_height)), (0, 0))

    # Display "2024" prominently
    display_text("2024", year_font, year_color, -50)

    # Display "all rights are reserved" in the bottom right corner
    rights_text = rights_font.render("all rights are reserved", True, white)
    screen.blit(rights_text, (maze_length - rights_text.get_width() - 20, maze_height - rights_text.get_height() - 20))

    pygame.display.flip()
    pygame.time.wait(2000)  # Display for 2 seconds

def show_menu():
    screen.fill(menu_background_color)
    
    # Add border
    pygame.draw.rect(screen, white, screen.get_rect(), 10)

    display_text("khashi's coc maze", asian_font, white, -200)
    
    # Display text with emoji
    display_text("🎉 Happy Birthday Khashi 🎉", emoji_font, yellow, -150)
    
    # Uncomment to use emoji image instead of emoji font
    # display_text("Happy Birthday Khashi", small_font, yellow, -150)
    # screen.blit(emoji_image, ((maze_length // 2) + 200, (maze_height // 2) - 200))  # Adjust position as needed
    
    # Button positions
    button_width = 300  # Adjusted to better fit text
    button_height = 60  # Adjusted to better fit text
    button_y_start = (maze_height // 2) - 25
    button_x_center = (maze_length - button_width) // 2
    outline_thickness = 4  # Thickness of the outline

    play_button_rect = pygame.Rect(button_x_center, button_y_start, button_width, button_height)
    about_button_rect = pygame.Rect(button_x_center, button_y_start + 90, button_width, button_height)
    credits_button_rect = pygame.Rect(button_x_center, button_y_start + 180, button_width, button_height)

    # Draw buttons with outline
    pygame.draw.rect(screen, outline_color, play_button_rect.inflate(outline_thickness, outline_thickness))
    pygame.draw.rect(screen, button_color, play_button_rect)
    
    pygame.draw.rect(screen, outline_color, about_button_rect.inflate(outline_thickness, outline_thickness))
    pygame.draw.rect(screen, button_color, about_button_rect)
    
    pygame.draw.rect(screen, outline_color, credits_button_rect.inflate(outline_thickness, outline_thickness))
    pygame.draw.rect(screen, button_color, credits_button_rect)

    # Display text on buttons (centered vertically within the rectangles)
    text_offset = (button_height - small_font.get_height()) // 2  # Adjust text position inside button
    screen.blit(small_font.render("Play", True, button_text_color), 
                (play_button_rect.centerx - small_font.size("Play")[0] // 2, 
                 play_button_rect.centery - small_font.get_height() // 2))

    screen.blit(small_font.render("About", True, button_text_color), 
                (about_button_rect.centerx - small_font.size("About")[0] // 2, 
                 about_button_rect.centery - small_font.get_height() // 2))

    screen.blit(small_font.render("Credits", True, button_text_color), 
                (credits_button_rect.centerx - small_font.size("Credits")[0] // 2, 
                 credits_button_rect.centery - small_font.get_height() // 2))

    pygame.display.flip()

    return play_button_rect, about_button_rect, credits_button_rect

def show_about():
    screen.fill(menu_background_color)
    display_text("This game is a fun birthday gift!", font, white, -50)
    display_text("Made with love by Arad", font, white, 50)
    pygame.display.flip()
    wait_for_keypress()

def show_credits():
    screen.fill(menu_background_color)
    display_text("Game Design: Arad", font, white, -50)
    display_text("Special Thanks: Khashi", font, white, 50)
    pygame.display.flip()
    wait_for_keypress()

def wait_for_keypress():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False

def main_menu():
    display_anoofel_games()
    display_license()

    while True:
        play_button_rect, about_button_rect, credits_button_rect = show_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    return  # Start the game
                elif about_button_rect.collidepoint(event.pos):
                    show_about()
                elif credits_button_rect.collidepoint(event.pos):
                    show_credits()

# Call the Main Menu Before Starting the Game
main_menu()

# The rest of your game code starts here

# Maze Generation Functions
def one_connection(cell_x, cell_y):
    count = 0
    if [cell_x + cell_size, cell_y] in passage_list:
        count += 1
    if [cell_x - cell_size, cell_y] in passage_list:
        count += 1
    if [cell_x, cell_y + cell_size] in passage_list:
        count += 1
    if [cell_x, cell_y - cell_size] in passage_list:
        count += 1
    return count <= 1

def valid_cell(cell_x, cell_y):
    if [cell_x, cell_y] in potential_passage_list:
        impossible_passage.append([cell_x, cell_y])
    elif [cell_x, cell_y] in impossible_passage:
        impossible_passage.append([cell_x, cell_y])
    elif cell_x < 0 or cell_x >= maze_length - cell_size or cell_y < 0 or cell_y >= maze_height - cell_size:
        impossible_passage.append([cell_x, cell_y])
    elif not one_connection(cell_x, cell_y):
        impossible_passage.append([cell_x, cell_y])
    elif [cell_x, cell_y] not in passage_list:
        return True

def maze_passage(cell_x, cell_y):
    block_passage_list = []
    potential_passage_list.remove([cell_x, cell_y])
    if valid_cell(cell_x, cell_y):
        pygame.draw.rect(screen, white, [cell_x, cell_y, cell_size, cell_size])
        pygame.display.update()

        passage_list.append([cell_x, cell_y])

        if valid_cell(cell_x + cell_size, cell_y):
            block_passage_list.append([cell_x + cell_size, cell_y])
        if valid_cell(cell_x - cell_size, cell_y):
            block_passage_list.append([cell_x - cell_size, cell_y])
        if valid_cell(cell_x, cell_y + cell_size):
            block_passage_list.append([cell_x, cell_y + cell_size])
        if valid_cell(cell_x, cell_y - cell_size):
            block_passage_list.append([cell_x, cell_y - cell_size])

        shuffle(block_passage_list)

        for j in block_passage_list:
            potential_passage_list.append(j)

def reset_game():
    global player_pos, end_pos, enemy_positions, enemy_directions, done, passage_list, potential_passage_list, impossible_passage
    passage_list = []
    potential_passage_list = []
    impossible_passage = []
    done = False
    screen.fill(black)

    while not passage_list:  # Ensure the maze has at least one passage
        # Create initial cell
        start_cell = [randint(0, int(maze_height / cell_size)) * cell_size,
                      randint(0, int(maze_height / cell_size)) * cell_size]
        potential_passage_list.append(start_cell)

        # Generate Maze
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            for i in range(1, len(potential_passage_list) + 1):
                if randint(0, int(len(passage_list) / 50)) == 0:
                    maze_passage(potential_passage_list[-i][0], potential_passage_list[-i][1])
                    break

            if not potential_passage_list:
                if passage_list:  # Check if any passages were created
                    passage_list.sort()
                    player_pos = passage_list[0]  # Start position
                    end_pos = passage_list[-1]  # End position

                    pygame.draw.rect(screen, red, [end_pos[0] + 1, end_pos[1] + 1, cell_size - 2, cell_size - 2])
                    display_text("END", small_font, black, y_offset=end_pos[1] - player_pos[1], x_offset=end_pos[0] - player_pos[0] + 30)
                    pygame.draw.rect(screen, blue, [player_pos[0] + 1, player_pos[1] + 1, cell_size - 2, cell_size - 2])
                    pygame.display.update()

                    # Initialize Enemies
                    enemy_positions = []
                    enemy_directions = []
                    for _ in range(num_enemies):
                        enemy_pos = passage_list[randint(1, len(passage_list) - 2)]
                        enemy_positions.append(enemy_pos)
                        enemy_directions.append(choice([(0, -cell_size), (0, cell_size), (-cell_size, 0), (cell_size, 0)]))
                        pygame.draw.rect(screen, yellow, [enemy_pos[0] + 1, enemy_pos[1] + 1, cell_size - 2, cell_size - 2])
                    pygame.display.update()

                    done = True
                else:
                    # No passages were generated, regenerate the maze
                    break

    done = False

def show_loss_screen():
    screen.fill(black)
    text = font.render('You lost!', True, red)
    screen.blit(text, ((maze_length - text.get_width()) // 2, (maze_height - text.get_height()) // 2))
    text = font.render('Press Enter to restart', True, red)
    screen.blit(text, ((maze_length - text.get_width()) // 2, (maze_height - text.get_height()) // 2 + 100))
    pygame.display.flip()

    waiting_for_restart = True
    while waiting_for_restart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting_for_restart = False

def show_win_screen():
    screen.fill(black)
    text = font.render('You Win!', True, green)
    screen.blit(text, ((maze_length - text.get_width()) // 2, (maze_height - text.get_height()) // 2))
    pygame.display.flip()

    # Play the winning song
    pygame.mixer.music.load('taklif.mp3')
    pygame.mixer.music.play()

    # Launch fireworks
    launch_fireworks()

    waiting_for_restart = True
    while waiting_for_restart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting_for_restart = False

import math  # Import the math module

def launch_fireworks():
    for _ in range(5):  # Number of fireworks
        x = randint(100, maze_length - 100)
        y = maze_height
        lower_bound = min(maze_height // 2, maze_height // 4)  # Ensure lower_bound is less than upper_bound
        upper_bound = max(maze_height // 2, maze_height // 4)  # Ensure upper_bound is greater than lower_bound

        color = choice([red, blue, yellow, green])

        # Firework launch
        for i in range(maze_height, randint(lower_bound, upper_bound), -10):
            screen.fill(black)
            pygame.draw.circle(screen, color, (x, i), 5)
            pygame.display.flip()
            clock.tick(30)

        # Firework explosion
        for _ in range(50):
            screen.fill(black)
            for _ in range(30):
                angle = randint(0, 360)
                distance = randint(10, 50)
                x_offset = int(distance * math.cos(math.radians(angle)))  # Use math.cos and math.radians
                y_offset = int(distance * math.sin(math.radians(angle)))  # Use math.sin and math.radians
                pygame.draw.circle(screen, color, (x + x_offset, i + y_offset), 3)
            pygame.display.flip()
            clock.tick(30)



# Game Loop
reset_game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.USEREVENT + 1:  # End of song event
            play_random_song()

    keys = pygame.key.get_pressed()
    new_player_pos = list(player_pos)

    if keys[pygame.K_w]:
        new_player_pos[1] -= cell_size
    elif keys[pygame.K_s]:
        new_player_pos[1] += cell_size
    elif keys[pygame.K_a]:
        new_player_pos[0] -= cell_size
    elif keys[pygame.K_d]:
        new_player_pos[0] += cell_size

    if new_player_pos in passage_list:
        pygame.draw.rect(screen, white, [player_pos[0] + 1, player_pos[1] + 1, cell_size - 2, cell_size - 2])
        player_pos = new_player_pos
        pygame.draw.rect(screen, blue, [player_pos[0] + 1, player_pos[1] + 1, cell_size - 2, cell_size - 2])

    if player_pos == end_pos:
        show_win_screen()  # Show the win screen with fireworks and play the winning song
        reset_game()

    for idx, enemy_pos in enumerate(enemy_positions):
        pygame.draw.rect(screen, white, [enemy_pos[0] + 1, enemy_pos[1] + 1, cell_size - 2, cell_size - 2])

        new_enemy_pos = [enemy_pos[0] + enemy_directions[idx][0], enemy_pos[1] + enemy_directions[idx][1]]

        # Prevent enemies from occupying the end position
        if new_enemy_pos == end_pos:
            continue

        if new_enemy_pos not in passage_list or randint(0, 10) < 1:
            enemy_directions[idx] = choice([(0, -cell_size), (0, cell_size), (-cell_size, 0), (cell_size, 0)])
            new_enemy_pos = [enemy_pos[0] + enemy_directions[idx][0], enemy_pos[1] + enemy_directions[idx][1]]

        if new_enemy_pos in passage_list:
            enemy_positions[idx] = new_enemy_pos

        pygame.draw.rect(screen, yellow, [enemy_positions[idx][0] + 1, enemy_positions[idx][1] + 1, cell_size - 2, cell_size - 2])

        if player_pos == enemy_positions[idx]:
            show_loss_screen()
            reset_game()

    pygame.display.update()
    clock.tick(10)

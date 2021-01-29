import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
DISP_PROCESS_WIDTH_BORDER = 105
DISP_PROCESS_HEIGHT_BORDER = 70
DISP_PROCESS_WIDTH = 95
DISP_PROCESS_HEIGHT = 60
MENU_BUTTONS_WIDTH = 95
MENU_BUTTONS_HEIGHT = 525
MENU_BUTTONS_WIDTH_BORDER = 105
MENU_BUTTONS_HEIGHT_BORDER = 530

window = pygame.display.set_mode((WINDOW_WIDTH + DISP_PROCESS_WIDTH_BORDER, WINDOW_HEIGHT))

### Surfaces ###
s = pygame.surface.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
s_menu_border = pygame.surface.Surface((DISP_PROCESS_WIDTH_BORDER, DISP_PROCESS_HEIGHT_BORDER))
s_menu = pygame.surface.Surface((DISP_PROCESS_WIDTH, DISP_PROCESS_HEIGHT))
s_buttons = pygame.surface.Surface((MENU_BUTTONS_WIDTH, MENU_BUTTONS_HEIGHT))
s_buttons_border = pygame.surface.Surface((MENU_BUTTONS_WIDTH_BORDER, MENU_BUTTONS_HEIGHT_BORDER))

### Colors ###
grey = (45, 45, 45)
dark_grey = (30, 30, 30)
black = (0, 0, 0)
light_grey_1 = (70, 70, 70)
light_grey_2 = (155, 155, 155)
red = (150,0,0)

### Fonts ###
pygame.font.init()

def make_font(fonts, size):
    available = pygame.font.get_fonts()
    # get_fonts() returns a list of lowercase spaceless font names
    choices = map(lambda x:x.lower().replace(' ', ''), fonts)
    for choice in choices:
        if choice in available:
            return pygame.font.SysFont(choice, size)
    return pygame.font.Font(None, size)
    
_cached_fonts = {}

def get_font(font_preferences, size):
    global _cached_fonts
    key = str(font_preferences) + '|' + str(size)
    font = _cached_fonts.get(key, None)
    if font == None:
        font = make_font(font_preferences, size)
        _cached_fonts[key] = font
    return font

font_preferences = ["Consolas","Rockwell", "Calibri", "Arial", ]

font_1 = get_font(font_preferences, 12)
font_2 = get_font(font_preferences, 18)
font_3 = get_font(font_preferences, 14)

### Menu ###
def display_processes(processes_count):
    s_menu_border.fill(dark_grey)
    s_menu.fill(light_grey_1)
    
    text_0 = "Processes"
    text_1 = str(processes_count)
    
    text_0_render = font_2.render(text_0, 10, black)
    text_1_render = font_2.render(text_1, 10, light_grey_2)
    s_menu.blit(text_0_render, (4, 10))
    s_menu.blit(text_1_render, (40, 35))
    
    window.blit(s_menu_border, (0, 0))
    window.blit(s_menu, (5, 5))

### Buttons ###
def menu_buttons():
    s_buttons_border.fill(dark_grey)
    s_buttons.fill(light_grey_1)

    text_button_add = "Add"
    text_button_add_render = font_3.render(text_button_add, 10, black)
    s_buttons.blit(text_button_add_render, (33, 20))
    pygame.draw.circle(s_buttons, dark_grey, [47, 70], 30)
    button_add_process = pygame.draw.circle(s_buttons, light_grey_2, [47, 70], 25)

    text_button_add = "Add x10"
    text_button_add_render = font_3.render(text_button_add, 10, black)
    s_buttons.blit(text_button_add_render, (20, 120))
    pygame.draw.circle(s_buttons, dark_grey, [47, 170], 30)
    button_add_x10_process = pygame.draw.circle(s_buttons, light_grey_2, [47, 170], 25)

    text_button_remove = "Remove"
    text_button_remove_render = font_3.render(text_button_remove, 10, black)
    s_buttons.blit(text_button_remove_render, (24, 220))
    pygame.draw.circle(s_buttons, dark_grey, [47, 270], 30)
    button_remove_process = pygame.draw.circle(s_buttons, light_grey_2, [47, 270], 25)

    text_button_remove_all = "Remove All"
    text_button_remove_all_render = font_3.render(text_button_remove_all, 10, black)
    s_buttons.blit(text_button_remove_all_render, (9, 320))
    pygame.draw.circle(s_buttons, dark_grey, [47, 370], 30)
    button_remove_all_process = pygame.draw.circle(s_buttons, light_grey_2, [47, 370], 25)

    pygame.draw.line(s_buttons, dark_grey, (0,430), (105, 430), 5)

    text_button_close = "Quit"
    text_button_close_render = font_3.render(text_button_close, 10, black)
    s_buttons.blit(text_button_close_render, (32, 440))
    pygame.draw.circle(s_buttons, dark_grey, [47, 490], 30)
    button_close = pygame.draw.circle(s_buttons, red, [47, 490], 25)

    window.blit(s_buttons_border, (0, DISP_PROCESS_HEIGHT_BORDER))
    window.blit(s_buttons, (5, DISP_PROCESS_HEIGHT_BORDER))

    return button_add_process, button_add_x10_process, button_remove_process, button_remove_all_process, button_close

button_add_process = menu_buttons()[0]
button_add_x10_process = menu_buttons()[1]
button_remove_process = menu_buttons()[2]
button_remove_all_process = menu_buttons()[3]
button_close = menu_buttons()[4]
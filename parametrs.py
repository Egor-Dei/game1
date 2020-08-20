import pygame
import time
pygame.init()

windowWidth = 400  # 1530
windowHeight = 600  # 800

sizes = [(2560, 1440), (1920, 1200), (1920, 1080), (1280, 800), (1280, 720), (1024, 768), (1024, 600), (960, 540), \
         (854, 480), (800, 480), (480, 320)]

clock = pygame.time.Clock()
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Game")

check_start = True
start_icon_x = int(windowWidth // 2.7)
start_icon_y = int(windowHeight // 3)
start_icon_width = int(windowWidth // 4)
start_icon_height = int(windowHeight // 2)

image_arrow = pygame.image.load("images/arrow.png")
arrow_width, arrow_height = int(windowWidth * 0.03), int(windowHeight * 0.03)
image_arrow = pygame.transform.scale(image_arrow, (arrow_width, arrow_height))

image_demo = pygame.image.load("images/demoversion.png")
demo_width, demo_height = int(windowWidth), int(windowHeight)
image_demo = pygame.transform.scale(image_demo, (demo_width, demo_height))

image_button1 = pygame.image.load("images/button.png")
button1_width, button1_height = int(windowWidth // 10), int(windowHeight // 13)
image_button1 = pygame.transform.scale(image_button1, (button1_width, button1_height))

image_button = pygame.image.load("images/button_new.png")
button_width, button_height = int(windowWidth // 10), int(windowHeight // 13)
image_button = pygame.transform.scale(image_button, (button_width, button_height))

image_phon = pygame.image.load("images/phon.jpg")
image_phon = pygame.transform.scale(image_phon, (windowWidth, windowHeight))

image_card1 = pygame.image.load("images/card1.png")
card_width, card_height = int(windowWidth // 3), int(2 * windowHeight // 3)
image_card1 = pygame.transform.scale(image_card1, (card_width, card_height))

image_card2 = pygame.image.load("images/card2.png")
image_card2 = pygame.transform.scale(image_card2, (card_width, card_height))

image_bomb1 = pygame.image.load("images/bomb1.png")
image_bomb1 = pygame.transform.scale(image_bomb1, (card_width, card_height))

image_bomb2 = pygame.image.load("images/bomb2.png")
image_bomb2 = pygame.transform.scale(image_bomb2, (card_width, card_height))

image_bomb3 = pygame.image.load("images/bomb3.png")
image_bomb3 = pygame.transform.scale(image_bomb3, (card_width, card_height))

image_card3 = pygame.image.load("images/card3.png")
image_card3 = pygame.transform.scale(image_card3, (card_width, card_height))

image_button_no = pygame.image.load("images/button_no.png")
mini_button_width, mini_button_height = int(card_width // 5), int(card_width // 5)
image_button_no = pygame.transform.scale(image_button_no, (mini_button_width, mini_button_height))

image_button_yes = pygame.image.load("images/button_yes.png")
image_button_yes = pygame.transform.scale(image_button_yes, (mini_button_width, mini_button_height))

image_number = pygame.image.load("images/icon_number.png")
image_number = pygame.transform.scale(image_number, (mini_button_width, mini_button_height))

image_button_exit = pygame.image.load("images/exit.png")
exit_width, exit_height = int(card_width // 25), int(card_width // 25)
image_button_exit = pygame.transform.scale(image_button_exit, (exit_width, exit_height))

image_start_icon = pygame.image.load("images/start_icon.png")
start_icon2_width, start_icon2_height = int(windowWidth // 2), int(windowHeight // 2)
image_start_icon = pygame.transform.scale(image_start_icon, (start_icon2_width, start_icon2_height))

image_display = pygame.image.load("images/image_display.png")
display_width, display_height = int(windowWidth // 3), int(windowHeight // 2)
image_display = pygame.transform.scale(image_display, (display_width, display_height))

image_gamer = pygame.image.load("images/gamers.png")
gamer_width, gamer_height = int(windowWidth // 6), int(windowHeight // 8)
image_gamer = pygame.transform.scale(image_gamer, (gamer_width, gamer_height))

pygame.display.set_icon(image_start_icon)

pygame.mixer.init()
sound_button = pygame.mixer.Sound("SoundsAndMusics/button.wav")

command_count = 2
field_size = 2

command_click_check = False

field_width = int(0.7 * windowHeight)
cell_width = int(0.8 * field_width // field_size)
cell_space = int(0.1 * field_width // field_size)
field_x = int(windowWidth // 2 - field_width // 2 + cell_space // 2)
field_y = int(0.15 * windowHeight)

fields = [[], []]

need_input_name = False
input_tick = 30
enter = False

name_of_game = "НАЖМИТЕ ДЛЯ ВВОДА НАЗВАНИЯ ИГРЫ"

commands = []

time_click = time.time()

check_continue = 0

button_name_x = int(windowWidth // 3.6)
button_name_y = int(0.01 * windowHeight)
button_name_width = int(windowWidth // 2.5)
button_name_height = int(windowHeight // 14)

final_cells = 0

cards = [image_card1, image_card2, image_card3]
bombs = [image_bomb1, image_bomb2, image_bomb3]

final_code = "НАЖМИТЕ СЮДА"

keys = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8]

check_full_version = False

check_end = False
MANUAL_CURSOR = pygame.image.load('Images/cursor.png').convert_alpha()

demo_check = True

all_quests = []
with open("quests.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        all_quests.append(line.replace("\n", ""))


def init():
    global clock, window, check_start, start_icon_x, start_icon_width, start_icon_height, start_icon_y, image_button, \
        image_gamer, image_display, image_phon, image_button_exit, image_button_yes, image_bomb1, image_card3, \
        image_card2, image_card1, image_start_icon, image_number, image_button1, image_bomb2, image_bomb3, button1_height, \
        button1_width, button_height, button_width, card_width, card_height, image_button_no, mini_button_height, \
        mini_button_width, exit_height, exit_width, start_icon2_height, start_icon2_width, display_height, \
        display_width, gamer_width, gamer_height, field_x, field_y, field_width, cell_space, cell_width, button_name_x, \
        button_name_y, button_name_width, button_name_height, cards, bombs, windowHeight, windowWidth, MANUAL_CURSOR, \
        image_demo, demo_width, demo_height, image_arrow, arrow_width, arrow_height

    window = pygame.display.set_mode((windowWidth, windowHeight), pygame.FULLSCREEN | pygame.HWSURFACE)

    start_icon_x = int(windowWidth // 2.7)
    start_icon_y = int(windowHeight // 3)
    start_icon_width = int(windowWidth // 4)
    start_icon_height = int(windowHeight // 2)

    pygame.mouse.set_visible(False)
    MANUAL_CURSOR = pygame.transform.scale(MANUAL_CURSOR, (int(windowWidth // 80), int(windowHeight // 50)))

    image_button1 = pygame.image.load("images/button.png")
    button1_width, button1_height = int(windowWidth // 10), int(windowHeight // 13)
    image_button1 = pygame.transform.scale(image_button1, (button1_width, button1_height))

    image_button = pygame.image.load("images/button_new.png")
    button_width, button_height = int(windowWidth // 10), int(windowHeight // 13)
    image_button = pygame.transform.scale(image_button, (button_width, button_height))

    image_phon = pygame.image.load("images/phon.jpg")
    image_phon = pygame.transform.scale(image_phon, (windowWidth, windowHeight))

    image_card1 = pygame.image.load("images/card1.png")
    card_width, card_height = int(windowWidth // 3), int(2 * windowHeight // 3)
    image_card1 = pygame.transform.scale(image_card1, (card_width, card_height))

    image_card2 = pygame.image.load("images/card2.png")
    image_card2 = pygame.transform.scale(image_card2, (card_width, card_height))

    image_bomb1 = pygame.image.load("images/bomb1.png")
    image_bomb1 = pygame.transform.scale(image_bomb1, (card_width, card_height))

    image_bomb2 = pygame.image.load("images/bomb2.png")
    image_bomb2 = pygame.transform.scale(image_bomb2, (card_width, card_height))

    image_bomb3 = pygame.image.load("images/bomb3.png")
    image_bomb3 = pygame.transform.scale(image_bomb3, (card_width, card_height))

    image_card3 = pygame.image.load("images/card3.png")
    image_card3 = pygame.transform.scale(image_card3, (card_width, card_height))

    image_button_no = pygame.image.load("images/button_no.png")
    mini_button_width, mini_button_height = int(card_width // 5), int(card_width // 5)
    image_button_no = pygame.transform.scale(image_button_no, (mini_button_width, mini_button_height))

    image_button_yes = pygame.image.load("images/button_yes.png")
    image_button_yes = pygame.transform.scale(image_button_yes, (mini_button_width, mini_button_height))

    image_number = pygame.image.load("images/icon_number.png")
    image_number = pygame.transform.scale(image_number, (mini_button_width, mini_button_height))

    image_button_exit = pygame.image.load("images/exit.png")
    exit_width, exit_height = int(card_width // 25), int(card_width // 25)
    image_button_exit = pygame.transform.scale(image_button_exit, (exit_width, exit_height))

    image_start_icon = pygame.image.load("images/start_icon.png")
    start_icon2_width, start_icon2_height = int(windowWidth // 2), int(windowHeight // 2)
    image_start_icon = pygame.transform.scale(image_start_icon, (start_icon2_width, start_icon2_height))

    image_display = pygame.image.load("images/image_display.png")
    display_width, display_height = int(windowWidth // 3), int(windowHeight // 2)
    image_display = pygame.transform.scale(image_display, (display_width, display_height))

    image_gamer = pygame.image.load("images/gamers.png")
    gamer_width, gamer_height = int(windowWidth // 5), int(windowHeight // 8)
    image_gamer = pygame.transform.scale(image_gamer, (gamer_width, gamer_height))

    image_arrow = pygame.image.load("images/arrow.png")
    arrow_width, arrow_height = int(windowWidth * 0.03), int(windowHeight * 0.03)
    image_arrow = pygame.transform.scale(image_arrow, (arrow_width, arrow_height))

    field_width = int(0.7 * windowHeight)
    cell_width = int(0.8 * field_width // field_size)
    cell_space = int(0.1 * field_width // field_size)
    field_x = int(windowWidth // 2 - field_width // 2 + cell_space // 2)
    field_y = int(0.15 * windowHeight)

    button_name_x = int(windowWidth // 3.6)
    button_name_y = int(0.01 * windowHeight)
    button_name_width = int(windowWidth // 2.5)
    button_name_height = int(windowHeight // 14)

    cards = [image_card1, image_card2, image_card3]
    bombs = [image_bomb1, image_bomb2, image_bomb3]

    demo_width, demo_height = int(windowWidth), int(windowHeight)
    image_demo = pygame.transform.scale(image_demo, (demo_width, demo_height))

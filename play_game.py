import main_menu
import pygame
import parametrs
import printtext
import button
import sys

buttons = []

width, height = parametrs.sizes[4][0], parametrs.sizes[4][1]
size_index = 4

for i in range(11):
    buttons.append(button.Button(parametrs.image_button1, int(parametrs.windowWidth * 2 // 3), \
                                 int(parametrs.windowHeight // 15),
                                 str(parametrs.sizes[i][0]) + "x" + str(parametrs.sizes[i][1])))
button_start = button.Button(parametrs.image_button, int(parametrs.windowWidth // 2), int(parametrs.windowHeight * 0.1), \
                             "Начать игру")


def play():
    def click(index):
        global width, height, size_index
        width, height = parametrs.sizes[index][0], parametrs.sizes[index][1]
        size_index = index

    def start_game(kort):
        global buttons, width, height, size_index, button_start
        parametrs.windowWidth, parametrs.windowHeight = kort
        try:
            main_menu.menu()

        except:
            parametrs.windowWidth = 400  # 1530
            parametrs.windowHeight = 600  # 800
            parametrs.window = pygame.display.set_mode((parametrs.windowWidth, parametrs.windowHeight))
            buttons = []

            width, height = parametrs.sizes[4][0], parametrs.sizes[4][1]
            size_index = 4

            for i in range(11):
                buttons.append(button.Button(parametrs.image_button1, int(parametrs.windowWidth * 2 // 3), \
                                             int(parametrs.windowHeight // 15),
                                             str(parametrs.sizes[i][0]) + "x" + str(parametrs.sizes[i][1])))
            button_start = button.Button(parametrs.image_button, int(parametrs.windowWidth // 2),
                                         int(parametrs.windowHeight * 0.1), \
                                         "Начать игру")
            play()

    check = True
    while check:
        parametrs.window.fill((255, 255, 255))
        printtext.print_text2("Выберите разрешение экрана", int(parametrs.windowWidth // 2), \
                              int(parametrs.windowHeight // 16), int(parametrs.windowHeight // 25), font_color=(0, 0, 0))
        n = 0
        for i in range(len(buttons)):
            x = int(parametrs.windowWidth // 2 - buttons[i].width // 2)
            y = int(parametrs.windowHeight // 10 + n)
            color = (255, 255, 255)
            if i == size_index:
                color = (0, 0, 0)
            buttons[i].print2(x, y, int(buttons[i].height * 0.7), color1=color, color2=(0, 0, 0), func=click, other=i)
            n += buttons[i].height
        button_start.print2(int(parametrs.windowWidth // 2 - button_start.width // 2), int(parametrs.windowHeight * 0.85), \
                            int(button_start.height * 0.5), color1=(0, 0, 0), color2=(0, 0, 255), func=start_game,\
                             other=(width, height))
        printtext.print_text2("Если не запускается, то разрешение не поддерживается. Выберите другое", \
                              int(parametrs.windowWidth // 2), int(parametrs.windowHeight * 0.975), \
                              (parametrs.windowHeight // 50), font_type="Fonts/Lilita-One-Russian.ttf")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4 and event.mod == pygame.KMOD_LALT:
                    pygame.quit()
                    sys.exit(0)

        pygame.display.update()
        parametrs.clock.tick(60)


play()

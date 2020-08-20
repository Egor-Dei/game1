import pygame
import parametrs
import button
import printtext
import commandmenu
import fieldsizemenu
import cells
import texts
import gamers
import final_game
import name_game
import demo_view
import pause
import sys


def click_continue():
    if parametrs.field_size**2 >= parametrs.command_count:
        parametrs.check_start = False


def game():
    button_of_continue = button.Button(parametrs.image_button, int(2.2 * parametrs.button1_width),
                                       int(parametrs.button1_height * 0.85), \
                                       "НАЧАТЬ ИГРУ")
    check_on_field = True
    check = True
    parametrs.check_start = True
    while check:
        parametrs.window.blit(parametrs.image_phon, (0, 0))
        conti = False
        if parametrs.check_start:
            button_of_count = button.Button(parametrs.image_button1, parametrs.button1_width, parametrs.button1_height, \
                                            str(parametrs.command_count))
            button_of_field = button.Button(parametrs.image_button1, parametrs.button1_width, parametrs.button1_height, \
                                            str(parametrs.field_size) + " x " + str(parametrs.field_size))
            button_field_setting = button.Button(parametrs.image_button1, int(2 * parametrs.button1_width), \
                                                 parametrs.button1_height, "ДАЛЕЕ")

            printtext.print_text2("НАСТРОЙКА ИГРЫ", int(parametrs.start_icon_x + parametrs.start_icon_width // 2), \
                                 int(parametrs.start_icon_y + parametrs.start_icon_height // 10), \
                                 int(parametrs.start_icon_height // 10), (25, 25, 112))
            printtext.print_text("КОЛИЧЕСТВО", int(parametrs.start_icon_x + parametrs.start_icon_width // 10), \
                                 int(parametrs.start_icon_y + parametrs.start_icon_height // 3.6), int(parametrs.button1_height \
                                 // 4), (25, 25, 112))
            printtext.print_text("КОМАНД", int(parametrs.start_icon_x + parametrs.start_icon_width // 7), \
                                 int(parametrs.start_icon_y + parametrs.start_icon_height // 3.2), int(parametrs.button1_height \
                                 // 4), (25, 25, 112))
            button_of_count.print2(int(parametrs.start_icon_x + parametrs.start_icon_width // 2), \
                                            int(parametrs.start_icon_y + parametrs.start_icon_height // 4), \
                                            int(0.7 * button_of_count.height), commandmenu.draw_menu, color1=(255, 255, 255))

            printtext.print_text("РАЗМЕР", int(parametrs.start_icon_x + parametrs.start_icon_width // 5.8), \
                                 int(parametrs.start_icon_y + parametrs.start_icon_height // 1.9), int(parametrs.button1_height \
                                 // 4), (25, 25, 112))
            printtext.print_text("ПОЛЯ", int(parametrs.start_icon_x + parametrs.start_icon_width // 5), \
                                 int(parametrs.start_icon_y + parametrs.start_icon_height // 1.8), int(parametrs.button1_height \
                                 // 4), (25, 25, 112))
            button_of_field.print2(int(parametrs.start_icon_x + parametrs.start_icon_width // 2), \
                                  int(parametrs.start_icon_y + parametrs.start_icon_height // 2), \
                                  int(0.7 * button_of_field.height), fieldsizemenu.draw_menu, color1=(255, 255, 255))
            button_field_setting.print2(int(parametrs.start_icon_x + parametrs.start_icon_width // 7), \
                                  int(parametrs.start_icon_y + 0.8 * parametrs.start_icon_height), \
                                  int(0.7 * button_field_setting.height), click_continue, color1=(255, 255, 255))
            printtext.print_text2("*Количество ячеек должно быть не меньше количества команд", int(parametrs.windowWidth // 2), \
                                  int(parametrs.windowHeight * 0.95), int(parametrs.windowHeight * 0.025), font_color=(255, 255, 255))

            if commandmenu.click_on_menu:
                commandmenu.draw_menu()

            if fieldsizemenu.click_on_menu:
                fieldsizemenu.draw_menu()
        else:
            if check_on_field:
                parametrs.cell_width = int(0.8 * parametrs.field_width // parametrs.field_size)
                parametrs.cell_space = int(0.1 * parametrs.field_width // parametrs.field_size)
                parametrs.field_x = int(parametrs.windowWidth // 2 - parametrs.field_width // 2 + parametrs.cell_space)

                commandmenu.click_on_menu = False
                fieldsizemenu.click_on_menu = False
                n = 0
                if parametrs.command_count == 2:
                    n = int(parametrs.windowHeight // 3)
                for i in range(parametrs.command_count):
                    color = (128, 0, 0)
                    if i == 1:
                        color = (0, 128, 0)
                    elif i == 2:
                        color = (0, 0, 128)
                    elif i == 3:
                        color = (128, 128, 0)
                    elif i == 4:
                        color = (128, 0, 128)
                    elif i == 5:
                        color = (0, 255, 0)
                    elif i == 6:
                        color = (255, 0, 0)
                    elif i == 7:
                        color = (0, 0, 255)
                    if i % 2 == 0:
                        x = int(parametrs.windowWidth // 8)
                    else:
                        x = int(7 * parametrs.windowWidth // 8)
                    parametrs.commands.append(gamers.Gamer("КОМАНДА " + str(i + 1), x, int(parametrs.windowHeight // 7 + n),  \
                                                           int(parametrs.windowHeight // 20), 0, color))
                    if parametrs.command_count % 2 == 1:
                        n += int(0.8 * parametrs.windowHeight // parametrs.command_count)
                    elif parametrs.command_count % 2 == 0 and i % 2 == 1:
                        n += int(0.8 * parametrs.windowHeight // parametrs.command_count * 2)
                parametrs.fields = [[] for i in range(parametrs.field_size)]
                check_on_field = False
                parametrs.cell_width = int(0.8 * parametrs.field_width // parametrs.field_size)
                parametrs.cell_space = int(0.2 * parametrs.field_width // parametrs.field_size)
                numb = 1
                for i in range(len(parametrs.fields)):
                    for j in range(parametrs.field_size):
                        parametrs.fields[i].append(cells.Cell((255, 255, 255), parametrs.cell_width, numb))
                        numb += 1
                parametrs.check_continue = parametrs.field_size**2

            for i in range(parametrs.command_count):
                parametrs.commands[i].print()
                if i % 2 == 0:
                    parametrs.window.blit(pygame.transform.rotate(parametrs.image_arrow, 180), \
                                      (parametrs.commands[i].x + parametrs.gamer_width * 0.5, \
                                       parametrs.commands[i].y - parametrs.arrow_height // 2))
                else:
                    parametrs.window.blit(parametrs.image_arrow, \
                                          (parametrs.commands[i].x - parametrs.gamer_width * 0.5 - parametrs.arrow_width,
                                           parametrs.commands[i].y - parametrs.arrow_height // 2))

            check = name_game.name_draw()
            parametrs.window.blit(pygame.transform.rotate(parametrs.image_arrow, 90), \
                                  (int(parametrs.windowWidth // 2 - parametrs.arrow_height // 2), \
                                  int(parametrs.windowHeight // 16 + parametrs.windowHeight // 50)))
            if not check:
                break
            mouse = pygame.mouse.get_pos()  # для получения координат стрелки мышки
            click = pygame.mouse.get_pressed()

            x, y = parametrs.field_x, parametrs.field_y
            for i in range(len(parametrs.fields)):
                for j in range(parametrs.field_size):
                    conti = parametrs.fields[i][j].print(x, y, int(parametrs.fields[i][j].width // 4), \
                                                 parametrs.fields[i][j].print_window)

                    x += int(parametrs.cell_width + parametrs.cell_space)
                if conti:
                    break
                y += int(parametrs.cell_width + parametrs.cell_space)
                x = parametrs.field_x
            if conti:
                continue
            if parametrs.check_continue == parametrs.field_size ** 2:
                check = button_of_continue.print2(int(0.7 * parametrs.windowWidth), int(parametrs.windowHeight // 150), \
                                                  int(0.7 * button_of_continue.height), final_game.game)
            if not check:
                break
            for i in range(parametrs.command_count):
                x, y, width, height = parametrs.commands[i].x, parametrs.commands[i].y, parametrs.gamer_width, \
                                      parametrs.gamer_height

                need_input = False
                if x - width // 2 <= mouse[0] <= x + width // 2 and y - height // 2 <= mouse[1] <= y + height // 2:
                    if click[0]:
                        need_input = True
                        parametrs.commands[i].name = ""
                while need_input:
                    parametrs.commands[i].print()
                    parametrs.commands[i].name, need_input = texts.input_txt(parametrs.commands[i].name, \
                                                                             need_input, 10)
                    parametrs.input_tick -= 1
                    demo_view.view()
                    if check:
                        check = pause.pause()
                    if not check:
                        break
                    if parametrs.check_end:
                        break
                    pygame.display.update()
            printtext.print_text2("*Нажмите на ячейки, чтобы их настроить", int(parametrs.windowWidth // 2), \
                                  int(parametrs.windowHeight * 0.94), int(parametrs.windowHeight * 0.025), (255, 255, 255))
            printtext.print_text2("**Выберите названия команд и игры", int(parametrs.windowWidth // 2), \
                                  int(parametrs.windowHeight * 0.96), int(parametrs.windowHeight * 0.025),
                                  (255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4 and event.mod == pygame.KMOD_LALT:
                    pygame.quit()
                    sys.exit(0)
        demo_view.view()
        if check:
            check = pause.pause()
        if parametrs.check_end:
            break
        parametrs.window.blit(parametrs.MANUAL_CURSOR, (pygame.mouse.get_pos()))
        pygame.display.update()
        parametrs.clock.tick(60)

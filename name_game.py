import pygame
import printtext
import parametrs
import texts
import demo_view
import pause


def name_draw():
    name_width, name_height = printtext.print_text2(parametrs.name_of_game, int(parametrs.windowWidth // 2), int(parametrs.windowHeight // 16), \
                         int(parametrs.windowHeight // 25), (255, 255, 255), other="name")
    name_x, name_y = int(parametrs.windowWidth // 2 - name_width // 2), int(parametrs.windowHeight // 16 - name_height // 2)
    printtext.print_text2(parametrs.name_of_game, int(parametrs.windowWidth // 2), int(parametrs.windowHeight // 16), \
                         int(parametrs.windowHeight // 25), (255, 255, 255))

    mouse = pygame.mouse.get_pos()  # для получения координат стрелки мышки
    click = pygame.mouse.get_pressed()

    if name_x <= mouse[0] <= name_x + name_width and name_y <= mouse[1] <= name_y + name_height:
        if click[0] == 1:
            parametrs.need_input_name = True
            parametrs.name_of_game = ""

    while parametrs.need_input_name:
        parametrs.window.blit(parametrs.image_phon, (0, 0))

        for i in range(parametrs.command_count):
            parametrs.commands[i].print()

        x, y = parametrs.field_x, parametrs.field_y
        for i in range(len(parametrs.fields)):
            for j in range(parametrs.field_size):
                parametrs.fields[i][j].print(x, y, int(parametrs.fields[i][j].width // 4))

                x += int(parametrs.cell_width + parametrs.cell_space)
            y += int(parametrs.cell_width + parametrs.cell_space)
            x = parametrs.field_x

        printtext.print_text2(parametrs.name_of_game, int(parametrs.windowWidth // 2),
                              int(parametrs.windowHeight // 16), \
                              int(parametrs.windowHeight // 25), (255, 255, 255))
        parametrs.name_of_game, parametrs.need_input_name = texts.input_txt(parametrs.name_of_game, \
                                                                            parametrs.need_input_name, 35)
        parametrs.input_tick -= 3
        demo_view.view()
        if not pause.pause():
            parametrs.need_input_name = False
            return False
        if parametrs.check_end:
            break
        pygame.display.update()
    if parametrs.name_of_game == "":
        parametrs.name_of_game = "НАЖМИТЕ ДЛЯ ВВОДА НАЗВАНИЯ ИГРЫ"
    return True

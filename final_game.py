import pygame
import parametrs
import printtext
import button
import end_of_game
import demo_view
import pause
import sys


def game():
    check = True
    command_index = 0
    need_input_command_numb = False
    points = 0
    while check:
        conti = 0
        parametrs.window.blit(parametrs.image_phon, (0, 0))

        for i in range(parametrs.command_count):
            parametrs.commands[i].print()

        printtext.print_text2(parametrs.name_of_game, int(parametrs.windowWidth // 2),
                              int(parametrs.windowHeight // 16), int(parametrs.windowHeight // 25), (255, 255, 255))

        x, y = parametrs.field_x, parametrs.field_y
        for i in range(len(parametrs.fields)):
            for j in range(parametrs.field_size):
                conti = parametrs.fields[i][j].print(x, y, int(parametrs.fields[i][j].width // 4), \
                                                     parametrs.fields[i][j].print_game_window, setting_click=False)
                if not need_input_command_numb:
                    if conti == 1:
                        if parametrs.fields[i][j].cards == parametrs.cards:
                            if parametrs.fields[i][j].color != (255, 0, 0):
                                points = 1 + parametrs.fields[i][j].type_numb
                        else:
                            if parametrs.fields[i][j].color != (0, 255, 0):
                                points = -1 - parametrs.fields[i][j].type_numb
                        need_input_command_numb = True
                if conti != 0:
                    break
                x += int(parametrs.cell_width + parametrs.cell_space)
            if conti != 0:
                break
            y += int(parametrs.cell_width + parametrs.cell_space)
            x = parametrs.field_x

        if conti != 0:
            continue

        if parametrs.final_cells == parametrs.field_size**2:
            end_width, end_height = printtext.print_text2("ЗАКОНЧИТЬ ИГРУ", font_size=int(parametrs.windowHeight // 20), \
                                                          other=True)
            button_end = button.Button(parametrs.image_button, int(end_width), int(end_height), "ЗАКОНЧИТЬ ИГРУ")
            check = button_end.print2(int(0.72 * parametrs.windowWidth), int(parametrs.windowHeight // 150), \
                                      int(button_end.height * 0.7), end_of_game.end)
        if not check:
            break
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

        if need_input_command_numb:
            parametrs.commands[command_index].points = str(int(parametrs.commands[command_index].points) + points)
            need_input_command_numb = False
            points = 0
            command_index += 1
            if command_index >= parametrs.command_count:
                command_index = 0

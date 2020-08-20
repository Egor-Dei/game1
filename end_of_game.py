import parametrs
import pygame
import printtext
import button
import demo_view
import pause
import sys

menu_width, menu_height = printtext.print_text2("В главное меню", font_size=int(parametrs.windowHeight // 16), other=True)
button_menu = button.Button(parametrs.image_button1, int(menu_width), int(menu_height), "В главное меню")


def end():
    check = True
    while check:
        parametrs.window.blit(parametrs.image_phon, (0, 0))

        printtext.print_text2("Рейтинг", int(parametrs.windowWidth // 2), int(parametrs.windowHeight // 5), \
                              int(parametrs.windowHeight // 16), font_color=(255, 255, 255))

        indexs = []
        for i in range(parametrs.command_count):
            max_index = 0
            max_points = 0
            for j in range(parametrs.command_count):
                if int(parametrs.commands[j].points) >= max_points and j not in indexs:
                    max_points = int(parametrs.commands[j].points)
                    max_index = j
            indexs.append(max_index)
        n = 0
        ind = 0
        for j in indexs:
            color = (25, 25, 112)
            if ind == 0:
                color = (255, 0, 0)
            elif ind == 1:
                color = (0, 255, 0)
            elif ind == 2:
                color = (0, 0, 255)
            printtext.print_text(str(ind + 1) + ") " + parametrs.commands[j].name + ": " + parametrs.commands[j].points, \
                                 int(0.4 * parametrs.windowWidth), int(0.25 * parametrs.windowHeight + n), \
                                 int(parametrs.windowHeight // 24), color)
            n += int(1.1 * parametrs.commands[j].height)
            ind += 1

        check = button_menu.print2(int(parametrs.windowWidth // 2 - button_menu.width // 2), int(7 * parametrs.windowHeight // 8), \
                                   int(button_menu.height * 0.7), check_click_end, color1=(255, 255, 255))

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


def check_click_end():
    parametrs.check_end = True
    return False

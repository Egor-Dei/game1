import parametrs
import button
import demo_view
import pygame
import sys


def click():
    return False


def run():
    to_game = button.Button(parametrs.image_button, int(parametrs.display_width * 2 // 3),
                            int(parametrs.display_height // 5), \
                            "В ИГРУ")
    to_menu = button.Button(parametrs.image_button, int(parametrs.display_width * 2 // 3),
                            int(parametrs.display_height // 5), \
                            "В МЕНЮ")

    check = True
    while check:
        parametrs.window.blit(parametrs.image_phon, (0, 0))
        parametrs.window.blit(parametrs.image_display, (int(parametrs.windowWidth // 2 - parametrs.display_width // 2), \
                                                        int(parametrs.windowHeight // 2 - parametrs.display_height // 2)))
        check = to_game.print2(int(parametrs.windowWidth // 2 - to_game.width // 2), \
                       int(parametrs.windowHeight // 2 - parametrs.display_height // 4 - to_game.height // 2), \
                       int(to_game.height * 0.7), click)
        if not check:
            return True

        if not to_menu.print2(int(parametrs.windowWidth // 2 - to_game.width // 2), \
                       int(parametrs.windowHeight // 2 + parametrs.display_height // 4 - to_game.height // 2), \
                       int(to_game.height * 0.7), click):
            parametrs.check_end = True
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
        parametrs.window.blit(parametrs.MANUAL_CURSOR, (pygame.mouse.get_pos()))
        pygame.display.update()
        parametrs.clock.tick(60)


def pause():
    to_pause = button.Button(parametrs.image_button, int(parametrs.display_width * 2 // 3),
                             int(parametrs.display_height // 8), \
                             "ПАУЗА")
    return to_pause.print2(int(parametrs.windowWidth // 100), int(parametrs.windowHeight // 150), int(to_pause.height * 0.7), run)
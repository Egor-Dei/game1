import pygame
import parametrs
import button
import game
import generate_code
import check_generate_code
import demo_view
import pickle
import sys
pygame.init()


def quit_game():
    pygame.quit()
    sys.exit(0)


def menu():
    parametrs.init()
    button_play = button.Button(parametrs.image_button, int(parametrs.windowWidth // 3), \
                                int(parametrs.windowHeight // 16), "Играть")

    button_quit = button.Button(parametrs.image_button, int(parametrs.windowWidth // 3), \
                                int(parametrs.windowHeight // 16), "Выход")

    button_demo = button.Button(parametrs.image_button, int(parametrs.windowWidth // 3), \
                                int(parametrs.windowHeight // 16), "Демоверсия")
    try:
        with open('file.bin', "rb") as f:
            line = pickle.load(f)
            line = line.rstrip()
            parametrs.check_full_version = check_generate_code.check_code(line)
            if parametrs.check_full_version:
                parametrs.final_code = line
            f.close()
    except Exception:
        pass

    file = "SoundsAndMusics/phon_music.ogg"
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1)
    except Exception:
        pass
    check = True
    parametrs.demo_check = True
    while check:
        if parametrs.demo_check:
            with open('file.bin', "wb") as f:
                pickle.dump(parametrs.final_code, f)
            parametrs.demo_check = False

        parametrs.window.blit(parametrs.image_phon, (0, 0))
        parametrs.window.blit(parametrs.image_start_icon, (int(parametrs.windowWidth // 4), \
                                                           int(parametrs.windowHeight // 16)))

        demo_view.view()
        parametrs.commands.clear()
        parametrs.fields.clear()
        parametrs.command_click_check = False
        parametrs.check_continue = 0
        parametrs.final_cells = 0
        parametrs.field_size = 2
        parametrs.command_count = 2
        parametrs.need_input_name = False
        parametrs.input_tick = 30
        parametrs.enter = False
        parametrs.check_end = False
        parametrs.name_of_game = "НАЖМИТЕ ДЛЯ ВВОДА НАЗВАНИЯ ИГРЫ"
        b_p_x, b_p_y = int(parametrs.windowWidth // 8), int(2 * parametrs.windowHeight // 3)
        button_play.print2(b_p_x, b_p_y, int(0.8 * button_play.height), game.game, type="Fonts/Lilita-One-Russian.ttf")
        b_q_x, b_q_y = int(parametrs.windowWidth // 2 - button_quit.width // 2), int(parametrs.windowHeight * 3 // 4 + \
                                                                                     1.1 * button_play.height)
        button_quit.print2(b_q_x, b_q_y, int(0.8 * button_quit.height), quit_game, type="Fonts/Lilita-One-Russian.ttf")
        b_d_x, b_d_y = int(0.55 * parametrs.windowWidth), int(parametrs.windowHeight * 3 // 4.5)
        button_demo.print2(b_d_x, b_d_y, int(0.8 * button_demo.height), generate_code.code, type="Fonts/Lilita-One-Russian.ttf")

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
        parametrs.check_end = False

import uuid
import parametrs
import pygame
import button
import printtext
import texts
import check_generate_code
import demo_view
import time
import sys


def click0():
    return False


mac_addr = hex(uuid.getnode()).replace('0x', '')
new_code = check_generate_code.generate(mac_addr)


def code():
    button_exit = button.Button(parametrs.image_button, int(parametrs.windowWidth // 3), \
                                int(parametrs.windowHeight // 16), "В главное меню")
    check_time = time.time()
    check = True
    while check:
        parametrs.window.blit(parametrs.image_phon, (0, 0))
        parametrs.window.blit(parametrs.image_start_icon, (int(parametrs.windowWidth // 4), \
                                                           int(parametrs.windowHeight // 16)))

        printtext.print_text2("Код для отправки", int(parametrs.windowWidth // 4), int(parametrs.windowHeight * 0.6), \
                              (parametrs.windowHeight // 30), font_type="Fonts/Lilita-One-Russian.ttf")
        printtext.print_text2(str(new_code), int(parametrs.windowWidth // 4), int(parametrs.windowHeight * 0.6 + \
                                                                                  parametrs.windowHeight // 16), \
                              int(parametrs.windowHeight // 30), font_type="Fonts/Lilita-One-Russian.ttf")
        printtext.print_text2("Введите код для снятия демоверсии", int(parametrs.windowWidth * 3 // 4), \
                              int(parametrs.windowHeight * 0.6), int(parametrs.windowHeight // 30), font_type="Fonts/Lilita-One-Russian.ttf")
        width, height = printtext.print_text2(str(parametrs.final_code), font_size=int(parametrs.windowHeight // 30), \
                                                    other="name", font_type="Fonts/Lilita-One-Russian.ttf")
        x, y = int(parametrs.windowWidth * 3 // 4 - width // 2), int(parametrs.windowHeight * 0.6 + \
                                                                     parametrs.windowHeight // 16 - height // 2)

        if parametrs.final_code == "" or parametrs.final_code == "|":
            # pygame.draw.rect(parametrs.window, (128, 128, 128), (x, y, 0.01 * parametrs.windowWidth, height))
            parametrs.final_code = "НАЖМИТЕ СЮДА"
        printtext.print_text2(str(parametrs.final_code), int(x + width // 2), int(y + height // 2), \
                              int(parametrs.windowHeight // 30), font_type="Fonts/Lilita-One-Russian.ttf")

        mouse = pygame.mouse.get_pos()  # для получения координат стрелки мышки
        click = pygame.mouse.get_pressed()
        if x <= mouse[0] <= x + width and y <= mouse[1] <= y + height:
            if click[0] and time.time() - check_time >= 0.7:
                parametrs.need_input_name = True
                if parametrs.final_code == "НАЖМИТЕ СЮДА":
                    parametrs.final_code = ""

        while parametrs.need_input_name:
            parametrs.window.blit(parametrs.image_phon, (0, 0))
            parametrs.window.blit(parametrs.image_start_icon, (int(parametrs.windowWidth // 4), \
                                                               int(parametrs.windowHeight // 16)))

            printtext.print_text2("Код для отправки", int(parametrs.windowWidth // 4),
                                  int(parametrs.windowHeight * 0.6), int(parametrs.windowHeight // 30), \
                                  font_type="Fonts/Lilita-One-Russian.ttf")
            printtext.print_text2(str(new_code), int(parametrs.windowWidth // 4), int(parametrs.windowHeight * 0.6 + \
                                                                                      parametrs.windowHeight // 16), \
                                  int(parametrs.windowHeight // 30), font_type="Fonts/Lilita-One-Russian.ttf")
            printtext.print_text2("Введите код для снятия демоверсии", int(parametrs.windowWidth * 3 // 4), \
                                  int(parametrs.windowHeight * 0.6), int(parametrs.windowHeight // 30), \
                                  font_type="Fonts/Lilita-One-Russian.ttf")
            width, height = printtext.print_text2(str(parametrs.final_code),
                                                  font_size=int(parametrs.windowHeight // 30), \
                                                  other="name", font_type="Fonts/Lilita-One-Russian.ttf")
            x, y = int(parametrs.windowWidth * 3 // 4 - width // 2), int(parametrs.windowHeight * 0.6 + \
                                                                         parametrs.windowHeight // 16 - height // 2)

            printtext.print_text2(str(parametrs.final_code), int(x + width // 2), int(y + height // 2), \
                                  int(parametrs.windowHeight // 30), font_type="Fonts/Lilita-One-Russian.ttf")

            button_exit.print2(int(parametrs.windowWidth // 2 - button_exit.width // 2), \
                                       int(parametrs.windowHeight * 0.8 - button_exit.height // 2), \
                                       int(button_exit.height * 0.7), type="Fonts/Lilita-One-Russian.ttf")

            parametrs.final_code, parametrs.need_input_name = texts.input_txt(
                str(parametrs.final_code), parametrs.need_input_name, 20)
            parametrs.final_code = parametrs.final_code
            parametrs.input_tick -= 2

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F4 and event.mod == pygame.KMOD_LALT:
                        pygame.quit()
                        sys.exit(0)
            demo_view.view()
            if not check:
                parametrs.need_input_name = False
                break
            pygame.display.update()
        if not check:
            break
        parametrs.check_full_version = check_generate_code.check_code(parametrs.final_code)
        check = button_exit.print2(int(parametrs.windowWidth // 2 - button_exit.width // 2), \
                                   int(parametrs.windowHeight * 0.8 - button_exit.height // 2), \
                                   int(button_exit.height * 0.7), click0, type="Fonts/Lilita-One-Russian.ttf")
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
        if parametrs.final_code == "Author VEN":
            parametrs.final_code = "Vakrushev Egor N."
    if parametrs.final_code == "":
        parametrs.final_code = "НАЖМИТЕ СЮДА"
    parametrs.demo_check = True

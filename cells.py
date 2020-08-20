import pygame
import parametrs
import printtext
import button
import texts
import time
import demo_view
import pause
import sys
from random import randint

new_quests = [*parametrs.all_quests]


class Cell:
    def __init__(self, color, width, message):
        global new_quests
        self.color = color  # картинка кнопки
        self.message = str(message)
        self.width = width

        self.type = "bomb"
        self.cards = parametrs.bombs
        if randint(0, 1) == 0:
            self.type = "normal"
            self.cards = parametrs.cards
        self.type_numb = randint(0, 2)

        if len(new_quests) == 0:
            new_quests = [*parametrs.all_quests]
        rand = randint(0, len(new_quests) - 1)
        self.text = new_quests.pop(rand)
        print(parametrs.all_quests, new_quests)
        self.setting_click = True
        self.points = "0"
        self.texts = self.text.split()

    def print(self, x, y, text_size, func=None, other=None, setting_click=None):
        mouse = pygame.mouse.get_pos()  # для получения координат стрелки мышки
        click = pygame.mouse.get_pressed()  # для проверки нажатия мышкой
        pygame.draw.rect(parametrs.window, self.color, (x, y, self.width, self.width))
        if setting_click is False:
            self.setting_click = False
        if self.setting_click:
            mes = "б"
            if self.type == "normal":
                mes = "н"
            printtext.print_text2(mes, int(x + 0.1 * self.width), int(y + 0.1 * self.width), int(self.width // 10))
        if x <= mouse[0] <= x + self.width and y <= mouse[1] <= y + self.width:  # стрелка расположена на кнопке
            printtext.print_text2(self.message, int(x + self.width // 2), int(y + self.width // 2), text_size)  # вывожу увеличенный текст на кнопке

            if click[0] == 1 and time.time() - parametrs.time_click >= 0.7:  # ЛКМ
                parametrs.time_click = time.time()
                pygame.mixer.Sound.play(parametrs.sound_button)
                pygame.time.delay(300)  # приостановить
                if func is not None:
                    if func == "quit":
                        pygame.quit()
                        sys.exit(0)
                    if other is not None:
                        return func(other)
                    else:
                        return func()  # вызываю функцию, к которой привязана кнопка
        else:
            printtext.print_text2(self.message, int(x + self.width // 2), int(y + self.width // 2), text_size, (128, 128, 128))
        return False

    def print_window(self):
        check = [True]
        check_time = time.time()
        check_for_numbs = time.time()

        def click_okey():
            check[0] = False

        while check[0]:
            parametrs.window.blit(parametrs.image_phon, (0, 0))
            for i in range(parametrs.command_count):
                parametrs.commands[i].print()

            x, y, width, height = int(parametrs.windowWidth // 2 - parametrs.card_width // 2), int(parametrs.windowHeight // 5), \
                                  int(parametrs.card_width), int(parametrs.card_height)

            bomb_x, bomb_y, bomb_width = int(3 * parametrs.windowWidth // 8), int(y - (height // 5) + (height // 20)), \
                                         int(width // 10)
            normal_x, normal_y, normal_width = int(4.3 * parametrs.windowWidth // 8), int(y - (height // 5) + (height // 20)), \
                                         int(width // 10)

            mouse = pygame.mouse.get_pos()  # для получения координат стрелки мышки
            click = pygame.mouse.get_pressed()

            if time.time() - check_for_numbs >= 0.8:
                if x <= mouse[0] <= x + width and y <= mouse[1] <= y + 0.45 * height:
                    if click[0]:
                        self.type_numb += 1
                        check_for_numbs = time.time()
                        if self.type_numb > 2:
                            self.type_numb = 0

            if self.type == "bomb":
                self.cards = parametrs.bombs
                parametrs.window.blit(parametrs.bombs[self.type_numb], (x, y))
            else:
                self.cards = parametrs.cards
                parametrs.window.blit(parametrs.cards[self.type_numb], (x, y))

            parametrs.window.blit(parametrs.image_number, (int(x - parametrs.mini_button_width // 2), \
                                                           int(y - parametrs.mini_button_height // 2)))
            printtext.print_text2(self.message, x, y, int(parametrs.mini_button_height * 4 // 5), font_color=(255, 255, 255))

            printtext.print_text2("Выберите тип карточки", int(x + width // 2), int(y - height // 5), int(height // 20), font_color=(255, 255, 255))

            type_bomb = button.Button(parametrs.image_button1, int(2.5 * bomb_width), bomb_width, "бомба")
            type_bomb.print2(bomb_x, bomb_y, int(0.7 * bomb_width), self.click, "bomb", color1=(255, 255, 255))
            parametrs.window.blit(parametrs.image_arrow, (int(bomb_x - parametrs.arrow_width), \
                                                          int(bomb_y + parametrs.arrow_height // 2)))

            type_normal = button.Button(parametrs.image_button1, int(2.5 * normal_width), normal_width, "норма")
            type_normal.print2(normal_x, normal_y, int(0.7 * normal_width), self.click, "normal", color1=(255, 255, 255))
            parametrs.window.blit(pygame.transform.rotate(parametrs.image_arrow, 180), \
                                  (int(normal_x + type_normal.width), int(normal_y + parametrs.arrow_height // 2)))

            printtext.print_text2("Выберите количество очков", int(x + width // 2), int(y + 0.05 * height), int(height // 35))

            printtext.print_text2("Введите задание", int(x + width // 2), int(y + 0.51 * height), int(height // 35))

            printtext.print_text2("*ВВЕДИТЕ ЗАДАНИЕ ДЛЯ НАЧАЛА ИГРЫ", int(x + width // 2), int(parametrs.windowHeight * 0.9), \
                                  int(height // 25), font_color=(255, 255, 255))

            okey_x, okey_y, okey_width, okey_height = int(x + width // 3), int(y + height // 1.2), int(width // 3), \
                                                      int(height // 10)

            display_x, display_y, display_width, display_height = int(x + 0.05 * width), int(y + 0.55 * height), \
                                                                  int(0.9 * width), int(0.25 * height)

            parametrs.window.blit(parametrs.image_arrow, (int(x - parametrs.arrow_width // 2), \
                                                          int(display_y + display_height // 2 - parametrs.arrow_height // 2)))
            parametrs.window.blit(pygame.transform.rotate(parametrs.image_arrow, 180), (int(x + width - parametrs.arrow_width // 2), \
                                                          int(display_y + display_height // 2 - parametrs.arrow_height // 2)))

            parametrs.window.blit(parametrs.image_arrow, (int(x + width * 0.05), int(y + height * 0.25)))
            parametrs.window.blit(pygame.transform.rotate(parametrs.image_arrow, 180), \
                                  (int(x + width * 0.95 - parametrs.arrow_width), int(y + height * 0.25)))

            text_x, text_y, text_width, text_height = display_x + 0.1 * display_width, display_y + 0.2 * display_height, \
            0.9 * display_width, 0.9 * display_height
            pygame.draw.rect(parametrs.window, (230, 230, 250), (display_x, display_y, display_width, display_height))

            new_text_width, new_text_height = printtext.print_text2(self.text, font_size=int(display_height // 7), \
                                                                    other=True)
            new_texts_size = int(new_text_width // text_width) + 1
            new_texts = ["" for i in range(new_texts_size + 1)]

            self.texts = self.text.split()
            new_word = ""
            index = 0
            for word in self.texts:
                wid, hei = printtext.print_text2(new_word + " " + word, font_size=int(display_height // 7), other=True)
                if wid <= text_width:
                    new_word += " " + word
                else:
                    new_word = word
                    index += 1
                new_texts[index] = new_word

            n = 0
            for string in new_texts:
                printtext.print_text2(string, int(parametrs.windowWidth // 2), int(0.2 * display_height + display_y + n), \
                                      int(display_height // 7), (0, 0, 0))
                wid, hei = printtext.print_text2(string, font_size=int(display_height // 7), other=True)
                n += int(1.1 * hei)

            button_okey = button.Button(parametrs.image_button, okey_width, okey_height, "ОК")
            button_okey.print2(okey_x, okey_y, int(button_okey.height * 0.7), click_okey)

            if time.time() - check_time >= 1:
                if display_x <= mouse[0] <= display_x + display_width and \
                        display_y <= mouse[1] <= display_y + display_height:
                    if click[0] == 1:
                        parametrs.need_input_name = True

            while parametrs.need_input_name:
                pygame.draw.rect(parametrs.window, (230, 230, 250), (display_x, display_y, display_width, display_height))
                new_text_width, new_text_height = printtext.print_text2(self.text, font_size=int(display_height // 7), \
                                                                        other=True)
                new_texts_size = int(new_text_width // text_width) + 1
                new_texts = ["" for i in range(new_texts_size + 1)]

                self.texts = self.text.split()
                new_word = ""
                index = 0
                for word in self.texts:
                    wid, hei = printtext.print_text2(new_word + " " + word, font_size=int(display_height // 7), other=True)
                    if wid <= text_width:
                        new_word += " " + word
                    else:
                        new_word = word
                        index += 1
                    new_texts[index] = new_word

                n = 0
                for string in new_texts:
                    printtext.print_text2(string, int(parametrs.windowWidth // 2), int(0.2 * display_height + display_y + n), \
                                          int(display_height // 7), (0, 0, 0))
                    wid, hei = printtext.print_text2(string, font_size=int(display_height // 7), other=True)
                    n += int(1.1 * hei)

                self.text, parametrs.need_input_name = texts.input_txt(self.text, parametrs.need_input_name, 100)

                parametrs.input_tick -= 1
                demo_view.view()
                if check[0]:
                    check[0] = pause.pause()
                if parametrs.check_end:
                    break
                if not check[0]:
                    break
                pygame.display.update()
            if not check[0]:
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
            if check[0]:
                check[0] = pause.pause()
            parametrs.window.blit(parametrs.MANUAL_CURSOR, (pygame.mouse.get_pos()))
            pygame.display.update()
            parametrs.clock.tick(60)
            if parametrs.check_end:
                break
        if self.text == "" and self.setting_click:
            self.setting_click = False
            parametrs.check_continue -= 1
        elif self.setting_click is False and self.text != "" and parametrs.check_continue < parametrs.field_size**2:
            parametrs.check_continue += 1
            self.setting_click = True
        return True

    def print_game_window(self):
        check = [True]

        def click_button(name):
            check[0] = False
            if name == "EXIT":
                return 2
            else:
                if self.color == (255, 255, 255):
                    parametrs.final_cells += 1
                if name == "YES":
                    self.color = (0, 255, 0)
                else:
                    self.color = (255, 0, 0)
            return 1

        while check[0]:
            parametrs.window.blit(parametrs.image_phon, (0, 0))
            printtext.print_text2(parametrs.name_of_game, int(parametrs.windowWidth // 2),
                                  int(parametrs.windowHeight // 16), int(parametrs.windowHeight // 25), (255, 255, 255))
            for i in range(parametrs.command_count):
                parametrs.commands[i].print()

            x, y, width, height = int(parametrs.windowWidth // 2 - parametrs.card_width // 2), int(
                parametrs.windowHeight // 5), \
                                  int(parametrs.card_width), int(parametrs.card_height)

            if self.type == "bomb":
                parametrs.window.blit(parametrs.bombs[self.type_numb], (x, y))
            else:
                parametrs.window.blit(parametrs.cards[self.type_numb], (x, y))

            parametrs.window.blit(parametrs.image_number, (int(x - parametrs.mini_button_width // 2), \
                                                           int(y - parametrs.mini_button_height // 2)))
            printtext.print_text2(self.message, x, y, int(parametrs.mini_button_height * 4 // 5),
                                  font_color=(255, 255, 255))

            display_x, display_y, display_width, display_height = int(x + 0.05 * width), int(y + 0.6 * height), \
                                                                  int(0.9 * width), int(0.25 * height)
            text_x, text_y, text_width, text_height = display_x + 0.1 * display_width, display_y + 0.2 * display_height, \
                                                      0.8 * display_width, 0.8 * display_height

            new_text_width, new_text_height = printtext.print_text2(self.text, font_size=int(display_height // 7), \
                                                                    other=True)
            new_texts_size = int(new_text_width // text_width) + 1
            new_texts = ["" for i in range(new_texts_size + 1)]

            self.texts = self.text.split()
            new_word = ""
            index = 0
            for word in self.texts:
                wid, hei = printtext.print_text2(new_word + " " + word, font_size=int(display_height // 7), other=True)
                if wid <= text_width:
                    new_word += " " + word
                else:
                    new_word = word
                    index += 1

                new_texts[index] = new_word

            n = 0
            for string in new_texts:
                printtext.print_text2(string, int(parametrs.windowWidth // 2),
                                      int(0.2 * display_height + display_y + n), \
                                      int(display_height // 7), (0, 0, 0))
                wid, hei = printtext.print_text2(string, font_size=int(display_height // 7), other=True)
                n += int(1.1 * hei)

            yes_button = button.Button(parametrs.image_button_yes, parametrs.mini_button_width, \
                                       parametrs.mini_button_height, "")
            yes_button.print2(int(x + width - 0.7 * parametrs.mini_button_width), int(y + height - parametrs.mini_button_height // 2), \
                              int(parametrs.mini_button_height * 0.8), click_button, "YES")

            no_button = button.Button(parametrs.image_button_no, parametrs.mini_button_width, \
                                      parametrs.mini_button_height, "")
            no_button.print2(int(x - 0.5 * parametrs.mini_button_width), int(y + height - parametrs.mini_button_height // 2), \
                             int(parametrs.mini_button_height * 0.8), click_button, "NO")

            exit_button = button.Button(parametrs.image_button_exit, parametrs.exit_width, \
                                        parametrs.exit_height, "")
            a = exit_button.print2(int(x + width - 3 * parametrs.exit_width), int(y + 2 * parametrs.exit_height), \
                               int(parametrs.exit_height * 0.8), click_button, "EXIT")
            if a == 2:
                return 2
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F4 and event.mod == pygame.KMOD_LALT:
                        pygame.quit()
                        sys.exit(0)
            demo_view.view()
            if check[0]:
                check[0] = pause.pause()
            if parametrs.check_end:
                break
            parametrs.window.blit(parametrs.MANUAL_CURSOR, (pygame.mouse.get_pos()))
            pygame.display.update()
            parametrs.clock.tick(60)
        return 1

    def click(self, typ):
        self.type = typ


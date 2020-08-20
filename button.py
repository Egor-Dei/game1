import pygame
import parametrs
import printtext
import time
import sys
pygame.init()


class Button:
    def __init__(self, image, width, height, message):
        self.image = image  # картинка кнопки
        self.message = str(message)
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def print(self, x, y, text_x, text_y, func=None, other=None):
        mouse = pygame.mouse.get_pos()  # для получения координат стрелки мышки
        click = pygame.mouse.get_pressed()  # для проверки нажатия мышкой
        parametrs.window.blit(self.image, (x, y))  # рисовка кнопки на соответствующих координатах
        if x <= mouse[0] <= x + self.width and y <= mouse[1] <= y + self.height:  # стрелка расположена на кнопке
            printtext.print_text(self.message, text_x, text_y, 0.8 * self.height, (255, 0, 0))  # вывожу увеличенный текст на кнопке

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
            printtext.print_text(self.message, text_x, text_y, 0.8 * self.height, (0, 255, 0))
        return True

    def print2(self, x, y, text_size, func=None, other=None, color1=(0, 0, 0), color2=(0, 0, 255), \
               type="Fonts/Lilita-One-Russian.ttf"):
        mouse = pygame.mouse.get_pos()  # для получения координат стрелки мышки
        click = pygame.mouse.get_pressed()  # для проверки нажатия мышкой
        parametrs.window.blit(self.image, (x, y))  # рисовка кнопки на соответствующих координатах
        if x <= mouse[0] <= x + self.width and y <= mouse[1] <= y + self.height:  # стрелка расположена на кнопке
            printtext.print_text2(self.message, int(x + self.width // 2), int(y + self.height // 2), text_size, \
                                  color2, font_type=type)  # вывожу увеличенный текст на кнопке

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
            printtext.print_text2(self.message, int(x + self.width // 2), int(y + self.height // 2), text_size, color1, \
                                  font_type=type)
        return True

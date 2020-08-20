import pygame
import parametrs
pygame.init()


def print_text(message, x, y, font_size, font_color, font_type="Fonts/text.otf"):
    font_type = pygame.font.Font(font_type, int(font_size))  # шрифт и размер текста
    text = font_type.render(str(message), True, font_color)  # создание текста определенного шрифта
    parametrs.window.blit(text, (x, y))
    return font_type.size(str(message))


def print_text2(message, center_x=int(parametrs.windowWidth // 2), center_y=int(parametrs.windowHeight // 2), \
                font_size=0, font_color=(0, 0, 0), font_type="Fonts/Lilita-One-Russian.ttf", other=False):
    font_type = pygame.font.Font(font_type, int(font_size))
    text = font_type.render(str(message), True, font_color)
    width, height = font_type.size(str(message))
    x, y = center_x - width // 2, center_y - height // 2
    if other == "name":
        if width <= 10:
            return 50, height
    elif other == False:
        parametrs.window.blit(text, (x, y))
    return width, height

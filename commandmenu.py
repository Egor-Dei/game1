import parametrs
import button
click_on_menu = False


def click(count):
    global click_on_menu
    parametrs.command_count = int(count)
    click_on_menu = False


def draw_menu():
    global click_on_menu
    width, height = int(parametrs.windowWidth // 10), int(parametrs.windowHeight // 4)
    button1 = button.Button(parametrs.image_button1, width, int(height // 7), 2)
    button2 = button.Button(parametrs.image_button1, width, int(height // 7), 3)
    button3 = button.Button(parametrs.image_button1, width, int(height // 7), 4)
    button4 = button.Button(parametrs.image_button1, width, int(height // 7), 5)
    button5 = button.Button(parametrs.image_button1, width, int(height // 7), 6)
    button6 = button.Button(parametrs.image_button1, width, int(height // 7), 7)
    button7 = button.Button(parametrs.image_button1, width, int(height // 7), 8)
    buttons = [button1, button2, button3, button4, button5, button6, button7]
    coordinate_x = int(1.1 * (parametrs.start_icon_x + parametrs.start_icon_width))
    click_on_menu = True
    if click_on_menu:
        #pygame.draw.rect(parametrs.window, (255, 255, 255), (coordinate_x, parametrs.start_icon_y, width, height))

        n = 0
        for but in buttons:
            but.print2(coordinate_x, int(parametrs.start_icon_y + n), int(0.7 * but.height), click, but.message, color1=(255, 255, 255))
            n += int(height // 7)


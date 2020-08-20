import pygame
import parametrs
import sys


def input_txt(inp_txt, need_inp, max_size=30, type="Fonts/text.otf"):
    parametrs.enter = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F4 and event.mod == pygame.KMOD_LALT:
                pygame.quit()
                sys.exit(0)
            inp_txt = inp_txt.replace("|", "")
            parametrs.input_tick = 30

            if event.key == pygame.K_RETURN:
                need_inp = False
                parametrs.enter = True
                return inp_txt, need_inp

            elif event.key == pygame.K_BACKSPACE:
                inp_txt = inp_txt[:-1]

            elif len(inp_txt) < max_size:
                need_inp = True
                symbol = event.unicode
                if type == "number":
                    numbs1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
                    numbs2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
                    if symbol in numbs1 or symbol in numbs2:
                        inp_txt += symbol
                else:
                    inp_txt += symbol
    inp_txt = inp_txt.replace("|", "")
    if parametrs.input_tick <= 0:
        inp_txt += "|"
    if parametrs.input_tick <= -30:
        inp_txt = inp_txt.replace("|", "")
        parametrs.input_tick = 30

    return inp_txt, need_inp

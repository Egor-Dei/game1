import parametrs
#import printtext


def view():
    if not parametrs.check_full_version:
        '''printtext.print_text2("ДЕМОВЕРСИЯ", center_x=int(parametrs.windowWidth // 2), center_y=int(parametrs.windowHeight // 2),\
                              font_size=int(parametrs.windowHeight // 5), font_color=(128, 128, 128), \
                              font_type="Fonts/mr_CoasterG Black.otf")'''
        parametrs.window.blit(parametrs.image_demo, (0, 0))
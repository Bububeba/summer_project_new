from main import *

pygame.init()

SCREEN = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Menu")

BG = pygame.image.load("images/background.png")
mus = "music\\main_menu.mp3"
pygame.mixer.music.load(mus)
pygame.mixer.music.play(-1)


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("fonts\\better-vcr_0.ttf", size)


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.image.load("images/b1_fon.png"), pos=(290, 500),
                             text_input="NEW GAME", font=get_font(80), base_color="white",
                             hovering_color=(130, 17, 245))
        CONTINUE_BUTTON = Button(image=pygame.image.load("images/b2_fon.png"), pos=(290, 600),
                                 text_input="CONTINUE", font=get_font(80), base_color="white",
                                 hovering_color=(130, 17, 245))
        QUIT_BUTTON = Button(image=pygame.image.load("images/b3_fon.png"), pos=(170, 700),
                             text_input="QUIT", font=get_font(80), base_color="white", hovering_color=(130, 17, 245))

        for button in [PLAY_BUTTON, CONTINUE_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.music.stop()
                    game(0)
                if CONTINUE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game(1)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()

# здесь подключаются модули
import random

import sys
from random import *
from weapon import *
import pygame_gui
from enemy import *
from main_hero import *
from map import Room
from button import *
from save import Save


def improvements(hero: Hero):
    window_surface = pygame.display.set_mode((1000, 800))

    background = pygame.Surface((1000, 800))
    background.fill(pygame.Color('orange'))

    manager = pygame_gui.UIManager((1000, 800))

    max_hp_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((400, 375), (200, 100)),
                                                 text='+max hp(2)',
                                                 manager=manager)

    speed_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((400, 175), (200, 100)),
                                                text='+speed(2)',
                                                manager=manager)

    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
                is_running = False
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if hero.coins_score > 1:
                    if event.ui_element == speed_button:
                        hero.coins_score -= 2
                        hero.speed += 0.4

                    if event.ui_element == max_hp_button:
                        hero.coins_score -= 2
                        hero.max_hp += 10

            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        pygame.display.update()


def game(is_load):
    # константы
    global range
    WIDTH = 1000
    HEIGHT = 800
    FPS = 30

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    # здесь происходит инициация,
    # создание объектов
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BLACK)
    pygame.display.set_caption("game_VZ")
    clock = pygame.time.Clock()

    pygame.time.set_timer(pygame.USEREVENT, 5000)

    flmove_up = False  # двигаться вверх?
    flmove_down = False  # двигаться вниз?
    flmove_right = False  # двигаться впрвао?
    flmove_left = False  # двигаться влево?
    fllast_move_is_right = True  # последнее движение было вправо?

    move_right = [pygame.image.load('sprites\\move_right_1.png').convert_alpha(),
                  pygame.image.load('sprites\\move_right_2.png').convert_alpha(),
                  pygame.image.load('sprites\\move_right_3.png').convert_alpha(),
                  pygame.image.load('sprites\\move_right_4.png').convert_alpha(),
                  pygame.image.load('sprites\\move_right_5.png').convert_alpha(),
                  pygame.image.load('sprites\\move_right_6.png').convert_alpha()]

    move_left = [pygame.image.load('sprites\\move_left_1.png').convert_alpha(),
                 pygame.image.load('sprites\\move_left_2.png').convert_alpha(),
                 pygame.image.load('sprites\\move_left_3.png').convert_alpha(),
                 pygame.image.load('sprites\\move_left_4.png').convert_alpha(),
                 pygame.image.load('sprites\\move_left_5.png').convert_alpha(),
                 pygame.image.load('sprites\\move_left_6.png').convert_alpha()]

    coin_anim = [pygame.image.load('sprites\\coin_1.png').convert_alpha(),
                 pygame.image.load('sprites\\coin_2.png').convert_alpha(),
                 pygame.image.load('sprites\\coin_3.png').convert_alpha(),
                 pygame.image.load('sprites\\coin_4.png').convert_alpha(),
                 pygame.image.load('sprites\\coin_5.png').convert_alpha(),
                 pygame.image.load('sprites\\coin_6.png').convert_alpha(),
                 pygame.image.load('sprites\\coin_1.png').convert_alpha(),
                 pygame.image.load('sprites\\coin_2.png').convert_alpha(),
                 pygame.image.load('sprites\\coin_3.png').convert_alpha(),
                 pygame.image.load('sprites\\coin_4.png').convert_alpha(),
                 pygame.image.load('sprites\\coin_5.png').convert_alpha(),
                 pygame.image.load('sprites\\coin_6.png').convert_alpha()]

    cross_anim = [pygame.image.load('sprites\\cross_1.png').convert_alpha(),
                  pygame.image.load('sprites\\cross_2.png').convert_alpha(),
                  pygame.image.load('sprites\\cross_3.png').convert_alpha(),
                  pygame.image.load('sprites\\cross_4.png').convert_alpha(),
                  pygame.image.load('sprites\\cross_3.png').convert_alpha(),
                  pygame.image.load('sprites\\cross_2.png').convert_alpha()]

    enemy_anim = [pygame.image.load('sprites\\enemy_1.png').convert_alpha(),
                  pygame.image.load('sprites\\enemy_2.png').convert_alpha(),
                  pygame.image.load('sprites\\enemy_3.png').convert_alpha(),
                  pygame.image.load('sprites\\enemy_4.png').convert_alpha(),
                  pygame.image.load('sprites\\enemy_5.png').convert_alpha(),
                  pygame.image.load('sprites\\enemy_6.png').convert_alpha(),
                  pygame.image.load('sprites\\enemy_hit_1.png').convert_alpha(),
                  pygame.image.load('sprites\\enemy_hit_2.png').convert_alpha(),
                  pygame.image.load('sprites\\enemy_hit_3.png').convert_alpha(),
                  pygame.image.load('sprites\\enemy_hit_4.png').convert_alpha(),
                  pygame.image.load('sprites\\enemy_hit_5.png').convert_alpha(),
                  pygame.image.load('sprites\\enemy_hit_6.png').convert_alpha()]

    # range_anim = [pygame.image.load('sprites\\i_range_1.png').convert_alpha(),
    #               pygame.image.load('sprites\\i_range_2.png').convert_alpha(),
    #               pygame.image.load('sprites\\i_range_3.png').convert_alpha(),
    #               pygame.image.load('sprites\\i_range_4.png').convert_alpha(),
    #               pygame.image.load('sprites\\i_range_5.png').convert_alpha(),
    #               pygame.image.load('sprites\\i_range_6.png').convert_alpha()]

    # range_hit_anim =   [pygame.image.load('sprites\\i_range_hit_1.png').convert_alpha(),
    #                     pygame.image.load('sprites\\i_range_hit_2.png').convert_alpha(),
    #                     pygame.image.load('sprites\\i_range_hit_3.png').convert_alpha(),
    #                     pygame.image.load('sprites\\i_range_hit_4.png').convert_alpha(),
    #                     pygame.image.load('sprites\\i_range_hit_5.png').convert_alpha(),
    #                     pygame.image.load('sprites\\i_range_hit_6.png').convert_alpha()]

    load_anim = [pygame.transform.scale(pygame.image.load('images\\load1.png'), (WIDTH, HEIGHT)).convert_alpha(),
                 pygame.transform.scale(pygame.image.load('images\\load2.png'), (WIDTH, HEIGHT)).convert_alpha(),
                 pygame.transform.scale(pygame.image.load('images\\load3.png'), (WIDTH, HEIGHT)).convert_alpha(),
                 pygame.transform.scale(pygame.image.load('images\\load4.png'), (WIDTH, HEIGHT)).convert_alpha(),
                 pygame.transform.scale(pygame.image.load('images\\load5.png'), (WIDTH, HEIGHT)).convert_alpha(),
                 pygame.transform.scale(pygame.image.load('images\\load6.png'), (WIDTH, HEIGHT)).convert_alpha(),
                 pygame.transform.scale(pygame.image.load('images\\load7.png'), (WIDTH, HEIGHT)).convert_alpha(),
                 pygame.transform.scale(pygame.image.load('images\\load8.png'), (WIDTH, HEIGHT)).convert_alpha(),
                 pygame.transform.scale(pygame.image.load('images\\load9.png'), (WIDTH, HEIGHT)).convert_alpha(),
                 pygame.transform.scale(pygame.image.load('images\\load10.png'), (WIDTH, HEIGHT)).convert_alpha(),
                 pygame.transform.scale(pygame.image.load('images\\load11.png'), (WIDTH, HEIGHT)).convert_alpha(),
                 pygame.transform.scale(pygame.image.load('images\\load12.png'), (WIDTH, HEIGHT)).convert_alpha(),
                 pygame.transform.scale(pygame.image.load('images\\load13.png'), (WIDTH, HEIGHT)).convert_alpha(),
                 pygame.transform.scale(pygame.image.load('images\\load14.png'), (WIDTH, HEIGHT)).convert_alpha(),
                 pygame.transform.scale(pygame.image.load('images\\load15.png'), (WIDTH, HEIGHT)).convert_alpha(),
                 pygame.transform.scale(pygame.image.load('images\\load16.png'), (WIDTH, HEIGHT)).convert_alpha()]

    lift_anim = [pygame.transform.scale(pygame.image.load('sprites\\lift_anim1.png'), (WIDTH, HEIGHT)).convert_alpha(),
                 pygame.transform.scale(pygame.image.load('sprites\\lift_anim2.png'), (WIDTH, HEIGHT)).convert_alpha(),
                 pygame.transform.scale(pygame.image.load('sprites\\lift_anim3.png'), (WIDTH, HEIGHT)).convert_alpha(),
                 pygame.transform.scale(pygame.image.load('sprites\\lift_anim4.png'), (WIDTH, HEIGHT)).convert_alpha(),
                 pygame.transform.scale(pygame.image.load('sprites\\lift_anim5.png'), (WIDTH, HEIGHT)).convert_alpha(),
                 pygame.transform.scale(pygame.image.load('sprites\\lift_anim6.png'), (WIDTH, HEIGHT)).convert_alpha(),
                 pygame.transform.scale(pygame.image.load('sprites\\lift_anim1.png'), (WIDTH, HEIGHT)).convert_alpha(),
                 pygame.transform.scale(pygame.image.load('sprites\\lift_anim2.png'), (WIDTH, HEIGHT)).convert_alpha(),
                 pygame.transform.scale(pygame.image.load('sprites\\lift_anim3.png'), (WIDTH, HEIGHT)).convert_alpha(),
                 pygame.transform.scale(pygame.image.load('sprites\\lift_anim4.png'), (WIDTH, HEIGHT)).convert_alpha(),
                 pygame.transform.scale(pygame.image.load('sprites\\lift_anim5.png'), (WIDTH, HEIGHT)).convert_alpha(),
                 pygame.transform.scale(pygame.image.load('sprites\\lift_anim6.png'), (WIDTH, HEIGHT)).convert_alpha(), ]

    image_weapon = pygame.image.load('sprites\\oar_1.png').convert_alpha()
    image_weapon = pygame.transform.rotate(image_weapon, -15)
    image_weapon = pygame.transform.scale(image_weapon,
                                          (image_weapon.get_width() * 1.3, image_weapon.get_height() * 1.3))

    image_range = pygame.image.load('sprites\\i_range_1.png').convert_alpha()
    image_range_hit = pygame.image.load('sprites\\i_range_hit_1.png').convert_alpha()

    animcount = 0  # счетчик кадров для анимации
    # U - up wall, R - right wall, D, L
    # A - правый верхний угол, B - правый нижний, C - левый нижний, E -
    map0 = """WWWWWWWWWWWWWWWWW
WWWWEUUGGGUUAWWWW
WWWWL       RWWWW
WWWWL       RWWWW
WWWWL       RWWWW
WWWWL       RWWWW
WWWWL       RWWWW
WWWWL       RWWWW
WWWWL       RWWWW
WWWWL       RWWWW
WWWWL       RWWWW
WWWWL       RWWWW
WWWWL       RWWWW
WWWWL       RWWWW
WWWWCDDDDDDDBWWWW
WWWWWWWWWWWWWWWWW
"""
    map1 = """WWWWWWWWWWWWWWWWWWWW
WWWWEGGGUUUUUUUAWWWW
WWWWL          RWWWW
WWWWL          RWWWW
WWWWL          RWWWW
WWWWL          RWWWW
WWWWL          RWWWW
WWWWL          RWWWW
WWWWL          RWWWW
WWWWG          RWWWW
WWWWG          RWWWW
WWWWG          RWWWW
WWWWCDDDDDDDDDDBWWWW
WWWWWWWWWWWWWWWWWWWW
"""
    map2 = """WWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWEUUUUUUUUUUUUUUUUAWWWW
WWWWL                RWWWW
WWWWG                GWWWW
WWWWG                GWWWW
WWWWG                GWWWW
WWWWL                RWWWW
WWWWL                RWWWW
WWWWL                RWWWW
WWWWL                RWWWW
WWWWCDDDDDDDDDGGGDDDDBWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWW
"""
    map3 = """WWWWWWWWWWWWWWWWWWWWWW
WWWWEUUGGGUUUUUUUAWWWW
WWWWL            RWWWW
WWWWL            RWWWW
WWWWL            RWWWW
WWWWL            RWWWW
WWWWL            RWWWW
WWWWL            RWWWW
WWWWL            RWWWW
WWWWL            RWWWW
WWWWL            RWWWW
WWWWL            GWWWW
WWWWL            GWWWW
WWWWL            GWWWW
WWWWCDDDDDDDDDDDDBWWWW
WWWWWWWWWWWWWWWWWWWWWW
"""
    map4 = """WWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWEUUUUUUUUUUUUUUUUAWWWW
WWWWG                GWWWW
WWWWG                GWWWW
WWWWG                GWWWW
WWWWCDDDDDDDDDDDDDDDDBWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWW
"""
    map5 = """WWWWWWWWWWWWWWWWWWWWWWWWW
WWWWEUUUUUUUUUUUUUUUAWWWW
WWWWG               RWWWW
WWWWG               RWWWW
WWWWG               RWWWW
WWWWL               RWWWW
WWWWL               RWWWW
WWWWL               RWWWW
WWWWL               RWWWW
WWWWL               RWWWW
WWWWCDDDDDGGGDDDDDDDBWWWW
WWWWWWWWWWWWWWWWWWWWWWWWW
"""
    maps = [map0, map1, map2, map3, map4, map5]
    chars = [' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'f', 'F', '*']
    r0, r1, r2, r3, r4, r5 = '', '', '', '', '', ''
    rrr = [r0, r1, r2, r3, r4, r5]

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == ' ':
                r = random.randint(0, len(chars) - 1)
                rrr[i] += chars[r]
            else:
                rrr[i] += maps[i][j]

    end_game = False
    end_time = 0
    # level_num = 0
    level_num = 0
    clear_rooms = 0
    need_rooms = 5
    room0 = Room(rrr[0], WIDTH, HEIGHT, 425, -50, -1, -1, -1, -1, -1, -1, 17, 16, level_num)
    room1 = Room(rrr[1], WIDTH, HEIGHT, 250, 0, -1, -1, -1, -1, 100, 500, 20, 14, level_num)
    room2 = Room(rrr[2], WIDTH, HEIGHT, -1, -1, 900, 250, 550, 600, -50, 250, 26, 12, level_num)
    room3 = Room(rrr[3], WIDTH, HEIGHT, 300, -50, 800, 550, -1, -1, -1, -1, 22, 16, level_num)
    room4 = Room(rrr[4], WIDTH, HEIGHT, -1, -1, 900, 325, -1, -1, -50, 325, 26, 7, level_num)
    room5 = Room(rrr[5], WIDTH, HEIGHT, -1, -1, -1, -1, 375, 600, -25, 200, 25, 12, level_num)
    rooms = [room0, room1, room2, room3, room4, room5]
    rooms_u = [1, 3]
    rooms_r = [2, 3, 4]
    rooms_d = [2, 5]
    rooms_l = [1, 2, 4, 5]
    room_num = 0

    # rooms[room_num].room_draw(screen, WIDTH, HEIGHT, rooms[room_num].room_w/50, rooms[room_num].room_h/50)

    Main_Hero = Hero(500, 655, 'sprites\\move_right_1.png', 100, 0, 20)

    killed_enemy = 0
    fake_coins = Main_Hero.coins_score
    sum_time = 0
    runs = 1

    weapon = Weapon(Main_Hero.rect.centerx + 33, Main_Hero.rect.centery - 10, 'sprites\\scythe3.png', "Main_Hero", 100,
                    300, 1)
    center = weapon.rect.center
    weapon.rect = weapon.image.get_rect(center=center)

    range = Range(*Main_Hero.rect.center, 'sprites\\i_range_1.png')

    Main_Hero.range = range
    Main_Hero.weapon = weapon

    coins = pygame.sprite.Group()
    enemys = pygame.sprite.Group()
    crosses = pygame.sprite.Group()

    # enemy1 = Enemy(WIDTH//2-200, HEIGHT // 2-200, 'sprites\\enemy1.png', 100, 1, 4, 1, enemys, None, None)

    enemy_count = 0
    spawn_time = 0
    max_enemy = 0

    st_mus = "music\\1.mp3"  # ["music\\1GatesofHell.mp3", "music\\1FinalExpense.mp3", "music\\1RiverofFlame.mp3"]
    el_mus = "music\\2.mp3"  # ["music\\2TheKingandtheBull.mp3", "music\\2FieldofSouls.mp3", "music\\2TheExalted.mp3"]
    as_mus = "music\\3.mp3"  # ["music\\3ThroughAsphodel.mp3", "music\\3MouthOfStyx.mp3", "music\\3TheBloodless.mp3"]
    tr_mus = "music\\4.mp3"  # ["music\\4OutOfTartarus.mp3", "music\\4TheHouseOfHades.mp3", "music\\4ThePainfulWay.mp3"]
    end_mus = "music\\Silence.mp3"

    battle_music = [st_mus, el_mus, as_mus, tr_mus, end_mus]
    death_mus = "music\\DeathandI.mp3"
    lift_ost = "music\\lift_ost.ogg"

    save = Save(Main_Hero, level_num, room_num, need_rooms)

    if is_load:
        Main_Hero.x, Main_Hero.y, Main_Hero.coins_score, Main_Hero.max_hp, \
            Main_Hero.hp, Main_Hero.speed, level_num, room_num, clear_rooms = save.get_data()

    pygame.mixer.music.load(battle_music[level_num])
    pygame.mixer.music.play(-1)



    # rect = pygame.rect

    # если надо до цикла отобразить
    # какие-то объекты, обновляем экран
    pygame.display.update()

    while True:

        # задержка
        clock.tick(FPS)

        # цикл обработки событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    improvements(Main_Hero)

                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    flmove_up = True
                    flmove_down = False
                    # flmove_left  = False
                    # flmove_right = False

                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    flmove_up = False
                    flmove_down = True
                    # flmove_left  = False
                    # flmove_right = False


                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    # flmove_up    = False
                    # flmove_down  = False
                    flmove_left = True
                    flmove_right = False

                    fllast_move_is_right = False


                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    # flmove_up    = False
                    # flmove_down  = False
                    flmove_left = False
                    flmove_right = True

                    fllast_move_is_right = True
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    flmove_up = False

                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    flmove_down = False

                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    flmove_left = False

                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    flmove_right = False

            # elif event.type == pygame.USEREVENT:
            #     pass
            # Coin(randint(WIDTH//2 - rooms[room_num].room_w // 2 + 100, WIDTH//2 + rooms[room_num].room_w // 2 - 50), # 50 - размер клетки
            #     randint(HEIGHT//2 - rooms[room_num].room_h // 2 + 100, HEIGHT//2 + rooms[room_num].room_h // 2 - 50),'sprites\\coin_1.png', coins)

            # elif event.type == VIDEORESIZE:# Изменение значений констант при изменении размера окна
            #     WIDTH = event.w
            #     HEIGHT = event.h
            #     screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)

        # обновление объектов
        if level_num == 0:
            hp = 100
            damage = 2
            speed = 4


        elif level_num == 1:
            hp = 110
            damage = 4
            speed = 5

        elif level_num == 2:
            hp = 120
            damage = 6
            speed = 6

        elif level_num == 3:
            hp = 140
            damage = 10
            speed = 8

        current_time = pygame.time.get_ticks()

        if Main_Hero.hp <= 0:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(death_mus)
            pygame.mixer.music.play(0)
            cnt = 0
            coins.empty()
            enemys.empty()
            clear_rooms = 0
            while (cnt < 100):
                # screen.blit(Rect(screen, RED, pygame.Rect(0, 0, 1000, 1000), 1), (0, 0))
                # pygame.draw.rect(screen, BLACK, pygame.Rect(0, 350, 1000, 100))
                font = pygame.font.Font("fonts\\Zlusa _font.ttf", int(75))
                text = font.render("ВЫ МЕРТВЫ", True, (130, 17, 245))
                screen.blit(text, (350, 355))
                pygame.display.flip()
                cnt += 1
                clock.tick(20)
            level_num, room_num, max_enemy, enemy_count, Main_Hero.hp = 0, 0, 0, 0, 100
            Main_Hero.x = 500
            Main_Hero.y = 655
            pygame.mixer.music.load(battle_music[level_num])
            pygame.mixer.music.play(-1)

        if enemy_count > 0 and pygame.time.get_ticks() >= spawn_time:
            # print(enemy_count, "ADD")
            Cross(
                randint(WIDTH // 2 - rooms[room_num].room_w // 2 + 400, WIDTH // 2 + rooms[room_num].room_w // 2 - 400),
                randint(HEIGHT // 2 - rooms[room_num].room_h // 2 + 150,
                        HEIGHT // 2 + rooms[room_num].room_h // 2 - 150),
                'sprites\\cross_1.png', pygame.time.get_ticks(), crosses)

            enemy_count -= 1
            spawn_time = pygame.time.get_ticks() + 3000
            # print( pygame.time.get_ticks())
            # print( spawn_time)
            # print (enemy_count, len(enemys))

        # print (enemy_count, len(enemys))
        # clock = pygame.time.Clock()
        if rooms[room_num].is_clear:
            room_last = room_num
            rooms[room_num].gates.clear()
            save.update(Main_Hero, level_num, room_num, clear_rooms)

            if rooms[room_num].portal1_x != -1:
                # pygame.draw.rect(screen, BLUE, pygame.Rect(*rooms[room_num].rect1.topleft, 150, 150), 1)
                # pygame.display.update()
                # pygame.draw.rect(screen, RED, pygame.Rect(*x.rect.topleft,  x.image.get_width(), x.image.get_height()), 1)
                if rooms[room_num].rect1.collidepoint(*Main_Hero.rect.center):
                    killed_enemy += max_enemy
                    if clear_rooms == need_rooms:
                        room_num = 0
                        Main_Hero.x = 500
                        Main_Hero.y = 555
                        level_num += 1
                        clear_rooms = 0
                        max_enemy = 0
                        cnt = 0
                        pygame.mixer.music.stop()
                        while (cnt < len(load_anim)):
                            screen.blit(load_anim[cnt], (0, 0))
                            pygame.display.flip()
                            cnt += 1
                            clock.tick(20)
                        cnt = 0
                        pygame.mixer.music.load(lift_ost)
                        pygame.mixer.music.play(-1)
                        while (cnt < len(lift_anim) * 12):
                            screen.blit(lift_anim[cnt % 12], (0, 0))
                            pygame.display.flip()
                            cnt += 1
                            clock.tick(12)
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load(battle_music[level_num])
                        pygame.mixer.music.play(-1)
                    else:
                        room_num = random.choice(rooms_d)
                        Main_Hero.x = rooms[room_num].rect3.centerx
                        Main_Hero.y = rooms[room_num].rect3.top - 100
                        max_enemy = randint(0, 1)
                        clear_rooms += 1
                    coins.empty()
                    enemy_count = max_enemy
                    cnt = 0
                    while (cnt < len(load_anim)):
                        screen.blit(load_anim[cnt], (0, 0))
                        pygame.display.flip()
                        cnt += 1
                        clock.tick(20)
                    rooms[room_last].kills_cnt = 0
                    rooms[room_last].is_clear = False

            if rooms[room_num].portal2_x != -1:
                # pygame.draw.rect(screen, BLUE, pygame.Rect(*rooms[room_num].rect2.topleft, 150, 150), 1)
                # pygame.display.update()
                # if pygame.Rect.colliderect(Main_Hero.rect, rooms[room_num].rect2):
                if rooms[room_num].rect2.collidepoint(*Main_Hero.rect.center):
                    killed_enemy += max_enemy
                    if clear_rooms == need_rooms:
                        room_num = 0
                        Main_Hero.x = 500
                        Main_Hero.y = 555
                        level_num += 1
                        clear_rooms = 0
                        max_enemy = 0
                        cnt = 0
                        pygame.mixer.music.stop()
                        while (cnt < len(load_anim)):
                            screen.blit(load_anim[cnt], (0, 0))
                            pygame.display.flip()
                            cnt += 1
                            clock.tick(20)
                        cnt = 0
                        pygame.mixer.music.load(lift_ost)
                        pygame.mixer.music.play(-1)
                        while (cnt < len(lift_anim) * 12):
                            screen.blit(lift_anim[cnt % 12], (0, 0))
                            pygame.display.flip()
                            cnt += 1
                            clock.tick(12)
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load(battle_music[level_num])
                        pygame.mixer.music.play(-1)
                    else:
                        room_num = random.choice(rooms_l)
                        Main_Hero.x = rooms[room_num].rect4.right + 100
                        Main_Hero.y = rooms[room_num].rect4.centery
                        max_enemy = randint(0, 1)
                        clear_rooms += 1
                    cnt = 0
                    coins.empty()
                    enemy_count = max_enemy
                    while (cnt < len(load_anim)):
                        screen.blit(load_anim[cnt], (0, 0))
                        pygame.display.flip()
                        cnt += 1
                        clock.tick(16)
                    rooms[room_last].kills_cnt = 0
                    rooms[room_last].is_clear = False

            if rooms[room_num].portal3_x != -1:
                # pygame.draw.rect(screen, BLUE, pygame.Rect(*rooms[room_num].rect3.topleft, 150, 150), 1)
                # pygame.display.update()
                # if pygame.Rect.colliderect(Main_Hero.rect, rooms[room_num].rect3):
                if rooms[room_num].rect3.collidepoint(*Main_Hero.rect.center):
                    killed_enemy += max_enemy
                    if clear_rooms == need_rooms:
                        room_num = 0
                        Main_Hero.x = 500
                        Main_Hero.y = 555
                        level_num += 1
                        clear_rooms = 0
                        max_enemy = 0
                        cnt = 0
                        pygame.mixer.music.stop()
                        while (cnt < len(load_anim)):
                            screen.blit(load_anim[cnt], (0, 0))
                            pygame.display.flip()
                            cnt += 1
                            clock.tick(20)
                        cnt = 0
                        pygame.mixer.music.load(lift_ost)
                        pygame.mixer.music.play(-1)
                        while (cnt < len(lift_anim) * 12):
                            screen.blit(lift_anim[cnt % 12], (0, 0))
                            pygame.display.flip()
                            cnt += 1
                            clock.tick(12)
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load(battle_music[level_num])
                        pygame.mixer.music.play(-1)
                    else:
                        room_num = random.choice(rooms_u)
                        Main_Hero.x = rooms[room_num].rect1.centerx
                        Main_Hero.y = rooms[room_num].rect1.bottom + 100
                        max_enemy = randint(0, 1)
                        clear_rooms += 1
                    coins.empty()
                    enemy_count = max_enemy
                    cnt = 0
                    while (cnt < len(load_anim)):
                        screen.blit(load_anim[cnt], (0, 0))
                        pygame.display.flip()
                        cnt += 1
                        clock.tick(16)
                    rooms[room_last].kills_cnt = 0
                    rooms[room_last].is_clear = False

            if rooms[room_num].portal4_x != -1:
                # pygame.draw.rect(screen, BLUE, pygame.Rect(*rooms[room_num].rect4.topleft, 150, 150), 1)
                # pygame.display.update()
                # if pygame.Rect.colliderect(Main_Hero.rect, rooms[room_num].rect4):
                if rooms[room_num].rect4.collidepoint(*Main_Hero.rect.center):
                    killed_enemy += max_enemy
                    if clear_rooms == need_rooms:
                        room_num = 0
                        Main_Hero.x = 500
                        Main_Hero.y = 555
                        level_num += 1
                        clear_rooms = 0
                        max_enemy = 0
                        cnt = 0
                        pygame.mixer.music.stop()
                        while (cnt < len(load_anim)):
                            screen.blit(load_anim[cnt], (0, 0))
                            pygame.display.flip()
                            cnt += 1
                            clock.tick(20)
                        cnt = 0
                        pygame.mixer.music.load(lift_ost)
                        pygame.mixer.music.play(-1)
                        while (cnt < len(lift_anim) * 12):
                            screen.blit(lift_anim[cnt % 12], (0, 0))
                            pygame.display.flip()
                            cnt += 1
                            clock.tick(12)
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load(battle_music[level_num])
                        pygame.mixer.music.play(-1)
                    else:
                        room_num = random.choice(rooms_r)
                        Main_Hero.x = rooms[room_num].rect2.left - 100
                        Main_Hero.y = rooms[room_num].rect2.centery
                        max_enemy = randint(0, 1)
                        clear_rooms += 1
                    coins.empty()
                    enemy_count = max_enemy
                    cnt = 0
                    while (cnt < len(load_anim)):
                        screen.blit(load_anim[cnt], (0, 0))
                        pygame.display.flip()
                        cnt += 1
                        clock.tick(16)
                    rooms[room_last].kills_cnt = 0
                    rooms[room_last].is_clear = False

            if level_num == 4:
                level_num = 0
                end_game = True
                end_time = current_time

                # rooms[room_num].room_draw(screen, WIDTH, HEIGHT, rooms[room_num].room_w / 50,rooms[room_num].room_h / 50)
                # rooms[room_num-1].kill

        animcount += 1
        if animcount + 2 >= FPS:
            animcount = 0

        crosses.update(animcount, cross_anim, pygame.time.get_ticks(), enemys, rooms[room_num], hp, damage, speed)
        enemys.update(animcount, enemy_anim, Main_Hero, pygame.time.get_ticks(), rooms[room_num], coins)
        coins.update(animcount, coin_anim, Main_Hero)

        Main_Hero.update(animcount, move_right, move_left,
                         flmove_up, flmove_down, flmove_left, flmove_right,
                         fllast_move_is_right, rooms[room_num])

        Main_Hero.update_weapon(animcount, fllast_move_is_right,
                                Main_Hero.weapon, image_weapon,
                                range, image_range, image_range_hit,
                                enemys, coins, pygame.time.get_ticks())

        rooms[room_num].update(enemy_count, max_enemy, room_num, screen, WIDTH, HEIGHT, enemys)

        #

        # rooms[room_num].update(Main_Hero, enemy_count, room_num, screen, WIDTH, HEIGHT, enemys, rooms)

        # --------

        # обновление экрана
        screen.fill(BLACK)
        rooms[room_num].tiles.clear()

        rooms[room_num].room_draw(screen, WIDTH, HEIGHT, rooms[room_num].room_w / 50, rooms[room_num].room_h / 50,
                                  level_num)
        screen.blit(range.image, (range.rect[0], range.rect[1]))
        crosses.draw(screen)
        coins.draw(screen)
        screen.blit(Main_Hero.image, Main_Hero.rect)
        screen.blit(weapon.image, (weapon.rect[0], weapon.rect[1] - 30 + animcount // 6))
        enemys.draw(screen)

        font = pygame.font.SysFont('couriernew', int(40))
        text1 = font.render(str("HP: " + str(Main_Hero.hp)), True, WHITE)
        text2 = font.render(str("Coins: " + str(Main_Hero.coins_score)), True, WHITE)

        screen.blit(text1, (0, 0))
        screen.blit(text2, (0, 50))

        # pygame.draw.rect(screen, RED,
        #                  pygame.Rect(rooms[room_num].x_offset, rooms[room_num].y_offset, rooms[room_num].room_w,
        #                              rooms[room_num].room_h), 1)

        # pygame.draw.rect(screen, RED, pygame.Rect(*Main_Hero.rect.topleft, 100, 100), 1)
        # pygame.draw.rect(screen, RED, pygame.Rect(*Main_Hero.range.rect.topleft, Main_Hero.range.image.get_width(),
        #                                           Main_Hero.range.image.get_height()), 1)

        # for x in rooms[room_num].tiles:
        #     pygame.draw.rect(screen, RED, pygame.Rect(*x.rect.topleft, x.image.get_width(), x.image.get_height()), 1)

        # for x in enemys:
        #     pygame.draw.rect(screen, RED, pygame.Rect(*x.rect.topleft, x.image.get_width(), x.image.get_height()), 1)
        #     pygame.draw.circle(screen, RED, x.rect.center, x.range, 1)

        if end_game:
            screen.fill(BLACK)
            coins.empty()
            enemys.empty()
            font = pygame.font.Font("fonts\\better-vcr_0.ttf", int(50))
            text = font.render("RUN №" + str(runs), True, WHITE)
            text0 = font.render("TIME: " + str(end_time / 1000 - sum_time / 1000), True, WHITE)
            text1 = font.render("ENEMIES KILLED: " + str(killed_enemy), True, WHITE)
            text2 = font.render("OBOLS COLLECTED: " + str(Main_Hero.coins_score - fake_coins), True, WHITE)
            screen.blit(text, (0, 0))
            screen.blit(text0, (0, 50))
            screen.blit(text1, (0, 100))
            screen.blit(text2, (0, 150))

            MENU_MOUSE_POS = pygame.mouse.get_pos()
            RESPAWN_BUTTON = Button(image=pygame.image.load("images/b2_fon.png"), pos=(WIDTH // 2, 700),
                                    text_input = "TO THE SURFACE", font=pygame.font.Font("fonts\\better-vcr_0.ttf", 80),
                                    base_color = "white", hovering_color = (130, 17, 245))
            for button in [RESPAWN_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if RESPAWN_BUTTON.checkForInput(MENU_MOUSE_POS):
                        killed_enemy = 0
                        fake_coins = Main_Hero.coins_score
                        sum_time += pygame.time.get_ticks()
                        runs += 1
                        end_game = False
                        level_num, room_num, max_enemy, enemy_count, Main_Hero.hp = 0, 0, 0, 0, 100
                        Main_Hero.x = 500
                        Main_Hero.y = 655
                        pygame.mixer.music.load(battle_music[level_num])
                        pygame.mixer.music.play(-1)
            pygame.display.update()

        pygame.display.update()

# game(1)

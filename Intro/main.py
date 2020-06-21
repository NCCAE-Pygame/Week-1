import pygame
import os

def main():
    folder = "data"
    pygame.init()
    s_width = 1280
    s_height = 720
    screen = pygame.display.set_mode((s_width, s_height))
    dragon = pygame.image.load(os.path.join(folder, "dragon1.jpg"))
    m = pygame.Surface((100, 100))
    m.fill((255, 0, 0))
    m = m.convert()

    # clock
    clock = pygame.time.Clock()
    milliseconds = clock.tick(40)
    playtime = 0.0
    playtime += milliseconds / 1000.0

    # scaling images
    dragon_w = 400
    dragon_h = 400
    half = dragon_w / 2
    dragon_x = s_width / 2 - half
    dragon_y = s_height / 2 - half
    speed_x = 30
    speed_y = 30
    m = pygame.transform.scale(m, (s_width, s_height))
    dragon = pygame.transform.scale(dragon, (dragon_w, dragon_h))

    # transparency
    # alpha, sets to half transparent
    m.set_alpha(128)
    m = m.convert_alpha()
    # color key
    dragon.set_colorkey((255, 255, 255))

    # convert for better performance
    m = m.convert()
    dragon = dragon.convert()

    screen.blit(m, (0, 0))
    screen.blit(dragon, (dragon_x, dragon_y))
    pygame.display.flip()

    # event loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if dragon_x < 0 or dragon_x > s_width - dragon_w:
            speed_x = -speed_x
        if dragon_y < 0 or dragon_y > s_height - dragon_h:
            speed_y = -speed_y
        milliseconds = clock.tick(40)
        playtime += milliseconds / 1000.0
        dragon_x += speed_x
        dragon_y += speed_y
        screen.blit(m, (0, 0))
        screen.blit(dragon, (dragon_x, dragon_y))
        pygame.display.flip()


if __name__ == "__main__":
    main()
    pygame.quit()
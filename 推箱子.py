import pygame
from pygame.locals import *


def main():
    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("推箱子游戏")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    BLOCK_SIZE = 30
    GAP = 10

    TARGET_POSITION = [(400, 500), (350, 450), (400, 450)]

    box_position = [300, 500]
    box_rotation = 0
    box_shape = [
        [1, 1, 1, 1],
    ]

    def rotate_box():
        nonlocal box_shape
        new_shape = []
        for i in range(len(box_shape)):
            new_row = []
            for j in range(len(box_shape[i])):
                new_row.append(box_shape[j][i])
            new_shape.append(new_row)
        box_shape = new_shape

    def is_collide():
        nonlocal box_position, box_rotation
        for target in TARGET_POSITION:
            x = target[0]
            y = target[1] - GAP

            if (box_position[0] + BLOCK_SIZE > x and
                    box_position[1] + BLOCK_SIZE > y and
                    box_position[0] < x):
                return True
        return False

    success = False
    clock = pygame.time.Clock()

    while not success:
        screen.fill(BLACK)

        for i in range(len(box_shape)):
            x_pos = box_position[0] + i * BLOCK_SIZE
            y_pos = box_position[1] + i * BLOCK_SIZE

            if box_rotation == 90:
                y_pos = box_position[1] + (len(box_shape) - 1 - i) * BLOCK_SIZE
            elif box_rotation == -90:
                y_pos = box_position[1] + (i) * BLOCK_SIZE

            pygame.draw.rect(screen, WHITE, (x_pos, y_pos, BLOCK_SIZE, BLOCK_SIZE))

        if is_collide():
            print("成功！")
            success = True

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    box_position[0] -= 5
                elif event.key == pygame.K_RIGHT:
                    box_position[0] += 5

                if event.key == pygame.K_q:
                    rotate_box()
                if event.key == pygame.K_w:
                    box_rotation = -box_rotation

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()


if __name__ == "__main__":
    main()
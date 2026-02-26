# Brick Breaker
import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Brick Breaker")

clock = pygame.time.Clock()
FPS = 120

screen_width, screen_height = screen.get_size()


class Player:
    def __init__(self, x, y, speed, color, width, height):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.base_width = width
        self.width = width
        self.height = height

        self.player_collision = pygame.Rect(self.x, self.y, self.width, self.height)

        self.powerup_on = False
        self.powerup_end = 0

    def set_collision(self):
        self.player_collision.width = self.width
        self.player_collision.height = self.height

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed

    def update_rect(self):
        self.player_collision.x = self.x
        self.player_collision.y = self.y

    def boundarys(self):
        if self.x <= 0:
            self.x = 0
        elif self.x >= screen_width - self.width:
            self.x = screen_width - self.width

    def increase_width(self):
        self.width += 30
        self.set_collision()

    def increase_speed(self):
        self.speed += 5

    def increase_balls(self, balls):
        balls.append(Ball(250, 10, 0, 2, (255, 255, 255), 5))

    def collision(self, powerup, balls):
        if powerup.active and self.player_collision.colliderect(powerup.rect) and not self.powerup_on:
            self.powerup_on = True

            if powerup.type == 1:
                self.increase_width()
            if powerup.type == 2:
                self.increase_speed()
            if powerup.type == 3:
                self.increase_balls(balls)

            powerup.active = False
            powerup.next_spawn_time = pygame.time.get_ticks() + random.randint(5000, 10000)

            self.powerup_end = pygame.time.get_ticks() + 5000

    def powerup_active(self, powerup):
        if self.powerup_on and pygame.time.get_ticks() > self.powerup_end:
            self.powerup_on = False
            if powerup.type == 1:
                self.width = self.base_width
            if powerup.type == 2:
                self.speed -= 5
            self.set_collision()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.player_collision)

    def update(self, screen, powerup, balls):
        self.movement()
        self.boundarys()
        self.update_rect()
        self.collision(powerup, balls)
        self.powerup_active(powerup)
6        self.draw(screen)


class Ball:
    def __init__(self, x, y, vel_x, vel_y, color, radius):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.color = color
        self.radius = radius

        self.ball_collision = pygame.Rect(
            self.x - radius,
            self.y - radius,
            radius * 2,
            radius * 2
        )

    def revert_vel_y(self):
        self.vel_y = 4

    def update_rect(self):
        self.ball_collision.center = (self.x, self.y)

    def limits(self):
        if self.x <= self.radius or self.x >= screen_width - self.radius:
            self.vel_x *= -1
        if self.y <= self.radius:
            self.vel_y *= -1

    def collision(self, player):
        if self.ball_collision.colliderect(player.player_collision):
            self.revert_vel_y()
            self.vel_y *= -1
            self.vel_x = random.randint(-3, 3)
            self.y = player.player_collision.top - self.radius

    def movement(self):
        self.x += self.vel_x
        self.y += self.vel_y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def update(self, screen, player):
        self.limits()
        self.movement()
        self.update_rect()
        self.collision(player)
        self.draw(screen)


class Brick:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 3)


class Powerup:
    def __init__(self, x, y, w, h, vel_y, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vel_y = vel_y
        self.color = color

        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.type = random.randint(1, 3)

        self.active = False
        self.next_spawn_time = pygame.time.get_ticks() + random.randint(1000, 2000)

    def spawn(self):
        self.x = random.randint(30, 470)
        self.y = -10
        self.type = random.randint(1, 3)
        self.active = True

        if self.type == 1:
            self.color = (255, 0, 0)
        if self.type == 2:
            self.color = (0, 255, 0)
        if self.type == 3:
            self.color = (0, 0, 255)

    def movement(self):
        self.y += self.vel_y
        if self.y > 500:
            self.active = False
            self.next_spawn_time = pygame.time.get_ticks() + random.randint(5000, 10000)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def update_rect(self):
        self.rect.topleft = (self.x, self.y)

    def update(self, screen):
        current_time = pygame.time.get_ticks()

        if not self.active:
            if current_time >= self.next_spawn_time:
                self.spawn()
        else:
            self.movement()
            self.update_rect()
            self.draw(screen)

class enemy:
    def __init__(self,x,y,w,h,vel_x,vel_y,color):
        self.x = x
        self.y =y
        self.w = w
        self.h = h
        self.vel_x = vel_X
        self.vel_y = vel_y
        self.color = color


player = Player(230, 450, 5, (255, 255, 255), 40, 10)
balls = [Ball(250, 10, 0, 2, (255, 255, 255), 5)]
powerup = Powerup(0, 0, 10, 10, 3, (0, 100, 100))
bricks = []

for row in range(1, 5):
    y = 20 * row
    for col in range(1, 24):
        bricks.append(Brick(20 * col, y, 20, 20, (100, 100, 120)))

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((20, 20, 20))

    player.update(screen, powerup, balls)

    for ball in balls[:]:
        ball.update(screen, player)

        for brick in bricks[:]:
            if ball.ball_collision.colliderect(brick.rect):
                bricks.remove(brick)
                ball.vel_y *= -1
                break

    powerup.update(screen)

    for brick in bricks:
        brick.draw(screen)

    pygame.display.flip()

pygame.quit()

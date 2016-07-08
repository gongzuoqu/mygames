import time

import pygame
import pyganim
from pygame.locals import *

# define some constants
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

class Sprite():
    def __init__(self):
        self.animation = None
        # self.image = None
        self.rect = None
        self.x = 0
        self.y = 0

    def loadFrames(self, frames, f_width, f_height):
        self.animation = pyganim.PygAnimation(frames)
        self.rect = pygame.Rect(0, 0, f_width, f_height)
        self.width = f_width
        self.height = f_height

    # def loadImage(self, filename, f_width, f_height):
    #     self.image = pygame.image.load(filename)
    #     self.rect = pygame.Rect(0, 0, f_width, f_height)
    #     self.width = f_width
    #     self.height = f_height

    def getPos(self):
        return (self.x, self.y)

    def setPos(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def getRect(self):
        return self.rect

    def createCopy(self, xaxis=False, yaxis=False):
        if self.animation is None:
            return None
        s = Sprite()
        if xaxis is False and yaxis is False:
            s.animation = self.animation.getCopy()
            s.animation.stop()
        else:
            s.animation = self.animation.flip(xaxis, yaxis)
            s.animation.makeTransformsPermanent()

        s.width = self.width
        s.height = self.height
        s.rect = pygame.Rect(0, 0, self.width, self.height)
        return s

    def move(self, inc_x, inc_y):
        self.x += inc_x
        self.y += inc_y

    def blit(self, windowSurface):
        if self.animation is not None:
            self.animation.blit(windowSurface, self.getPos())

    def processEvents(self, event):
        pass

    def update(self):
        return True


class MultiSprite(Sprite):
    INDEX_ANIM = 0
    INDEX_RECT = 1
    def __init__(self):
        Sprite.__init__(self)
        self.animations = {}
        self.currentAnimationName = None

    def addAnimationFrames(self, animName, frames, f_width, f_height):
        self.loadFrames(frames, f_width, f_height)
        self.animations[animName] = [self.animation, pygame.Rect(self.getRect())]

    def getAnimation(self, animName):
        return self.animations[animName]

    # def move(self, inc_x, inc_y):
    #     self.x += inc_x
    #     self.y += inc_y
    #     if self.animation is not None:
    #         self.animation.move(inc_y, inc_y)

    def setAnimation(self, animName):
        if animName == self.currentAnimationName:
            return
        if self.animation is not None:
            self.animation.stop()

        self.currentAnimationName = animName
        self.animation = self.animations[self.currentAnimationName][MultiSprite.INDEX_ANIM]
        self.rect = self.animations[self.currentAnimationName][MultiSprite.INDEX_RECT]
        self.animation.play()


PLAYER_WIDTH = 64
PLAYER_HEIGHT = 128


class Player(MultiSprite):
    def __init__(self):
        MultiSprite.__init__(self)

        self.direction = DOWN
        self.speed = 8
        self.isMoving = False

    def loadRsc(self):
        # load animation frames for walk back view, front view and right view
        animTypes = 'back_walk front_walk right_walk'.split()
        for animType in animTypes:
            imagesAndDurations = [('images/Bman_%s_f%s.png' % (animType, str(num).rjust(2, '0')), 50) for num in range(8)]
            self.addAnimationFrames(animType, imagesAndDurations, PLAYER_WIDTH, PLAYER_HEIGHT)

        # create a transform a copy of right walk to create left walk
        rwa = self.getAnimation("right_walk")
        lwa = rwa[MultiSprite.INDEX_ANIM].getCopy()
        lwa.flip(True, False)
        self.animations["left_walk"] = [lwa, pygame.Rect(rwa[MultiSprite.INDEX_RECT])]

        # load/create stay still animation frames
        self.addAnimationFrames("front_standing", [('images/Bman_front_walk_f00.png', 100)], PLAYER_WIDTH, PLAYER_HEIGHT)
        self.addAnimationFrames("back_standing", [('images/Bman_back_walk_f00.png', 100)], PLAYER_WIDTH, PLAYER_HEIGHT)
        self.addAnimationFrames("right_standing", [('images/Bman_right_walk_f00.png', 100)], PLAYER_WIDTH, PLAYER_HEIGHT)

        # for left standing, create a transformed copy of right standing
        rsa = self.getAnimation("right_standing")
        lsa = rsa[MultiSprite.INDEX_ANIM].getCopy()
        lsa.flip(True, False)
        self.animations["left_standing"] = [lsa, pygame.Rect(rsa[MultiSprite.INDEX_RECT])]


    def processEvents(self, event):
        if event.type == KEYDOWN:
            if event.key == K_UP:
                self.direction = UP
                self.isMoving = True
            elif event.key == K_DOWN:
                self.direction = DOWN
                self.isMoving = True
            elif event.key == K_LEFT:
                self.direction = LEFT
                self.isMoving = True
            elif event.key == K_RIGHT:
                self.direction = RIGHT
                self.isMoving = True

        elif event.type == KEYUP:
            if event.key == K_UP:
                self.isMoving = False
            elif event.key == K_DOWN:
                self.isMoving = False
            elif event.key == K_LEFT:
                self.isMoving = False
            elif event.key == K_RIGHT:
                self.isMoving = False

    def update(self):
        if self.isMoving is True:
            inc_x = 0
            inc_y = 0
            if self.direction == UP:
                self.setAnimation("back_walk")
                inc_y = self.speed * -1
            if self.direction == DOWN:
                self.setAnimation("front_walk")
                inc_y = self.speed
            if self.direction == RIGHT:
                self.setAnimation("right_walk")
                inc_x = self.speed
            if self.direction == LEFT:
                self.setAnimation("left_walk")
                inc_x = self.speed * -1

            self.move(inc_x, inc_y)

        else:
            if self.direction == UP:
                self.setAnimation("back_standing")
            if self.direction == DOWN:
                self.setAnimation("front_standing")
            if self.direction == RIGHT:
                self.setAnimation("right_standing")
            if self.direction == LEFT:
                self.setAnimation("left_standing")

        return True


BOMB_WIDTH = 48
BOMB_HEIGHT = 48
DEFAULT_BOMB_DURATION = 5

class Bomb(Sprite):
    LOAD_RSC = False
    def __init__(self):
        Sprite.__init__(self)
        if Bomb.LOAD_RSC is False:
            imagesAndDurations = [('images/Bomb_f%s.png' % (str(num).rjust(2, '0')), 300) for num in range(3)]
            self.loadFrames(imagesAndDurations, BOMB_WIDTH, BOMB_HEIGHT)
            self.animation.play()
            Bomb.LOAD_RSC = True
        self.timeToExplosion = DEFAULT_BOMB_DURATION
        self.startTime = time.time()

    def createCopy(self):
        b = Bomb()
        s = Sprite.createCopy(self, False, False)
        b.animation = s.animation
        b.setPos(s.getPos())
        b.rect = s.getRect()
        b.animation.play()
        return b


    def update(self):
        Sprite.update(self)
        self.elapsed =  time.time() - self.startTime
        if self.elapsed > self.timeToExplosion:
            self.animation.stop()
            return False
        return True


FLAME_WIDTH = 48
FLAME_HEIGHT = 48
DEFAULT_FLAME_DURATION = 10

class Flame(Sprite):
    LOAD_RSC = False
    def __init__(self):
        Sprite.__init__(self)
        if Flame.LOAD_RSC is False:
            imagesAndDurations = [('images/Flame_f%s.png' % (str(num).rjust(2, '0')), 300) for num in range(3)]
            self.loadFrames(imagesAndDurations, FLAME_WIDTH, FLAME_HEIGHT)
            self.animation.play()
            Flame.LOAD_RSC = True
        self.timeToExtinguish = DEFAULT_FLAME_DURATION
        self.startTime = time.time()

    def createCopy(self):
        f = Flame()
        s = Sprite.createCopy(self, False, False)
        f.animation = s.animation
        f.setPos(s.getPos())
        f.rect = s.getRect()
        f.animation.play()
        return f


    def update(self):
        Sprite.update(self)
        self.elapsed =  time.time() - self.startTime
        if self.elapsed > self.timeToExtinguish:
            self.animation.stop()
            return False
        return True


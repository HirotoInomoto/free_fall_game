import math
import pygame
from pygame import K_SPACE
import pymunk
import random


pygame.init()

disp_size = (800, 900)
display = pygame.display.set_mode(disp_size)
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = 0, -400
FPS = 100

BLACK = (0, 0, 0)
WHEAT = (245, 222, 179)
WHITE = (255, 255, 255)

color_01 = (255,   0,   0)
color_02 = (255, 100, 100)
color_03 = (100,   0, 150)
color_04 = (255, 150,   0)
color_05 = (255, 100,   0)
color_06 = (255,   0,   0)
color_07 = (255, 255, 150)
color_08 = (255, 200, 200)
color_09 = (255, 200,   0)
color_10 = (100, 200,  50)
color_11 = (  0, 150,   0)

radius_01 = 10+5
radius_02 = 15+5
radius_03 = 20+5
radius_04 = 25+5
radius_05 = 30+5
radius_06 = 35+5
radius_07 = 40+5
radius_08 = 45+5
radius_09 = 50+5
radius_10 = 55+5
radius_11 = 60+5


def convert_cordinates(point):
    return point[0], disp_size[1]-point[1]

def rotate_cordinates(point, d):
    rad = math.radians(d)
    rotated_x = point[0] * math.cos(rad) - point[1] * math.sin(rad)
    rotated_y = point[0] * math.sin(rad) + point[1] * math.cos(rad)
    return rotated_x, rotated_y

class Ball(object):
    def __init__(self, x, y, color, radius, mass, collision_type, image=None):
        self.color = color
        self.radius = radius
        if image:
            loaded_image = pygame.image.load(image).convert_alpha()
            # 画像のサイズをボールの直径に基づいて調整します。
            self.original_image = pygame.transform.scale(loaded_image, (radius*2, radius*2))
        else:
            self.original_image = None
        self.body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        self.body.position = x, y
        self.body.mass = mass
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.collision_type = collision_type
        self.shape.density = 1
        self.shape.elasticity = 0.05
        self.shape.friction = 5
        space.add(self.body, self.shape)

    def draw(self):
        pos = convert_cordinates(self.body.position)
        if self.original_image:
            angle = math.degrees(self.body.angle)
            # 元の画像を回転させることで、画像の品質を保ちます。
            rotated_image = pygame.transform.rotate(self.original_image, angle)
            rect = rotated_image.get_rect(center=pos)
            display.blit(rotated_image, rect)
        else:
            pygame.draw.circle(
                display,
                self.color,
                pos,
                self.radius
            )

class Ball01(Ball):
    def __init__(self, x, y):
        # super().__init__(x, y, color_01, radius_01, 10, 1, "image/rdesign_09987.png")
        super().__init__(x, y, color_01, radius_01, 10, 1, "image/kotaro.png")
        pass

class Ball02(Ball):
    def __init__(self, x, y):
        # super().__init__(x, y, color_02, radius_02, 15, 2,"image/rdesign_09984.png")
        super().__init__(x, y, color_02, radius_02, 15, 2,"image/takato.png")
        pass

class Ball03(Ball):
    def __init__(self, x, y):
        # super().__init__(x, y, color_03, radius_03, 20, 3, "image/rdesign_09974.png")
        super().__init__(x, y, color_03, radius_03, 20, 3, "image/tetsuya.png")
        pass

class Ball04(Ball):
    def __init__(self, x, y):
        # super().__init__(x, y, color_04, radius_04, 25, 4, "image/rdesign_09980.png")
        super().__init__(x, y, color_04, radius_04, 25, 4, "image/seki.png")
        pass

class Ball05(Ball):
    def __init__(self, x, y):
        # super().__init__(x, y, color_05, radius_05, 30, 5, "image/rdesign_09982.png")
        super().__init__(x, y, color_05, radius_05, 30, 5, "image/papa.png")
        pass

class Ball06(Ball):
    def __init__(self, x, y):
        # super().__init__(x, y, color_06, radius_06, 35, 6, "image/rdesign_09971_resized.png")
        super().__init__(x, y, color_06, radius_06, 35, 6, "image/omio.png")
        pass

class Ball07(Ball):
    def __init__(self, x, y):
        # super().__init__(x, y, color_07, radius_07, 40, 7, "image/rdesign_09973.png")
        super().__init__(x, y, color_07, radius_07, 40, 7, "image/luc.png")
        pass

class Ball08(Ball):
    def __init__(self, x, y):
        # super().__init__(x, y, color_08, radius_08, 45, 8, "image/rdesign_09983.png")
        super().__init__(x, y, color_08, radius_08, 45, 8, "image/taki.png")
        pass

class Ball09(Ball):
    def __init__(self, x, y):
        # super().__init__(x, y, color_09, radius_09, 50, 9, "image/rdesign_09981.png")
        super().__init__(x, y, color_09, radius_09, 50, 9, "image/issei.png")
        pass

class Ball10(Ball):
    def __init__(self, x, y):
        # super().__init__(x, y, color_10, radius_10, 55, 10, "image/rdesign_09977.png")
        super().__init__(x, y, color_10, radius_10, 55, 10, "image/yusaku.png")
        pass

class Ball11(Ball):
    def __init__(self, x, y):
        # super().__init__(x, y, color_11, radius_11, 60, 11, "image/rdesign_09986.png")
        super().__init__(x, y, color_11, radius_11, 60, 11, "image/keiya.png")
        pass

def collide(arbiter, space, data):
    # collided shapes
    a, b = arbiter.shapes
    # collision type
    a_ct = a.collision_type
    b_ct = b.collision_type
    # 衝突処理を実施しない場合を判定
    if(a_ct != b_ct):
        # 異なるBall同士の衝突の場合
        return
    if(a_ct == 11 or b_ct == 11):
        # Ball11同士の衝突の場合
        return
    # 衝突座標を算出
    a_x, a_y = a.body.position
    b_x, b_y = b.body.position
    x = (a_x + b_x) / 2
    y = (a_y + b_y) / 2
    # 削除するBallを求める
    balls_to_remove = []
    for ball in data["balls"]:
        if(ball.shape == a or ball.shape == b):
            balls_to_remove.append(ball)
    # Ballを削除する
    for ball in balls_to_remove:
        space.remove(ball.shape, ball.body)
        data["balls"].remove(ball)
    # Ballの作成かつスコア更新
    if(a_ct == 1 and b_ct == 1):
        data["balls"].append(Ball02(x, y))
        data["score"] += 1
    elif(a_ct == 2 and b_ct == 2):
        data["balls"].append(Ball03(x, y))
        data["score"] += 3
    elif(a_ct == 3 and b_ct == 3):
        data["balls"].append(Ball04(x, y))
        data["score"] += 6
    elif(a_ct == 4 and b_ct == 4):
        data["balls"].append(Ball05(x, y))
        data["score"] += 10
    elif(a_ct == 5 and b_ct == 5):
        data["balls"].append(Ball06(x, y))
        data["score"] += 15
    elif(a_ct == 6 and b_ct == 6):
        data["balls"].append(Ball07(x, y))
        data["score"] += 21
    elif(a_ct == 7 and b_ct == 7):
        data["balls"].append(Ball08(x, y))
        data["score"] += 28
    elif(a_ct == 8 and b_ct == 8):
        data["balls"].append(Ball09(x, y))
        data["score"] += 36
    elif(a_ct == 9 and b_ct == 9):
        data["balls"].append(Ball10(x, y))
        data["score"] += 45
    elif(a_ct == 10 and b_ct == 10):
        data["balls"].append(Ball11(x, y))
        data["score"] += 55
    pass


class Field():
    def __init__(self, tlx, tly, brx, bry):
        self.tlx = tlx
        self.tly = tly
        self.brx = brx
        self.bry = bry
        self.edge = int(brx - tlx)
        self.step = 7
        self.width = 3
        # Start and Stop
        self.rl_start, self.rl_stop = (brx, tly), (brx, bry)
        self.bl_start, self.bl_stop = (tlx, bry), (brx, bry)
        self.ll_start, self.ll_stop = (tlx, tly), (tlx, bry)
        # Create Line
        self.create_line(self.rl_start, self.rl_stop)  # Right
        self.create_line(self.bl_start, self.bl_stop)  # Bottom
        self.create_line(self.ll_start, self.ll_stop)  # Left
    def draw(self):
        # Top Line
        for i in range(0, self.edge, self.step):
            if(i % (self.step * 2) == 0):
                pygame.draw.line(
                    display,
                    BLACK,
                    convert_cordinates((self.tlx+i, self.tly)),
                    convert_cordinates((self.tlx+i+self.step, self.tly)),
                    self.width
                )
        # Right Line
        pygame.draw.line(
            display,
            BLACK,
            convert_cordinates(self.rl_start),
            convert_cordinates(self.rl_stop),
            self.width
        )
        # Bottom Line
        pygame.draw.line(
            display,
            BLACK,
            convert_cordinates(self.bl_start),
            convert_cordinates(self.bl_stop),
            self.width
        )
        # Left Line
        pygame.draw.line(
            display,
            BLACK,
            convert_cordinates(self.ll_start),
            convert_cordinates(self.ll_stop),
            self.width
        )
    def create_line(self, start, stop):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape = pymunk.Segment(body, start, stop, self.width)
        shape.elasticity = 0.75
        shape.friction = 0.9
        space.add(shape, body)

class Circle(object):
    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
    def draw(self):
        pygame.draw.circle(
            display,
            self.color,
            convert_cordinates((self.x, self.y)),
            self.radius
        )

class CurrentCircle(Circle):
    def __init__(self, x, y, color, radius, start, stop):
        super().__init__(x, y, color, radius)
        self.dist = 10
        self.start = start
        self.stop = stop
    def get_ball(self):
        if(self.radius == radius_01):
            ball = Ball01(self.x, self.y)
        elif(self.radius == radius_02):
            ball = Ball02(self.x, self.y)
        elif(self.radius == radius_03):
            ball = Ball03(self.x, self.y)
        elif(self.radius == radius_04):
            ball = Ball04(self.x, self.y)
        elif(self.radius == radius_05):
            ball = Ball05(self.x, self.y)
        elif(self.radius == radius_06):
            ball = Ball06(self.x, self.y)
        elif(self.radius == radius_07):
            ball = Ball07(self.x, self.y)
        elif(self.radius == radius_08):
            ball = Ball08(self.x, self.y)
        elif(self.radius == radius_09):
            ball = Ball09(self.x, self.y)
        elif(self.radius == radius_10):
            ball = Ball10(self.x, self.y)
        elif(self.radius == radius_11):
            ball = Ball11(self.x, self.y)
        return ball
    def handle_keys(self):
        key = pygame.key.get_pressed()
        if(key[pygame.K_LEFT] and (self.x - self.dist) >= self.start):
            self.x -= self.dist
        if(key[pygame.K_RIGHT] and (self.x + self.dist) <= self.stop):
            self.x += self.dist

# r = 1

class NextCircle(Circle):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 1
        self.update()

    def update(self):
        
        self.r += 1

        # r = random.randint(1, 5)
        if(self.r == 1):
            self.color = color_01
            self.radius = radius_01
        elif(self.r == 2):
            self.color = color_02
            self.radius = radius_02
        elif(self.r == 3):
            self.color = color_03
            self.radius = radius_03
        elif(self.r == 4):
            self.color = color_04
            self.radius = radius_04
        elif(self.r == 5):
            self.color = color_05
            self.radius = radius_05
        elif(self.r == 6):
            self.color = color_06
            self.radius = radius_06
        elif(self.r == 7):
            self.color = color_07
            self.radius = radius_07
        elif(self.r == 8):
            self.color = color_08
            self.radius = radius_08
        elif(self.r == 9):
            self.color = color_09
            self.radius = radius_09
        elif(self.r == 10):
            self.color = color_10
            self.radius = radius_10
        elif(self.r == 11):
            self.color = color_11
            self.radius = radius_11        
            self.r = 1
        # if self.r==12:

def check_game_over(balls, y):
    result = False
    for ball in balls:
        ball_top = ball.body.position[1] + ball.shape.radius
        if(ball_top >= y):
            result = True
            break
    return result


def game():
    # Fiel d
    tlx, tly = 200, 750
    brx, bry = 600, 50
    field = Field(tlx, tly, brx, bry)
    step = 1

    # Ball in Field
    balls = []

    # Sample Ball
    cx, cy = 1000, 200
    sample_circles = [
        Circle(cx, cy, color_01, radius_01),
        Circle(cx, cy, color_02, radius_01),
        Circle(cx, cy, color_03, radius_01),
        Circle(cx, cy, color_04, radius_01),
        Circle(cx, cy, color_05, radius_01),
        Circle(cx, cy, color_06, radius_01),
        Circle(cx, cy, color_07, radius_01),
        Circle(cx, cy, color_08, radius_01),
        Circle(cx, cy, color_09, radius_01),
        Circle(cx, cy, color_10, radius_01),
        Circle(cx, cy, color_11, radius_01),
    ]
    for i, ball in enumerate(sample_circles):
        d = -30 + (-30) * i
        x, y = rotate_cordinates((0, 100), d)
        ball.x += x
        ball.y += y
        pass

    # Current Circle
    current_circle = CurrentCircle(
        tlx + (brx - tlx) / 2,  # フィールド中央
        tly + radius_11 +100,        # フィールド上端からボール6半径分上
        color_01,
        radius_01,
        tlx + radius_06,         # フィールド左端からボール6半径分内側
        brx - radius_06          # フィールド右端からボール6半径分内側
    )

    # Next Circle
    next_circle = NextCircle(cx, cx)  # サンプルボールの上方に表示

    # CollisionHandler
    handler = space.add_default_collision_handler()
    handler.data["balls"] = balls
    handler.data["score"] = 0
    handler.post_solve = collide

    # Common Font
    font = pygame.font.SysFont(None, 50)
    # Next Text
    next_text = font.render("Next", True, BLACK)
    next_rect = next_text.get_rect(
        midbottom=convert_cordinates((cx, cx+radius_06))
    )

    # Game Over Custom Event
    CHECKGAMEOVER = pygame.USEREVENT + 1
    # Game Over Flag
    GAME_OVER_FLAG = False


    # Game Start
    while(not GAME_OVER_FLAG):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                return
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                # if(pygame.key.get_pressed()[pygame.K_SPACE]):
                    # Reset Game Over Custom Event
                    pygame.time.set_timer(CHECKGAMEOVER, 0)
                    # Drop Current Circle
                    balls.append(current_circle.get_ball())
                    # Update Current Circle
                    current_circle.color = next_circle.color
                    current_circle.radius = next_circle.radius
                    # Update Next Circle
                    next_circle.update()
                    # Set Game Over Custom Event
                    pygame.time.set_timer(CHECKGAMEOVER, 1000)
            # if(event.type == CHECKGAMEOVER):
            #     # Check Game Over
            #     GAME_OVER_FLAG = check_game_over(balls, tly)
                
        # Fill background
        display.fill(WHEAT)

        # Draw Field
        field.draw()

        # Draw Ball in Field
        for ball in balls:
            ball.draw()
        
        # Draw Sample Ball
        for ball in sample_circles:
            ball.draw()
        
        # Draw Current Circle
        current_circle.draw()
        current_circle.handle_keys()

        # Draw Next Circle
        next_circle.draw()

        # Draw Next Text
        display.blit(next_text, next_rect)

        # # Draw Score Text
        # score_text = font.render("Score: {:,}".format(handler.data["score"]), True, BLACK)
        # score_rect = score_text.get_rect(
        #     bottomleft=convert_cordinates((tlx, cx+radius_06))
        # )
        # display.blit(score_text, score_rect)

        # Display Update
        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)

        step += 1
        if step>15:
            current_circle.x = random.randint(250, 550)
            pygame.time.set_timer(CHECKGAMEOVER, 0)
            # Drop Current Circle
            balls.append(current_circle.get_ball())
            # Update Current Circle
            current_circle.color = next_circle.color
            current_circle.radius = next_circle.radius
            # Update Next Circle
            next_circle.update()
            step = 1
    
    # Game Over Text
    game_over_text = font.render("Game Over", True, BLACK)
    game_over_rect = game_over_text.get_rect(
        midbottom=(disp_size[0]/2, disp_size[1]/2)
    )

    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                return
        # Fill background
        display.fill(WHEAT)

        # Draw Field
        field.draw()

        # Draw Ball in Field
        for ball in balls:
            ball.draw()
        
        # Draw Sample Ball
        for ball in sample_circles:
            ball.draw()
        
        # Draw Current Circle
        current_circle.draw()

        # Draw Next Circle
        next_circle.draw()

        # Draw Next Text
        display.blit(next_text, next_rect)

        # Draw Score Text
        score_text = font.render("Score: {:,}".format(handler.data["score"]), True, BLACK)
        score_rect = score_text.get_rect(
            bottomleft=convert_cordinates((tlx, cx+radius_06))
        )
        display.blit(score_text, score_rect)

        # Draw Game Over Text
        display.blit(game_over_text, game_over_rect)

        # Display Update
        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)




game()
pygame.quit()
import pygame
import random
import time

pygame.init()

# -------------------- WINDOW --------------------
WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smart Traffic Junction – SUMO Queue Model")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 18)
big_font = pygame.font.Font(None, 26)

# -------------------- COLORS --------------------
BG = (210, 210, 210)
ROAD = (90, 90, 90)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 180, 0)
CAR = (50, 120, 230)
BUS = (20, 170, 20)
TRUCK = (120, 120, 120)
AMBULANCE = (255, 140, 0)
FIRE = (255, 220, 0)
GLASS = (180, 220, 255)

# -------------------- JUNCTION --------------------
CENTER = WIDTH // 2
ROAD_WIDTH = 130
LANE_OFFSET = 24
CAR_SPEED = 2
SAFE_GAP = 8

directions = ["North", "East", "South", "West"]
current_green = "North"
green_timer = 30

# -------------------- VEHICLE TYPES --------------------
vehicle_types = {
    "Car": (CAR, (22, 34)),
    "Bus": (BUS, (26, 46)),
    "Truck": (TRUCK, (28, 42)),
    "Ambulance": (AMBULANCE, (24, 36)),
    "Fire": (FIRE, (24, 36))
}

vehicles = {d: [] for d in directions}
waiting_time = {d: 0 for d in directions}

emergency_active = False
emergency_direction = None

# -------------------- STOP LINES --------------------
stop_lines = {
    "North": CENTER - ROAD_WIDTH // 2,
    "South": CENTER + ROAD_WIDTH // 2,
    "West":  CENTER - ROAD_WIDTH // 2,
    "East":  CENTER + ROAD_WIDTH // 2
}

# -------------------- VEHICLE CLASS --------------------
class Vehicle:
    def __init__(self, direction, lane):
        self.direction = direction
        self.lane = lane
        self.type = random.choices(
            list(vehicle_types.keys()),
            weights=[55, 20, 15, 5, 5]
        )[0]

        self.color, (self.w, self.h) = vehicle_types[self.type]
        self.spawn_time = time.time()

        if direction == "North":
            self.x = CENTER - lane * LANE_OFFSET
            self.y = -60
        elif direction == "South":
            self.x = CENTER + lane * LANE_OFFSET
            self.y = HEIGHT + 60
        elif direction == "West":
            self.x = -60
            self.y = CENTER + lane * LANE_OFFSET
        else:
            self.x = WIDTH + 60
            self.y = CENTER - lane * LANE_OFFSET

    def front_pos(self):
        return self.y + self.h if self.direction == "North" else \
               self.y if self.direction == "South" else \
               self.x + self.w if self.direction == "West" else \
               self.x

    def move(self, can_go, front_vehicle):
        if not can_go and front_vehicle is None:
            if self.direction == "North" and self.y + self.h >= stop_lines["North"]:
                return
            if self.direction == "South" and self.y <= stop_lines["South"]:
                return
            if self.direction == "West" and self.x + self.w >= stop_lines["West"]:
                return
            if self.direction == "East" and self.x <= stop_lines["East"]:
                return

        if front_vehicle:
            gap = front_vehicle.front_pos() - self.front_pos()
            if gap <= SAFE_GAP:
                return

        if self.direction == "North":
            self.y += CAR_SPEED
        elif self.direction == "South":
            self.y -= CAR_SPEED
        elif self.direction == "West":
            self.x += CAR_SPEED
        else:
            self.x -= CAR_SPEED

    def draw(self):
        body = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(screen, self.color, body, border_radius=4)
        glass = pygame.Rect(self.x + 4, self.y + 5, self.w - 8, 7)
        pygame.draw.rect(screen, GLASS, glass, border_radius=2)

        label = font.render(self.type, True, BLACK)
        screen.blit(label, (self.x, self.y - 14))

# -------------------- FUNCTIONS --------------------
def spawn_vehicles():
    for d in directions:
        if len(vehicles[d]) < 6:
            vehicles[d].append(Vehicle(d, random.choice([1, 2])))

def draw_roads():
    screen.fill(BG)
    pygame.draw.rect(screen, ROAD, (CENTER - ROAD_WIDTH // 2, 0, ROAD_WIDTH, HEIGHT))
    pygame.draw.rect(screen, ROAD, (0, CENTER - ROAD_WIDTH // 2, WIDTH, ROAD_WIDTH))

def draw_signals():
    positions = {
        "North": (CENTER - 35, CENTER - 90),
        "South": (CENTER + 25, CENTER + 70),
        "West": (CENTER - 90, CENTER + 25),
        "East": (CENTER + 70, CENTER - 35),
    }

    for d, (x, y) in positions.items():
        active = d == (emergency_direction if emergency_active else current_green)
        pygame.draw.circle(screen, GREEN if active else RED, (x, y), 11)

        t = big_font.render(str(green_timer if active else "-"), True, BLACK)
        screen.blit(t, (x - 8, y + 14))

        wt = font.render(f"Wait: {waiting_time[d]}s", True, BLACK)
        screen.blit(wt, (x - 35, y - 30))

def update_vehicles():
    active_dir = emergency_direction if emergency_active else current_green

    for d in directions:
        can_go = d == active_dir
        lane_groups = {}

        for v in vehicles[d]:
            lane_groups.setdefault(v.lane, []).append(v)

        for lane, lane_vehicles in lane_groups.items():
            for i, v in enumerate(lane_vehicles):
                front = lane_vehicles[i - 1] if i > 0 else None
                v.move(can_go, front)

        vehicles[d] = [v for v in vehicles[d] if -100 < v.x < WIDTH + 100 and -100 < v.y < HEIGHT + 100]

def emergency_detector():
    global emergency_active, emergency_direction
    if not emergency_active and random.randint(1, 900) == 1:
        emergency_direction = random.choice(directions)
        emergency_active = True

    if emergency_active and not vehicles[emergency_direction]:
        emergency_active = False

# -------------------- MAIN LOOP --------------------
frame = 0
running = True

while running:
    clock.tick(60)
    frame += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    spawn_vehicles()
    emergency_detector()

    if frame % 60 == 0:
        waiting_time[current_green] += 1
        green_timer -= 1
        if green_timer <= 0:
            current_green = directions[(directions.index(current_green) + 1) % 4]
            green_timer = 30

    update_vehicles()

    draw_roads()
    draw_signals()

    for d in directions:
        for v in vehicles[d]:
            v.draw()

    pygame.display.flip()

pygame.quit()

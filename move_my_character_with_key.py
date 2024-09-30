from pico2d import *

open_canvas()

ground = load_image('TUK_GROUND.png')
character = load_image('dog_sprite.png')

def handle_events():
    global running, dirX, dirY, imageY, w, h
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirX= 1
                imageY = 1
                w = 256
                y = 200
            elif event.key == SDLK_LEFT:
                dirX = -1
                imageY = 2
                w = 256
                y = 200
            elif event.key == SDLK_UP:
                dirY = 1
                imageY = 0
                w = 200
                y = 256
            elif event.key == SDLK_DOWN:
                dirY = -1
                imageY = 3
                w = 200
                y = 256
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirX = 0
            elif event.key == SDLK_LEFT:
                dirX = 0
            elif event.key == SDLK_UP:
                dirY = 0
            elif event.key == SDLK_DOWN:
                dirY = -0

running = True
x = 800 // 2
y = 600 // 2
w = 200
h = 200
frame = 0
dirX = 0
dirY = 0
imageY = 3

while running:
    clear_canvas()
    ground.draw(400, 300)
    character.clip_draw(frame * 256, imageY * 256, w, h, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 4
    if x < 780 and dirX > 0 :
        x += dirX * 10
    if y < 580 and dirY > 0:
        y += dirY * 10
    if dirX < 0 and x > 20 :
        x += dirX * 10
    if dirY < 0 and y > 20:
        y += dirY * 10
    delay(0.1)

close_canvas()
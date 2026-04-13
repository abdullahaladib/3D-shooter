from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import random

ARENA_SIZE = 15
TILE_SIZE = 1.0
TOTAL_ENEMIES = 5
PROJECTILE_SPEED = 0.3
camera_angle = 0
camera_radius = 15
camera_height = 18
camera_mode = True
player_x = ARENA_SIZE / 2
player_z = ARENA_SIZE / 2
player_rot = 0
player_health = 5
player_score = 0
shots_missed = 0
auto_mode = False
fire_delay = 0
death_rot = 0
game_over = False
shots = []
enemies = []

def spawn_enemy():
    while True:
        x = random.uniform(1, ARENA_SIZE-1)
        z = random.uniform(1, ARENA_SIZE-1)
        if abs(x-player_x) > 3 and abs(z-player_z) > 3:
            return {"x":x, "z":z, "scale":1.0, "shrink":True}

def reset_game():
    global player_x, player_z, player_rot, player_health
    global player_score, shots_missed, shots, enemies, game_over, death_rot
    player_x = ARENA_SIZE/2
    player_z = ARENA_SIZE/2
    player_rot = 0
    player_health = 5
    player_score = 0
    shots_missed = 0
    shots = []
    enemies = [spawn_enemy() for _ in range(TOTAL_ENEMIES)]
    game_over = False
    death_rot = 0

def draw_floor():
    for i in range(ARENA_SIZE):
        for j in range(ARENA_SIZE):
            glColor3f(1, 1, 1) if (i+j)%2==0 else glColor3f(0.627, 0.125, 0.941)
            glBegin(GL_QUADS)
            glVertex3f(i,0,j)
            glVertex3f(i+1,0,j)
            glVertex3f(i+1,0,j+1)
            glVertex3f(i,0,j+1)
            glEnd()

def draw_walls():
    L = ARENA_SIZE
    glColor3f(0,0,1)
    glPushMatrix()
    glTranslatef(L/2,0.5,0.1)
    glScalef(L,1,0.2)
    glutSolidCube(1)
    glPopMatrix()

    glColor3f(0,1,0)
    glPushMatrix()
    glTranslatef(L/2,0.5,L-0.1)
    glScalef(L,1,0.2)
    glutSolidCube(1)
    glPopMatrix()

    glColor3f(0,1,1)
    glPushMatrix()
    glTranslatef(0.1,0.5,L/2)
    glScalef(0.2,1,L)
    glutSolidCube(1)
    glPopMatrix()

    glColor3f(1,0,1)
    glPushMatrix()
    glTranslatef(L-0.1,0.5,L/2)
    glScalef(0.2,1,L)
    glutSolidCube(1)
    glPopMatrix()

def draw_player():
    global death_rot
    glPushMatrix()
    glTranslatef(player_x,0,player_z)
    glRotatef(player_rot,0,1,0)
    if game_over:
        death_rot = min(death_rot+1,90)
        glRotatef(death_rot,1,0,0)
    glScalef(0.9,0.9,0.9)

    glColor3f(0,0,1)
    for o in [-0.2,0.2]:
        glPushMatrix()
        glTranslatef(o,0.4,0)
        glRotatef(-90,1,0,0)
        gluCylinder(gluNewQuadric(),0.1,0.05,0.4,10,10)
        glPopMatrix()

    glColor3f(0.4,0.5,0.2)
    glPushMatrix()
    glTranslatef(0,1,0)
    glScalef(0.4,0.6,0.2)
    glutSolidCube(1)
    glPopMatrix()

    glColor3f(0.96,0.8,0.69)
    for o in [-0.15,0.15]:
        glPushMatrix()
        glTranslatef(o,1.2,0.1)
        gluCylinder(gluNewQuadric(),0.1,0.05,0.4,10,10)
        glPopMatrix()

    glColor3f(0.5,0.5,0.5)
    glPushMatrix()
    glTranslatef(0,1.2,0.1)
    gluCylinder(gluNewQuadric(),0.08,0,0.8,10,10)   # parameters are: quadric, base radius, top radius, height, slices, stacks
    glTranslatef(100, 0, 100) 
    glPopMatrix()

    glColor3f(0,0,0)
    glPushMatrix()
    glTranslatef(0,1.65,0)
    gluSphere(gluNewQuadric(),0.2,10,10)
    glPopMatrix()
    glPopMatrix()

def draw_enemies():
    for e in enemies:
        glPushMatrix()
        glTranslatef(e["x"],0.4,e["z"])
        glScalef(e["scale"],e["scale"],e["scale"])
        glColor3f(1,0,0)
        glutSolidSphere(0.2,10,10)
        glColor3f(0,0,0)
        glTranslatef(0,0.25,0)
        glutSolidSphere(0.12,10,10)
        glPopMatrix()

def draw_shots():
    glColor3f(0.8,0.33,0)
    for s in shots:
        glPushMatrix()
        glTranslatef(s["x"],1.2,s["z"])
        glScalef(0.15,0.15,0.15)
        glutSolidCube(1)
        glPopMatrix()
def draw_text(x, y, text, font=GLUT_BITMAP_HELVETICA_18): # type: ignore
    glColor3f(1,1,1)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, 1000, 0, 800)

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(font, ord(ch))

    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

def idle():
    global fire_delay, shots_missed, game_over, player_health, player_score

    if game_over:
        glutPostRedisplay()
        return

    if auto_mode:
        global player_rot
        player_rot = (player_rot + 2) % 360
        if fire_delay == 0 and enemies:
            t = enemies[0]
            ang = math.degrees(math.atan2(t["x"]-player_x, t["z"]-player_z))
            shots.append({"x":player_x,"z":player_z,"a":ang})
            fire_delay = 60
        fire_delay = max(fire_delay-1,0)

    new_shots = []
    for s in shots:
        s["x"] += PROJECTILE_SPEED*math.sin(math.radians(s["a"]))
        s["z"] += PROJECTILE_SPEED*math.cos(math.radians(s["a"]))
        hit = False
        for e in enemies[:]:
            if math.hypot(s["x"]-e["x"], s["z"]-e["z"]) < 0.5:
                enemies.remove(e)
                player_score += 10
                hit = True
                break
        if not hit:
            if 0<=s["x"]<=ARENA_SIZE and 0<=s["z"]<=ARENA_SIZE:
                new_shots.append(s)
            else:
                shots_missed += 1
    shots[:] = new_shots

    for e in enemies[:]:
        dx = player_x-e["x"]
        dz = player_z-e["z"]
        d = math.hypot(dx,dz)
        if d>0:
            e["x"] += 0.0015*dx/d
            e["z"] += 0.0015*dz/d
        e["scale"] += (-0.002 if e["shrink"] else 0.002)
        if e["scale"]<0.6: e["shrink"]=False
        if e["scale"]>1.2: e["shrink"]=True
        if d<0.5:
            player_health -= 1
            enemies.remove(e)

    while len(enemies)<TOTAL_ENEMIES:
        enemies.append(spawn_enemy())

    if player_health<=0 or shots_missed>=10:
        game_over=True

    glutPostRedisplay()


# ================= INPUT =================
def special_keys(key, x, y):
    global camera_angle, camera_radius, camera_height
    if key == GLUT_KEY_LEFT:
        camera_angle = (camera_angle - 5) % 360
    elif key == GLUT_KEY_RIGHT:
        camera_angle = (camera_angle + 5) % 360
    elif key == GLUT_KEY_UP:
        camera_radius = max(camera_radius - 1, 5)
        camera_height = max(camera_height - 1, 8)
    elif key == GLUT_KEY_DOWN:
        camera_radius = min(camera_radius + 1, 25)
        camera_height = min(camera_height + 1, 25)
    glutPostRedisplay()


def keyboard(key,x,y):
    global player_x, player_z, player_rot, auto_mode
    if game_over:
        if key==b'r': reset_game()
        return
    if key==b'w':
        player_x += 0.2*math.sin(math.radians(player_rot))
        player_z += 0.2*math.cos(math.radians(player_rot))
    if key==b's':
        player_x -= 0.2*math.sin(math.radians(player_rot))
        player_z -= 0.2*math.cos(math.radians(player_rot))
    if key==b'a': player_rot=(player_rot-5)%360
    if key==b'd': player_rot=(player_rot+5)%360
    if key==b'c': auto_mode=not auto_mode
    
    min_pos = 0.5
    max_pos = ARENA_SIZE - 0.5
    player_x = max(min(player_x, max_pos), min_pos)
    player_z = max(min(player_z, max_pos), min_pos)

def mouse(btn,state,x,y):
    global camera_angle, camera_radius, camera_height, shots, game_over, camera_mode
    if btn==GLUT_LEFT_BUTTON and state==GLUT_DOWN and not game_over:
        shots.append({"x":player_x,"z":player_z,"a":player_rot})
    if btn==GLUT_RIGHT_BUTTON and state==GLUT_DOWN and not game_over:
        camera_mode = not camera_mode
# ================= CAMERA =================
def camera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45,1.25,1,100)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    if not camera_mode:
        eye_x = player_x + 0.7*math.sin(math.radians(player_rot + 180))
        eye_y = 1.5  # slightly lower than head, approx gun base
        eye_z = player_z + 0.7*math.cos(math.radians(player_rot + 180))  # forward offset

    # Camera looks along gun direction

        center_x = eye_x + math.sin(math.radians(player_rot)) * 0.8
        center_y = eye_y
        center_z = eye_z + math.cos(math.radians(player_rot)) * 0.8

        gluLookAt(eye_x, eye_y, eye_z, center_x, center_y, center_z, 0, 1, 0)
    else:
        x = ARENA_SIZE/2 + camera_radius*math.sin(math.radians(camera_angle))
        z = ARENA_SIZE/2 + camera_radius*math.cos(math.radians(camera_angle))
        gluLookAt(x,camera_height,z, ARENA_SIZE/2,0,ARENA_SIZE/2, 0,1,0)

# ================= DISPLAY =================
def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    camera()
    draw_floor()
    draw_walls()
    draw_player()
    draw_shots()
    draw_enemies()

    # ---------- UI TEXT ----------
    if not game_over:
        draw_text(10, 770, f"Score: {player_score}")
        draw_text(10, 745, f"Life: {player_health}")
        draw_text(10, 720, f"Missed: {shots_missed}")

        if auto_mode:
            draw_text(800, 770, "CHEAT MODE ON")
    else:
        # Show only Game Over and restart instructions
        draw_text(10, 770, "GAME OVER", GLUT_BITMAP_HELVETICA_18) # type: ignore
        draw_text(10, 745, "Press 'r' to Restart", GLUT_BITMAP_HELVETICA_18) # type: ignore

    glutSwapBuffers()


# ================= MAIN =================
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
    glutInitWindowSize(1000,800)
    glutCreateWindow(b"Combat Arena")
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special_keys)
    glutMouseFunc(mouse)
    glutIdleFunc(idle)
    glutMainLoop()

main()

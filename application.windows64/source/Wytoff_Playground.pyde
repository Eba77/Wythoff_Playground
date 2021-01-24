TRIANGLE_MODE = None
class STAR_632:
    def __init__(self):
        global TRIANGLE_MODE
        TRIANGLE_MODE = STAR_632
        
    @staticmethod
    def asstr():
        return "*632"
        
class STAR_442:
    def __init__(self):
        global TRIANGLE_MODE
        TRIANGLE_MODE = STAR_442
        
    @staticmethod
    def asstr():
        return "*442"

SIZE = 500
TRIANGLE_MODE = STAR_632
blue_point_x, blue_point_y = 0, 20
mouse_x, mouse_y = 0, 0

def setup():
    global SIZE
    size(SIZE, SIZE, P2D)
    textAlign(CENTER, CENTER)
    
    # Button positions are relative to the bottom-right
    # portion of the screen
    Button(SIZE // 4 - 50, 10, 40, 10, STAR_632, STAR_632.asstr())
    Button(SIZE // 4 - 50, 30, 40, 10, STAR_442, STAR_442.asstr())
    
class Button:
    all_buttons = set({})
    def __init__(self, x, y, sx, sy, on_click, txt):
        self.x = x
        self.y = y
        self.size_x = sx
        self.size_y = sy
        self.topright = x + sx
        self.bottomleft = y + sy
        self.on_click = on_click
        self.txt = txt
        Button.all_buttons.add(self)
        
    def draw_button(self):
        pushMatrix()
        translate(self.x, self.y)
        textSize(10)
        stroke(0, 0, 0)
        fill(0, 255, 255)
        rect(0, 0, self.size_x, self.size_y)
        fill(0, 0, 0)
        text(self.txt, self.size_x // 2, self.size_y // 2)
        popMatrix()
        
        
    def handle_click(self, mx, my):
        if (
            mx > self.x
            and mx < self.topright
            and my > self.y
            and my < self.bottomleft
        ):
            # clicked on!
            self.on_click()
    
    @staticmethod
    def draw_buttons():
        for button in Button.all_buttons:
            button.draw_button()
            
    @staticmethod
    def check_clicks(mx, my):
        for button in Button.all_buttons:
            button.handle_click(mx, my)
    
def draw():
    global SIZE, TRIANGLE_MODE, blue_point_x, blue_point_y
    global mouse_x, mouse_y
    background(127, 127, 127)
    translate(SIZE // 2, SIZE // 2)
    
    # Draw tiling
    pushMatrix()
    scale(1.2, 1.2)
    draw_tiling(0, 0)
    popMatrix()
    
    # Draw wytoff playground moveable box
    fill(255, 255, 255)
    translate(SIZE // 4, SIZE // 4)
    rect(0, 0, SIZE // 4, SIZE // 4)
    
    # Draw current mode
    textSize(14)
    fill(0, 0, 0)
    text(TRIANGLE_MODE.asstr(), SIZE // 16, 10)
    
    # Mouse coordinate translations must be done manually
    mouse_x = mouseX - 3 * SIZE // 4
    mouse_y = mouseY - 3 * SIZE // 4
    
    Button.draw_buttons()
    if mousePressed:
        Button.check_clicks(mouse_x, mouse_y)
        blue_point_x, blue_point_y = 0, 20
    
    # Draw triangle!
    px = SIZE // 8 + 30 if TRIANGLE_MODE == STAR_632 else SIZE // 8
    draw_triangle(px, SIZE // 8, calc_mouse=True)
    
def draw_tiling(x, y, depth=4):
    global TRIANGLE_MODE
    pushMatrix()
    translate(x, y)
    
    if TRIANGLE_MODE == STAR_632:
        draw_triangle(0, 0)
        
        pushMatrix()
        rotate(PI)
        draw_triangle(0, 0)
        popMatrix()
        
        pushMatrix()
        rotate(4*PI/6)
        scale(1, -1)
        draw_triangle(0, 0)
        popMatrix()
        
        pushMatrix()
        rotate(-PI/3)
        scale(1, -1)
        draw_triangle(0, 0)
        popMatrix()
        
    else:
        draw_triangle(0, 0)
        pushMatrix()
        rotate(PI)
        draw_triangle(0, 0)
        popMatrix()
        pushMatrix()
        rotate(PI/2)
        scale(1, -1)
        draw_triangle(0, 0)
        popMatrix()
        pushMatrix()
        rotate(-PI/2)
        scale(1, -1)
        draw_triangle(0, 0)
        popMatrix()
    
    if depth > 0:
        # recurse tilling
        if TRIANGLE_MODE == STAR_442:
            d = 120*cos(PI / 4)
            scale(1, -1)
            draw_tiling(d, 0, depth=depth-1)
            draw_tiling(-d, 0, depth=depth-1)
            draw_tiling(0, d, depth=depth-1)
            draw_tiling(0, -d, depth=depth-1)
        elif TRIANGLE_MODE == STAR_632:
            pushMatrix()
            scale(1, -1)
            rotate(-60*PI/180)
            dx = 75
            dy = 44
            draw_tiling(dx, dy, depth=depth-1)
            popMatrix()
            
            pushMatrix()
            scale(1, -1)
            rotate(-60*PI/180)
            dx = -75
            dy = -44
            draw_tiling(dx, dy, depth=depth-1)
            popMatrix()
            
            pushMatrix()
            rotate(240*PI/180)
            dy = -44
            dx = -75
            draw_tiling(dx, dy, depth=depth-1)
            popMatrix()
            
            pushMatrix()
            rotate(240*PI/180)
            dy = 44
            dx = 75
            draw_tiling(dx, dy, depth=depth-1)
            popMatrix()

    
    popMatrix()
    
def draw_triangle(tri_x, tri_y, calc_mouse=False):
    global TRIANGLE_MODE, blue_point_x, blue_point_y
    global mouse_x, mouse_y
    pushMatrix()
    translate(tri_x, tri_y)
    mouse_x -= tri_x
    mouse_y -= tri_y
    if TRIANGLE_MODE == STAR_442:
        ts = 60 # triangle size parameter
        delx = ts * sin(PI / 4)
        dely = ts * cos(PI / 4)
        tx1, ty1 = 0, 0
        tx2, ty2 = tx1 - delx, ty1 + dely
        tx3, ty3 = tx1 + delx, ty1 + dely
        stroke(0, 0, 0)
        fill(200, 100, 100)
        triangle(tx1, ty1, tx2, ty2, tx3, ty3)
    elif TRIANGLE_MODE == STAR_632:
        ts = 50 # triangle size parameter
        tx1, ty1 = 0, 0
        dy = ts / 2 * sqrt(3)
        tx2, ty2 = tx1 - dy / tan(PI / 6), ty1 + dy
        tx3, ty3 = tx1 + dy / tan(PI / 3), ty1 + dy
        stroke(0, 0, 0)
        fill(200, 100, 100)
        triangle(tx1, ty1, tx2, ty2, tx3, ty3)
        
    def inside_triangle(px, py):
        # Check if point is inside triangle
        # Code from (link split onto two lines):
        # https://stackoverflow.com/questions/2049582/
        # how-to-determine-if-a-point-is-in-a-2d-triangle
        # It uses 'barycentric coordinates' to determine if inside
        # the triangle!
        area = 0.5 *(-ty2*tx3 + ty1*(-tx2 + tx3) + tx1*(ty2 - ty3) + tx2*ty3);
        s = 1/(2*area)*(ty1*tx3 - tx1*ty3 + (ty3 - ty1)*px + (tx1 - tx3)*py)
        t = 1/(2*area)*(tx1*ty2 - ty1*tx2 + (ty1 - ty2)*px + (tx2 - tx1)*py)
        return s > 0 and t > 0 and (1-s-t) > 0
        
    fill(0, 0, 255)
    if calc_mouse and inside_triangle(mouse_x, mouse_y):
        blue_point_x = mouse_x
        blue_point_y = mouse_y
    circle(blue_point_x, blue_point_y, 10)
    
    # We want to draw the perpendicular lines
    # to triangle's edge
    stroke(0, 0, 255)
    def drop_perp(ax, ay, bx, by):
        # a & b are vertices of line segment
        # you want to drop perp from blue point to
        px, py = blue_point_x, blue_point_y
        pmax, pmay = px - ax, py - ay
        bmax, bmay = bx - ax, by - ay
        bdp = (pmax * bmax + pmay * bmay) / (bmax**2 + bmay**2)
        dx, dy = pmax - bdp * bmax, pmay - bdp * bmay
        line(px, py, px - dx, py - dy)
            
        
    # right edge
    drop_perp(tx1, ty1, tx2, ty2)
    drop_perp(tx1, ty1, tx3, ty3)
    drop_perp(tx2, ty2, tx3, ty3)
        
        
        
    popMatrix()
    
    
    

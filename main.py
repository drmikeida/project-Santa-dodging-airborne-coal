import pyxel
import time
time.sleep(5)
class App:
    def __init__(self):
        # Initialize the Pyxel window (width, height)
        pyxel.init(160, 120)

        pyxel.load("my_resource.pyxres")
        
        # Set the initial position of the santa
        self.x = 20
        self.y = 55
        self.score = 0
        
        
        # Set the initial position and velocity of the coals
        self.sprite_x = 150
        self.sprite_y = pyxel.rndi(0, 120)
        self.sprite_dx = 2
        self.sprite_dy = 2

        self.spreet_x = 150
        self.spreet_y = pyxel.rndi(0, 120)
        self.spreet_dx = 2
        self.spreet_dy = 2
        
        # Start the game loop
        pyxel.run(self.update, self.draw)

    def update(self):
        # Update the square's position based on arrow keys
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= 2
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 2
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 2

        
        if pyxel.frame_count % 25 == 0:
            self.score += 100

        
        # Change the sprite's direction to move left 
        self.sprite_x += pyxel.rndi(-4, -5)
        if self.sprite_x < 0:
            self.sprite_x = 160
            self.sprite_y = pyxel.rndi(0, 120)
            self.sprite_dx = -2
            self.sprite_dy = -2


        self.spreet_x += pyxel.rndi(-3, -4)
        if self.spreet_x < 0:
            self.spreet_x = 160
            self.spreet_y = pyxel.rndi(0, 120)
            self.spreet_dx = -2
            self.spreet_dy = -2
        
        
        if self.x <= 0:
            self.x += 2
        if self.x >= 145:
            self.x -= 2
        if self.y <= 0:
            self.y += 2
        if self.y >= 105:
            self.y -= 2
        
        
        if abs(self.x - self.sprite_x) <= 10 and abs(self.y - self.sprite_y) <= 10:
            time.sleep(5)
            pyxel.quit()
        if abs(self.x - self.spreet_x) <= 15 and abs(self.y - self.spreet_y) <= 15:
            time.sleep(5)
            pyxel.quit()
            
        
            


        
    def draw(self):
        
        pyxel.cls(7)

        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16)  
        
        pyxel.blt(self.sprite_x, self.sprite_y, 2, 0, 0, 8, 8)

        pyxel.blt(self.spreet_x, self.spreet_y,1, 0, 0, 8, 8)
        
        pyxel.text(5, 5, f"Score: {self.score}", 0)
        
App()









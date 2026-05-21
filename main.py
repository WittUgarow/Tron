import pygame, sys
import numpy

width = 500
height = width

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
size = 10
speed = 10
gameSpeed=.3
running = True

cols = int(height/size)
rows = int(height/size)

spaces = numpy.zeros((int(height/size), int(width/size)))

def printMap():
  for row in spaces:
    txt=""
    for col in row:
      txt+=" "+str(col)
    print(txt)
  print("\n")

class Player:
  
  def die(self):
    global running
    screen.fill(red)
    running = False
    #pygame.quit()

  def clamp(self, min, max, value):
    if(value>max):
      value=max
      self.die()
    if(value<min):
      value=min
      self.die()
    return value
  
  def getArrayPos(self, pos):
    row = self.clamp(0, len(spaces)-1, round(pos[0]/size))
    col = self.clamp(0, len(spaces[row])-1, round(pos[1]/size))
    self.row=row
    self.col=col
  
  def __init__(self, color, x, y, direction, number):
    self.color = color
    self.x = x
    self.y = y
    self.direction = direction
    self.number = number
    self.getArrayPos((x,y))
    
  def fillSpace(self):
    #print(f"{self.row}, {self.col}\n")
    spaces[self.row][self.col]=1
    
  def checkCollide(self, pos):
    if(spaces[pos[0]][pos[1]]==1):
      self.die()
  
  def turn(self, x, y):
    self.direction = (x,y) if x!=self.direction[0]*-1 and y!=self.direction*-1 else self.direction

  def draw(self):
    pygame.draw.rect(screen, self.color, (self.x, self.y, size, size))
  
  def move(self):
    self.checkCollide((self.row, self.col))
    self.draw()
    self.fillSpace()
    self.x += self.direction[0]*speed
    self.y += self.direction[1]*speed
    self.getArrayPos((self.x, self.y))
    
p1 = Player(blue, 50, 50, (0, 1), 1)
p2 = Player(red, 450, 450, (0,-1), 2)
players = [p1, p2]


while running:
  clock.tick(60*gameSpeed)
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
          p1.turn(0, -1)
        if event.key == pygame.K_s:
          p1.turn(0, 1)
        if event.key == pygame.K_a:
          p1.turn(-1, 0)
        if event.key == pygame.K_d:
          p1.turn(1, 0)
        
        if event.key == pygame.K_UP:
          p2.turn(0, -1)
        if event.key == pygame.K_DOWN:
          p2.turn(0, 1)
        if event.key == pygame.K_LEFT:
          p2.turn(-1, 0)
        if event.key == pygame.K_RIGHT:
          p2.turn(1, 0)
      
  for player in players:
    player.move()
    #printMap()
    
  pygame.display.update()
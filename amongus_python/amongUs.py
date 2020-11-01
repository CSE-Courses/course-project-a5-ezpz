import pygame
from client import Client

#########################################################################################################################################
class Lobby():

    def __init__(self, w, h, name="None"):
        self.screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption(name)
        self.width = w
        self.height = h

    def getLobby(self):
        return self.screen

    def drawLobbyBackground(self):
        #Place background image for lobby
        self.bg_img = pygame.image.load('Images/stars.jpg')
        self.screen.blit(self.bg_img, self.bg_img.get_rect())
        #myfont = pygame.font.SysFont("monspace", 20)
        #self.screen.blit(self.button, self.button.get_rect())

class Button():
    def __init__(self, w, h, x, y, Lobby):
        self.width = w
        self.height = h
        self.posx = x
        self.posy = y
        self.screen = pygame.display.set_mode((w, h))
        self.Lobby = Lobby

    def draw(self):
        #rect = pygame.draw.rect(self.screen, (0,200,0), (150, 550, 100, 50))
        #self.screen.blit(rect, (self.posx, self.posy))
        pygame.draw.rect(self.Lobby.getLobby(), (0, 200, 0), (150, 500, 100, 50))



    ########################################################################################################################################
class Player():

    def __init__(self, startx, starty, w , h, color):
        self.x = startx
        self.y = starty
        self.rate = 2
        self.height = h #48pixels
        self.width = w #36pixels
        self.screen = pygame.display.set_mode((w, h))
        self.color = color #color is not a string it is a pygame.Surface type containing the .png file that will produce character

    #directKey parameter will be used to move player instance in certain direction
    def move(self, directKey):
        if directKey == 0:#right
            self.x = self.x + self.rate
        elif directKey == 1:#left
            self.x = self.x - self.rate
        elif directKey == 2:#up
            self.y = self.y - self.rate
        else:#down
            self.y = self.y + self.rate

    def draw(self, player):
        player = pygame.image.load(self.color).convert()
        self.screen.blit(player, (self.x,self.y) )# params converted image, starting positions of characters




########################################################################################################################################
class Enemy():

    def __init__(self, startx, starty, w, h, end, color):
        self.x = startx
        self.y = starty
        self.height = h  # 48pixels
        self.width = w  # 36pixels
        self.end = end
        self.path = [self.x, self.end] #represents where we are starting and where we are ending
        self.walkCount = 0
        self.rate = 2
        self.screen = pygame.display.set_mode((w, h))
        self.color = color  # color is not a string it is a pygame.Surface type containing the .png file that will produce character

    def moveX(self):
        if self.rate > 0:
            if self.x + self.rate < self.path[1]:
                self.x = self.x + self.rate
            else:
                self.rate = self.rate * -1
                self.walkCount = 0
        else:
            if self.x - self.rate > self.path[0]:
                self.x = self.x + self.rate
            else:
                self.rate = self.rate * -1
                self.walkCount = 0


    def draw(self, g):
        self.moveX()
        player = pygame.image.load(self.color).convert()
        self.screen.blit(player, (self.x, self.y))  # params converted image, starting positions of characters












class Game():
    clock = pygame.time.Clock()  # create an object to help track time

    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.network = Client()
        self.player1 = Player(40, 40, 36, 48, 'Images/cyan.png') #Initializing Player class instance at set point(40,40) in map
        self.player2 = Player(300, 300, 36, 48, 'Images/orange.png') #Initializing Player class instance at set point(300,300) in map
        self.enemy = Enemy(100, 100, 36, 48, 475, 'Images/blue.png')  # Initializing Player class instance at set point(100,100)
        self.lobby = Lobby(self.width, self.height, "Version 1.0") #Creating Lobby class instance
        #self.button = Button(100, 100, 50, 50, self.lobby)


    # will get info from server in a form we can understand so we can then draw the other character
    @staticmethod
    def parseData(data):
        try:
            arr = data.split(":")[1].split(",")
            return int(arr[0]), int(arr[1])
        except:
            return -1, -1

    # this is what will send ur current position in certain form to the server
    def sendData(self):
        data = str(self.network.id) + ":" + str(self.player1.x) + "," + str(self.player1.y)
        reply = self.network.sendData(data)
        return reply


    def run(self):
        running = True
        while running:
            self.clock.tick(60) #once per frame, the program will never running at more than 60 fps.
            # Properly quit (pygame will crash without this)
            for event in pygame.event.get():
                # If key pressed is ESC key, quit program
                if event.type == pygame.K_ESCAPE:
                    running = False
                # If closed out, quit program
                if event.type == pygame.QUIT:
                    running = False

            #making character move
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                if self.player1.x <= self.width - self.player1.rate:
                    self.player1.move(0)
            if keys[pygame.K_LEFT]:
                if self.player1.x >= self.player1.rate:
                    self.player1.move(1)
            if keys[pygame.K_UP]:
                if self.player1.y >= self.player1.rate:
                    self.player1.move(2)
            if keys[pygame.K_DOWN]:
                if self.player1.y <= self.height - self.player1.rate:
                    self.player1.move(3)

            # Send Network data
            self.player2.x, self.player2.y = self.parseData(self.sendData())
            #self.player3.x, self.player3.y = self.parse_data(self.send_data())

            # Update Lobby
            self.lobby.drawLobbyBackground()
            self.player1.draw(self.lobby.getLobby())
            self.player2.draw(self.lobby.getLobby())
            self.enemy.draw(self.lobby.getLobby())
            #self.button.draw()
            pygame.init()
            font = pygame.font.Font(None, 30)
            scoretext = font.render("Press 'Enter' when all players have joined.", 1, (255, 255, 255))
            self.lobby.getLobby().blit(scoretext, (150, 457))
            pygame.display.update()

        pygame.quit()




########################################################################################################################################
from tkinter import *
import random
import time

master = Tk()
master.title("SORRY!!")

board = Canvas(master, width=700, height = 700)
board.pack()

#board.create_line(30,30,30,670, fill = "black")

#top left to top right
for x in range (30,670,40):
    board.create_line(x,30,x,70, fill="black")
    board.create_line(x,70,x+40,70, fill = "black")
    board.create_line(x+40,70,x+40,30, fill = "black")
    board.create_line(x+40, 30, x, 30, fill = "black")

#top left to bottom left
for x in range (30,670,40):
    board.create_line(30,x,70,x, fill="black")
    board.create_line(70,x,70,x+40, fill = "black")
    board.create_line(70,x+40,30,x+40, fill = "black")
    board.create_line(30,x+40, 30,x, fill = "black")

#bottom left to bottom right
for x in range (30,670,40):
    board.create_line(x,630,x,670, fill="black")
    board.create_line(x,670,x+40,670, fill = "black")
    board.create_line(x+40,670,x+40,630, fill = "black")
    board.create_line(x+40, 630, x, 630, fill = "black")

#top right to bottom right
for x in range (30,670,40):
    board.create_line(630,x,670,x, fill="black")
    board.create_line(670,x,670,x+40, fill = "black")
    board.create_line(670,x+40,630,x+40, fill = "black")
    board.create_line(630,x+40, 630,x, fill = "black")

board.create_rectangle(110,70,150,270, fill = "lemonchiffon") #these four create the safe zones
board.create_rectangle(430,110,630,150, fill = "lightgreen")
board.create_rectangle(550,430,590,630, fill = "lightcoral")
board.create_rectangle(70,550,270,590, fill = "skyblue")

#space lines for the safe zones:
#yellow
for x in range (70,230,40):
    board.create_line(110,x,150,x, fill="black")
    board.create_line(110,x,110,x+40, fill = "black")
    board.create_line(150,x+40,110,x+40, fill = "black")
    board.create_line(110,x+40, 110,x, fill = "black")

#green
for x in range (430,630,40):
    board.create_line(x,110,x,150, fill="black")
    board.create_line(x,150,x+40,150, fill = "black")
    board.create_line(x+40,150,x+40,110, fill = "black")
    board.create_line(x+40, 110, x, 110, fill = "black")

#red
for x in range (430,630,40):
    board.create_line(550,x,590,x, fill="black")
    board.create_line(590,x,590,x+40, fill = "black")
    board.create_line(590,x+40,550,x+40, fill = "black")
    board.create_line(550,x+40, 550,x, fill = "black")

#blue
for x in range (30,270,40):
    board.create_line(x,550,x,590, fill="black")
    board.create_line(x,590,x+40,590, fill = "black")
    board.create_line(x+40,590,x+40,550, fill = "black")
    board.create_line(x+40, 550, x, 550, fill = "black")


#making circles
board.create_oval(80,270,180,370, fill = "lemonchiffon")
board.create_oval(520, 330,620,430, fill = "lightcoral")
board.create_oval(330,80,430,180,fill = "lightgreen")
board.create_oval(270,520,370,620, fill = "skyblue")

board.create_oval(440,530,540,630, fill = "lightcoral")
board.create_oval(70,440,170,540,fill = "skyblue")
board.create_oval(160,70,260,170, fill = "lemonchiffon")
board.create_oval(530,160,630,260, fill = "lightgreen")


#8 rectangles
board.create_rectangle(647,95,653,210, fill="lightgreen")
board.create_rectangle(647,415,653,570, fill="lightgreen")
board.create_rectangle(605,647,490,653, fill = "lightcoral")
board.create_rectangle(285,647,130,653, fill = "lightcoral")
board.create_rectangle(53,605,47,490, fill="skyblue")
board.create_rectangle(53,285,47,130,fill="skyblue")
board.create_rectangle(95,53,210,47,fill="lemonchiffon")
board.create_rectangle(415,53,570,47, fill="lemonchiffon")

#8 triangles
board.create_polygon(35,620,65,620,50,595, fill="skyblue",outline="black")
board.create_polygon(35,300,65,300,50,275, fill="skyblue", outline="black")
board.create_polygon(275,650,300,635,300,665, fill="lightcoral", outline = "black")
board.create_polygon(595,650,620,635,620,665, fill="lightcoral", outline = "black")
board.create_polygon(80,35,80,65,105,50, fill="lemonchiffon",outline="black")
board.create_polygon(400,35,400,65,425,50, fill = "lemonchiffon", outline = "black")
board.create_polygon(635,80,665,80,650,105, fill = "lightgreen", outline="black")
board.create_polygon(635,400,665,400,650,425, fill = "lightgreen", outline = "black")

#8 circles
board.create_oval(35,475,65,505, fill = "skyblue")
board.create_oval(35,115,65,145, fill = "skyblue")
board.create_oval(195,35,225,65, fill = "lemonchiffon")
board.create_oval(555,35,585,65, fill = "lemonchiffon")
board.create_oval(635,195,665,225, fill = "lightgreen")
board.create_oval(635,555,665,585, fill = "lightgreen")
board.create_oval(475,635,505,665, fill = "lightcoral")
board.create_oval(115,635,145,665, fill = "lightcoral") 

#SORRY!!
board.create_text(350,350,font = ("Purisa", 60), text="SORRY!")
txt = board.create_text(350, 450, font = ("Purisa",45), text = "No cards yet")









def convert_coordinates(x,y,color):
    #0-66 depending on color

    #safe zones
    if y == 2 and x > 0 and x < 7:
        return x + 60
    if x == 13 and y > 0 and y < 7:
        return y + 60
    if x == 2 and y < 15 and y > 8:
        return 75 - y
    if y == 13 and x > 8 and x < 15:
        return 75-x
    answer = 0
    if color == "red":
        if y == 0 and x < 13:
            answer = 12-x
        if y == 0 and x >12:
            answer = 73-x
        if x == 0:
            answer = 13 + y
        if y == 15:
            answer = 28 + x
        if x == 15:
            answer = 58 - y

    if color == "blue":
        if x == 0 and y > 2:
            answer = y - 2
        if x == 0 and y < 3:
            answer = 58 + y
        if y == 15:
            answer = 13 + x
        if x == 15:
            answer = 43 - y
        if y == 0:
            answer = 58 - x
    if color == "yellow":
        if y == 15 and x > 2:
            answer = x - 2
        if y == 15 and x < 3:
            answer = x + 58
        if x == 15:
            answer = 28 - y
        if y == 0:
            answer = 43 - x
        if x == 0:
            answer = 43 + y

    if color == "green":
        if x == 15 and y < 13:
            answer = 13 - y
        if x == 15 and y > 12:
            answer = 73 - y
        if y == 0:
            answer = 28 - x
        if x == 0:
            answer = 28 + y
        if y == 15:
            answer = 43 + x






        
    return answer


class Deck():
    all_cards = []
    remaining_cards = []

    def __init__(self):
        for i in range(5):
            self.all_cards.append("1")
        for i in range(4):
            self.all_cards.append("0")
            self.all_cards.append("2")
            self.all_cards.append("3")
            self.all_cards.append("4")
            self.all_cards.append("5")
            self.all_cards.append("8")
            self.all_cards.append("10")
            self.all_cards.append("11")
            self.all_cards.append("12")
        self.shuffle()

    def shuffle(self):
        self.remaining_cards = []
        for card in self.all_cards:
            self.remaining_cards.append(card)
        for i in range(10):
            num1 = random.randint(0, len(self.all_cards)-1)
            num2 = random.randint(0, len(self.all_cards)-1)
            if num1 != num2:
                temp = self.remaining_cards[num1]
                self.remaining_cards[num1] = self.remaining_cards[num2]
                self.remaining_cards[num2] = temp

    def deal_card(self):
        next_card = self.remaining_cards.pop()
        if next_card != '0':
            board.itemconfigure(txt, text=next_card)
        else:
            board.itemconfigure(txt, text="SORRY")
        board.update()
        if len(self.remaining_cards) == 0:
            print("Cards Shuffled...")
            self.shuffle()
        return next_card

graphics = []
pawns = []
class Pawn():
    color = ""
    x=0
    y=0
    start_x = 0
    start_y = 0
    roaming = 0
    graphic_index = 0
    pawn_index = 0
    home = 0

    def __init__(self, startx, starty, color):
        self.home = 0 #pawn isn't all the way to home
        self.roaming = 0
        self.graphic_index = len(graphics)
        self.pawn_index = len(pawns)
        pawns.append(self)
        graphics.append(board.create_oval(400,300,440,340, fill = color))
        
        self.color = color
        self.start_x = startx
        self.start_y = starty
        self.x = startx
        self.y = starty

        left_x = 40*self.x + 30
        right_x = left_x + 40
        bottom_y = 670 - 40 * self.y
        top_y = bottom_y - 40

        board.coords(graphics[self.graphic_index], left_x, top_y, right_x, bottom_y)

    def switch_places(self, pawn2):
        temp_x = self.x
        temp_y = self.y
        self.x = pawn2.x
        self.y = pawn2.y
        pawn2.x = temp_x
        pawn2.y = temp_y
        
        left_x = 40*self.x + 30
        right_x = left_x + 40
        bottom_y = 670 - 40 * self.y
        top_y = bottom_y - 40
        
        board.coords(graphics[self.graphic_index], left_x, top_y, right_x, bottom_y)

        left_x = 40*pawn2.x + 30
        right_x = left_x + 40
        bottom_y = 670 - 40 * pawn2.y
        top_y = bottom_y - 40

        board.coords(graphics[pawn2.graphic_index], left_x, top_y, right_x, bottom_y)
        


    def move_from_start(self):

        if self.color == "red":
            self.x = 11
            self.y = 0
        if self.color == "green":
            self.x = 15
            self.y = 11
        if self.color == "blue":
            self.x = 0
            self.y = 4
        if self.color == "yellow":
            self.x = 4
            self.y = 15
        
        left_x = 40*self.x + 30
        right_x = left_x + 40
        bottom_y = 670 - 40 * self.y
        top_y = bottom_y - 40

        board.coords(graphics[self.graphic_index], left_x, top_y, right_x, bottom_y)
        self.roaming = 1

        self.capture_others(self.x, self.x, self.y, self.y)
    
    #takes either a positive or negative number
    def move(self, num):
        if num > -1:
            for i in range(num):
                time.sleep(0.25)
                self.move_one_space()
        else:
            for i in range(num*(-1)):
                time.sleep(0.25)
                self.move_backwards_one_space()

        if self.y == 0:
            if self.x == 6:
                self.slide(-4,0)
                self.capture_others(2,6,0,0)
            if self.x == 14 and self.color != "red":
                self.slide(-3, 0)
                self.capture_others(11,14,0,0)

        if self.y == 15:
            if self.x == 1 and self.color != "yellow":
                self.slide(3,0)
                self.capture_others(1,4,15,15)
            if self.x == 9:
                self.slide(4,0)
                self.capture_others(9,13,15,15)
                
        if self.x == 0:
            if self.y == 1 and self.color != "blue":
                self.slide(0,3)
                self.capture_others(0,0,1,4)
            if self.y == 9:
                self.slide(0,4)
                self.capture_others(0,0,9,13)

        if self.x == 15:
            if self.y == 14 and self.color != "green":
                self.slide(0, -3)
                self.capture_others(15,15, 11,14)
            if self.y == 6:
                self.slide(0, -4)
                self.capture_others(15,15, 2,6)

        if convert_coordinates(self.x, self.y, self.color) != 66:           
            self.capture_others(self.x, self.x, self.y, self.y)

    def capture_others(self, high_x, low_x, high_y, low_y):
        for pawn in pawns:
            if pawn.graphic_index != self.graphic_index: #if it isn't this pawn
                
                if pawn.x <= high_x and pawn.x >= low_x and pawn.y <= high_y and pawn.y >= low_y:
                    pawn.capture()

    def slide(self, dx, dy):

        self.x = self.x + dx
        self.y = self.y + dy
        
        dx = dx*40
        dy = dy*40

        if abs(dx) == 120 or abs(dy) == 120:
            dx = (dx/12)
            dy = (dy/12)
            for i in range(12):
                time.sleep(0.05)
                board.move(graphics[self.graphic_index], dx, dy*(-1))
                board.update()

        if abs(dx) == 160 or abs(dy) == 160:
            dx = (dx/16)
            dy = (dy/16)
            for i in range(16):
                time.sleep(0.05)
                board.move(graphics[self.graphic_index], dx, dy*(-1))
                board.update()
    
    
    def capture(self):
        self.x = self.start_x
        self.y = self.start_y
        self.roaming = 0
        
        left_x = 40*self.start_x + 30
        right_x = left_x + 40
        bottom_y = 670 - 40 * self.start_y
        top_y = bottom_y - 40

        board.coords(graphics[self.graphic_index], left_x, top_y, right_x, bottom_y)

    def move_one_space(self):
        #if going into safety zone or home
        if self.color == "green" and self.x > 9 and self.y == 13:
            self.x = self.x -1
            board.move(graphics[self.graphic_index], -40,0)
            if self.x == 9:
                self.home = 1
        elif self.color == "red" and self.x == 13 and self.y < 6:
            self.y = self.y + 1
            board.move(graphics[self.graphic_index], 0, -40)
            if self.y == 6:
                self.home = 1
        elif self.color == "blue" and self.x < 6 and self.y == 2:
            self.x = self.x + 1
            board.move(graphics[self.graphic_index], 40, 0)
            if self.x == 6:
                self.home = 1
        elif self.color == "yellow" and self.x == 2 and self.y > 9:
            self.y = self.y - 1
            board.move(graphics[self.graphic_index], 0, 40)
            if self.y == 9:
                self.home = 1
        else: #other location on board
            if self.x == 0 and self.y < 15:
                self.y = self.y + 1
                board.move(graphics[self.graphic_index], 0, -40)
            elif self.y == 15 and self.x < 15:
                self.x = self.x + 1
                board.move(graphics[self.graphic_index], 40,0)
            elif self.x == 15 and self.y > 0:
                self.y = self.y - 1
                board.move(graphics[self.graphic_index], 0, 40)
            elif self.y == 0 and self.x > 0:
                self.x = self.x - 1
                board.move(graphics[self.graphic_index], -40, 0)

        board.update()
        
    
    def check_availability(self, num):
        coord1 = convert_coordinates(self.x, self.y, self.color)
        if coord1 + num > 66:
            return False
        if coord1 + num == 66:
            return True
        for pawn in pawns:
            coord2 = convert_coordinates(pawn.x, pawn.y, pawn.color)
            if coord1 + num == coord2 and pawn.color == self.color:
                return False
        return True
        

    def move_backwards_one_space(self):
        #if inside safety zone or home
        if self.color == "green" and self.x > 9 and self.y == 13 and self.x < 15:
            self.x = self.x + 1
            board.move(graphics[self.graphic_index], 40,0)
        elif self.color == "red" and self.x == 13 and self.y < 6 and self.y > 0:
            self.y = self.y - 1
            board.move(graphics[self.graphic_index], 0, 40)
        elif self.color == "blue" and self.x < 6 and self.y == 2 and self.x > 0:
            self.x = self.x - 1
            board.move(graphics[self.graphic_index], -40, 0)
        elif self.color == "yellow" and self.x == 2 and self.y > 9 and self.y < 15:
            self.y = self.y + 1
            board.move(graphics[self.graphic_index], 0, -40)
        else: #other location on board
            if self.x == 0 and self.y > 0:
                self.y = self.y - 1
                board.move(graphics[self.graphic_index], 0,40)
            elif self.y == 15 and self.x > 0:
                self.x = self.x - 1
                board.move(graphics[self.graphic_index], -40, 0)
            elif self.x == 15 and self.y < 15:
                self.y = self.y + 1
                board.move(graphics[self.graphic_index], 0, -40)
            elif self.y == 0 and self.x < 15:
                self.x = self.x + 1
                board.move(graphics[self.graphic_index], 40, 0)

        board.update()
        

         

class Player():
    color = ""
    pawn1 = ""
    pawn2 = ""
    pawn3 = ""
    pawn4 = ""
    current_turn = False
    name = ""
    home_x = 0
    home_y = 0

    player_number = 0

    def __init__(self, color, name, player_number):
        self.player_number = player_number
        self.name = name
        self.color = color

        #startx, starty, color
        if color == "red":
            self.pawn1 = Pawn(11,1,"red")
            self.pawn2 = Pawn(10.5,1.5,"red")
            self.pawn3 = Pawn(11,2,"red")
            self.pawn4 = Pawn(11.5,1.5,"red")
            self.home_x = 13
            self.home_y = 6
        elif color == "green":
            self.pawn1 = Pawn(14,11,"green")
            self.pawn2 = Pawn(13.5, 10.5, "green")
            self.pawn3 = Pawn(13,11,"green")
            self.pawn4 = Pawn(13.5, 11.5, "green")
            self.home_x = 9
            self.home_y = 13
        elif color == "yellow":
            self.pawn1 = Pawn(4,14,"yellow")
            self.pawn2 = Pawn(4.5, 13.5, "yellow")
            self.pawn3 = Pawn(4,13,"yellow")
            self.pawn4 = Pawn(3.5, 13.5, "yellow")
            self.home_x = 2
            self.home_y = 9
        elif color == "blue":
            self.pawn1 = Pawn(1,4,"blue")
            self.pawn2 = Pawn(1.5,4.5,"blue")
            self.pawn3 = Pawn(2, 4, "blue")
            self.pawn4 = Pawn(1.5,3.5,"blue")
            self.home_x = 6
            self.home_y = 2

    def check_if_winner(self):
        if self.pawn1.x != self.home_x or self.pawn1.y != self.home_y:
            return False
        if self.pawn2.x != self.home_x or self.pawn2.y != self.home_y:
            return False
        if self.pawn3.x != self.home_x or self.pawn3.y != self.home_y:
            return False
        if self.pawn4.x != self.home_x or self.pawn4.y != self.home_y:
            return False
        return True





class Option():
    pawn = 0
    num = 0
    pawn2 = 0
    enter_game = False
    sorry = False
    def __init__(self, pawn, num, pawn2, enter_game, sorry):
        self.sorry = sorry
        self.pawn = pawn
        self.num = num
        self.pawn2 = pawn2 #if 11, player can switch with another player
        self.enter_game = enter_game


    def execute(self):
        if self.enter_game == True:
            self.pawn.move_from_start()

        elif self.pawn2 != 0 and self.sorry == True:
            new_x = self.pawn2.x
            new_y = self.pawn2.y
            
            left_x = 40*self.pawn2.x + 30
            right_x = left_x + 40
            bottom_y = 670 - 40 * self.pawn2.y
            top_y = bottom_y - 40

            self.pawn.capture_others(self.pawn2.x, self.pawn2.x, self.pawn2.y, self.pawn2.y)
            
            board.coords(graphics[self.pawn.graphic_index], left_x, top_y, right_x, bottom_y)
            self.pawn.x = new_x
            self.pawn.y = new_y

            self.pawn.roaming = 1
            
        #switch pawns with another pawn
        elif self.pawn2 != 0:
            self.pawn.switch_places(self.pawn2)
        
        else:
            self.pawn.move(self.num)

    def list_option(self, i):
        print(" ")
        print("Option " + str(i) + ":")
        if self.sorry == True:
            print("Commit Sorry on " + self.pawn2.color + " at the coordinates " + str(self.pawn2.x) + "," + str(self.pawn2.y))
        elif self.enter_game == True:
            print("Move a pawn from START into the game.")
        elif self.pawn2 == 0:
            print("Move pawn at location " + str(self.pawn.x) + "," + str(self.pawn.y) + " " + str(self.num) + " spaces.")
        else:
            print("Switch your pawn at " + str(self.pawn.x) + "," + str(self.pawn.y) + " with the " + self.pawn2.color + " pawn at " + str(self.pawn2.x) + "," + str(self.pawn2.y))
            



#BEGIN GAMEPLAY
while True:
    num_players = int(input("Number of players? (2-4)"))
    if num_players == 2 or num_players == 3 or num_players == 4:
        break
    else:
        print("You can only have between 2 and 4 players")

players = []
for i in range(num_players):
    name = input("Player " + str(len(players)+1) + ", please input your name")
    for player in players:
        if player.name == name:
            print("Wow, this will be confusing!")

    while True:
        color = input("Please choose a color from red, blue, green, or yellow")
        same = False
        for player in players:
            if player.color == color:
                same = True
        if same == True:
            print("You can't choose the same color as another player!")
        else:
            players.append(Player(color, name, i))
            break




def not_outside_start(color, player):
    home_x = 0
    home_y = 0
    if color == "blue":
        home_x = 0
        home_y = 4
    elif color == "yellow":
        home_x = 4
        home_y = 15
    elif color == "green":
        home_x = 15
        home_y = 11
    elif color == "red":
        home_x = 11
        home_y = 0
    
    if player.pawn1.x == home_x and player.pawn1.y == home_y:
        return 0
    if player.pawn2.x == home_x and player.pawn2.y == home_y:
        return 0
    if player.pawn3.x == home_x and player.pawn3.y == home_y:
        return 0
    if player.pawn4.x == home_x and player.pawn4.y == home_y:
        return 0
    return 1
    
        

current_player = 0
players[0].current_turn = True


deck = Deck()
deck.shuffle()

card_dealt = 0
while True:
    # player does their turn
    p = players[current_player]
    options = []

    repeat = 1

    while repeat == 1:
        options = []
        for i in range(5):
            print(" ")
        print("It's " + p.name + "'s turn!!")
        time.sleep(0.5)
        card_dealt = deck.deal_card()

        #print("If there is a pawn right outside START, print False : " + str(not_outside_start(p.color, player)))

        #Options are 1,2,3,4,5,8,10,11,12,0(Sorry)
        if card_dealt == '3' or card_dealt == '5' or card_dealt == '8' or card_dealt == '10' or card_dealt == '12' or card_dealt == '11':
            if p.pawn1.roaming == 1:
                if p.pawn1.check_availability(int(card_dealt)) == True:
                    options.append(Option(p.pawn1, int(card_dealt), 0, False,False))
            if p.pawn2.roaming == 1:
                if p.pawn2.check_availability(int(card_dealt)) == True:
                    options.append(Option(p.pawn2, int(card_dealt), 0, False,False))
            if p.pawn3.roaming == 1:
                if p.pawn3.check_availability(int(card_dealt)) == True:
                    options.append(Option(p.pawn3, int(card_dealt), 0, False,False))
            if p.pawn4.roaming == 1:
                if p.pawn4.check_availability(int(card_dealt)) == True:
                    options.append(Option(p.pawn4, int(card_dealt), 0, False,False))

        if card_dealt == '1' or card_dealt == '2':
            if p.pawn1.roaming == 1:
                if p.pawn1.check_availability(int(card_dealt)) == True:
                    options.append(Option(p.pawn1, int(card_dealt), 0, False,False))
            if p.pawn2.roaming == 1:
                if p.pawn2.check_availability(int(card_dealt)) == True:
                    options.append(Option(p.pawn2, int(card_dealt), 0, False,False))
            if p.pawn3.roaming == 1:
                if p.pawn3.check_availability(int(card_dealt)) == True:
                    options.append(Option(p.pawn3, int(card_dealt), 0, False,False))
            if p.pawn4.roaming == 1:
                if p.pawn4.check_availability(int(card_dealt)) == True:
                    options.append(Option(p.pawn4, int(card_dealt), 0, False,False))
            if not_outside_start(p.color, player) == 1:
                if p.pawn1.roaming == 0:
                    options.append(Option(p.pawn1, '1', 0, True, False))
                elif p.pawn2.roaming == 0:
                    options.append(Option(p.pawn2, '1', 0, True, False))
                elif p.pawn3.roaming == 0:
                    options.append(Option(p.pawn3, '1', 0, True, False))
                elif p.pawn4.roaming == 0:
                    options.append(Option(p.pawn4, '1', 0, True, False))
        if card_dealt == '4' or card_dealt == '10':
            if card_dealt == '10':
                card_dealt = '1'
            if p.pawn1.roaming == 1 and p.pawn1.home == 0:
                if p.pawn1.check_availability(int(card_dealt)*(-1)) == True:
                    options.append(Option(p.pawn1, int(card_dealt)*(-1), 0, False,False))
            if p.pawn2.roaming == 1 and p.pawn2.home == 0:
                if p.pawn2.check_availability(int(card_dealt)*(-1)) == True:
                    options.append(Option(p.pawn2, int(card_dealt)*(-1), 0, False,False))
            if p.pawn3.roaming == 1 and p.pawn3.home == 0:
                if p.pawn3.check_availability(int(card_dealt)*(-1)) == True:
                    options.append(Option(p.pawn3, int(card_dealt)*(-1), 0, False,False))
            if p.pawn4.roaming == 1 and p.pawn4.home == 0:
                if p.pawn4.check_availability(int(card_dealt)*(-1)) == True:
                    options.append(Option(p.pawn4, int(card_dealt)*(-1), 0, False,False))

        if card_dealt == '0':
            if p.pawn1.roaming == 0:
                for player in players:
                    if player.color != p.color:
                        if player.pawn1.roaming == 1 and convert_coordinates(player.pawn1.x, player.pawn1.y, player.color) < 61:
                            options.append(Option(p.pawn1, 0, player.pawn1, False, True))
                        if player.pawn2.roaming == 1 and convert_coordinates(player.pawn2.x, player.pawn2.y, player.color) < 61:
                            options.append(Option(p.pawn1, 0, player.pawn2, False, True))
                        if player.pawn3.roaming == 1 and convert_coordinates(player.pawn3.x, player.pawn3.y, player.color) < 61:
                            options.append(Option(p.pawn1, 0, player.pawn3, False, True))
                        if player.pawn4.roaming == 1 and convert_coordinates(player.pawn4.x, player.pawn4.y, player.color) < 61:
                            options.append(Option(p.pawn1, 0, player.pawn4, False, True))
            elif p.pawn2.roaming == False:
                for player in players:
                    if player.color != p.color:
                        if player.pawn1.roaming == 1 and convert_coordinates(player.pawn1.x, player.pawn1.y, player.color) < 61:
                            options.append(Option(p.pawn2, 0, player.pawn1, False, True))
                        if player.pawn2.roaming == 1 and convert_coordinates(player.pawn2.x, player.pawn2.y, player.color) < 61:
                            options.append(Option(p.pawn2, 0, player.pawn2, False, True))
                        if player.pawn3.roaming == 1 and convert_coordinates(player.pawn3.x, player.pawn3.y, player.color) < 61:
                            options.append(Option(p.pawn2, 0, player.pawn3, False, True))
                        if player.pawn4.roaming == 1 and convert_coordinates(player.pawn4.x, player.pawn4.y, player.color) < 61:
                            options.append(Option(p.pawn2, 0, player.pawn4, False, True))
            elif p.pawn3.roaming == False:
                for player in players:
                    if player.color != p.color:
                        if player.pawn1.roaming == 1 and convert_coordinates(player.pawn1.x, player.pawn1.y, player.color) < 61:
                            options.append(Option(p.pawn3, 0, player.pawn1, False, True))
                        if player.pawn2.roaming == 1 and convert_coordinates(player.pawn2.x, player.pawn2.y, player.color) < 61:
                            options.append(Option(p.pawn3, 0, player.pawn2, False, True))
                        if player.pawn3.roaming == 1 and convert_coordinates(player.pawn3.x, player.pawn3.y, player.color) < 61:
                            options.append(Option(p.pawn3, 0, player.pawn3, False, True))
                        if player.pawn4.roaming == 1 and convert_coordinates(player.pawn4.x, player.pawn4.y, player.color) < 61:
                            options.append(Option(p.pawn3, 0, player.pawn4, False, True))
            elif p.pawn4.roaming == False:
                for player in players:
                    if player.color != p.color:
                        if player.pawn1.roaming == 1 and convert_coordinates(player.pawn1.x, player.pawn1.y, player.color) < 61:
                            options.append(Option(p.pawn4, 0, player.pawn1, False, True))
                        if player.pawn2.roaming == 1 and convert_coordinates(player.pawn2.x, player.pawn2.y, player.color) < 61:
                            options.append(Option(p.pawn4, 0, player.pawn2, False, True))
                        if player.pawn3.roaming == 1 and convert_coordinates(player.pawn3.x, player.pawn3.y, player.color) < 61:
                            options.append(Option(p.pawn4, 0, player.pawn3, False, True))
                        if player.pawn4.roaming == 1 and convert_coordinates(player.pawn4.x, player.pawn4.y, player.color) < 61:
                            options.append(Option(p.pawn4, 0, player.pawn4, False, True))
        

                                              
        if card_dealt == '11':
            if p.pawn1.roaming == True and convert_coordinates(p.pawn1.x, p.pawn1.y, p.color) < 61:
                for player in players:
                    if player.color != p.color:
                        if player.pawn1.roaming == 1 and convert_coordinates(player.pawn1.x, player.pawn1.y, player.color) < 61:
                            options.append(Option(p.pawn1, 0, player.pawn1, False, False))
                        if player.pawn2.roaming == 1 and convert_coordinates(player.pawn2.x, player.pawn2.y, player.color) < 61:
                            options.append(Option(p.pawn1, 0, player.pawn2, False, False))
                        if player.pawn3.roaming == 1 and convert_coordinates(player.pawn3.x, player.pawn3.y, player.color) < 61:
                            options.append(Option(p.pawn1, 0, player.pawn3, False, False))
                        if player.pawn4.roaming == 1 and convert_coordinates(player.pawn4.x, player.pawn4.y, player.color) < 61:
                            options.append(Option(p.pawn1, 0, player.pawn4, False, False))
            if p.pawn2.roaming == True and convert_coordinates(p.pawn2.x, p.pawn2.y, p.color) < 61:
                for player in players:
                    if player.color != p.color:
                        if player.pawn1.roaming == 1 and convert_coordinates(player.pawn1.x, player.pawn1.y, player.color) < 61:
                            options.append(Option(p.pawn2, 0, player.pawn1, False, False))
                        if player.pawn2.roaming == 1 and convert_coordinates(player.pawn2.x, player.pawn2.y, player.color) < 61:
                            options.append(Option(p.pawn2, 0, player.pawn2, False, False))
                        if player.pawn3.roaming == 1 and convert_coordinates(player.pawn3.x, player.pawn3.y, player.color) < 61:
                            options.append(Option(p.pawn2, 0, player.pawn3, False, False))
                        if player.pawn4.roaming == 1 and convert_coordinates(player.pawn4.x, player.pawn4.y, player.color) < 61:
                            options.append(Option(p.pawn2, 0, player.pawn4, False, False))
            if p.pawn3.roaming == True and convert_coordinates(p.pawn3.x, p.pawn3.y, p.color) < 61:
                for player in players:
                    if player.color != p.color:
                        if player.pawn1.roaming == 1 and convert_coordinates(player.pawn1.x, player.pawn1.y, player.color) < 61:
                            options.append(Option(p.pawn3, 0, player.pawn1, False, False))
                        if player.pawn2.roaming == 1 and convert_coordinates(player.pawn2.x, player.pawn2.y, player.color) < 61:
                            options.append(Option(p.pawn3, 0, player.pawn2, False, False))
                        if player.pawn3.roaming == 1 and convert_coordinates(player.pawn3.x, player.pawn3.y, player.color) < 61:
                            options.append(Option(p.pawn3, 0, player.pawn3, False, False))
                        if player.pawn4.roaming == 1 and convert_coordinates(player.pawn4.x, player.pawn4.y, player.color) < 61:
                            options.append(Option(p.pawn3, 0, player.pawn4, False, False))
            if p.pawn4.roaming == True and convert_coordinates(p.pawn4.x, p.pawn4.y, p.color) < 61:
                for player in players:
                    if player.color != p.color:
                        if player.pawn1.roaming == 1 and convert_coordinates(player.pawn1.x, player.pawn1.y, player.color) < 61:
                            options.append(Option(p.pawn4, 0, player.pawn1, False, False))
                        if player.pawn2.roaming == 1 and convert_coordinates(player.pawn2.x, player.pawn2.y, player.color) < 61:
                            options.append(Option(p.pawn4, 0, player.pawn2, False, False))
                        if player.pawn3.roaming == 1 and convert_coordinates(player.pawn3.x, player.pawn3.y, player.color) < 61:
                            options.append(Option(p.pawn4, 0, player.pawn3, False, False))
                        if player.pawn4.roaming == 1 and convert_coordinates(player.pawn4.x, player.pawn4.y, player.color) < 61:
                            options.append(Option(p.pawn4, 0, player.pawn4, False, False))

        chosen = False
        while chosen == False:
            if len(options) == 0:
                print("Sorry, no available moves")
                break
            for i in range(len(options)):
                options[i].list_option(i)
            choice = input("Which option would you like to do?")
            try:
                options[int(choice)].execute()
                chosen = True
            except:
                print("Please input a valid choice")

            
        board.update()

        if card_dealt != '2':
            repeat = 0



    
    #next player
    if players[current_player].check_if_winner():
        print("CONGRATULATIONS " + players[current_player].name + "!!!!!!!!!!!!!!")
        break
    
    players[current_player].current_turn = False
    if current_player == len(players) - 1:
        current_player = 0
    else:
        current_player = current_player + 1
    players[current_player].current_turn = True
    









from tkinter import *
import random

class Square:
    def __init__(self, color, column, row, end):
        self.color=color
        if(end):
            self.color = 'antique white'
        else:
            if(color):
                self.color = 'tan4'
            else:
                self.color = 'tan1'
        self.column = column
        self.row = row
        self.canvas = canvas
        if(row<5):
            self.zone='defendFalse'
        elif(row>=10):
            self.zone='defendTrue'
        else:
            self.zone='attack'
        self.draw()

    def draw(self):
        canvas.create_rectangle(self.column*50, self.row*50, self.column*50+50,
                                self.row*50+50, fill=self.color)

class Piece:
    def __init__(self, player, knife, column, row, zone):
        self.player = player
        if(self.player==True):
            self.color = 'dark blue'
        else:
            self.color = 'dark red'

        self.knife = knife
        self.column = column
        self.row = row
        if(zone == 'defend'):
            self.zone = zone+str(player)
        else:
            self.zone = zone
        self.clicked = False
        
        self.draw()

    def draw(self):
        self.oval = canvas.create_oval(self.column*50, self.row*50, self.column*50+50,
                                self.row*50+50, fill=self.color)
        if(self.knife):
            self.line = canvas.create_line(self.column*50+25, self.row*50,
                               self.column*50+25, self.row*50+50,
                               fill='yellow', width=3)

    def click(self):
        if(self.player):
            if not self.clicked:
                canvas.itemconfig(self.oval, fill='dark green')
            else:
                canvas.itemconfig(self.oval, fill='dark blue')

            self.clicked = not self.clicked
        else:
            if not self.clicked:
                canvas.itemconfig(self.oval, fill='purple')
            else:
                canvas.itemconfig(self.oval, fill='dark red')

            self.clicked = not self.clicked

    def move(self, square):
        canvas.delete(self.oval)
        if(self.knife):
            canvas.delete(self.line)
        self.column = square.column
        self.row = square.row
        self.draw()
        self.clicked = not self.clicked
        is_surrounded = surrounded(self)
        if(is_surrounded):
            self.destroy()
            if(self.knife):
                knife_pieces.remove(self)
            else:
                attack_pieces.remove(self)

    def destroy(self):
        canvas.delete(self.oval)
        if(self.knife):
            canvas.delete(self.line)

    def reset(self):
        if(self.knife):
            canvas.delete(self.oval)
            canvas.delete(self.line)
            if(self.player):
                self.column = 4
                self.row = 14
            else:
                self.column = 4
                self.row = 0
        self.draw()
        self.clicked = False
        
    def str(self):
        if(self.player == True):
            playerName = 'Player'
        else:
            playerName = 'Opponent'
            
        print(playerName + ': ' + str(self.column) +
              ', ' + str(self.row) + ', ' + self.zone)

def choose_formation(root):
    
    formations = ['2 attack, 5 defend',
        '3 attack, 4 defend',
        '4 attack, 3 defend',
        '5 attack, 2 defend',
        '6 attack, 1 defend',
        '7 attack, 0 defend']
    stringVar = StringVar(root)
    stringVar.set('Player 1, choose your formation')

    global player_dropdown
    player_dropdown = OptionMenu(root, stringVar, *formations,
                          command = destroy_dropdown_player)
    player_dropdown.config(width=40, font=('Helvetica', 12))
    player_dropdown.pack()

    stringVar = StringVar(root)
    stringVar.set('Player 2, choose your formations')

    global opponent_dropdown
    opponent_dropdown = OptionMenu(root, stringVar, *formations,
                          command = destroy_dropdown_opponent)
    opponent_dropdown.config(width=40, font=('Helvetica', 12))
    opponent_dropdown.pack()

def destroy_dropdown_player(formation):
    player_dropdown.destroy()
    draw_pieces(formation,True)

def destroy_dropdown_opponent(formation):
    opponent_dropdown.destroy()
    draw_pieces(formation,False)

def draw_pieces(formation,player):
    if(player):
        y_attack=8
        y_defend=11
        y_knife=14
    else:
        y_attack=6
        y_defend=3
        y_knife=0
    if(formation=='2 attack, 5 defend'):
        attack_pieces.append(Piece(player,False,1,y_attack,'attack'))
        attack_pieces.append(Piece(player,False,7,y_attack,'attack'))
        defend_pieces.append(Piece(player,False,0,y_defend,'defend'))
        defend_pieces.append(Piece(player,False,2,y_defend,'defend'))
        defend_pieces.append(Piece(player,False,4,y_defend,'defend'))
        defend_pieces.append(Piece(player,False,6,y_defend,'defend'))
        defend_pieces.append(Piece(player,False,8,y_defend,'defend'))
        knife_pieces.append(Piece(player,True,4,y_knife,'knife'))
    elif(formation=='3 attack, 4 defend'):
        attack_pieces.append(Piece(player,False,0,y_attack,'attack'))
        attack_pieces.append(Piece(player,False,4,y_attack,'attack'))
        attack_pieces.append(Piece(player,False,8,y_attack,'attack'))
        defend_pieces.append(Piece(player,False,1,y_defend,'defend'))
        defend_pieces.append(Piece(player,False,3,y_defend,'defend'))
        defend_pieces.append(Piece(player,False,5,y_defend,'defend'))
        defend_pieces.append(Piece(player,False,7,y_defend,'defend'))
        knife_pieces.append(Piece(player,True,4,y_knife,'knife'))
    elif(formation=='4 attack, 3 defend'):
        attack_pieces.append(Piece(player,False,1,y_attack,'attack'))
        attack_pieces.append(Piece(player,False,3,y_attack,'attack'))
        attack_pieces.append(Piece(player,False,5,y_attack,'attack'))
        attack_pieces.append(Piece(player,False,7,y_attack,'attack'))
        defend_pieces.append(Piece(player,False,0,y_defend,'defend'))
        defend_pieces.append(Piece(player,False,4,y_defend,'defend'))
        defend_pieces.append(Piece(player,False,8,y_defend,'defend'))
        knife_pieces.append(Piece(player,True,4,y_knife,'knife'))
    elif(formation=='5 attack, 2 defend'):
        attack_pieces.append(Piece(player,False,0,y_attack,'attack'))
        attack_pieces.append(Piece(player,False,2,y_attack,'attack'))
        attack_pieces.append(Piece(player,False,4,y_attack,'attack'))
        attack_pieces.append(Piece(player,False,6,y_attack,'attack'))
        attack_pieces.append(Piece(player,False,8,y_attack,'attack'))
        defend_pieces.append(Piece(player,False,1,y_defend,'defend'))
        defend_pieces.append(Piece(player,False,7,y_defend,'defend'))
        knife_pieces.append(Piece(player,True,4,y_knife,'knife'))
    elif(formation=='6 attack, 1 defend'):
        attack_pieces.append(Piece(player,False,0,y_attack,'attack'))
        attack_pieces.append(Piece(player,False,1,y_attack,'attack'))
        attack_pieces.append(Piece(player,False,3,y_attack,'attack'))
        attack_pieces.append(Piece(player,False,5,y_attack,'attack'))
        attack_pieces.append(Piece(player,False,7,y_attack,'attack'))
        attack_pieces.append(Piece(player,False,8,y_attack,'attack'))
        defend_pieces.append(Piece(player,False,4,y_defend,'defend'))
        knife_pieces.append(Piece(player,True,4,y_knife,'knife'))
    elif(formation=='7 attack, 0 defend'):
        attack_pieces.append(Piece(player,False,0,y_attack,'attack'))
        attack_pieces.append(Piece(player,False,1,y_attack,'attack'))
        attack_pieces.append(Piece(player,False,3,y_attack,'attack'))
        attack_pieces.append(Piece(player,False,4,y_attack,'attack'))
        attack_pieces.append(Piece(player,False,5,y_attack,'attack'))
        attack_pieces.append(Piece(player,False,7,y_attack,'attack'))
        attack_pieces.append(Piece(player,False,8,y_attack,'attack'))
        knife_pieces.append(Piece(player,True,4,y_knife,'knife'))

def blocker(piece, piece2, square):
    #horizontal
    if(piece2.row == piece.row and piece.row == square.row):
        #moving right
        if(square.column > piece.column):
            #piece2 is in the same direction
            if(piece2.column > piece.column):
                #if the piece2 is closer
                if(piece2.column - piece.column <
                   square.column - piece.column):
                    return True
        #moving left
        if(square.column < piece.column):
            #piece2 is in the same direction
            if(piece2.column < piece.column):
                #if the piece2 is closer
                if(abs(piece2.column - piece.column) <
                   abs(square.column - piece.column)):
                    return True
    #verticle
    if(piece2.column == piece.column and piece.column == square.column):
        #moving down
        if(square.row > piece.row):
            #piece2 is in the same direction
            if(piece2.row > piece.row):
                #if the piece2 is closer
                if(piece2.row - piece.row <
                   square.row - piece.row):
                    return True
        #moving left
        if(square.row < piece.row):
            #piece2 is in the same direction
            if(piece2.row < piece.row):
                #if the piece2 is closer
                if(abs(piece2.row - piece.row) <
                   abs(square.row - piece.row)):
                    return True

    #diagonal
    if(abs(square.column-piece.column)==abs(square.row-piece.row) and
       abs(piece2.column-piece.column)==abs(piece2.row-piece.row)):
        #down, right
        if(square.column>piece.column and square.row>piece.row):
            #piece 2 in same direction
            if(piece2.column>piece.column and piece2.row>piece.row):
                #if the piece2 is closer
                if(piece2.column-piece.column<square.column-piece.column):
                    return True
        #down, left
        if(square.column<piece.column and square.row>piece.row):
            #piece 2 in same direction
            if(piece2.column<piece.column and piece2.row>piece.row):
                #if the piece2 is closer
                if(piece2.row-piece.row<square.row-piece.row):
                    return True
        #up, right
        if(square.column>piece.column and square.row<piece.row):
            #piece 2 in same direction
            if(piece2.column>piece.column and piece2.row<piece.row):
                #if the piece2 is closer
                if(piece2.column-piece.column<square.column-piece.column):
                    return True
        #up, left
        if(square.column<piece.column and square.row<piece.row):
            #piece 2 in same direction
            if(piece2.column<piece.column and piece2.row<piece.row):
                #if the piece2 is closer
                if(abs(piece2.row-piece.row)<abs(square.row-piece.row)):
                    return True
    return False

def distance(piece, square):
    #check for pieces in the way
    for piece2 in attack_pieces:
        if blocker(piece, piece2, square):
            return False

    for piece2 in defend_pieces:
        if blocker(piece, piece2, square):
            return False

    for piece2 in knife_pieces:
        if blocker(piece, piece2, square):
            return False
        
    dif_row = abs(square.row-piece.row)
    dif_col = abs(square.column-piece.column)
    
    if(piece.zone.startswith('defend')):
        if(dif_row>2 or
           dif_col>2):
            return False
        if(square.column == 4 and (square.row == 12 or square.row == 2)):
           return False
    elif(piece.zone =='attack'):
        if(dif_row>2 or
           dif_col>2):
            return False
        if(dif_row!=0 and dif_col!=0):
            if(dif_row!=dif_col):
                return False
    elif(piece.zone =='knife'):
        if(dif_row>1 or
           dif_col>1):
            return False
        if(dif_row!=0 and dif_col!=0):
            if(dif_row!=dif_col):
                return False
    return True

def same_line(danger_piece):
    count = 0
    for piece in defend_pieces:
        if(piece.row != danger_piece.row and piece.column
           == danger_piece.column and piece.player == danger_piece.player):
            count += 1
    for knife in knife_pieces:
        if(knife.player == danger_piece.player and
           knife.column == danger_piece.column):
            if(knife.player):
                if(knife.row>9):
                       count += 1
            else:
                if(knife.row<5):
                   count += 1
           
    if(count>1):
        return True
    return False

def surrounded(danger_piece):
    if(same_line(danger_piece)):
        return False
    num_surround = 0
    for piece in attack_pieces:
        if(piece.player is not danger_piece.player):
            #next door in column
            if(piece.row==danger_piece.row and
               abs(piece.column-danger_piece.column)==1):
                num_surround += 1
            #next door in row
            elif(piece.column==danger_piece.column and
                 abs(piece.row-danger_piece.row)==1):
                num_surround += 1
                
    if(danger_piece.knife and num_surround>=3):
        return True
    elif(not danger_piece.knife and num_surround>=2):
        return True
    return False

def destroyed(piece):
    #check that piece's surroundings
    piece_surrounded = surrounded(piece);
    if(piece_surrounded):
        if(piece.knife):
            piece.reset()
        else:
            piece.destroy()
            attack_pieces.remove(piece)

def clicked(event):
    global turn
    column = int(event.x/50)
    row = int(event.y/50)

    clicked_piece = 'unset'
    move_piece = 'unset'

    for piece in attack_pieces:
        if(piece.clicked):
            move_piece = piece
            
    for piece in defend_pieces:
        if(piece.clicked):
            move_piece = piece

    for piece in knife_pieces:
        if(piece.clicked):
            move_piece = piece
            

    for piece in attack_pieces:
        if(piece.row == row and piece.column == column):
            clicked_piece = piece
            
    for piece in defend_pieces:
        if(piece.row == row and piece.column == column):
            clicked_piece = piece

    for piece in knife_pieces:
        if(piece.row == row and piece.column == column):
            clicked_piece = piece

    if ((clicked_piece != 'unset' and clicked_piece.player == turn
         and move_piece == 'unset')
        or (move_piece is clicked_piece != 'unset')):
          clicked_piece.click()

    if(move_piece != 'unset' and clicked_piece == 'unset'):
        for square in squares:
            if(square.row == row and
               square.column == column and
               (square.zone == move_piece.zone or move_piece.knife)):
                if(distance(move_piece, square)):
                    move_piece.move(square)
                    #check if any piece was destroyed by that move
                    for piece in attack_pieces:
                        destroyed(piece)
                    for piece in defend_pieces:
                        destroyed(piece)
                    for piece in knife_pieces:
                        destroyed(piece)

                    for piece in knife_pieces:
                        if piece.player:
                            if piece.row == 2 and piece.column == 4:
                                end_game(True)
                        else:
                            if piece.row == 12 and piece.column == 4:
                                end_game(False)

                    turn = not turn

def end_game(win):
    canvas.destroy()
        
    if win:
        label = Label(root, text = "Player 1 wins!", fg="blue",
                      font=("Helvetica", 40))
    else:
        label = Label(root, text = "Player 2 wins!", fg="red",
                      font=("Helvetica", 40))
    label.pack()
    
def game():
    color = True
    
    for column in range(9):
        for row in range(15):
            if(column == 4 and (row == 2 or row == 12)):
                squares.append(Square(color,column,row,True))
            else:
                squares.append(Square(color,column,row,False))
            color = not color

    canvas.create_line(0,250,450,250,fill='black',width=5)
    canvas.create_line(0,500,450,500,fill='black',width=5)

    choose_formation(root)
    canvas.pack(anchor='center')
    while True:
        root.update_idletasks()
        root.update()

root = Tk()
squares = []
attack_pieces = []
defend_pieces = []
knife_pieces = []
turn = True
canvas = Canvas(root, width=450, height=750)
canvas.bind("<Button-1>", clicked)
game()

import random
from functools import partial

from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        
        loader = QUiLoader()
        self.ui = loader.load('form1.ui', None)
        self.ui.show()
        
        self.game = [[self.ui.btn_1, self.ui.btn_2, self.ui.btn_3],
                     [self.ui.btn_4, self.ui.btn_5, self.ui.btn_6],
                     [self.ui.btn_7, self.ui.btn_8, self.ui.btn_9]]
        
        self.round = 'X'
        self.point_X = 0
        self.point_O = 0
        self.point_Draw = 0
        self.ui.radioButton_1.setChecked(True)
        
        self.score_Board()
        
        for i in range(3):
            for j in range(3):    
                self.game[i][j].setText('')
                self.game[i][j].setStyleSheet('color: black; background-color: skyblue')   
                self.game[i][j].clicked.connect(partial(self.play, i, j))
        
        self.ui.btn_new.clicked.connect(self.New_Game)
        self.ui.btn_about.clicked.connect(self.about)
    
    def play(self, i, j):
        if self.game[i][j].text() == '':
            
            if self.round == 'X':
                    self.game[i][j].setStyleSheet('color: green; background-color: lightgreen')
                    self.game[i][j].setText('X') 
                    self.round = 'O'
                    
                    self.check()
                    
                    if self.ui.radioButton_2.isChecked():
                        if self.round == 'O':
                            while True:
                                i = random.randint(0,2)
                                j = random.randint(0,2)
                                if self.game[i][j].text() == '':
                                    self.game[i][j].setStyleSheet('color: red; background-color: pink')
                                    self.game[i][j].setText('O')
                                    self.round = 'X'
                                    break        
                                         
            else:
                if self.ui.radioButton_1.isChecked():
                    self.game[i][j].setStyleSheet('color: red; background-color: pink')
                    self.game[i][j].setText('O')
                    self.round = 'X'
    
        self.check()
    
    def check(self):
        end_game = False
        
        for i in range(3):
            if (self.game[i][0].text() == 'X' and self.game[i][1].text() == 'X' and self.game[i][2].text() == 'X') or (self.game[0][i].text() == 'X' and self.game[1][i].text() == 'X' and self.game[2][i].text() == 'X') or (self.game[0][0].text() == 'X' and self.game[1][1].text() == 'X' and self.game[2][2].text() == 'X') or (self.game[0][2].text() == 'X' and self.game[1][1].text() == 'X' and self.game[2][0].text() == 'X'):
                msgBox = QMessageBox()
                msgBox.setText('Player 1 wins')
                msgBox.setStyleSheet('color: white; background-color: gray')
                msgBox.exec()
                self.point_X += 1
                self.score_Board()
                self.New_Game()
                end_game = True
                break
            
            if (self.game[i][0].text() == 'O' and self.game[i][1].text() == 'O' and self.game[i][2].text() == 'O') or (self.game[0][i].text() == 'O' and self.game[1][i].text() == 'O' and self.game[2][i].text() == 'O') or (self.game[0][0].text() == 'O' and self.game[1][1].text() == 'O' and self.game[2][2].text() == 'O') or (self.game[0][2].text() == 'O' and self.game[1][1].text() == 'O' and self.game[2][0].text() == 'O'):
                msgBox = QMessageBox()
                msgBox.setText('Player 2 wins')
                msgBox.setStyleSheet('color: white; background-color: gray')
                msgBox.exec()
                self.point_O += 1
                self.score_Board()
                self.New_Game()
                end_game = True
                break
            
        counter = 0
        for i in range(3):
            for j in range(3):
                if self.game[i][j].text() == 'O' or self.game[i][j].text() == 'X':
                    counter += 1
                    
        if counter == 9 and end_game == False:
            msgBox = QMessageBox()
            msgBox.setText('Draw')
            msgBox.setStyleSheet('color: white; background-color: gray')
            msgBox.exec()
            self.point_Draw += 1
            self.score_Board()
            self.New_Game()
            end_game = True
                
    def New_Game(self):
        for i in range(3):
            for j in range(3):
                self.game[i][j].setText('')
                self.game[i][j].setStyleSheet('color: red; background-color: gray')

    def about(self):
        msgBox = QMessageBox()
        msgBox.setText('Tic-Tac-Toe Game using PySide6\nYou can play with your friend or computer\nThis game programmed with Python and Programmer is Maryam Khoshkhoo')
        msgBox.setStyleSheet('color: white; background-color: gray')
        msgBox.exec()
    
    def score_Board(self):
        self.ui.linex.setText(str(self.point_X))
        self.ui.lineo.setText(str(self.point_O))
        self.ui.linedraw.setText(str(self.point_Draw))

app = QApplication([])
window = TicTacToe()
app.exec() 
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 00:36:26 2022

@author: nilay
"""


import PySimpleGUI
import chess
import chess.pgn
import chess.polyglot
import chess.svg

board = chess.Board()
print(board)

pgn = open("firstGame.pgn")
firstGame = chess.pgn.read_game(pgn)
firstGameBoard = firstGame.board()
for move in firstGame.mainline_moves():
     firstGameBoard.push(move)
print(firstGameBoard)

chess.svg.board(board, size=400)
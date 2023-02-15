#ifndef CHESSBOARD_H
#define CHESSBOARD_H

#include <iostream>
#include <cstdlib>
#include <cstring>
#include "ChessPiece.h"



class ChessBoard{
public:
  ChessBoard();
  ~ChessBoard();  
  void submitMove(const char* source,const char* des);
  void setBoard();  //set the board to initial set up 
  void resetBoard();
  //check if your own king is in check after making move
  // bool in_check(int source_rank, int source_file, int des_rank,
  //		    int des_file, ChessPiece* Board[][8]);
  // check if your move checks your opponent
  bool checking(ChessPiece* Board[][8], bool colour);
private:
  //first int indicate row number (1-8), second int indicate column number (A-H)
  ChessPiece* board[8][8];
  int turn_number ; //the number of turns in a game
  struct{
    int rank;
    int file;
  } w_king_position;
  struct {
    int rank;
    int file;
  } b_king_position;
  bool source_empty(int source_rank, int source_file);
  bool correct_turn(int source_rank, int source_file); 
};

#endif


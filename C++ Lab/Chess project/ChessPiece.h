#ifndef CHESSPIECE_H
#define CHESSPIECE_H

#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;


class ChessPiece{
public:
  ChessPiece();
  virtual ~ChessPiece();
  
  // check if moving the piece satisfies the piece moving rules of chess 
  virtual bool validate_move(int source_rank, int source_file,
			     int des_rank, int des_file, ChessPiece* Board[][8]) = 0;
  
  //check if the destination has an enemy
  bool meet_enemy(int source_rank, int source_file, int des_rank,
		  int des_file, ChessPiece* Board[][8]);
  
  // check if the destination is occupied by a piece of same colour
  bool des_occupied(int source_rank, int source_file, int des_rank,
		  int des_file, ChessPiece* Board[][8]);

  // check if the rank is clear if piece is making horizontal move
  bool rank_clear(int source_rank, int source_file, int des_rank,
		  int des_file, ChessPiece* Board[][8]);

  // check if the file is clear if piece is making vertical move
  bool file_clear(int source_rank, int source_file, int des_rank,
		  int des_file, ChessPiece* Board[][8]);

  bool diag_clear(int source_rank, int source_file, int des_rank,
		  int des_file, ChessPiece* Board[][8]);
  
  //check if your own king is in check after making move
  bool in_check(int source_rank, int source_file, int des_rank,
		    int des_file, ChessPiece* Board[][8]);

  // check if it is the turn to move for the piece
  //bool check_turn(const char* source, turn);

  bool getColour(){
    return colour;
  }
  
  void setColour(bool newColour){
    colour = newColour;
  }
  
  const char* getPiece(){
    return piece;
  }

  void setPiece(char* newPiece){
    piece = newPiece;
  }

  
protected:
  const char* piece;
  //if true, colour is white, if false, colour is black
  bool colour;
};





class King: public ChessPiece{
public:
  King(bool cl){
    this->colour = cl;
    this->piece = "King";
  }
  bool validate_move(int source_rank, int source_file,
		     int des_rank, int des_file, ChessPiece* Board[][8]) override {
    bool des_occupation = des_occupied(source_rank, source_file, des_rank, des_file, Board);
    if (des_occupation)
      return false;
    
    if (  (abs(des_rank-source_rank) == 1) && (abs(des_file - source_file) == 1)  ){
      return true;
    }
    else
      return false;
  }  
};

class Queen: public ChessPiece{
public:
  Queen(bool cl){
    this->colour = cl;
    this->piece = "Queen";
  }
  bool validate_move(int source_rank, int source_file,
		     int des_rank, int des_file, ChessPiece* Board[][8]) override {
    bool des_occupation = des_occupied(source_rank, source_file, des_rank, des_file, Board);
    bool rank_occupation = !rank_clear(source_rank, source_file, des_rank, des_file, Board);
    bool file_occupation = !file_clear(source_rank, source_file, des_rank, des_file, Board);
    bool diag_occupation = !diag_clear(source_rank, source_file, des_rank, des_file, Board);
    
    if (des_occupation)
      return false;

    if  (!((des_rank-source_rank == 0) || (des_file-source_file == 0) ||
	   (abs(des_rank-source_rank) == abs(des_file-source_file)))){
      return false;
    }

    if ((des_file - source_file) == 0){
      if (file_occupation){
	return false;
      }   
    }

    if ((des_rank - source_rank) == 0){
      if (rank_occupation){
	return false;
      }
    }

    if ( abs(des_rank-source_rank) == abs(des_file-source_file) ){
      if (diag_occupation){
	return false;
      }
    }
    return true;
  }
};

class Rook: public ChessPiece{
public:
  Rook(bool cl){
    this->colour = cl;
    this->piece = "Rook";
  }
  bool validate_move(int source_rank, int source_file,
		     int des_rank, int des_file, ChessPiece* Board[][8]) override {
    bool des_occupation = des_occupied(source_rank, source_file, des_rank, des_file, Board);
    bool rank_occupation = !rank_clear(source_rank, source_file, des_rank, des_file, Board);
    bool file_occupation = !file_clear(source_rank, source_file, des_rank, des_file, Board);
     
    if (des_occupation)
      return false;

    if (!((des_rank-source_rank == 0) || (des_file-source_file == 0))){
      return false;
    }

    if ((des_file - source_file) == 0){
      if (file_occupation){
	return false;
      }   
    }

    if ((des_rank - source_rank) == 0){
      if (rank_occupation){
	return false;
      }
    }
    return true;
  }

};

class Bishop: public ChessPiece{
public:
  Bishop(bool cl){
    this->colour = cl;
    this->piece = "Bishop";
  }
  bool validate_move(int source_rank, int source_file,
		     int des_rank, int des_file, ChessPiece* Board[][8]) override {
    bool des_occupation = des_occupied(source_rank, source_file, des_rank, des_file, Board);
    bool diag_occupation = !diag_clear(source_rank, source_file, des_rank, des_file, Board);
      
    if (des_occupation){
      return false;
      cout << "destination occupied" << endl;
    }
    
    if ( !(abs(des_rank-source_rank) == abs(des_file-source_file)) ){
      return false;
      cout << "not moving diagonally" << endl;
    }

    if ( abs(des_rank-source_rank) == abs(des_file-source_file) ){
      if (diag_occupation){
	return false;
	cout << "something is blocking bishop's way" << endl;
      }
    }
    return true;
  }
};

class Knight: public ChessPiece{
public:
  Knight(bool cl){
    this->colour = cl;
    this->piece = "Knight";
  }
  bool validate_move(int source_rank, int source_file,
		     int des_rank, int des_file, ChessPiece* Board[][8]) override {
    bool des_occupation = des_occupied(source_rank, source_file, des_rank, des_file, Board);

    if (des_occupation)
       return false;
    
    if ( ((abs(des_rank-source_rank) == 2) && (abs(des_file-source_file) == 1)) ||
	 ((abs(des_rank-source_rank) == 1) && (abs(des_file-source_file) == 2)) )
    {
      return true;
    }
    else
      return false;
  }
    
};

class Pawn: public ChessPiece{
public:
  Pawn(bool cl){
    this->colour = cl;
    this->piece = "Pawn";
    if (colour == true){
      //white pawns can only move upward
      direction = 1;
    }
    else{
      //black pawns can only move downward
      direction = -1;
    }
  }
  bool validate_move(int source_rank, int source_file,
		     int des_rank, int des_file, ChessPiece* Board[][8]) override {
    bool des_occupation = des_occupied(source_rank, source_file, des_rank, des_file, Board);

    if (des_occupation)
       return false;
    
    if (Board[des_rank][des_file] == NULL){
       if (((des_rank-source_rank)*direction == 1) && ((des_file-source_file) == 0)){
	 return true;
       }
       else if (((colour) && (source_rank == 1) && (((des_rank-source_rank)*direction) == 2)) ||
	     ((!colour) && (source_rank == 6) && (((des_rank-source_rank)*direction) == 2))){
	 return true;
       }
    }
    else if (Board[des_rank][des_file] != NULL){
      if ( ((des_rank-source_rank)*direction == 1) && (abs(des_file-source_file) == 1) ){
	return true;
      }
    }
    return false;
  }
private:
  signed int direction;
};


#endif

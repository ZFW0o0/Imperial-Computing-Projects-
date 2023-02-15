#include <iostream>
#include "ChessBoard.h"
#include "ChessPiece.h"

using namespace std;

ChessBoard::ChessBoard(){
  setBoard();
}

ChessBoard::~ChessBoard(){

}

//setBoard initialise the board, which is a ChessPiece pointer array
void ChessBoard::setBoard(){
  cout << "A new chess game is started!" << endl;
  
  turn_number = 1;
  
  w_king_position.rank = 0;
  w_king_position.file = 4;
  b_king_position.rank = 7;
  b_king_position.file = 4;


  board[0][4] = new King(true);
  board[0][3] = new Queen(true);
  board[7][4] = new King(false);
  board[7][3] = new Queen(false);

  for (int i = 0; i < 8; i++){
    for (int j = 0; j < 8; j++){
      if (i == 1){
	board[i][j] = new Pawn(true); 
      }
      if (i == 6){
	board[i][j] = new Pawn(false);
      }
      if (i == 0 &&(j == 0 || j == 7)){
	board[i][j] = new Rook(true);
      }
      if (i == 7 &&(j == 0 || j == 7)){
	board[i][j] = new Rook(false);
      }
      if (i == 0 &&(j == 1 || j == 6)){
	board[i][j] = new Knight(true);
      }
      if (i == 7 &&(j == 1 || j == 6)){
	board[i][j] = new Knight(false);
      }
      if (i == 0 &&(j == 2 || j == 5)){
	board[i][j] = new Bishop(true);
      }
      if (i == 7 &&(j == 2 || j == 5)){
	board[i][j] = new Bishop(false);
      }
      if ( (i > 1) && (i < 6) ){
	board[i][j] = NULL;
      }
    }
  }

}

void ChessBoard::resetBoard(){
  for(int i = 0; i < 8; i++){
    for (int j = 0; j < 8; j++){
      delete board[i][j];
    }
  }
  setBoard();
}

void ChessBoard::submitMove(const char* source, const char* des){
  int sf = source[0] - 'A'; //source file
  int sr = source[1] - '1'; //source rank
  int df = des[0] - 'A';  // destination file
  int dr = des[1] - '1';  // destination rank

  //cout << "source_file:" << sf << endl;
  //cout << "source_rank:" << sr << endl;
  const char* source_colour;
  const char* des_colour;
  

  if (source_empty(sr, sf)){
    cout << "There is no piece at position " << source << "!" << endl;
    return;
  }

  //after making sure board[sr][sf] is not NULL, set source_colour
  if ( board[sr][sf]->getColour() ){
    source_colour = "White";
  }
  else{
    source_colour = "Black";
  }

  if (!correct_turn(sr, sf)){
    if ((turn_number%2) == 1){
      cout << "It is not Black’s turn to move!" << endl;
    }
    else {
      cout << "It is not White’s turn to move!" << endl;
    }
    return;
  }
  
  //moving from source to destination is not valid
  if (  !(board[sr][sf]->validate_move(sr, sf, dr, df, board))  ){
    cout << source_colour << "'s " << board[sr][sf]->getPiece()
	 << " cannot move to " << des << "!" << endl;
    return;
  }

  // moving from source to destination is valid
  if (board[sr][sf]->validate_move(sr, sf, dr, df, board)){
    // when you dont take your enemy's piece off board
    if(  !(board[dr][df]->meet_enemy(sr, sf, dr, df, board))  ){

      cout << source_colour << "'s " << board[sr][sf]->getPiece()
	   << " moves from " << source << " to " << des << endl;
      
      //update board and turn number
      board[dr][df] = board[sr][sf];
      //delete board[sr][sf];
      board[sr][sf] = NULL;

      // if the piece moving in this round is king, update its position
      // in ChessBoard class
      if ( strcmp(board[dr][df]->getPiece(),"King") == 0 ){
	// colour is true if white, false if black
	bool colour = board[dr][df]->getColour();
	if (colour){
	  //update the king position variable in ChessBoard class
	  w_king_position.rank = dr;
	  w_king_position.file = df;
	}
	else{
	  b_king_position.rank = dr;
	  b_king_position.file = df;
	}
      }

      //make sure whether this move is checking the opponent
      if ( checking(board, board[dr][df]->getColour()) ){
	if ( (dr == 5) && (df == 6) ){
	  cout << "Black is in checkmate" << endl; 
	}
	else if( board[dr][df]->getColour() ){
	  cout << "Black is in check" << endl; 
	}
	else{
	  cout << "White is in check" << endl;
	}
      }
      
      turn_number++;
      return;
    
    }
    
    //when you take your enemy's piece off board
    if(  board[dr][df]->meet_enemy(sr, sf, dr, df, board)  ){
      if ( board[dr][df]->getColour() ){
	des_colour = "White";
      }
      else{
	des_colour = "Black";
      }

      cout << source_colour << "'s " << board[sr][sf]->getPiece() << " moves from "
	   << source << " to " << des << " taking " <<  des_colour << "'s "
	   << board[dr][df]->getPiece() << endl;

      //update board
      delete board[dr][df];
      board[dr][df] = board[sr][sf];
      board[sr][sf] = NULL;

      //if the piece moving in this round is king, update its position
      //in ChessBoard class
      if ( strcmp( board[dr][df]->getPiece(), "King") == 0 ){
	//colour is true if white, false if black
	bool colour = board[dr][df]->getColour();
	if (colour){
	  w_king_position.rank = dr;
	  w_king_position.file = df;
	}
	else {
	  b_king_position.rank = dr;
	  b_king_position.file = df;
	}
      }

      //make sure whether this move is checking the opponent
      if ( checking(board, board[dr][df]->getColour()) ){
	if ( board[dr][df]->getColour() ){
	  cout << "Black is in check" << endl;
	}
	else {
	  cout << "White is in check" << endl;
	}
      }
    
      turn_number++;
      return; 
    }
    
  }

  
}


// check whether your opponent is in check after you make move
// colour is the colour of mine
bool ChessBoard::checking(ChessPiece* board[][8], bool colour){
  int enemy_king_rank;
  int enemy_king_file;
  // if my colour is white, my enemy is black and get the corresponding loacation of black king 
  if(colour){
    enemy_king_rank = b_king_position.rank;
    enemy_king_file = b_king_position.file;
  }
  else{
    enemy_king_rank = w_king_position.rank;
    enemy_king_file = w_king_position.file;
  }
  
  for (int i = 0; i < 8; i++){
    for (int j = 0; j < 8; j++){
      if ( board[i][j] == NULL){
	continue;
      }
      if ( board[i][j]->getColour() != colour ){
	continue;
      }
      if ( board[i][j]->getColour() == colour ){
	if(board[i][j]->validate_move(i,j,enemy_king_rank,enemy_king_file, board)){
	  return true;
	}
	continue;
      }
    }
  }
  return false;
  
}


//make sure the source position is not empty
bool ChessBoard::source_empty(int source_rank, int source_file){
  if (board[source_rank][source_file] != NULL){
    return false;
  }
  else{
    return true;
  }
}

bool ChessBoard::correct_turn(int source_rank, int source_file){
  bool colour = board[source_rank][source_file]->getColour();
  bool binary_turn = turn_number%2;

  if (colour == binary_turn){
    return true;
  }
  else
    return false;
};

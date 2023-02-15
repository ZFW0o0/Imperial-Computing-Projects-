#include "ChessPiece.h"

ChessPiece::ChessPiece(){
  // cout << "ChessPiece constructor called" << endl;
}

ChessPiece::~ChessPiece(){
}

bool ChessPiece::meet_enemy(int source_rank, int source_file, int des_rank,
			    int des_file, ChessPiece* Board[][8]){
  if (Board[des_rank][des_file] != NULL){
    if (Board[des_rank][des_file]->getColour() != Board[source_rank][source_file]->getColour()){
      return true;
    }
    else
      return false;
  }
  else
    return false;
}

bool ChessPiece::des_occupied(int source_rank, int source_file, int des_rank,
	       int des_file, ChessPiece* Board[][8]){
  if (Board[des_rank][des_file] == NULL){
    return false;
  }
  else if (Board[des_rank][des_file]->colour == Board[source_rank][source_file]->colour){
    return true;
  }
  else
    return false;
}

bool ChessPiece::rank_clear(int source_rank, int source_file, int des_rank,
			    int des_file, ChessPiece* Board[][8]){
  if (des_file - source_file > 0){
    for (int i = 1; i < (des_file - source_file); i++){
      if (Board[source_rank][source_file + i] != NULL){
	return false;
      }
    }
  }
  else if (des_file - source_file < 0){
    for (int i = 1; i < (source_file - des_file); i++){
      if (Board[des_rank][des_file + i] != NULL){
	return false;
      }
    }
  }
    return true;
}


bool ChessPiece::file_clear(int source_rank, int source_file, int des_rank,
			    int des_file, ChessPiece* Board[][8]){
  if (des_rank - source_rank > 0){
    for (int i = 1; i < (des_rank - source_rank); i++){
      if (Board[source_rank + i][source_file] != NULL){
	return false;
      }
    }
  }
  else if (des_rank - source_rank < 0){
    for (int i = 1; i < (des_rank - source_rank); i++){
      if (Board[des_rank + i][des_file] != NULL){
	return false;
      }
    }
  }
    return true;
}

bool ChessPiece::diag_clear(int source_rank, int source_file, int des_rank,
		  int des_file, ChessPiece* Board[][8]){
  for ( int i = 1; i < abs(des_rank-source_rank); i++){
    int testing_rank = ((des_rank-source_rank)/abs(des_rank-source_rank))*i + source_rank;
    int testing_file = ((des_file-source_file)/abs(des_file-source_file))*i + source_file;
    if (Board[testing_rank][testing_file] != NULL){
      return false;
    }   
  }
  return true;
}


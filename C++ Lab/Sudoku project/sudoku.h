#ifndef SUDOKU_H
#define SUDOKU_H
#include <cstring>
#include <string>
#include <iostream>
using namespace std;

void load_board(const char* filename, char board[9][9]);
void display_board(const char board[9][9]);
void print_frame(int row);
void print_row(const char* data, int row);
bool is_complete(const char board[9][9]);
bool make_move(const string position,char digit,char board[9][9]);
bool save_board(const char* filename, char board[9][9]);
string coord_convert(int row, int column);
char digit_convert(int number);
bool solve_board(char board[9][9]);
bool back_tracking(char board[9][9],int row,int column, int &recursion_count);



#endif

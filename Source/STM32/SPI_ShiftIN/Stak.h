// Stak class{{{
/*}}}*/
/* include bloc {{{*/
#ifndef STAK_h
#define STAK_h
// the #include statment and code go here...
#if ARDUINO >= 100
#include "Arduino.h"
#else
#include "WProgram.h"
#endif
/*}}}*/
//define bloc  {{{
#define STAKSIZE 30   
/*}}}*/
//  calss{{{
class Stak {
 public: // {{{
	 Stak(int );
	 int	peek();
	 int	pull();
	 int	push(int );
	 int	staksize();
	 void	reset();
	/*}}}*/
 private:/*{{{*/
	int  		command_stak[STAKSIZE] ;
	int 		command_stak_point 	= 0 ;
	/*}}}*/
 };
 /*}}}*/
#endif

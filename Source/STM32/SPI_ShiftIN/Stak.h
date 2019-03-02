// Stak class{{{
/*}}}*/
/* include bloc {{{*/
#ifndef SLAVESPI_h
#define SLAVESPI_h
// the #include statment and code go here...
#if ARDUINO >= 100
#include "Arduino.h"
#else
#include "WProgram.h"
#endif
/*}}}*/
//define bloc  {{{
#define STEKSIZE 30   
/*}}}*/
//  calss{{{
class Stak {
 public: // {{{
	 Stak(int );
	 int	peek();
	 int	pull();
	 int	staksize();
	 void setmsg( int );
	/*}}}*/
 private:/*{{{*/
	int  		command_stak[STEKSIZE] ;
	int 		command_stak_point 	= 0 ;
	void 		add_to_stak(void);
	/*}}}*/
 };
 /*}}}*/
#endif

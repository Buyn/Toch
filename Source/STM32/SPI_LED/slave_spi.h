// SPI full-duplex slave example{{{
// TODO size down all int to byte()
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
#include <SPI.h>
#include <cstdint>
/*}}}*/
//define bloc  {{{
#define SPI_CS_PIN PA4   // slave spi pin CS\SS
#define STEKSIZE 30   
//Commands list
//Stak commands
#define ENDOFSESION			0xFF
#define ENDOFFILE				0xEF
#define EXECUTE				0xAA
/*}}}*/
//  calss{{{
class SLAVESPI {
 public: // {{{
	 int	peek();
	 int	pull();
	 int	staksize();
	 bool	runtime();
	 bool isExecution();
	 byte spiaddress;
	 void setmsg( uint8_t);
	/*}}}*/
 private:/*{{{*/
	uint8_t 	command_stak[STEKSIZE] ;
	int 		commands_waiting 		= 0;
	int 		command_stak_point 	= 0 ;
	bool		spi_pasiv 				= false;
	bool		spi_sesion				= false;
	bool		command_to_execute 	= false;
	uint8_t 	msg = 0;
	uint8_t	back_msg = 0;
	void 		execute_command(void)
	/*}}}*/
 };
 /*}}}*/

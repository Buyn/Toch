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
//#include <cstdint>
/*}}}*/
//define bloc  {{{
#define SPI_CS_PIN PA4   // slave spi pin CS\SS
#define STEKSIZE 30   
#define SESIONTIMEOUT 10   
//Commands list
//Stak commands
#define ENDOFSESION			0xFF
#define ENDOFFILE				0xEF
#define EXECUTE				0xAA
/*}}}*/
//define ERROR bloc  {{{
#define DISINHRONERROR						0x10
#define DISINHRONADRESSERROR				0x11
#define STAKERRORCOMAND						0x20
#define TIMEOUTSESION						0x20
/*}}}*/
//  calss{{{
class SlaveSPI {
 public: // {{{
	 SlaveSPI(int );
	 int	peek();
	 int	pull();
	 int	staksize();
	 bool	runtime();
	 bool isExecute();
	 int 	spiaddress;
	 void setmsg( int );
	void 	spinit(void);
	/*}}}*/
 private:/*{{{*/
	int  		command_stak[STEKSIZE] ;
	int 		commands_waiting 		= 0;
	int 		command_stak_point 	= 0 ;
	bool		spi_pasiv 				= false;
	bool		spi_sesion				= false;
	bool		command_to_execute 	= false;
	int 		msg = 0;
	int 		back_msg = 0;
	long		sesionend;
	bool		isSesionEnd(void);
	void 		execute_command(void);
	void 		spirutine(void);
	void 		add_to_stak(void);

	/*}}}*/
 };
 /*}}}*/
#endif

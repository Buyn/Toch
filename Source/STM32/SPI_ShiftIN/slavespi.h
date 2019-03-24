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
#include "Stak.h"
/*}}}*/
//define Debug mods block{{{
//#define DEBUGMSG_RECIVSEND
//#define DEBUGMSG_EXECUTESTAK
/*}}}*/
//define msg bloc  {{{
#define SPI_CS_PIN PA4   // slave spi pin CS\SS
#define STEKSIZE 30   
#define SESIONTIMEOUT 900   
//Commands list
//Stak commands
#define ENDOFSESION			0xFF
#define ENDOFFILE				0xEF
#define EXECUTE				0xAA
#define SC_ISMSGWATING  	0xB0
#define SC_GETVARBYNAME    0xBA
#define SC_GETMSGBYCOUNT   0xBC
/*}}}*/
//define ERROR bloc  {{{
#define DISINHRONERROR						0x10
#define DISINHRONADRESSERROR				0x11
#define STAKERRORCOMAND						0x20
#define TIMEOUTSESION						0x30
/*}}}*/
//  calss{{{
class SlaveSPI {
 public: // {{{
	 SlaveSPI(int );
	 int	peek();
	 int	pull();
	 int	staksize();
	 int	addMSG(int , unsigned int);
	 bool	runtime();
	 bool isExecute();
	 int 	spiaddress;
	 void setmsg( int );
	 void spinit(void);
	/*}}}*/
 private:/*{{{*/
	Stak 		command_stak = Stak(1);
	Stak 		msg_stak = Stak(1);
	int 		commands_waiting 		= 0;
	int 		msg_waiting				= 0;
	bool		command_to_execute 	= false;
	bool		spi_sesion				= false;
	int 		msg 			= 0;
	int 		back_msg 	= 0;
	long		sesionend;
	bool		isSesionEnd(void);
	void		sendFromStak(void);
	void 		execute_command(void);
	void 		spirutine(void);
	void 		add_to_stak(void);
	uint16 	readyTransfer(uint16 );
	/*}}}*/
 };
 /*}}}*/
#endif

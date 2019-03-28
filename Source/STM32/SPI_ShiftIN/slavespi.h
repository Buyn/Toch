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
//#include "Stak.h"
#include "Stack.h"
/*}}}*/
//define  block{{{
#define UINT unsigned int 
#define STACK_COMMAND_SIZE 10
#define STACK_MSG_SIZE		10
//#define DEBUGMSG_EXECUTESTAK
/*}}}*/
//define Debug mods block{{{
//#define DEBUGMSG_RECIVSEND
//#define DEBUGMSG_EXECUTESTAK
/*}}}*/
//define msg bloc  {{{
#define SESIONTIMEOUT 900   
//Commands list
//Stack commands
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
	void spinit( void );
	void setmsg( int );
	//move to privat after test
#ifdef UNITTEST/*{{{*/
	int 	spiaddress;
	void testmsg( int );
	bool		spi_sesion				= false;
	int 		back_msg 	= 0;
#endif/*UNITTEST }}}*/
 private:/*{{{*/
#ifndef UNITTEST/*{{{*/
	int 	spiaddress;
	void testmsg( int );
	bool		spi_sesion				= false;
	int 		back_msg 	= 0;
#endif/*UNITTEST }}}*/
	Stack <int> 		command_stak;
	Stack <int> 		msg_stak;
	int 		commands_waiting 		= 0;
	int 		msg_waiting				= 0;
	bool		command_to_execute 	= false;
	int 		msg 			= 0;
	long		sesionend;
	bool		isSesionEnd(void);
	void		sendFromStack(void);
	void 		execute_command(void);
	void 		spirutine(void);
	void 		add_to_stak(void);
	UINT	 	readyTransfer(UINT );
	/*}}}*/
 };
 /*}}}*/
#endif

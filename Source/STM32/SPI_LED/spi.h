// SPI full-duplex slave example{{{
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
#define LED_MAX_VALUE 255
#define STEKSIZE 30   
//Commands list
#define SPIADRRES			0x08
//LED comands
#define LEDSTART		0x11
#define LEDSTOP 		0x10
#define LEDSET	 		0x14
#define LED01SET		0x1A
#define LED02SET		0x1B
//Stak commands
#define ENDOFSESION			0xFF
#define ENDOFFILE				0xEF
#define EXECUTE				0xAA
/*}}}*/
//  calss{{{
class SLAVESPI {
 public: // {{{
	int commands_waiting = 0;
	uint8_t command_stak[STEKSIZE] ;
	int command_stak_point = 0 ;
	bool led_activ  = false;
	bool spi_pasiv  = false;
	bool spi_sesion = false;
	uint8_t msg = 0;
	uint8_t back_msg = 0;
	void SlaveLED::execute_command(void){
	/*}}}*/
 private:/*{{{*/
	/*}}}*/
 };
 /*}}}*/

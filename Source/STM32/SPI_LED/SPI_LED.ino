// SPI full-duplex slave example{{{
// STM32 acts as a SPI slave and reads 8 bit data frames over SPI.
// Master also gets a reply from the slave, which is a a simple count (0, 1, 2, 3)
// that is incremented each time a data frame is received.
// Serial output is here for debug
/*}}}*/
/* Include Block{{{*/
#include "RGB_LED.h"
#include "LED.h"
#include <SPI.h>
#include <cstdint>
/*}}}*/

/*Define Block{{{*/
#define RBG_PIN_R PA7   // пин для канала R
#define RBG_PIN_G PB1   // пин для канала G
#define RBG_PIN_B PB0   // пин для канала B
//#define SPI_CS_PIN PA4   // пин для канала B
#define LED_MAX_VALUE 255    
#define MAX_STATS 1    
#define FADESPEED 50   
//#define STEKSIZE 30   
#define TITLEABOUT "SPI LED v 0.1"
//Commands list
#define SPIADRRES			0x08
//LED comands
#define LEDSTART		0x11
#define LEDSTOP 		0x10
#define LEDSET	 		0x14
#define LED01SET		0x1A
#define LED02SET		0x1B

/*}}}*/
/*Varibls Block{{{*/
RGB_LED led_Line(RBG_PIN_R, RBG_PIN_G, RBG_PIN_B);
int state = 0;
unsigned int ledstate01[] = {255, 0, 255, 20} ;
unsigned int ledstate02[] = {0, 255, 0, 20} ;
bool led_activ  = false;
LED test(LED_BUILTIN);
SlaveSPI = sspi(SPIADRRES);
/*}}}*/

/*   setupLEDLine   * {{{ */
void setupLEDLine(void){
	// RGBLED
	pinMode(RBG_PIN_R, OUTPUT);
	pinMode(RBG_PIN_G, OUTPUT);
	pinMode(RBG_PIN_B, OUTPUT);
	test.trige();
	Serial.println("Full Red");
	led_Line.set_to( 255, 0, 0);
	delay(1000);
	test.trige();
	Serial.println("Full Green");
	led_Line.set_to( 0, 255 , 0);
	delay(1000);
	test.trige();
	Serial.println("Full Blue");
	led_Line.set_to(0, 0, 255);
	delay(1000);
	test.trige();
	led_Line.set_speed(FADESPEED);
	} //}}}

void setup() {/*{{{*/
	//enable serial data print
	test.trige();
	Serial.begin(115200);
	delay(100);
	Serial.println(TITLEABOUT);
	setupLEDLine();
	setupSPI();
	Serial.println("End Setup");
	}/*}}}*/

/*   execute_command   *  {{{ */
void execute_command(void){
	switch (sspi.pull()) {/*{{{*/
		case LEDSTART:/*{{{*/
			Serial.println("Start LED");
			led_activ = true;
			test.trige();
			break;/*}}}*/
		case LEDSTOP:/*{{{*/
			Serial.println("Stop LED");
			led_activ = false;
			test.trige();
			sspi.setmsg( 0 );
			break;/*}}}*/
		case LED01SET:/*{{{*/
			Serial.println("Set Led 01");
				for (int i = 0; i < 3; i++) {
					ledstate01[i] = command_stak[i];		
				}
			command_stak_point = 0;
			test.trige();
			back_msg = 0;
			break;/*}}}*/
		case LED02SET:/*{{{*/
			Serial.println("Set Led 02");
				for (int i = 0; i < 3; i++) {
					ledstate02[i] = command_stak[i];		
				}
			command_stak_point = 0;
			test.trige();
			back_msg = 0;
			break;/*}}}*/
		case LEDSET:/*{{{*/
			Serial.println("To Led Fade");
			led_Line.fade_to( command_stak[0], command_stak[1], command_stak[2]);
			led_Line.set_speed(command_stak[3]);
			command_stak_point = 0;
			test.trige();
			back_msg = 0;
			break;/*}}}*/
		default:/*{{{*/
			Serial.println("Error in command execute!!!");
			test.trige();
			back_msg = 1;
			/*}}}*/
			}/*}}}*/
	} //}}}

/*   spirotine   *  {{{ */
void spirutine(void){
	//if (!spi_pasiv) 
		msg = SPI.transfer(back_msg); 
	//else { msg = SPI.transfer(); }
	if (!spi_sesion && msg == SPIADRRES) {/*{{{*/
		back_msg = msg;	
		spi_sesion = true;
		Serial.print("Connected: Start sesion");
		return;
		}/*}}}*/
	else if (commands_waiting == 0) {/*{{{*/
		execute_command();
		}/*}}}*/
	else if (commands_waiting > 0) {/*{{{*/
		commands_waiting--;
		command_stak[command_stak_point] = msg;
		command_stak_point++;
		back_msg = msg;	
		}/*}}}*/
	else  {/*{{{*/
		Serial.print("Disinhron!  Error");
		}/*}}}*/
	Serial.print("Received = 0b");
	Serial.print(msg, BIN);
	Serial.print(", 0x");
	Serial.print(msg, HEX);
	Serial.print(", ");
	Serial.println(msg);
	Serial.print("Send = ");
	Serial.println(back_msg);
	} //}}}

/*   led_loop   * {{{ */
void led_loop(void){
	switch (state) {
		case 0:/*{{{*/
			Serial.println("To LED 01");
			Serial.print(state);
			led_Line.fade_to( ledstate01[0], ledstate01[1], ledstate01[2]);
			led_Line.set_speed(ledstate01[3]);
			state++;
			state = (state)%MAX_STATS;
			Serial.println(state);
			test.trige();
			break;/*}}}*/
		case 1:/*{{{*/
			Serial.println("To LED 02");
			Serial.print(state);
			led_Line.fade_to( ledstate02[0], ledstate02[1], ledstate02[2]);
			led_Line.set_speed(ledstate02[3]);
			state++;
			state = (state)%MAX_STATS;
			Serial.println(state);
			test.trige();
			break;/*}}}*/
		default:/*{{{*/
			Serial.println("Error in LED State!!!");
			state++;
			state = (state)%MAX_STATS;
			Serial.println(state);
			test.trige();
			/*}}}*/
			}
	}/*}}}*/

void loop() {/*{{{*/
	if (led_activ && led_Line.done()) {/*{{{*/
		Serial.println("LED line Done");
		led_loop();
		}/*}}}*/
	if (digitalRead(SPI_CS_PIN)>=HIGH) { //{{{
		spirutine();
		}/*}}}*/
	led_Line.runtime();
	}/*}}}*/


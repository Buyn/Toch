// SPI full-duplex slave example{{{
// STM32 acts as a SPI slave and reads 8 bit data frames over SPI.
// Master also gets a reply from the slave, which is a a simple count (0, 1, 2, 3)
// that is incremented each time a data frame is received.
// Serial output is here for debug
/*}}}*/
/* Include Block{{{*/
#include "RGB_LED.h"
#include "LED.h"
#include "slaveSPI.h"
#include "Shiftin.h"
#include "ShiftOut.h"
#include <cstdint>
/*}}}*/

/*Define Block{{{*/
#define RBG_PIN_R PA8   // пин для канала R
#define RBG_PIN_G PA9   // пин для канала G
#define RBG_PIN_B PA10  // пин для канала B
//debug msges 
//#define					DEBUGMSG_LEDLINE
//#define SPI_CS_PIN PA4   // пин для канала B
#define LED_MAX_VALUE 255    
#define MAX_STATS 3    
#define FADESPEED 10   
//#define STEKSIZE 30   
#define TITLEABOUT "SPI LED v 0.1"
//Commands list
#define SPIADRRES			0x08
//LED comands
#define LEDSTOP 		0x10
#define LEDSTART		0x11
#define LEDMAXSTATE 	0x12
#define LEDSET	 		0x14
#define LED01SET		0x1A
#define LED02SET		0x1B
#define LED03SET		0x1C
//ShiftOut comands
#define SETSHIFTOUT     0x21
//Step Drivers
#define STARTDRIVER    0x31
#define STOPDRIVER     0x32
#define STEPDRIVERTIMEOUT     1000
#define STEPDRIVERPIN01     PB9
#define STEPDRIVERPIN02     PB8
#define STEPDRIVERPIN03     PB7
#define STEPDRIVERPIN04     PB6
//encounter comands
#define STARTECOUNTER    0x41
#define STOPECOUNTER     0x42
/*}}}*/

/*Varibls Block{{{*/
RGB_LED led_Line(RBG_PIN_R, RBG_PIN_G, RBG_PIN_B);
int state = 0;
unsigned int ledstate01[] = {255	, 0	, 0	, 10};
unsigned int ledstate02[] = {0	, 255	, 0	, 10};
unsigned int ledstate03[] = {0	, 0	, 255	, 10};
bool led_activ  = true;
int max_state = MAX_STATS;
LED test(LED_BUILTIN);
SlaveSPI sspi(SPIADRRES);
ShiftIn sinput;
ShiftOut shiftout;
unsigned long stepDrivetime = 0;
bool stepDriveMode = false;

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
	delay(100);
	test.trige();
	Serial.println("Full Green");
	led_Line.set_to( 0, 255 , 0);
	delay(100);
	test.trige();
	Serial.println("Full Blue");
	led_Line.set_to(0, 0, 255);
	delay(100);
	test.trige();
	led_Line.set_speed(FADESPEED);
	} //}}}

/*   execute_command   *  {{{ */
void execute_command(void){
	Serial.print("In execut Switch");
	Serial.println(sspi.peek());
	switch (sspi.pull()) {/*{{{*/
		case LEDSTART:/*{{{*/
			Serial.println("Start LED");
			led_activ = true;
			test.trige();
			sspi.setmsg( 0 );
			break;/*}}}*/
		case LEDSTOP:/*{{{*/
			Serial.println("Stop LED");
			led_activ = false;
			test.trige();
			sspi.setmsg( 0 );
			break;/*}}}*/
		case LED01SET:/*{{{*/
			Serial.println("Set Led 01");
				for (int i = 0; i <= 3; i++) {
					ledstate01[i] = sspi.pull();		
				}
			test.trige();
			sspi.setmsg( 0 );
			break;/*}}}*/
		case LED02SET:/*{{{*/
			Serial.println("Set Led 02");
				for (int i = 0; i <= 3; i++) {
					ledstate02[i] = sspi.pull();		
				}
			test.trige();
			sspi.setmsg( 0 );
			break;/*}}}*/
		case LED03SET:/*{{{*/
			Serial.println("Set Led 03");
				for (int i = 0; i <= 3; i++) {
					ledstate03[i] = sspi.pull();		
				}
			test.trige();
			sspi.setmsg( 0 );
			break;/*}}}*/
		case SETSHIFTOUT:/*{{{*/
			Serial.print("Set LEDs pins to:");
			Serial.println(sspi.peek(), BIN);
			shiftout.send16(sspi.pull());
			test.trige();
			sspi.setmsg( 0 );
			break;/*}}}*/
		case LEDSET:/*{{{*/
			Serial.println("To Led Fade");
			led_Line.set_to( sspi.pull(), sspi.pull(), sspi.pull());
			led_Line.set_speed(sspi.pull());
			test.trige();
			sspi.setmsg( 0 );
			break;/*}}}*/
		case LEDMAXSTATE:/*{{{*/
			Serial.print("Number of LED using - ");
			Serial.println(sspi.peek());
			max_state = sspi.pull();
			test.trige();
			sspi.setmsg( 0 );
			break;/*}}}*/
		case STARTDRIVER:/*{{{*/
			Serial.print("START DRIVER");
			stepDriveMode = true;
			test.trige();
			break;/*}}}*/
		case STOPDRIVER:/*{{{*/
			Serial.print("STOP DRIVER");
			stepDriveMode = false;
			test.trige();
			break;/*}}}*/
		case STARTECOUNTER:/*{{{*/
			Serial.print("STARTE COUNTER ");
			stepDriveMode = true;
			test.trige();
			break;/*}}}*/
		case STOPECOUNTER:/*{{{*/
			Serial.print("STOPE COUNTER");
			stepDriveMode = false;
			test.trige();
			break;/*}}}*/
		default:/*{{{*/
			Serial.println("Error in command execute!!!");
			test.trige();
			sspi.setmsg( 1 );
			/*}}}*/
			}/*}}}*/
	} //}}}

/*   led_loop   *{{{ */
void led_loop(void){
	switch (state) {
		case 0:/*{{{*/
			Serial.println("To LED 01");
			Serial.print(state);
			led_Line.fade_to( ledstate01[0], ledstate01[1], ledstate01[2]);
			led_Line.set_speed(ledstate01[3]);
			state++;
			state = (state)%max_state;
			Serial.println(state);
			test.trige();
			break;/*}}}*/
		case 1:/*{{{*/
			Serial.println("To LED 02");
			Serial.print(state);
			led_Line.fade_to( ledstate02[0], ledstate02[1], ledstate02[2]);
			led_Line.set_speed(ledstate02[3]);
			state++;
			state = (state)%max_state;
			Serial.println(state);
			test.trige();
			break;/*}}}*/
		case 2:/*{{{*/
			Serial.println("To LED 03");
			Serial.print(state);
			led_Line.fade_to( ledstate03[0], ledstate03[1], ledstate03[2]);
			led_Line.set_speed(ledstate03[3]);
			state++;
			state = (state)%max_state;
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

void setup() {/*{{{*/
	//enable serial data print
	Serial.begin(115200);
	test.trige();
	//delay(3000);
	setupLEDLine();
	sspi.spinit();
	Serial.println(TITLEABOUT);
   /* Initialize in digital pins...  */
	sinput.initpins();
   /* Initialize our digital pins...  */
	shiftout.initpins();
   /* Read in and display the pin states at startup.  */
	sinput.runtime();
//int perior =0;
//for (int i = 0; i < 33000; i++) {
//	if (perior == i) {
//		Serial.println(perior);
//			perior = i + 100;
//		}
//	shiftout.send16(i);
//	delay(10);
//	}
	
   pinMode(STEPDRIVERPIN01, OUTPUT);
   pinMode(STEPDRIVERPIN02, OUTPUT);
   pinMode(STEPDRIVERPIN03, OUTPUT);
   pinMode(STEPDRIVERPIN04, OUTPUT);
	Serial.println("End Setup");
	}/*}}}*/

void loop() {/*{{{*/
	if (led_activ && led_Line.done()) {/*{{{*/
#ifdef DEBUGMSG_LEDLINE/*{{{*/
		Serial.println("LED line Done");
#endif/*DEBUGMSG_LEDLINE}}}*/
		led_loop();
		}/*}}}*/
	if (sspi.runtime()) { //and return if is comand redy to exec{{{
		execute_command();
		}/*}}}*/
	led_Line.runtime();
   /* Read the state of all zones.  */
   //sinput.runtime();
   /* If there was a chage in state, display which ones changed.  */
   if(sinput.isChenged()) {/*and it do runtime(){{{*/
       Serial.print("*Pin value change detected*\r\n");
       sinput.display_pin_values();
		 sspi.addMSG(1, (unsigned int)sinput.oldPinValues); 
		 }/*}}}*/
   if(stepDriveMode && micros()> stepDrivetime) {/*and it do runtime(){{{*/
		stepDrivetime = micros() + STEPDRIVERTIMEOUT;
		digitalWrite(STEPDRIVERPIN01, HIGH);
		digitalWrite(STEPDRIVERPIN02, HIGH);
		digitalWrite(STEPDRIVERPIN03, HIGH);
      //Serial.print("Step - ");
      //Serial.println(stepDrivetime);
		//delayMicroseconds(100000);
		digitalWrite(STEPDRIVERPIN01, LOW);
		digitalWrite(STEPDRIVERPIN02, LOW);
		digitalWrite(STEPDRIVERPIN03, LOW);
		}/*}}}*/
	}/*}}}*/


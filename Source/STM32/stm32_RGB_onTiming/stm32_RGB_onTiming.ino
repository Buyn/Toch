/* Include Block{{{*/
#include "RGB_LED.h"
#include "LED.h"
/*}}}*/

/*Define Block{{{*/
#define RBG_PIN_R PA7   // пин для канала R
#define RBG_PIN_G PB1   // пин для канала G
#define RBG_PIN_B PB0   // пин для канала B
#define LED_MAX_VALUE 255    
#define MAX_STATS 5    
#define FADESPEED 50   

/*}}}*/

/*Varibls Block{{{*/
RGB_LED led_Line(RBG_PIN_R, RBG_PIN_G, RBG_PIN_B);
int state = 0;
LED test(LED_BUILTIN);
/*}}}*/

void setup(){/*{{{*/
	//enable serial data print
	test.trige();
	Serial.begin(9600); 
	Serial.println("RBG LED v 0.1");
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
	Serial.println("End Setup");
	}/*}}}*/

void loop(){/*{{{*/
	if (led_Line.done()) {/*{{{*/
		Serial.println("RBG LED v 0.1");
		switch (state) {
			case 0:/*{{{*/
				Serial.println("To Red");
				Serial.print(state);
				led_Line.fade_to( 255, 0, 0);
				state++;
				state = (state)%MAX_STATS;
				Serial.println(state);
				test.trige();
				break;/*}}}*/
			case 1:/*{{{*/
				Serial.println("To Green");
				Serial.print(state);
				led_Line.fade_to( 0, 255 , 0);
				state++;
				state = (state)%MAX_STATS;
				Serial.println(state);
				test.trige();
				break;/*}}}*/
			case 2:/*{{{*/
				Serial.println("To Blue");
				Serial.print(state);
				led_Line.fade_to( 0, 0 , 255);
				state++;
				state = (state)%MAX_STATS;
				Serial.println(state);
				test.trige();
				break;/*}}}*/
			case 3:/*{{{*/
				Serial.println("To Zero");
				Serial.print(state);
				led_Line.fade_to( 0, 0 , 0);
				state++;
				state = (state)%MAX_STATS;
				Serial.println(state);
				test.trige();
				break;/*}}}*/
			case 4:/*{{{*/
				Serial.println("To Full");
				Serial.print(state);
				led_Line.fade_to( 255, 255 , 255);
				state++;
				state = (state)%MAX_STATS;
				Serial.println(state);
				test.trige();
				break;/*}}}*/
			default:/*{{{*/
				Serial.println("Error!!!");
				state++;
				state = (state)%MAX_STATS;
				Serial.println(state);
				test.trige();
				/*}}}*/
			}
		}/*}}}*/
	led_Line.runtime();
}/*}}}*/


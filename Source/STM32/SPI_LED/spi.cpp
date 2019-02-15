#include "SlaveLED.h"

/*   SlaveLED::SlaveLED   * {{{ */
SlaveLED::SlaveLED(void) {
   // The clock value is not used
   // SPI1 is selected by default
   // MOSI, MISO, SCK and NSS PINs are set by the library
   SPI.beginTransactionSlave(SPISettings(18000000, MSBFIRST, SPI_MODE0, DATA_SIZE_8BIT));
	} //}}}

/*   SlaveLED::execute_command   *  {{{ */
void SlaveLED::execute_command(void){
	if (msg > 15) {
		commands_waiting = msg;	
		back_msg = command_stak_point;
		return;
		}
	switch (msg) {/*{{{*/
		case LEDSTART:/*{{{*/
			Serial.println("Start LED");
			led_activ = true;
			command_stak_point = 0;
			test.trige();
			back_msg = 0;
			break;/*}}}*/
		case LEDSTOP:/*{{{*/
			Serial.println("Stop LED");
			led_activ = false;
			command_stak_point = 0;
			test.trige();
			back_msg = 0;
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
		case EXECUTE:/*{{{*/
			Serial.println("Execute");
			commands_waiting = 0;
			test.trige();
			back_msg = command_stak_point;
			break;/*}}}*/
		case ENDOFFILE:/*{{{*/
			Serial.println("ENDOFFILE");
			commands_waiting = 0;
			test.trige();
			back_msg = command_stak_point;
			break;/*}}}*/
		case ENDOFSESION:/*{{{*/
			Serial.println("ENDOFSESION");
			spi_sesion = false;
			test.trige();
			break;/*}}}*/
		default:/*{{{*/
			Serial.println("Error in command execute!!!");
			test.trige();
			back_msg = 1;
			/*}}}*/
			}/*}}}*/
	} //}}}
/*   SlaveLED::spirotine   *  {{{ */
void SlaveLED::spirutine(void){
	//if (!spi_pasiv) 
		msg = SPI.transfer(back_msg); 
	//else { msg = SPI.transfer(); }
	if (!spi_sesion && msg == SPIADRRES) {/*{{{*/
		back_msg = msg;	
		spi_sesion = true;
		Serial.print("Connected: Start sesion");
		Serial.print(microseconds());
		//return;
		}/*}}}*/
	else if (spi_sesion && commands_waiting == 0) {/*{{{*/
		execute_command();
		}/*}}}*/
	else if (spi_sesion && commands_waiting > 0) {/*{{{*/
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

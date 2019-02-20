#include "SlaveSPI.h"

/*   SlaveSPI::SlaveSPI   * {{{ */
SlaveSPI::SlaveSPI(int adrress) {
	spiaddress = adrress;
	} //}}}

/*   SlaveSPI::spinit   * {{{ */
void SlaveSPI::spinit(void){
   // The clock value is not used
   // SPI1 is selected by default
   // MOSI, MISO, SCK and NSS PINs are set by the library
   SPI.beginTransactionSlave(SPISettings(18000000, MSBFIRST, SPI_MODE0, DATA_SIZE_8BIT));
	} //}}}

/*   SlaveSPI::add_to_stak   * {{{ */
void SlaveSPI::add_to_stak(void){
	Serial.print(micros());
	Serial.print(": Comannd adding. waiting = ");
	Serial.print(commands_waiting);
	Serial.print("stak = ");
	Serial.println(command_stak_point);
	commands_waiting--;
	command_stak[command_stak_point++] = msg;
	//TODO merje to one line
	//command_stak_point++;
	back_msg = msg;	
	} //}}}

/*   SlaveSPI::execute_command   *  {{{ */
void SlaveSPI::execute_command(void){
	Serial.print(micros());
	Serial.println(": Comannd Exekution  ");
	//{{{ is adding list command
	if (msg <= 15) {
		commands_waiting = msg;	
		Serial.print(micros());
		Serial.print(": Comannd waiting - ");
		Serial.println(commands_waiting);
		back_msg = command_stak_point;
		return;
		}/*}}}*/
	switch (msg) {/*{{{*/
		case EXECUTE:/*{{{*/
			Serial.println("Execute Last");
			commands_waiting = 0;
			back_msg = msg;
			command_to_execute	= true;
			break;/*}}}*/
		case ENDOFFILE:/*{{{*/
			Serial.println("ENDOFFILE");
			commands_waiting = 0;
			back_msg = msg;
			break;/*}}}*/
		case ENDOFSESION:/*{{{*/
			Serial.println("ENDOFSESION");
			back_msg = msg;
			spi_sesion = false;
			commands_waiting = 0;
			break;/*}}}*/
		default:/*{{{*/
			Serial.println("Error in stek command execute!!!");
			Serial.println("ENDOFSESION");
			spi_sesion = false;
			commands_waiting = 0;
			back_msg = STAKERRORCOMAND;
			/*}}}*/
			}/*}}}*/
	} //}}}

/*   SlaveSPI::peek   * {{{ */
int SlaveSPI::peek(void){
	return command_stak[command_stak_point];
	} //}}}

/*   SlaveSPI::pull   * {{{ */
int SlaveSPI::pull(void){
	if (command_stak_point == 0)
		return command_stak[command_stak_point];
	else	
		return command_stak[command_stak_point--];
	} //}}}

/*   SlaveSPI::staksize   * {{{ */
int SlaveSPI::staksize(void){
	return command_stak_point;
	} //}}}

/*   SlaveSPI::isExecute   * {{{ */
bool SlaveSPI::isExecute(void){
	return command_to_execute;
	} //}}}

/*   SlaveSPI::setmsg   * {{{ */
void SlaveSPI::setmsg(int newmsg){
	back_msg = newmsg;
	} //}}}

/*   SlaveSPI::runtime   * {{{ */
bool SlaveSPI::runtime(void){
	if (digitalRead(SPI_CS_PIN)>=HIGH) { 
		spirutine();
		}
	return command_to_execute;
	} //}}}

/*   SlaveSPI::spirotine   *  {{{ */
void SlaveSPI::spirutine(void){
	//if (!spi_pasiv) 
	msg = SPI.transfer(back_msg); 
	Serial.print("Recived = 0b");
	Serial.print(msg, BIN);
	Serial.print(", 0x");
	Serial.print(msg, HEX);
	Serial.print(", ");
	Serial.println(msg);
	Serial.print("Send = ");
	Serial.println(back_msg);
	//else { msg = SPI.transfer(); }
	if (!spi_sesion && msg == spiaddress) {/*{{{*/
		back_msg = msg;	
		spi_sesion = true;
		commands_waiting = 0;
		Serial.print(micros());
		Serial.println(": Connected: Start sesion");
		//return;
		}/*}}}*/
	else if (spi_sesion && commands_waiting == 0) {/*{{{*/
		execute_command();
		}/*}}}*/
	else if (spi_sesion && commands_waiting > 0) {/*{{{*/
		add_to_stak();
		}/*}}}*/
	else  {/*{{{ Error*/
		Serial.print(micros());
		Serial.println(": Disinhron!  Error  ");
		Serial.println("ENDOFSESION");
		back_msg = DISINHRONERROR;
		spi_sesion = false;
		commands_waiting = 0;
		if(msg != spiaddress) back_msg = DISINHRONADRESSERROR;
		}/*}}}*/
	} //}}}

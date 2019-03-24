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
#ifdef DEBUGMSG_EXECUTESTAK/*{{{*/
	Serial.print(micros());
	Serial.print(": command waiting: ");
	Serial.println(commands_waiting);
#endif/*}}}*/
	commands_waiting--;
	command_stak.push(msg);
	back_msg = msg;	
	} //}}}

/*   SlaveSPI::execute_command   *  {{{ */
void SlaveSPI::execute_command(void){
#ifdef DEBUGMSG_EXECUTESTAK/*{{{*/
	Serial.println(micros());
#endif/*}}}*/
	//{{{ is adding list command
	if (msg <= 15) {
		commands_waiting = msg;	
#ifdef DEBUGMSG_EXECUTESTAK/*{{{*/
		Serial.print(micros());
		Serial.print(": Comannd waiting - ");
		Serial.println(commands_waiting);
#endif/*}}}*/
		back_msg = command_stak.staksize();
		return;
		}/*}}}*/
#ifdef DEBUGMSG_EXECUTESTAK/*{{{*/
	Serial.println(": Comannd Exekution  ");
#endif/*}}}*/
	switch (msg) {/*{{{*/
		case EXECUTE:/*{{{*/
			Serial.println("Execute Last");
			commands_waiting = 0;
			back_msg = msg;
			command_to_execute	= true;
			break;/*}}}*/
		case SC_GETMSGBYCOUNT:/*{{{*/
			Serial.println("given back MSG");
			back_msg = msg_stak.pull();
			msg_waiting = 1;
			break;/*}}}*/
		case SC_ISMSGWATING:/*{{{*/
			Serial.println("Asket number of MSG: ");
			back_msg = msg_stak.staksize();
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

/*   SlaveSPI::sendFromStak   * {{{ */
void SlaveSPI::sendFromStak(void){
#ifdef DEBUGMSG_EXECUTESTAK/*{{{*/
	Serial.print("given back value : ");
	Serial.println(msg_waiting);
#endif/*}}}*/
	back_msg = msg_stak.pull();
	if( msg_waiting > 0 ) msg_waiting--;
	//msg_waiting = msg;
	} //}}}

/*   SlaveSPI::addMSG   * {{{ */
int SlaveSPI::addMSG(int name, unsigned int value){
	msg_stak.push(name);
	Serial.print("Pushingn in MSG stak : ");
	Serial.println(value);
	msg_stak.push(value);
	return msg_stak.staksize();
	} //}}}

/*   SlaveSPI::isSesionEnd   * {{{ */
bool SlaveSPI::isSesionEnd(void){
	if (millis() >= sesionend){
		back_msg = TIMEOUTSESION;	
		spi_sesion = false;
		commands_waiting = 0;
		msg_waiting = 0;
		Serial.print(micros());
		Serial.println(": Sesion end: Timeout Error");
		return true;
		}
	return false;
	} //}}}

/*   SlaveSPI::peek   * {{{ */
int SlaveSPI::peek(void){
	return command_stak.peek();
	} //}}}

/*   SlaveSPI::pull   * {{{ */
int SlaveSPI::pull(void){
		if (command_to_execute){
#ifdef DEBUGMSG_EXECUTESTAK/*{{{*/
			Serial.print( command_stak.peek());
			Serial.println(" : Set command to false");
#endif/*}}}*/
			command_to_execute = false;
			}
#ifdef DEBUGMSG_EXECUTESTAK/*{{{*/
		Serial.print( command_stak.peek());
		Serial.println(" - Get form stak ");
#endif/*}}}*/
		return command_stak.pull();
	} //}}}

/*   SlaveSPI::staksize   * {{{ */
int SlaveSPI::staksize(void){
	return command_stak.staksize();
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
	if ( spi_is_rx_nonempty(SPI.dev()) && !spi_is_busy(SPI.dev())) { /*{{{*/
		spirutine();
		}/*}}}*/
	return command_to_execute;
	} //}}}

/*   SlaveSPI::readyTransfer   * {{{ */
uint16 SlaveSPI::readyTransfer(uint16 response){
   spi_dev * spi_d = SPI.dev();
	if ( spi_is_tx_empty(spi_d) && !spi_is_busy(spi_d)) { 
		spi_tx_reg(spi_d, response); // write the data to be transmitted into the SPI_DR register (this clears the TXE flag)
	}else{
		Serial.println("tx reg not empty");}
   while (spi_is_busy(spi_d)); // "... and then wait until BSY=0 before disabling the SPI."
	return (uint16)spi_rx_reg(spi_d);
	} //}}}

/*   SlaveSPI::spirotine   *  {{{ */
void SlaveSPI::spirutine(void){
	msg = readyTransfer(back_msg);
	isSesionEnd();
#ifdef DEBUGMSG_RECIVSEND/*{{{*/
	Serial.print("Recived = 0x");
	Serial.print(msg, HEX);
	Serial.print(", ");
	Serial.println(msg);
	Serial.print("Send = ");
	Serial.println(back_msg);
#endif/*}}}*/
	if (!spi_sesion && msg == spiaddress) {/*{{{*/
		back_msg = msg;	
		spi_sesion = true;
		commands_waiting = 0;
		sesionend = millis() + SESIONTIMEOUT;
		command_stak.reset();
		Serial.print(micros());
		Serial.print(": Connected: Start sesion");
		Serial.println(millis());
		Serial.println(sesionend);
		return;
		}/*}}}*/
	else if (spi_sesion && msg_waiting != 0 && !isSesionEnd()) {/*{{{*/
		sendFromStak();
		}/*}}}*/
	else if (spi_sesion && commands_waiting == 0 && !isSesionEnd()) {/*{{{*/
		execute_command();
		}/*}}}*/
	else if (spi_sesion && commands_waiting > 0 && !isSesionEnd()) {/*{{{*/
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

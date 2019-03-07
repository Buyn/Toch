#include "Stak.h"

/*   Stak::Stak   * {{{ */
Stak::Stak(int size) {
	} //}}}

/*   Stak::push   * {{{ */
int Stak::push(int newValue){
	Serial.print("Add to Stak");
	Serial.print(newValue);
	Serial.print(") stak = ");
	Serial.println(command_stak_point);
	command_stak[command_stak_point++] = newValue;
	return command_stak_point ;
	} //}}}

/*   Stak::peek   * {{{ */
int Stak::peek(void){
	return command_stak[command_stak_point];
	} //}}}

/*   Stak::pull   * {{{ */
int Stak::pull(void){
	if (command_stak_point == 0)
		return command_stak[command_stak_point];
	else	
		return command_stak[command_stak_point--];
	} //}}}

/*   Stak::staksize   * {{{ */
int Stak::staksize(void){
	return command_stak_point;
	} //}}}


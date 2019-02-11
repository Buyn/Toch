#include "Encounter.h"

/*   Encounter::encounter   * {{{ */
Encounter::Encounter(void){
	sec_interaps = 0;
	min_interaps = 0;
	min_counter_time = millis() + 60000;
	sec_counter_time = millis() + 1000;
	} //}}}

/*   Encounter::encounter_interapt   * {{{ */
void Encounter::encounter_interapt(void){
	sec_interaps++;
	min_interaps++;
	} //}}}

/*   Encounter::have_rps   * {{{ */
bool Encounter::have_rps(void){
  if (millis() >= sec_counter_time) 
  		return true;
	else 
  		return false;
	} //}}}
/*   Encounter::have_rpm   * {{{ */
bool Encounter::have_rpm(void){
	if (millis() >= min_counter_time) 
		return true;
	else 
		return false;
	} //}}}

/*   rps_counter   * {{{ */
int Encounter::rps_counter(void){
	temptxt = sec_interaps;
	sec_interaps = 0;
	sec_counter_time = millis() + 1000;
	return temptxt;
	} //}}}
/*   min_counter   * {{{ */
int Encounter::rpm_counter(void){
	temptxt = min_interaps;
	min_interaps = 0;
	min_counter_time = millis() + 60000;
	return temptxt;
	} //}}}

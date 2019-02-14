#include "SlaveLED.h"

/*   SlaveLED::SlaveLED   * {{{ */
SlaveLED::SlaveLED(int _pin) {
	pin = _pin;
	to_value = 0;
	value = 0;
	fade_speed = 10;
	update_time = millis() + fade_speed;
	pinMode(pin, OUTPUT);
	} //}}}

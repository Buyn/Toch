/* coment bloc {{{
 *
 * Protatip of encounter class 
 * }}}*/
/* include bloc {{{*/
#ifndef encounter_h
#define encounter_h
// the #include statment and code go here...
#if ARDUINO >= 100
#include "Arduino.h"
#else
#include "WProgram.h"
#endif
/*}}}*/
//define bloc  {{{
/*}}}*/
// encounter calss{{{
class Encounter {
 public: // {{{
   Encounter(void);
	void encounter_interapt();
	int rps_counter(void);
	int rpm_counter(void);
	bool have_rpm();
	bool have_rps();
	/*}}}*/
 private:/*{{{*/
	void set_interrupts(void);
	void reset_time();
	unsigned long sec_counter_time, min_counter_time;
	int sec_interaps, min_interaps;
	int temptxt;
	/*}}}*/
 };
 /*}}}*/
#endif

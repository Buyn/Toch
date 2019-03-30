/* coment bloc  {{{
 *
 * Redifine pins for pogram used in Libs
 * must be includet last
***************************************
***************************************
 *  }}}*/
/* include bloc {{{*/
//#ifndef PINSREDEFINE_h
//#define PINSREDEFINE_h
// the #include statment and code go here...
/*}}}*/
//define bloc  {{{
// Pins from shiftin.h
#define SHIFTIN_PLOADPIN         PB12  // 1 sh\ld Connects to Parallel load pin 
#define SHIFTIN_CLOCKENABLEPIN   PB13 // clk inh Connects to Clock Enable pin 
#define SHIFTIN_DATAPIN          PB14 // Qh serial output Connects to the Q7 pin 
#define SHIFTIN_CLOCKPIN         PB15 // clk Connects to the Clock pin 
/*}}}*/
//define Debug mods block{{{
//#define DEBUGMSG_RECIVSEND
//#define DEBUGMSG_EXECUTESTAK
#define DEBUGMSG_MSGSTASK
#define DEBUGMSG_INFO
/*}}}*/
//#endif

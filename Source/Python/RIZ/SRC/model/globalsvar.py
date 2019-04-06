DEBUGMODE = False

# SPI Devise
BUS     = 0 
DEVICE  = 0

# buttons pins
B_RESET     = 13
B_OK        = 14
B_CHOICE    = 15
# LEDs pins
ledsPins = {
   "Sharpenning"           	: 15,
   "Polishing"             	: 14,
   "Ready"                 	: 13,
   "Right side"             	: 12,
   "Left side"              	: 11,
   "Ceramic knife"          	: 10,
   "Polishing disk cleaning"	: 9 ,
   "Full cycle"             	: 8 ,
   "Middle cycle"           	: 7
    }
L_SHARPENNING            = 15
L_POLISHING              = 14
L_READY                  = 13
L_RIGHTSIDE              = 12
L_LEFTSIDE               = 11
L_CERAMICKNIFE           = 10
L_POLISDHINGDISKCLEANING = 9
L_FULLCYCLE              = 8
L_MIDDLECYCLE            = 7

# SPI Adresses
LEDSTM_ADRRESS = 0x08
# SPI Timing
SPI_SLEEPAFTERSEND      = 0.1
SPI_SLEEPBETWINMSGGET   = 0.5
# SPI stek command
SC_EXECUTECOMMAND   = 0xAA
SC_ISMSGWATING      = 0xB0
SC_GETVARBYNAME     = 0xBA
SC_GETMSGBYCOUNT    = 0xBC
SC_ENDOFFILE        = 0xEF
SC_ENDOFSESION      = 0xFF
#define Vars Names
VN_BUTTONVAULT01    = 0x01
#define ERROR bloc  
DISINHRONERROR                    = 0x10
DISINHRONADRESSERROR              = 0x11
STAKERRORCOMAND                   = 0x20
TIMEOUTSESION                     = 0x30

# Commands list
# LED comands
SC_LEDSTOP         = 0x10
SC_LEDSTART        = 0x11
SC_LEDSET          = 0x14
SC_LED01SET        = 0x1A
SC_LED02SET        = 0x1B
SC_LED03SET        = 0x1C
#ShiftOut comands
SC_SETSHIFTOUT     = 0x21



DEBUGMODE = False

# SPI Devise
BUS     = 0 
DEVICE  = 0

# SPI Adresses
LEDSTM_ADRRESS = 0x08
SPI_SLEEPAFTERSEND = 0.1
# SPI stek command
SC_EXECUTECOMMAND   = 0xAA
SC_GETALLMSG        = 0xB0
SC_GETVARBYNAME     = 0xBA
SC_GETMSGBYCOUNT    = 0xBC
SC_ENDOFFILE        = 0xEF
SC_ENDOFSESION      = 0xFF
#define Vars Names
VN_BUTTONVAULT01    = 0xA1
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
# Stak commands



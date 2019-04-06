   if(sinput.isChenged()) {/*and it do runtime(){{{*/
       Serial.print("*Pin value change detected*\r\n");
       sinput.display_pin_values();
		 sspi.addMSG(1, (unsigned int)sinput.oldPinValues); 
		 }/*}}}*/

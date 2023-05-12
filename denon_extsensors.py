#!/usr/bin/python3
#denon_avr_parameter v0.9
#namor_noditz@hkv.de 2023-05-12

import sys
import denon_telnet

def extSensorSting(sensor):
    if sensor == "AudioOutputStr":
        parameter = "SYSMI " 
        val = "?"    
        r1 = denon_telnet.getresponse(parameter,val)
        parameter = "SSOUTFAISFOR "
        val = "?"    
        r2 = denon_telnet.getresponse(parameter,val)
        result = r1 + " (" +  r2 + ")"
    elif sensor == "AudioInputStr":
        parameter = "SYSDA " 
        val = "?"    
        r1 = denon_telnet.getresponse(parameter,val)
        parameter = "SSINFAISFOR "
        val = "?"    
        r2 = denon_telnet.getresponse(parameter,val)
        result = r1 + " (" +  r2 + ")"
    elif sensor == "AudioInOutStr":
        r1 = extSensorSting("AudioInputStr")
        r2 = extSensorSting("AudioOutputStr")
        result = r1 + " => "+ r2 
    elif sensor == "VideoInOutStr":
        parameter = "SYSDVIN " 
        val = "?"    
        r1 = denon_telnet.getresponse(parameter,val)
        parameter = "SYSDVOUT "
        val = "?"    
        r2 = denon_telnet.getresponse(parameter,val)
        result = r1 + " => "+ r2 
    else:
        result="undef"
    return(result)

def main(argv):    
    sensor = sys.argv[1]
    result = extSensorSting(sensor)
    print(result)

if __name__ == "__main__":
   main(sys.argv[1:])
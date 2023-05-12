#!/usr/bin/python3
#denon_avr_parameter v0.9
#namornoditz 2023-05-12

import sys
import telnetlib
import re #regex
import denon_helper

def getresponse(parameter,val):
    cmd = parameter + val    
    pattern = parameter + ".+\r"

    #special command handling
    if parameter=="SSOUTFAISFOR ":
        parameter = "CV" 
        cmd = parameter + val
        pattern = "\rCVEND\r"
    elif parameter=="MV":   
        pattern = "MV\d\d\d?\r"
    elif parameter=="SI":   
        pattern = "SI[^N].*\r"

    cmdb = bytes(cmd + "\r",'UTF-8')        
    patternb = bytes(pattern,'UTF-8')

    #telnet connect, send, wait for response
    try:
        #device
        HOST = "192.168.31.44"
        PORT = 23
        #open connection
        telnet = telnetlib.Telnet(HOST,PORT)
        #send command
        telnet.write(cmdb)
        #wait for response matching pattern
        idx, obj, responseb = telnet.expect([patternb],5)
        #close connection
        telnet.close()
    except:
        #return
        return("offline")

    #filter result from response
    try:
        #special command handling :-/
        if cmd=="MV?":
            pattern = "MV(\d\d\d?)\r"
        if cmd=="SI?":
            pattern = "SI([^N].*)\r"            
        else:
            pattern = parameter + "(.+)\r"
        response = responseb.decode("utf-8")
        match = re.search(pattern, response)
        if match is not None:
            result = match.groups()[0]
            #process/format responses
            #Disable next Line to show raw result
            result = denon_helper.responseHandling(parameter, result)
            return(result)
        else:
            result = "not found: <" + pattern.replace("\r","\\r") + "> in: <" + response.replace("\r","\\r") + ">"
            return(result)
    except:
        #return
        result = "not found: <" + pattern.replace("\r","\\r") + "> in: <" + response.replace("\r","\\r") + ">"
        return("error filter: " + result)

def main(argv):
    parameter = sys.argv[1]
    val = sys.argv[2]
    result = getresponse(parameter,val)
    print(result)

if __name__ == "__main__":
   main(sys.argv[1:])
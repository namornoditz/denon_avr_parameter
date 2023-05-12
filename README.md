# denon_avr_parameter
#### Get all and more parameters from Denon AVRs and use it in Home Assistant.

A set of python scripts to query (pull)
- documented parameters, 
- system paramters and 
- derived parameters 

from Denon AVRs and return them friendly formated to HA.

## Features

It is more then just send command and forward responses to HA.
Several parameters must be formated, some used system parameters are not included in the official documention and the <output channel layout> parameter must be derived from a set of CV-parameters for a nice presentation.
  
## Screenshots
  
![Alt text](screenshot%233.png?raw=true "Screenshot #3")
![Alt text](screenshot%232.png?raw=true "Screenshot #2")
![Alt text](screenshot%231.png?raw=true "Screenshot #1")

## Installation

1. Create a a folder <python_scripts> in your HA config folder.
2. Copy all python scripts to that folder.
3. Add sensors to your HA <configuration.yaml>. 
In <denon_example_configuration.yaml> you find examples for command_line sensors.
4. Use the sensors in your HA cards and automations

## Testing

```sh
>python3 /config/python_scripts/denon_extsensors.py "AudioInOutStr"
PCM (7.1) => Auro-3D (7.1.4)

>python3 /config/python_scripts/denon_telnet.py "NSFRN " "?"
Denon AVC-X4700H

>python3 /config/python_scripts/denon_telnet.py "SSOUTFAISFOR " "?"
7.1.4

>python3 /config/python_scripts/denon_telnet.py "SYSDVIN " "?"
1080p60

>python3 /config/python_scripts/denon_telnet.py "PSMULTEQ:" " ?"
Reference
  
>python3 /config/python_scripts/denon_telnet.py "MV" "70"
-10.0
```

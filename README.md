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

## Installation

1. Create a a folder <python_scripts> in your HA config folder 
2. Copy all python scripts to that place.
3. Add sensors to your HA <configuration.yaml>. 
In <denon_example_configuration.yaml> you find examples for command_line sensors.
4. Use the sensors in your cards and automations



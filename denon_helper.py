#!/usr/bin/python3
#denon_avr_parameter v0.9
#namornoditz 2023-05-12

import re #regex
import denon_dicts as dd

def responseHandling(parameter, result):
    #process responses
    if parameter == "MV":
        if len(result)==2:        
            result = result + "0"                
        vol = float(result)/10 - 80  
        result = str(vol)
    elif parameter == "PSDELAY ":
        vol = int(result)
        result = str(vol)
    elif parameter == "CV":
        result = generateDenonChannelString(result)
    elif parameter == "SSINFAISFOR ":
        result = convertDenonChannelString(result)
    elif parameter == "PSMULTEQ:":
        result = dd.eqdict.get(result) 
    elif parameter == "SSSMG ":
        result = dd.modedict.get(result) 
    elif parameter == "SV":
        result = dd.inputdict.get(result) 
    elif parameter == "SI":
        result = dd.inputdict.get(result)       
    elif parameter == "PSAUROMODE ":        
        result = dd.aurodict.get(result) 
    elif parameter == "PSAUROPR ":
        result = dd.aurodict.get(result) 

    result = result.rstrip()
    return(result)

def convertDenonChannelString(result):
    #response to SSINFAISFOR ?
    #example: 2/0/.0
    pattern = "(\d)/(\d)/.(\d)"
    match = re.search(pattern, result)
    if match is not None:
        layer1Count = int(match.groups()[0]) + int(match.groups()[1])
        layerSubCount = int(match.groups()[2])
        layer2Count = 0
        layer3Count = 0
        result = str(layer1Count) + "." + str(layerSubCount)
    else:
        result = "0.0"
    return (result)

def generateDenonChannelString(result):
    #response to SSOUTFAISFOR ?
    #example: FL 50\rCVFR 50\rCVC 50\rCVSL 50\rCVSR 50\rCVFHL 50\rCVFHR 50\rCVSHL 50\rCVSHR 50\rCVTS 50
    result = "CV" + result.replace(" 50\r",",")
    channels = result.split(",")
    layer1Count = 0
    layer2Count = 0
    layer3Count = 0
    layerSubCount = 0
    for ch in channels:
        if ch in dd.channelsLayer1:
            layer1Count += 1
        elif ch in dd.channelsLayer2:
            layer2Count += 1
        elif ch in dd.channelsLayer3:
            layer3Count += 1
        elif ch in dd.channelsLayerSub:
            layerSubCount += 1            
    if layer2Count > 0:
        if layer3Count > 0:
            result = str(layer1Count) + "." + str(layerSubCount) + "." + str(layer2Count) + "." + str(layer3Count)
        else:
            result = str(layer1Count) + "." + str(layerSubCount) + "." + str(layer2Count)
    else:
        result = str(layer1Count) + "." + str(layerSubCount)         
    return (result)

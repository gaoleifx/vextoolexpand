import json
import hou

def readJson(jsonPath):
    with open(jsonPath, 'r') as f:
        datas = json.load(f)
        
    return datas


def rampTypeValue():
    typeDict = {'Linear':hou.rampBasis.Linear,
                'Constant':hou.rampBasis.Constant,
                'CatmullRom':hou.rampBasis.CatmullRom,
                'MonotoneCubic':hou.rampBasis.CatmullRom,
                'Bezier':hou.rampBasis.Bezier,
                'BSpline':hou.rampBasis.BSpline,
                'Hermite':hou.rampBasis.Hermite}
    
    return typeDict
import plotting
import image
import math

def example(): return [2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 3+1j, 3.25+1j]

def rotate(S, theta): return { z*math.e**(theta*1j)for z in S }

def translateRightUp(S, o): return { o+z for z in S }

def translateLeftDown(S, o): return { -o+z for z in S }

def translateInvertLeft(S, o): return { o-z for z in S }

def translateInvertOpposite(S, o): return { -o-z for z in S }

def scale(S, s): return { s*z for z in S }

def rotateFromAxis180(S): return scale(S, -1)

def rotateFromAxis90(S): return scale(S, 1j)

def rotateAndScaled(S): return { 0.5*z for z in { 1j*s for s in S } }

def rotateAndScaled2(S): return { 0.5*1j*z for z in S }

def rotateAndScaledShiftDownAndRight(S): return { 0.5/1j*z - (0+1j) + (2+0j) for z in S }

def loadImageAndPlot(imageFile):
    data = image.color2gray(image.file2image(imageFile))
    row = len(data) 
    col = len(data[0])
    
    S = [ x+(y*1j) for y in range(len(data)) for x in range(len(data[y])) if data[row-y-1][x] < 120 ]
    
    plotting.plot(S, max(row, col), 1)
    
def loadImageAndPlotToCenter(imageFile):
    data = image.color2gray(image.file2image(imageFile))
    row = len(data) 
    col = len(data[0])
    
    yCenter = int(row / 2)
    xCenter = int(col / 2)
    
    toCenter = 0 - xCenter - yCenter * 1j
    
    S = [ x+(y*1j)+toCenter for y in range(len(data)) for x in range(len(data[y])) if data[row-y-1][x] < 120 ]
    
    plotting.plot(S, max(yCenter, xCenter), 1)
    
def loadImageAndPlotToCenterRotateAndScale(imageFile):
    data = image.color2gray(image.file2image(imageFile))
    row = len(data) 
    col = len(data[0])
    
    yCenter = int(row / 2)
    xCenter = int(col / 2)
    
    toCenter = 0 - xCenter - yCenter * 1j
    
    S = rotateAndScaled([ x+(y*1j)+toCenter for y in range(len(data)) for x in range(len(data[y])) if data[row-y-1][x] < 120 ])
    
    plotting.plot(S, max(yCenter, xCenter), 1)
    
def loadImageRotateAndPlot(imageFile, theta):
    data = image.color2gray(image.file2image(imageFile))
    row = len(data) 
    col = len(data[0])
    
    S = rotate([ x+(y*1j) for y in range(len(data)) for x in range(len(data[y])) if data[row-y-1][x] < 120 ], theta)

    plotting.plot(S, max(row * 1.5, col * 1.5), 1)
    
    
def loadImageRotateCenterAndPlot(imageFile, theta):
    data = image.color2gray(image.file2image(imageFile))
    row = len(data) 
    col = len(data[0])
    
    yCenter = int(row / 2)
    xCenter = int(col / 2)
    
    toCenter = 0 - xCenter - yCenter * 1j
    
    S = rotate([ x+(y*1j)+toCenter for y in range(len(data)) for x in range(len(data[y])) if data[row-y-1][x] < 120 ], theta)

    plotting.plot(S, max(yCenter * 1.5, xCenter * 1.5), 1)
    
def loadImageRotateCenterScaleAndPlot(imageFile, theta, scale):
    data = image.color2gray(image.file2image(imageFile))
    row = len(data) 
    col = len(data[0])
    
    yCenter = int(row / 2)
    xCenter = int(col / 2)
    
    toCenter = 0 - xCenter - yCenter * 1j
    
    S = [ math.e**(theta*1j)*scale*(x+(y*1j)+toCenter) for y in range(len(data)) for x in range(len(data[y])) if data[row-y-1][x] < 120 ]

    plotting.plot(S, max(yCenter * 1.5, xCenter * 1.5), 1)
    
    

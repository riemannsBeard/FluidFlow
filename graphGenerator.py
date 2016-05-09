from matplotlib import pyplot
import numpy 
import h5py

hFile = h5py.File('./logFiles/output.hdf5','r')
dataP = hFile.get("P")
dataU = hFile.get("U")
dataV = hFile.get("V")
pArray = numpy.array(dataP)
uArray = numpy.array(dataU)
vArray = numpy.array(dataV)

x = numpy.linspace(0,2,pArray.shape[1])
y = numpy.linspace(0,2,pArray.shape[2])
X,Y = numpy.meshgrid(x,y)

pyplot.figure(1)
pyplot.subplot(111)
pyplot.contourf(X, Y, pArray[pArray.shape[0]-99])
pyplot.subplot(111)
pyplot.quiver(X, Y, uArray[uArray.shape[0]-99], vArray[vArray.shape[0]-99])	
ax = pyplot.gca()
pyplot.show();

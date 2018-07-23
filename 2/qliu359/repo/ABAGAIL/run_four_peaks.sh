#!/bin/bash
# edit the classpath to to the location of your ABAGAIL jar file
#
export CLASSPATH=./ABAGAIL.jar:$CLASSPATH

# four peaks
echo "Four Peak"
javac -cp ABAGAIL.jar:. FourPeaksTest.java
java -cp ABAGAIL.jar:. FourPeaksTest
python plot.py FourPeaks.txt
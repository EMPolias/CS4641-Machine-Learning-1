#!/bin/bash
# edit the classpath to to the location of your ABAGAIL jar file
#
export CLASSPATH=./ABAGAIL.jar:$CLASSPATH

# traveling salesman
echo "Traveling Salesman"
javac -cp ABAGAIL.jar:. TravelingSalesmanTest.java
java -cp ABAGAIL.jar:. TravelingSalesmanTest
python plot.py TravelingSalesman.txt

# flip flop
echo "Flip Flop"
javac -cp ABAGAIL.jar:. FlipFlopTest.java
java -cp ABAGAIL.jar:. FlipFlopTest
python plot.py FlipFlop.txt

# four peaks
echo "Four Peak"
javac -cp ABAGAIL.jar:. FourPeaksTest.java
java -cp ABAGAIL.jar:. FourPeaksTest
python plot.py FourPeaks.txt

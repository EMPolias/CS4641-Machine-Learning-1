#!/bin/bash
# edit the classpath to to the location of your ABAGAIL jar file
#
export CLASSPATH=./ABAGAIL.jar:$CLASSPATH

# flip flop
echo "Flip Flop"
javac -cp ABAGAIL.jar:. FlipFlopTest.java
java -cp ABAGAIL.jar:. FlipFlopTest
python plot.py FlipFlop.txt
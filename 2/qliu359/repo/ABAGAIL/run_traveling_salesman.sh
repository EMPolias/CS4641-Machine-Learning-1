#!/bin/bash
# edit the classpath to to the location of your ABAGAIL jar file
#
export CLASSPATH=./ABAGAIL.jar:$CLASSPATH

# traveling salesman
echo "Traveling Salesman"
javac -cp ABAGAIL.jar:. TravelingSalesmanTest.java
java -cp ABAGAIL.jar:. TravelingSalesmanTest
python plot.py TravelingSalesman.txt
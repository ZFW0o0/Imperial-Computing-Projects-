traffic: main.o time.o trafficLight.o
	g++ -g main.o time.o trafficLight.o -o traffic

main.o: main.cpp trafficLight.h time.h
	g++ -Wall -g -c main.cpp

time.o: time.cpp time.h
	g++ -Wall -g -c time.cpp

trafficLight.o: trafficLight.cpp trafficLight.h
	g++ -Wall -g -c trafficLight.cpp

clean:
	rm -f *.o traffic



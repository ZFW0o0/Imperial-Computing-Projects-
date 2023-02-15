/* main.cpp - for MSc Computing C++ Assessed Exercise 2.  */

#include <iostream>
#include "trafficLight.h"
#include "time.h"

using namespace std;

int main()
{
	cout << "==========================\n"
	     << "Roads open in Sleepy Town:\n"
	     << "==========================\n";

	/* (a) initialise the time: */
	Time timeZero(0,0,0);
	TrafficLight::setTheTime(timeZero);						// event (a) completed


	/* (b) create a pair of traffic lights with delays 15 minutes and 5 minutes
	   respectively:                                                             */
	cout << "\nA pair T1 and T2 of (slow) collaborating lights is set up:\n";
	char  T1Name[]="T1 (North South)";
	char  T2Name[]="T2 (East West)";
	Time delayT1(0, 15, 0);
	Time delayT2(0, 5, 0);
	TrafficLight  LightT1(delayT1, T1Name);
	TrafficLight  LightT2(delayT2, T2Name, LightT1);		// event (b) completed


	/* (c)-(f) begin the simulation with 4 car crossings: */
	LightT1.carWantsToCross();								// event (c) completed
	LightT2.carWantsToCross();								// event (d) completed
	LightT1.carWantsToCross();								// event (e) completed
	LightT2.carWantsToCross();								// event (f) completed


	/* (g) create another pair of traffic lights with extra long delays of
	 6hrs, 15mins, 44secs and 14hrs, 5mins, 57secs respectively:                 */
	cout << "\nA new pair T3 and T4 of (very slow!) collaborating lights is now set up:\n";
	char  T3Name[]="T3 (North South)";
	char  T4Name[]="T4 (East West)";
	Time delayT3(6, 15, 44);
	Time delayT4(14, 5, 57);
	TrafficLight  LightT3(delayT3, T3Name);
	TrafficLight  LightT4(delayT4, T4Name, LightT3);		// event (g) completed


	/* (h)-(m) continue the simulation with 6 more car crossings:             */
	LightT3.carWantsToCross();								// event (h) completed
	LightT3.carWantsToCross();								// event (i) completed
	LightT4.carWantsToCross();								// event (j) completed
	LightT4.carWantsToCross();								// event (k) completed
	LightT3.carWantsToCross();								// event (l) completed
	LightT4.carWantsToCross();								// event (m) completed

	cout << "\n===================================\n"
	     << "Roads close forever in Sleepy Town.\n"
	     << "===================================\n";

	return 0;
}


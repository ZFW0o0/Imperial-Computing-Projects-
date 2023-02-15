/* trafficLights.h - header file for the class trafficLights */

#ifndef TRAFFICLIGHT_H
#define TRAFFICLIGHT_H

#include "time.h"
#include <cstring>

using namespace std;

/*********************** Class TrafficLight ***************************/

class TrafficLight {

public:
	
  TrafficLight(Time,char*);
  TrafficLight(Time,char*,TrafficLight&); 
		 
  void carWantsToCross();
  static void setTheTime(Time&);
       	
  friend std::ostream& operator << (std::ostream&, TrafficLight*);

private:

  /* add members and operations to complete the class yourself */
  // global clock
  static Time currentTime;
 
  // delay time of a traffic light.
  Time delayTime;
 
  // traffic light name
  char* name;
 
  // define a Colour data type that represents the colour status a traffic light can have.  
  enum Colour {Green, Yellow, Red};
 
  // the colour of the traffic light at the time point specified by currentTime.  
  Colour currentColour;
 
  // the collaborating light of this traffic light instance
  TrafficLight* collabLight; 
 
  // method to set collabLight if not defind during instantiation
  void setCollabLight(TrafficLight*);
 
  // method to to change currentColour of the traffic light to the Colour specified by the argument
  void changeColourReq(Colour);
 
};

#endif



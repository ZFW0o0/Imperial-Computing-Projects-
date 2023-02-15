#include <iostream>
#include "trafficLight.h"

using namespace std;

//instantiating a global clock that keeps track of the time 
Time TrafficLight::currentTime;

/*definition for TrafficLight constructor with 2 arguments 
initial colour of the traffic light set to red
*@param delayTime: the time which a traffic light has to wait
before it turns from one colour to an other
*@param name: unique name given to a traffic light, e.g., T1 (North South)
*/
TrafficLight::TrafficLight(Time delayTime,char* name):
  delayTime(delayTime), name(name){

  currentColour = Red;

}

/*definition for TrafficLight constructor with 3 arguments 
initial colour of the traffic light set to red
*@param delayTime: the time which a traffic light has to wait
before it turns from one colour to an other
*@param name: unique name given to a traffic light, e.g., T1 (North South)
*@param collabL: the collaborating light of this TrafficLight instance
*/
TrafficLight::TrafficLight(Time delayTime,char* name, TrafficLight& collabL):
  delayTime(delayTime), name(name), collabLight(&collabL){
  collabL.setCollabLight(this);
  currentColour = Red;
}


/*member function that is called when a car signals that it want to cross,
traffic light  changes colour (or do not change colour) depending on 
the colour status of the traffic light and the colour status of the collaborating light
*/
void TrafficLight::carWantsToCross(){
  
  /* when a car crosses a traffic light that is green, the car crosses the traffic light straight away,
  so nothing needs to be done, simply print out the car crossing information to the screen. 
  */
  if (this->currentColour == Green){
    cout << "\n***  at " << currentTime << " a car wants to cross light " << this
	 <<", with colour: green" << endl;
  } 

   /* when a car crosses a traffic light that is red, check the colour status of the collaborating light,
   if the collaborating light is green, request the collaborating light to turn to green, 
   if the collaborating light is red, then the light will turn yellow and then green.
  */
  if (this->currentColour == Red){
    cout << "\n***  at " << currentTime << " a car wants to cross light " << this
	 <<", with colour: red" << endl; 
    
    if (collabLight->currentColour == Green){
      collabLight->changeColourReq(Red);
    }

    if (collabLight->currentColour == Red){
      this->changeColourReq(Green);
    }
  }
}

// time setter to set up global clock
void TrafficLight::setTheTime(Time& t){
  
  currentTime = t;

}

// overloading insertion operator so "cout << TrafficLight instance" will print the name of the light
std::ostream& operator << (std::ostream& out, TrafficLight* trafficLight){
  
  out << trafficLight->name;
  return out;

}

/*setter to define the member attribute "collabLight" of a TrafficLight instance 
if the collabLight is not specified during instantiation of the TrafficLight, i.e., 
instantiation using constructor TrafficLight(Time,char*); 

*@param cl: pointer to the trafficlight which will be set to be the collaborating light. 
*/
void TrafficLight::setCollabLight(TrafficLight* cl){

  collabLight = cl;
 
}

/*this method is called when this light is requested to turn green or red,
the method augments the global clock everytime a traffic light delays. 
colour status of traffic lights and exact time printed to the screen, 
everytime a traffic light changes colour.
the receiver of this method can be either this light or the collaborating light of this light.

*@param clr: the colour that this traffic light is requested to change to, either red or green. 
 */
void TrafficLight::changeColourReq(Colour clr){

  if (clr == Red){

    if (this->currentColour == Green){
      currentTime.add(this->delayTime);
      currentColour = Yellow;
      cout << "     at " << currentTime << " " << this << " changes colour to yellow" << endl; 
      collabLight->changeColourReq(Green);
    }

    if (this->currentColour == Yellow){
      currentTime.add(this->delayTime);
      currentColour = Red;
      cout << "     at " << currentTime << " " << this << " changes colour to red" << endl;
      collabLight->changeColourReq(Green);
    }
    if (this->currentColour ==  Red){
       collabLight->changeColourReq(Green);
    }
  }

  if (clr == Green){
    
    if (this->currentColour == Red){
      currentTime.add(this->delayTime);
      currentColour = Yellow;
      cout << "     at " << currentTime << " " << this << " changes colour to yellow" << endl;
      collabLight->changeColourReq(Red);
    }

    if (this->currentColour == Yellow){
      currentTime.add(this->delayTime);
      currentColour = Green;
      cout << "     at " << currentTime << " " << this << " changes colour to green" << endl;
    }
  }
}

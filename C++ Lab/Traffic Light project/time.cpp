#include <iostream>
#include "time.h"

using namespace std;

// default constructor.  
Time::Time()
  :theHour(0),theMins(0),theSecs(0){};

Time::Time(int hours, int mins, int secs)
  :theHour(hours), theMins(mins), theSecs(secs){};

/*member function to update the global clock when there is a delay in a traffic light, the updating is 
simply adding the Time instance before delay and the traffic light delay time instance*/
void Time::add(Time& anotherTime){
  theHour = (theHour + anotherTime.theHour + (theMins + anotherTime.theMins + (theSecs + anotherTime.theSecs)/60)/60)%24;
  theMins = (theMins + anotherTime.theMins + ((theSecs + anotherTime.theSecs)/60))%60;
  theSecs = (theSecs + anotherTime.theSecs)%60;
}

// overloading insertion operator so "cout << time instance" outputs a digital form of time, e.g., 11:15:34  
std::ostream& operator << (std::ostream& out, Time& t){
  out << t.theHour << ":" << t.theMins << ":" << t.theSecs;

  return out;
}



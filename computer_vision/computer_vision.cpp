#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <windows.h>

		//min + (rand() % (int)(max - min + 1))

using namespace std;
int main(){
	bool someCondition = true;
	int timeout = 1, min = 5, max = 10;
	string gestures[4] = {"shrug", "waving", "crossedArms", "dancing"};
	ifstream infile; string line;
	ofstream outfile;

	outfile.open("computerVision.txt");

	while(someCondition){

		//process images, create a vec3 of head position
		int yaw = (rand() % (int)(180+ 1));

		int pitch = (rand() % (int)(180+ 1));
		outfile << yaw << " " << pitch;

		//recognise gesture
		outfile << " " << gestures[(rand() % (int)(4))] << endl;

		//check for end flag and (conditionally) exit loop
		infile.open("finishFlag.txt");
		if(infile.is_open()){
		  getline(infile, line);
		  infile.close();
		  if(line == "end"){
		    someCondition = false;
		    cout << "end";
		  }
		}

		//time until next gesture, etc.
		timeout = min + (rand() % (int)(max - min + 1));
		Sleep(timeout*1000);
	}

	outfile.close();

	return 0;
}


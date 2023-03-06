#include "DllHeader.h"
#include "variable.h"
#include "math.h"

void SignalGenerator() {			   
	Time_10 = 0;
}

void InitController() {			   
	
}

void InitINV() {			   
	
}

DLLEXPORT void plecsSetSizes(struct SimulationSizes* aSizes)
{
	aSizes->numInputs = 22;
	aSizes->numOutputs = 100;
}


//This function is automatically called at the beginning of the simulation
DLLEXPORT void plecsStart(struct SimulationState* aState)
{

}


//This function is automatically called every sample time
//output is written to DLL output port after the output delay
DLLEXPORT void plecsOutput(struct SimulationState* aState)
{

	//INPUT
	Vdc_load = aState->inputs[0]; 
	Vdc_source = aState->inputs[1]; 
	MIN_TIME = aState->inputs[2];
	// x = aState->inputs[n];


	INV_on = aState->inputs[20];
	Tsamp = aState->inputs[21];  //Fixed Tsamp


	if (init == 0) {
		SignalGenerator();
		INV_Vdc_load = 1/Vdc_load;
		INV_Vdc_source = 1 / Vdc_source;
		init = 1;
	}

	// Duty making
	if (INV_on) {
		Time += Tsamp;
		Time_10 = 10 * Time;
		if ((Time_10 - floor(Time_10)) < 0.5) {
			Duty = floor(Time_10) * 0.1;
		}
		else if ((Time_10 - floor(Time_10)) >= 0.5) {
			Duty = (floor(Time_10) * 0.1)+0.05;
		}

		if (Duty < 0.05) {
			Duty = 0;
		}
		else if (Duty > 0.95) {
			Duty = 1;
		}
	}
	else {
		Duty = 0.5;
	}


		
	//OUTPUT
	aState -> outputs[0] = Duty;
	
	// aState->outputs[n] = x ;
	











	
}






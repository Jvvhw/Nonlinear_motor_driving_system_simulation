#include "DllHeader.h"
#include "variable.h"
#include "math.h"

void SignalGenerator() {			   
	Time_10 = 0;
	Integral_Reset = 0;
	Integral_Signal = 0;
	prev_duty = 0;
	Vp_avg = 0;
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
		prev_duty = Duty;   

		if (Time - Duty > step_size) {   
			Duty += step_size;   
			if (prev_duty != Duty) {   
				Integral_Reset = 1;   
			}
		}
		else {   
			Integral_Reset = 0;  
		}

		if ((Time - Duty > 0.01) && (Time - Duty < 0.04)) {
			Integral_Signal = 1;
		}
		else {
			Integral_Signal = 0;
		}

	}
	else {
		Duty = 0.5;
	}

	//OUTPUT
	aState->outputs[0] = Duty;
	aState->outputs[1] = Integral_Signal;
	aState->outputs[2] = Integral_Reset;
	
	// aState->outputs[n] = x ;
	











	
}






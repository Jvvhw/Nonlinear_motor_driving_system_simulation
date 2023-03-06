# nonlinear_motor_driving_system_simulation
 Development of ANN-based simulation model for nonlinear motor driving system

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- ABOUT THE PROJECT -->
<h2 id="about-the-project"> :pencil: About The Project</h2>

<p align="justify"> 

 - Existing motor driving inverter simulation is modeled to linear-time-invariant system, which can not verify various non-linear feature of motor. 

 - ANN(artificial-neural-network) has a degree of freedom in setting input/output signals, so it is suitable for implementing nonlinear system. 

 - Therefore, an analysis of the factors that affect voltage output in existing inverter systems (power electronics) should take precedence, and a comprehensive understanding and utilization of deep learning theory is necessary.

 - In this project, the inverter output voltage of the motor drive system will be simulated with ANN.

 - verify through experiments that the proposed ANN simulation method can have higher accuracy than existing linear models.

</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<h2 id="project-files-description"> :floppy_disk: Files Description</h2>

<ul>
  <li><b>pptx</b> - study about the factors that affect voltage output in system</li>
  <li><b>Data2plot.py</b> - visualization voltage, duty, current data files from simulation</li>
  <li><b>main.c</b> - DLL code for running plecs simulation</li>
  <li><b>variable.h</b> - variable for main.c and general purpose define</li>
  <li><b>.plecs</b> - S/W based simulation</li>
</ul>

<h3>References</h3>
<ul>
  <li><b>Kim J -S , Choi J -W , Sul S -K . "Analysis and Compensation of Voltage Distortion by Zero Current Clamping in Voltage-Fed PWM Inverter" 電氣學會論文誌. D : 160-165.</b>
  
  <li><b>Kim Dongouk,Kwon Yong-Cheol,Sul Seung-Ki,Kim Jang-Hwan,Yu Rae-Sung. "Suppression of Injection Voltage Disturbance for High-Frequency Square-Wave Injection Sensorless Drive With Regulation of Induced High-Frequency Current Ripple" IEEE transactions on industry applications : 302-312.</b>
  
  <li><b>Murai, Y., Riyanto, A., Nakamura, H., & Matsui, K. (1992). PWM strategy for high frequency carrier inverters eliminating current clamps during switching dead-time. Conference Record of the 1992 IEEE Industry Applications Society Annual Meeting, 317-322 vol.1.</b>
</ul>

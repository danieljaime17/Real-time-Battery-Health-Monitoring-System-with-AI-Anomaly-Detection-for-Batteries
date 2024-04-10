# Real-time-Battery-Health-Monitoring-System-with-AI-Anomaly-Detection-for-Vehicle-Batteries

The system comprises a device that continuously monitors the voltage level, regardless of the vehicle's operating state: rest mode, start-up mode, and running mode. These data undergo filtering processes, preparing them for storage in a dataframe for subsequent analysis. The system labels the data based on voltage levels, such as:

## Start-up mode
This dataset comprises a small set of data, specifically the seconds during which the vehicle attempts to start. It is expected that the signal transitions from a stable level of approximately 12.5V to around 9.5V at the peak of maximum power, with a subsequent rise at the end of the signal as the battery enters a partially charged state after the vehicle is started.


## Rest mode
These data consist of voltage values that are slightly stable initially but gradually decrease over time due to the ongoing operation of control devices, even when the vehicle is turned off. These data can identify anomalies such as parasitic currents affecting the vehicle during rest mode. Additionally, this dataset is the largest among the three states. It's worth noting that the control device used in this project includes a temperature sensor, crucial for monitoring battery levels, especially when the vehicle is off, as temperature fluctuations can drastically reduce battery levels.


## Running mode
This dataset also exhibits slight stability, albeit less than that of the rest mode, as the battery voltage is negatively affected by various vehicle control devices and positively influenced as the alternator charges the battery.


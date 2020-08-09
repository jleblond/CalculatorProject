# COMP 354 Project - `ETERNITY`

## Motivation:
ETERNITY is a team project spanning over the Summer 2020 semester. Indeed, the goal of this project is to create a calculator and develop multiple iterations while applying the knowledge we have acquired from COMP 354 (Introduction to Software Engineering).

## Description:
ETERNITY is designed to be able to perform basic arithmetic, including addition, subtraction, multiplication, and division, as well as incorporate some of the most widely used transcendental functions.


## Installation:
Steps to run the project on Windows:
1. Run the 'Team-F_ETERNITY.exe' file by double-clicking it.
2. If, for whatever reason (say firewall), you cannot run the 'Team-F_ETERNITY.exe' file by simply double-clicking it,
   try to right-click the file and select 'Run as Administrator'.

A calculator GUI should appear (note: If you are on a MacOS system in dark mode, the calculator may not appear correctly).
To use the calculator, click on the desired number and/or function buttons in the appropriate order to perform a calculation. 

## How to use: 
For example, to perform 15^10, select the following buttons "pow(", "15", ",", "10", ")", "=". The calculator works like programming
a function, so a simple power would read "pow(15, 10)", or a simple sine would read "sin(5)".

The result and history of the performed calculations will appear on the right-hand side of the UI. 
When testing out any given task, it is important to use the input buttons provided by the calculator or input the values manually through the keyboard. 
Please avoid using copy-paste as it will cause unwanted results.  

Below are some examples of the tasks to be performed:
1. Calculate the following value: (15^12 + 0.78^3 ) * 5^(−0.2)
2. Calculate the following value: 10^10 * 10^(−0.2) − 10^2 
3. Calculate the following value: cosh(0.1 + (2 * cosh(3))) + 5 
4. Calculate the following value: MAD[(0, 9, 17, 22, 35, 48, 52, 60, 86, 104)] 
5. Calculate the following value: log10(254.2) * log10(0.0054) − log10(1000) 
6. Calculate the following value: StandardDeviation[(87, 68, 79, 42, 61, 93, 75, 54, 52, 51, 20, 67)]
7. Calculate the following value: sin(pi/4)

## Features


## Screenshots


## Design
`TODO`

### Implementation

### `Calculator` sub-package
#### `Calculator` module
+ contains the `Calculator` class. Keeps track of the last response
#### `Transcendental` module
+ contains the transcendental functions

### `MathHelper` sub-package
#### `MathHelper` module
+ contains all other math functions that are used to calculate transcendental functions

### `GUI` sub-package
`TODO`

### `Logger` sub-package
`TODO`



## Tests
Instructions to run all unit tests:
```
$ python -m unittest discover tests
```

## Members:
| Name | Assigned function |
|---|---|
|William Chack Suen Kang| 10^x|
|Kyungjin Kim| Hyperbolic Function|
|Andrew Korolus| x^y|
|Jeffrey Lam Yuk Tseung| MAD|
|Alexis Laurens Renner| log10(x)|
|Jasmine Leblond-Chartrand| Standard Deviation|
|Roman Lewandowski| sin(x)|

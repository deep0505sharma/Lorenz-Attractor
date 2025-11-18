# 📜 Decription
The Lorenz attractor is a set of chaotic solutions to a simplified system of three ordinary differential equations that model atmospheric convection. Its most famous characteristic is the "butterfly effect," where tiny changes in initial conditions lead to dramatically different outcomes over time. When plotted in 3D, the solutions form a complex, butterfly-like shape known as a "strange attractor". 
The Lorenz attractor is a set of chaotic solutions to a system of ordinary differential equations called the Lorenz system. First studied by Edward Lorenz with the help of Ellen Fetter, who developed a simplified mathematical model for atmospheric convection. The model is a system of three ODEs:

--------
$$
\frac{dx}{dt} = \sigma (y - x)
$$

$$
\frac{dy}{dt} = x(\rho - z) - y
$$


$$
\frac{dz}{dt} = xy - \beta z
$$

-------
The state variables are x, y and z. The rate at which states are changing is denoted by dx/dt, dy/dt and dz/dt respectively. The constants σ, ρ and β are the physical parameters.

***A chaotic system***: The Lorenz system is a classic example of a deterministic chaotic system, meaning its behavior is not random but extremely sensitive to its starting point.

***The butterfly effect***: This sensitivity to initial conditions is the origin of the term "butterfly effect," the idea that a butterfly flapping its wings in one place could, over time, influence weather patterns elsewhere.

***The butterfly shape***: The "attractor" part of the name refers to the fact that while the paths of the solutions are chaotic, they remain confined to a specific, bounded region of space, creating the iconic butterfly or figure-eight shape.

***How it works***: The system is defined by three equations for the rate of change of variables (x, y, and z) over time. For certain parameter values, the variables oscillate, with the path jumping from one "lobe" of the butterfly to the other in a complex, but bounded, pattern.

***Applications***: Originally designed to model weather, the Lorenz attractor is now a foundational concept in chaos theory and is used to study chaotic behavior in various scientific fields. 

In addition to this, I have also simulated [Rabinovich Fabrikant](https://en.wikipedia.org/wiki/Rabinovich%E2%80%93Fabrikant_equations) Attractor using RK4 method as well. 

# 📒 Runge-Kutta Method
The [Runge-Kutta](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods) method is a family of numerical methods for solving initial-value problems for ordinary differential equations (ODEs). It is more accurate than simpler methods like Euler's method because it calculates multiple weighted slopes within each step instead of just one. The most common version, the fourth-order Runge-Kutta method (RK4), uses four slopes to get a very good approximation of the next value without needing high-order derivatives. 

## ❄️ How it works 
_**Approximates the slope**_: Instead of a single slope, it calculates four different slopes over a step:

* `k₁`: The slope at the beginning of the interval.
* `k₂`: The slope at the midpoint, using `k₁` to estimate the value at the midpoint.
* `k₃`: The slope at the midpoint, using `k₂` to estimate the value at the midpoint.
* `k₄`: The slope at the end of the interval.
  
_**Creates a weighted average**_: It combines these four slopes into a weighted average to find a more accurate estimate of the next value. For the RK4 method, this is a specific weighted average:   **1/6 (k₁ + 2k₂ + 2k₃ + k₄)**.

_**Moves to the next step**_: This weighted average is then used to find the value of the next step, yₙ₊₁.

### Slopes used by the classical Runge-Kutta method
<img width="330" height="330" alt="Image" src="https://github.com/user-attachments/assets/2caf395b-350d-4d49-a0f7-badac5cda434" />

# 💻 Tech Stack
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Pillow](https://img.shields.io/badge/Pillow-%23000000.svg?style=for-the-badge&logo=Pillow&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

***Python*** : The complete project is written in python programming language.

***Pillow*** :  Powerful and user-friendly Python library for image processing and manipulation.

***Numpy*** : To work with matrices.

***matplotlib*** : Plotting library for python, used to plot figures.  

***Visual Studio Code*** : Editor used in the project.

# 📦 Getting Started / Setup

1. Clone this repository.

```javascript
  git clone https://github.com/deep0505sharma/Lorenz-Attractor.git
```  

2. Open the cloned directory in VS code & Install the given requirements in terminal one-by-one, using following commands-

```javascript
  pip3 install jupyter

  pip3 install pillow

  pip3 install numpy

  pip3 install matplotlib
```
3. Run the following commands in python, one-by-one -
------
```bash
  python3 Lorenz_3D.py
```
------
### Output-generated
<img width="600" height="500" alt="Image" src="https://github.com/user-attachments/assets/603d5836-9b88-4c2e-853d-d57b45a95ba1" />

-------
```bash
  python3 Lorenz_RK_Animated.py
```
-------
 ### Output-generated
![Image](https://github.com/user-attachments/assets/7bc335c8-6e56-4b73-854b-890ea62abe7b)

-------
```bash
  python3 Rabinovich_Fabrikant_Animated.py
```
-------
 ### Output-generated
![Image](https://github.com/user-attachments/assets/d2943702-652a-4e40-8f99-fec87fac65a7)

# 🐛 Bug Reporting
Feel free to [open an issue](https://github.com/deep0505sharma/Lorenz-Attractor/issues) on GitHub if you find bugs.

# 👨‍💻 Author

**Deepak Sharma**
- GitHub: [@deep0505sharma](https://github.com/deep0505sharma)
- LinkedIn: [Love to connect with you](https://www.linkedin.com/in/deepak-sharma-40a8781b8/)
- Email: [Contact me](mailto:ds8407205@gmail.com)
 

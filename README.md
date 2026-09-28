# Numerix – An Algorithmic Scientific Calculator Engine

## Overview

Numerix is a simple, menu-driven calculator program built in Python for my course project. It runs in the console and lets the user choose between three types of operations — basic arithmetic, trigonometry (for a fixed set of standard angles), and factorial. The whole idea behind this project was to practice loops, conditionals, functions, and recursion by actually building something useful instead of just doing separate small exercises for each topic.

It's not meant to replace a real scientific calculator — there's no external math library being used on purpose, everything is done using plain Python logic so that the working of each operation is visible and easy to understand.

## Features

- **Arithmetic operations:** addition, subtraction, multiplication, division, floor division, modulus (division by zero is handled with a proper message instead of crashing)
- **Trigonometry:** sin, cos and tan values for the standard angles 0°, 30°, 45°, 60° and 90° (the values are returned as exact fractions/expressions like `1/2`, `(3**0.5)/2` instead of decimal approximations, since no math module is used)
- **Factorial:** calculates the factorial of a number using a recursive function
- **Menu-driven interface:** the program keeps asking the user if they want to perform another calculation, so multiple calculations can be done in one run without restarting the program
- **Basic input validation:** invalid operators/angles are caught and a message is shown instead of the program crashing

## Technologies / Tools Used

- **Language:** Python 3
- **Concepts used:** while loops, if-elif-else chains, functions, recursion, list membership checks (`in` operator), basic string formatting
- **No external libraries** — this was intentional, to keep everything built from scratch using core Python only
- **Editor used:** VS Code
- **Version control:** Git & GitHub

## How to Install & Run

1. Make sure Python 3 is installed on your system. You can check by running:
   ```
   python --version
   ```
2. Clone this repository or just download the `Numerix_Project.py` file.
3. Open a terminal in the folder where the file is saved.
4. Run the program with:
   ```
   python Numerix_Project.py
   ```
5. Follow the on-screen prompts — type `yes` to perform a calculation, pick a category (Arithmetic / Trigonometry / Factorial), then enter the operator and values it asks for.
6. When you're done, type anything other than `yes` (e.g. `no`) at the prompt to exit — it'll print a thank-you message and close.

## Instructions for Testing

There's no automated test suite for this project (see the "Future Enhancements" section of the project report) — testing was done manually by running the program and trying different inputs. To test it yourself, try things like:

- A normal arithmetic operation, e.g. operator `+`, first number `10`, second number `5` → should print `Result: 15.0`
- Division by zero, e.g. operator `/`, `10` and `0` → should print `Undefined (division by zero).` instead of crashing
- A valid trig case, e.g. `sin(A)` with angle `30` → should print `Result:1/2`
- An invalid trig angle, e.g. `sin(A)` with angle `20` → should print the "only allowed" message
- Factorial, e.g. operator `C!` with `5` → should print `Result: 120`
- An invalid operator, e.g. typing `xyz` → should print `Invalid operator`
- Answering `no` at the very first prompt → program should exit immediately

## Screenshot
![image alt](https://github.com/birajaprasadmishra075-collab/Cs-project-/blob/7696d3b31d1a695dce2620cacb4312d202608ba2/Code1.png)
![image alt](https://github.com/birajaprasadmishra075-collab/Cs-project-/blob/7696d3b31d1a695dce2620cacb4312d202608ba2/Code2.png)
![image alt](https://github.com/birajaprasadmishra075-collab/Cs-project-/blob/7696d3b31d1a695dce2620cacb4312d202608ba2/Code3.png)
![image alt](https://github.com/birajaprasadmishra075-collab/Cs-project-/blob/7696d3b31d1a695dce2620cacb4312d202608ba2/Output.png)
## Known Limitations

- The whole program currently lives in a single file rather than separate modules — the plan to split it up is noted under "Future Enhancements" in the project report.
- Trigonometry only works for the five standard angles, not any arbitrary angle.
- Factorial doesn't check for negative input.



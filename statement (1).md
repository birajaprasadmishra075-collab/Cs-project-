# Project Statement – Numerix: An Algorithmic Scientific Calculator Engine

## Problem Statement

Most people just use their phone's calculator app or type sums into a search engine, which is fine for everyday use but doesn't really show *how* a calculator actually works behind the scenes. As a student, I wanted to understand how simple mathematical operations — arithmetic, trigonometry and factorial — could be handled step by step using just core programming logic (loops, conditionals, functions and recursion), without relying on any built-in math library to do the heavy lifting.

So the problem I set out to solve was: **build a menu-driven scientific calculator in Python that can perform basic arithmetic, give trigonometric values for standard angles, and calculate factorials — all using fundamental programming concepts rather than external libraries.**

## Scope of the Project

This project is a **console-based** calculator, not a GUI or web app. It's meant to be a learning-focused tool rather than a production-grade calculator, so the scope is intentionally kept small and focused:

- Covers three categories of operations: arithmetic, trigonometry (limited to standard angles), and factorial
- Runs as a single Python script that the user interacts with through the terminal
- Handles one calculation at a time, then loops back and asks if the user wants to do another
- Does basic error handling (like division by zero and invalid operator/angle input) but doesn't aim to cover every possible edge case
- Does **not** include a graphical interface, does **not** store any calculation history, and does **not** use any external math/scientific library

## Target Users

- Also usable by **beginner Python learners** who want a simple example of how loops, conditionals and recursion can come together in one working program
- Anyone who just wants to do a quick calculation from the terminal without opening a full calculator app

## High-Level Features

- Menu-driven loop that keeps running until the user chooses to stop
- Category selection: Arithmetic / Trigonometry / Factorial
- Arithmetic operations: `+`, `-`, `*`, `/`, `//`, `%`
- Trigonometric values (as exact expressions, not decimals) for angles 0°, 30°, 45°, 60°, 90° using `sin(A)`, `cos(A)`, `tan(A)`
- Factorial calculation using a recursive function
- Basic input validation with friendly error messages instead of the program crashing

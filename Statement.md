# Problem Statement — NutriFit

## Problem Statement
Most people don't have one simple place to check their BMI, BMR, TDEE and Body Fat Percentage
together — they usually have to look up each one on a different website. Also, a lot of those
calculators just show a number without saying what it means (like whether the BMI is healthy or
not). NutriFit is a simple Python program that puts all four calculations in one menu and also
tells the user what their BMI result means.

## Scope of the Project
- Covers four calculations: BMI, BMR, TDEE, and Body Fat Percentage.
- Runs in the terminal only — no GUI, no database.
- Doesn't save any data between runs — everything resets when you close the program.
- Just a simple personal calculator, not meant to replace actual medical advice.

## Target Users
- Anyone who wants a quick way to check basic health numbers without searching multiple
  websites.
- Students or fitness beginners who want to understand how these numbers are actually
  calculated.

## High-Level Features
- One menu to access all four calculators.
- BMI result comes with a simple label (Underweight / Healthy weight / Overweight / Obese).
- BMR calculation works differently for male and female.
- TDEE adjusts the result based on activity level (5 options).
- Body Fat Percentage works for 4 categories: Adult male, Adult female, Boy, Girl.
- Menu keeps repeating until the user chooses to exit.

## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.


## Rationale
**2.1 what refactoring signs (code smells) suggest this refactoring?**
* **Feature Envy:**
The price_code was being accessed and utilized primarily by the Rental class, 
not the Movie class. This suggests that the attribute is more relevant to Rental, 
and keeping it in Movie creates unnecessary dependencies.

**2.2 what design principle suggests this refactoring? Why?**
* **Single Responsibility Principle (SRP):**
SRP states that a class should have only one reason to change. 
The Movie class should focus solely on the details and behavior of a movie, 
while rental-specific logic, like price_code, belongs in the Rental class.

**5.2 Describe where you implement this method and the reasons for your choice.**
* **High Cohesion**
* **Information Expert**

The Rental class is responsible for managing movie rentals and contains information about 
the movie's release year, genre, and the number of days rented. This data can be used to calculate 
the rental price, determine rental points, and retrieve the price code for each movie.
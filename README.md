# Circumscribed_Circle

## Description
A program that given 3 random points on R2, validates them, graphs their lines and the circumscribed circle.

## Author:
Arnoldo Fernando Chue Sánchez

## Contact:
arnoldwork20@gmail.com

## License:
GNU General Public License v3.0

## Information about installation and execution
All the code was written in Python 3.10.7. Before cloning the repository, check if your Python version is compatible with this program.
Also, make sure to install (if you don't have them) all the modules that were used for this proyect (numpy and matplolib). 
After that, you just have to clone this repository on your local machine and run the archive named "Circumscribed_Circle.py" in the terminal of your preference.
You can run the program the number of times you want. But, it will generate different coordinate points every single time. That is the reason why I recommend saving every graph you get.

## Introduction
Triangles have multiple lines. Some of them are very useful for visualization and geometry applications. For example, altitude is useful for calculating the area of ​​a triangle. But, the line that will be helpful in this project is the perpendicular bisector.

A perpendicular bisector is a line that crosses one of the sides of the triangle at its midpoint. Also, (the bisector) is perpendicular to the side of the triangle. Therefore, since the triangle has three sides, it also has three perpendicular bisectors. Those bisectors converge at the same point: the circumcenter of the triangle. This point is fundamental because the distance between all the vertices of the triangle and the circumcenter is the same. Then, a circle is circumscribed when it is created with a radius of the mentioned distance, and its center is at the circumcenter.

Using these concepts and all the lessons in analytic geometry it is possible to find the circumscribed circle of any triangle. For this project, the corners of the triangle (the coordinate points) and its sides (segments of a straight line) are the most important components of a triangle.

## Objectives
- Create a set of functions which can construct the lines and the circumscribed circle from three random coordinate points.
- Plot the lines and circle in a good resolution and minimizing the margin of rendering error.

## Metodology

## Implementation

## Tests and results

## Conclusions
Working with random coordinate points can be hard beacause it is imposible to set a good scale for the render of all the executions. Nevertheless, the final result was a success. The render is fast and the curves are smooth enough. The margin of rendering error is close to 0.00001 between the points and the circle.
Future work can be focused on developing faster rendering tools and making statistics about the margin of rendering error

## References
1. Lehmann, C. H. (2014). Geometría analítica. Limusa.
2. Rees, P. K. (2003). Geometría analítica. Editorial Reverté.

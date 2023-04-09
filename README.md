# Computer Science I: Computational Physics (CSI 107), Muhlenberg College

## Course Description:
An introduction to Computer Science through the development of software to solve physics based problems. Emphasis is given to the implementation of models involving physics phenomena such as kinematics, the laws of motion, gravity, and momentum and energy conservation. Students learn to use basic software creation strategies, in designing and developing their physics simulations on their own and in collaboration with physics students. The course is intended for those with no prior experience in computer science but with a desire to hone problem solving and computing skills with a focus on physics. This course, in conjunction with PHY 1XX General Physics 1: Computational Physics, satisfies the IL requirement.

## Expected Course Outcomes: 
Course Outcomes are measurable achievements to be accomplished by the completion of the course. 

1.	Use problem-solving methods to develop and implement algorithms using a high-level programming language.
2.	Implement effective programs using the tools, abilities and concepts provided by Python, a widely used, structured programming language.
3.	Use features provided by science focused Python libraries such as matplotlib and scipy.
4.	Apply methods and algorithms to the basic techniques of design and implementation of physics models.
5.	Collaborate effectively with colleagues to accomplish specific goals.
6.	Design, code, debug, and document programs using good practices of programming style and structure.
7.	Adapt and apply modes of thinking from physics to better understand computer science principles, and to augment their problem-solving abilities.

## Projects:
### Project 1: Alley-oop
One of the most visually spectacular plays in basketball is the alley-oop dunk, where one player throws the ball into the air near the basket, and their teammate (or, occasionally, themselves) jumps, takes the ball in mid-air, and dunks it into the basket. Getting this play to work requires precise timing and aim for both the passer and the dunker, and while it is usually not a conscious calculation, every player that does it is using physics to figure out when and how to act. In this mini-project, you'll be more deliberately using physics to calculate how to keep an alley-oop from becoming an alley-oops. For simplicity, we will be confining ourselves to two dimensions, with the +x direction being towards the basket, and the +y direction being up.
For this project, you will be implementing a program that performs several calculations regarding the setup for an alley-oop dunk. You will need to prompt the user for the distance of the player with the ball from the hoop, in meters, the angle at which the ball is thrown, and the jumping player’s jumping speed, in meters per second. Then, assuming the jumping player is 0.375 meters from the hoop, the jumping player’s maximum reach is 2.35 meters, and that the ball is being thrown from a height of 1.5 meters, calculate the speed, in meters per second, at which the ball needs to be thrown and how long the jumping player must wait, in seconds, to catch the ball at the top of their jump for the alley-oop dunk.

### Project 2: Bad Data
Data processing is one of the most common activities that software is designed to perform. One of the largest data producers and consumers in the world is the US National Oceanic and Atmospheric Administration (NOAA). They collect data from a myriad of sensors all over the globe measuring temperature, barometric pressure, wind speed, tidal currents, and more to predict future weather patterns. However, sometimes sensors malfunction and either provide incorrect information, as seen by the temperature sensor that contributed to the Artemis I launch being scrubbed, or they fail to collect any information at all. In cases where no data is collected, interpolation can be used by selecting data that is in close proximity to the gap, taking the average of that data, and using the resulting value to fill the gap. Additionally, in order to verify that such methods are effective, if no real data is available, synthetic data can be generated that mimics the real data.
For this project, you will be creating a program that can generate and then interpolate synthetic temperature data. Your program will provide the user with a menu of options that include the ability to create a new synthetic temperature dataset of a desired size, the ability to interpolate holes in that dataset using the surrounding data or using the entire dataset, and the ability to compare the original dataset to the interpolated dataset.

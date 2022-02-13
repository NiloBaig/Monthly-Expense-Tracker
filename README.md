# Monthly-Expense-Tracker
MonthlyExpenseTracker is a Python application used to track all the expenses throughout the month.
Here a user can add his monthly income and keep a track of all the expenses occurred in the current month.
The expenses can be added in one-go using a csv file, or can be added anytime randomly.
It also shows a graphical view of the expenses throughout the month or for a given date range in a month.

## Input
User can upload a csv file with all the expenditures throughout the month, or can add it via running the program.
A sample expenses file is attached for reference.

## UML
### 1. Use case diagram
![This is an image](https://github.com/NiloBaig/Monthly-Expense-Tracker/blob/main/Use%20case%20diagram.png)
### 2. Activity diagram
![This is an image](https://github.com/NiloBaig/Monthly-Expense-Tracker/blob/main/Activity%20diagram.png)
### 3. Sequence diagram
![This is an image](https://github.com/NiloBaig/Monthly-Expense-Tracker/blob/main/Sequence%20diagram.png)

## DDD
## Metrics
[SonarCube](https://sonarcloud.io/project/overview?id=NiloBaig_Monthly-Expense-Tracker) is used to inspect the code quality and security of codebase.
  Below are the snippet of metrics:
![This is an image](https://github.com/NiloBaig/Monthly-Expense-Tracker/blob/main/Sonarcube2.PNG)
![This is an image](https://github.com/NiloBaig/Monthly-Expense-Tracker/blob/main/Sonarcube1.PNG)

## Clean Code Development
### 1. Consistent Naming Convention
snake_case convention has been followed throughout the code, for both variables as well as functions. 
All names are easy to remember, descriptive, searchable and clear.
![image](https://user-images.githubusercontent.com/99265854/153726108-9f4e0f53-ffde-4d35-ab6a-fa110e04e745.png)
### 2. Comments
Although the code is quite self-explanatory, few comments have been added to help someone understand in the plainest way possible.
![image](https://user-images.githubusercontent.com/99265854/153726211-52e9b8b9-ceb0-405b-afff-7c4fe954240b.png)
### 3. Exception handling
Try and except blocks have been added in every function to easily determine the cause and location of the error, and to make code look good.
![image](https://user-images.githubusercontent.com/99265854/153726226-3faa820e-0867-456f-85ed-f21a454ceee4.png)
### 4. Clean use of functions
Functions are kept short, with less arguments.
![image](https://user-images.githubusercontent.com/99265854/153726243-ab9c9f36-676a-4b1a-81cf-d3e5465d44b3.png)
### 5. Context Manager
To interact with the external data file, with statement is used. 
It helps in deallocating memory automatically outside of the block.
![image](https://user-images.githubusercontent.com/99265854/153726281-4b767909-af21-43dc-9def-a83d2fd7ba14.png)

## Build Management
To understand build management, Gradle is used to build a simple Java program that says Hello.
From Installation, to test and continuous delivery, Gradle helped in building the application.
![image](https://user-images.githubusercontent.com/99265854/153759666-079d39ca-b246-49d4-88a7-886ae711ef7e.png)

## Unit Tests
Unit test was also performed using Gradle on the same Java program.
![image](https://user-images.githubusercontent.com/99265854/153759699-d2650be4-0e0e-48dc-94df-f2d352c7c3e5.png)

## Continuous Delivery
Continuous Integration was implemented usig GitHub Actions, and Delivery using Gradle.
![image](https://user-images.githubusercontent.com/99265854/153759786-b45dedae-d3d8-410d-ba57-5ace530db92c.png)

## IDE
The IDE used for developing this application is PyCharm. 
Below are some of the shortcuts used as they are very handy and quick.
![image](https://user-images.githubusercontent.com/99265854/153722374-307776e8-4d11-48ce-9ede-752d23aeb750.png)

There are also some of them that are my favourites while working with Git:
![image](https://user-images.githubusercontent.com/99265854/153722483-c16bae5e-df5d-4557-9617-8f205ea086c9.png)

## DSL
Following the snippet of DOmain Specific language written in Groovy. This is used to run the Java application on Gradle.
![image](https://user-images.githubusercontent.com/99265854/153759984-15976c0c-0454-41e6-a53d-9a6b07d03123.png)

## Functional Programming
### The use of higher-order functions
The use of len() function is implemented in the code.
![image](https://user-images.githubusercontent.com/99265854/153726830-fc5b9086-27af-4650-920e-5496a538d32e.png)
### Functions as parameters and return values
This function takes the start date and the end date as input parameters to show graphical view during that time period.
![image](https://user-images.githubusercontent.com/99265854/153726877-45c01430-3c0e-4ff4-afbd-43029e8d95c2.png)
### Side effect free functions
Effect of overlying functions remains locally, hence using them will not have any side effects.
![image](https://user-images.githubusercontent.com/99265854/153726931-c46db30b-3bd1-44f5-ad83-1e487386822f.png)

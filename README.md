# SDSS Datathon - TTC Subway Delay Prediction
## Authors
* Zhe Wang
* Virat Talan
* Daivi Shah
* Euichan Kim

## Project Purpose
 The TTC serves as a lifeline for Toronto, offering millions of daily trips across streetcars, subways, and
 buses. Covering key routes from Union to Finch and Pearson Airport to the Toronto Zoo, the network plays
 a crucial role in urban mobility. However, recurring delays across various routes hinder the TTC’s ability
 to deliver consistent service. This reliability issue undermines public confidence and complicates efforts to
 promote sustainable transportation, crucial for reducing the city’s carbon footprint by encouraging fewer car
 journeys. Addressing these challenges is vital for the TTC to fulfill its mandate of providing an incentive to
 alternative transit solutions

 **Our project consists of three parts:**
 * First, our group analyzed the dataset of TTC subway delay, performing **graphical EDA with related visualizations**.
   This reveals key trends if the delays and can provide important business insights to TTC and private companies.
   (See the report)
 * Then, we used a **Random Desision Forests** Algorithm to train a machine learning model, which, given a set of information
   (Starting point, Destination, Departure Time, etc.) returns a prediction on the delay situation along with the
   perdicted probability of delay.
 * Finally, we **developed a website** that integrates with our machine learning model, enabling users to make predictions for
   their future travel super conveniently!

## Table of Contents
### 1. [Authors](#Authors)
### 2. [Project Purpose](#Project-Purpose)
### 3. [Usage Guide](#Usage-Guide)
### 3. [ML Model](#ML-Model)
### 5. [License](#License)
### 8. [How to Contribute?](#Contributions)

## Usage Guide
### Step 1:
Navigate to the website our group developed: https://datathon-pearl.vercel.app/

### Step 2:
Clone the project or download the zip file in [Our GitHub Repository](https://github.com/UofTDriv/Group157)
Open the project in your IDE.
![Image](images/github_repo.png)
### Step 3:
In **src/main/java/app**, find the file named `Main`.
Rightclick the file and click **Run** or open the file to run it.
![Image](images/project_main.png)
### Step 4:
Seeing the App displayed and you are ready to start your journey!
(See the [Software Features](#software-features) section for a tutorial of the app)

## License

Distributed under the Creative Commons Zero v1.0 Universal License. Project is dedicated to the world-wide public domain. The creators of the project (Zhe Wang, Virat Talan, Daivi Shah, Euichan Kim) disclaim responsibility for obtaining any necessary consents, permissions or other rights required for any use of this project. See LICENSE for more information.

## Contributions

How can users make a fork of this repo?
 1. Navigate to the home page of the repository
 2. In the top right of the page, click on 'Fork'
 3. Leave the 'Owner' selection as is. Change 'Repository Name' to the following format: {github username}_{fork number}, where 'fork number' specifies whether this is the first, second, third etc. fork you've made of this repo.
 4. Adding a description is not necessary
 5. Ensure that 'Copy the main branch only' is selected
 6. Click on 'Create fork'

Guidlines for creating a good merge request.
1. Write clear commit messages
2. Ensure code quality (Follow some kind of linter e.g SolarLint)
3. Appropriately use branching (i.e. create a branch when implementing a distinct feature or use case)
4. Ensure that the merge quest description is thorough
     - What does the merge request do?
     - Why are the changes necessary?
     - How were the changes implemented
5. Provide evidence of successful testing (i.e. screenshots for changes to the UI) and adequate test coverage from provided test suite (at least 90% code coverage for core logic)

Protocols for reviewing and merging contributions.
1. Automatic testing: automatic tests will be run to ensure that code in the merge request is correct and compatible with the current codebase.
2. Review. A review will be selected to review your merge request. Expect merge requests to be completed between 2 and 5 business days. Reviewers will take into consderation the aformentioned criteria/guidlines for a good merge request. 
4. Feedback. The reviewer will provide any necessary feedback regarding the request (NOTE: any merge requests NOT following these guidelines will be ignored and DELETED)
5. Approval mechanism. An additional reviewer may be called for a second opinion before merging.


### 

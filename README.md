# Google Advanced Data Analytics Employee Turnover Capstone Project

## 🚙 Project Overview
Salifort Motors is a fictional company experiencing large rate of employee turnover. I take on the role as a junior data analyst to build a machine learning model to predict when a employee would leave the company. 

Preliminary data analysis revealed that the number of projects contributed to employee stress, and exploratory data analysis was used to clean data and discover potential relationships that resulted in employee turnover. A random forest classification model was implemented as the prediction model with recall as the key metric to optimize. FastAPI app was created to test inputs for future employees.

## 📘 Executive Summary
The random forest model achieved a 0.92 recall score on the test data. The feature with the largest importances were satisfaction level, number of projects, time spent at the company, average monthly hours. It appears that employees that worked on a larger number of projects with higher hours seemed to leave the company at a higher rate than other employees. The recommended action would be for management at Salifort Motors to assess the workload undertaken by employees with larger projects and find ways to ease their responsbilities to retain a higher employee count.

<center>
<img width="557" height="357" alt="image" src="https://github.com/user-attachments/assets/4b0d89f1-72bb-436f-947c-d600e37aca59" />
</center>

## 🗒️ Python Notebook
The `salifort_motors_capstone_project.ipynb` file within the `notebooks` folder walks through the data cleaning process and modeling steps. The model performed well after hyperparameter tuning with GridSearchCV, resulting low values for false positives and false negatives.

<center>
<img width="565" height="441" alt="image" src="https://github.com/user-attachments/assets/44a95942-0bd8-403e-b403-a198e0e1adad" />
</center>

## 📘FastAPI App
The FastAPI was implemented as a method to use the model for future employees. A later dataset can be accepted by the app and show which employees are at risk of leaving the company, allowing managers and senior members to save time and resources by focusing on specific individuals rather than producing company-wide efforts.

<center>
<img width="1627" height="883" alt="image" src="https://github.com/user-attachments/assets/03c028b8-0915-40ad-b809-685516879ff8" />
</center>

## Technologies Used
- Python
- FastAPI
- Jupyter (extension)

## 🗒️ Dependencies
- ipykernel
- pandas
- numpy
- scikit-learn
- fastapi
- uvicorn
- httpx (explorations.ipynb)

## 📂 Getting Started
1. Install Python (3.12 or higher) and Anaconda Navigator
2. Install the Jupyter Notebook Extension provided by Microsoft on Visual Studio Code
3. Make a virtual environment through Anaconda Navigator to hold the project dependencies (no conflicting versions) as the extension requires a conda environent to run the ipykernel package
4. Clone the repository
```
git clone https://github.com/Cameron-Nann-Python/google-turnover-capstone.git
```
5. To run the app, use the following command:
```
uvicorn app.main:app -- reload
```

## 📂 Files Included

- `HR_capstone_dataset.csv`: csv file of employee data used for data analysis and predictive modeling
- `salifort_motors_capstone_project.ipynb`: lab notebook containing data analysis and random forest modeling to predict employee turnover
- `rf_opt.joblib`: binary version of optimal random forest model
- `capstone_project_executive_summary.pdf`: summary of key findings and recommendations to reduce employee turnover
- `main.py`: FastAPI app initialization file with home page that links to model testing
- `routes.py`: webpage containing Swagger Docs testing for model inputs
- `schemas.py`: Swagger Docs input and output classes for input and output fields
- `utils.py`: file containing input processing logic so that inputs are understood by model
- `explorations.ipynb`: notebook testing web functionality and input validation of the app
- `main_backup.py`: original app file before refactoring

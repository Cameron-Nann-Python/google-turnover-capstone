# from fastapi import FastAPI
# from pathlib import Path
# from app.routes import router

# DATA_PATH = Path("csv")
# MODEL_PATH = Path("models")

# app = FastAPI(title="Salifort Motors Employee Turover API")
# @app.get("/")
# def root():
#     return {"message": "Welcome to the Employee Turnover Prediction API"}

# app.include_router(router=router)

# # load dataset
# df = pd.read_csv(DATA_PATH / "HR_capstone_dataset.csv")

# # define inputs
# class EmployeeData(BaseModel):
#     satisfaction_level: float = Field(gt=0, le=1)
#     last_evaluation: float = Field(gt=0, le=1)
#     number_project: int = Field(gt=0)
#     average_montly_hours: int = Field(gt=0)
#     time_spend_company: int = Field(gt=0)
#     Work_accident: int = Field(ge=0, le=1)
#     promotion_last_5years: int = Field(ge=0)
#     Department: Literal['sales', 'accounting', 'hr', 'technical', 'support', 'management',
#        'IT', 'product_mng', 'marketing', 'RandD'] = Field(description="Department Category")
#     salary: Literal["low", "medium", "high"] = Field(description="Salary Category")

# # define output
# class EmployeeTurnover(BaseModel):
#     left: int 

# def preprocessing(df: pd.DataFrame):
#     # rename columns
#     df = df.rename({'Work_accident': 'work_accident',
#                   'average_montly_hours':'average_monthly_hours',
#                   'promotion_last_5years': 'promotion_last_five_years', 
#                   'Department':'department'}, axis=1)

#     # dummy encode categorical columns
#     df = pd.get_dummies(
#         df,
#         drop_first=False,
#         dtype=int
#         )

#     # reshape columns to model input
#     expected_cols = [
#         "satisfaction_level", "last_evaluation", "number_project", "average_monthly_hours", 
#         "time_spend_company", "work_accident", "promotion_last_five_years","department_RandD", 
#         "department_accounting", "department_hr", "department_management", "department_marketing", 
#         "department_product_mng", "department_sales", "department_support", "department_technical",	
#         "salary_low", "salary_medium"
#     ]

#     # drop dummy cols not in expected cols
#     for col in df.columns:
#         if col not in expected_cols:
#             df = df.drop(col, axis=1)
#     df = df.reindex(columns=expected_cols, fill_value=0)

#     return df

# router = APIRouter(prefix="/turnover")
# @router.get("")
# def read_data():
#     return df.to_dict(orient="records")

# @router.post("/predict", response_model=EmployeeTurnover)
# def predict(payload: EmployeeData):
#     predictor = pd.DataFrame(payload.model_dump(), index = [0])
#     processed_predictor = preprocessing(predictor)
#     rf_opt = joblib.load(MODEL_PATH / "rf_opt.joblib")
#     prediction = rf_opt.predict(processed_predictor)

#     return {"left": int(prediction[0])}


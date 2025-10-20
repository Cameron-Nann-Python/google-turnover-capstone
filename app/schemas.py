from typing import Literal
from pydantic import BaseModel, Field

# define inputs
class EmployeeData(BaseModel):
    satisfaction_level: float = Field(gt=0, le=1, examples=[0.73])
    last_evaluation: float = Field(gt=0, le=1, examples=[0.87])
    number_project: int = Field(gt=0)
    average_montly_hours: int = Field(gt=0)
    time_spend_company: int = Field(gt=0)
    Work_accident: int = Field(ge=0, le=1)
    promotion_last_5years: int = Field(ge=0)
    Department: Literal['sales', 'accounting', 'hr', 'technical', 'support', 'management',
       'IT', 'product_mng', 'marketing', 'RandD'] = Field(description="Department Category")
    salary: Literal["low", "medium", "high"] = Field(description="Salary Category")

# define output
class EmployeeTurnover(BaseModel):
    left: int 
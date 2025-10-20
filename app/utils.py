import pandas as pd

def preprocessing(df: pd.DataFrame):
    # rename columns
    df = df.rename({'Work_accident': 'work_accident',
                  'average_montly_hours':'average_monthly_hours',
                  'promotion_last_5years': 'promotion_last_five_years', 
                  'Department':'department'}, axis=1)

    # dummy encode categorical columns
    df = pd.get_dummies(
        df,
        drop_first=False,
        dtype=int
        )

    # reshape columns to model input
    expected_cols = [
        "satisfaction_level", "last_evaluation", "number_project", "average_monthly_hours", 
        "time_spend_company", "work_accident", "promotion_last_five_years","department_RandD", 
        "department_accounting", "department_hr", "department_management", "department_marketing", 
        "department_product_mng", "department_sales", "department_support", "department_technical",	
        "salary_low", "salary_medium"
    ]

    # drop dummy cols not in expected cols
    for col in df.columns:
        if col not in expected_cols:
            df = df.drop(col, axis=1)
    df = df.reindex(columns=expected_cols, fill_value=0)

    return df
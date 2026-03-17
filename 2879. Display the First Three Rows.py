import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    # Select the first three rows
    return employees.head(3)

import pandas as pd
import numpy as np
from scipy import stats

# Reading Excel file & turn into "Gender"
df = pd.read_excel("DATA_Kiss_count_gender_and_IQ.xlsx")
df['Gender_numeric'] = df['Gender'].map({'male': 0, 'female': 1})

# Selecting labels
variables = ['Gender_numeric', 'IQ', 'Kiss Count', 'Age of First Kiss', ]
n = len(df)

# Initializing
r_values = pd.DataFrame(index=variables, columns=variables, dtype=float)
t_values = pd.DataFrame(index=variables, columns=variables, dtype=float)
p_values = pd.DataFrame(index=variables, columns=variables, dtype=float)

for i in variables:
    for j in variables:
        if i == j:
            r = 1.0
            t = np.nan
            p = np.nan
        else:
            x = df[i]
            y = df[j]
            r, p = stats.pearsonr(x, y)
            t = r * np.sqrt((n - 2) / (1 - r**2)) if r**2 != 1 else np.inf

        r_values.loc[i, j] = r
        t_values.loc[i, j] = t
        p_values.loc[i, j] = p


# Printing results on terminal
print("=== R-values (Pearson correlation) ===")
print(r_values.round(3))
print("\n=== T-values ===")
print(t_values.round(3))
print("\n=== P-values ===")
print(p_values.round(5))

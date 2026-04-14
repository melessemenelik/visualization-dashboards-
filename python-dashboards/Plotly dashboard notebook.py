import plotly.express as px
import pandas as pd

# Sample healthcare KPI dataset
df = pd.DataFrame({
    "Department": ["Cardiology", "Oncology", "Neurology", "Pediatrics"],
    "ReadmissionRate": [0.12, 0.18, 0.10, 0.08],
    "PatientSatisfaction": [82, 76, 88, 91]
})

fig = px.scatter(
    df,
    x="ReadmissionRate",
    y="PatientSatisfaction",
    text="Department",
    size="PatientSatisfaction",
    hover_data=["Department"],
    title="Healthcare KPI Dashboard"
)
fig.show()

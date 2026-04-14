import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    "Dept": ["Cardiology", "Oncology", "Neurology", "Pediatrics"],
    "Satisfaction": [82, 76, 88, 91]
})

sns.barplot(x="Dept", y="Satisfaction", data=data)
plt.title("Patient Satisfaction by Department")
plt.show()

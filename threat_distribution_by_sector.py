import matplotlib.pyplot as plt

# Data
sectors = ["Financial Services", "Telecommunications", "Healthcare", "Utilities", "ICT Sector", "Transportation (Air/Water)"]
total_cases = [128, 106, 82, 63, 25, 24]
percentages = [31.40, 26, 20.10, 15.50, 6.10, 5.90]

# Pie chart
plt.figure(figsize=(8, 8))
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']
explode = (0.1, 0, 0, 0, 0, 0)  # Exploding Financial Services slightly for emphasis

plt.pie(
    total_cases, 
    labels=sectors, 
    autopct=lambda pct: f"{pct:.1f}%", 
    startangle=90, 
    colors=colors, 
    explode=explode
)

# Title
plt.title("Threat Distribution by Sector (Total Cases)", fontsize=14)
plt.tight_layout()

# Show plot
plt.show()

# Data Visualization Guide: Excel to Python

## Basic Chart Types and Their Uses

### 1. Bar Charts
```python
# Excel: Insert > Bar Chart
# Python:
import matplotlib.pyplot as plt
import seaborn as sns

# Basic bar chart
plt.figure(figsize=(10, 6))
plt.bar(categories, values)
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.show()

# Or with seaborn
sns.barplot(data=df, x='Category', y='Sales')
plt.show()
```

**Best Used For:**
- Comparing categories
- Showing distribution
- Ranking data

### 2. Line Charts
```python
# Excel: Insert > Line Chart
# Python:
plt.figure(figsize=(12, 6))
plt.plot(dates, values, marker='o')
plt.title('Sales Trend')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

# With pandas
df.plot(x='Date', y='Sales', kind='line')
plt.show()
```

**Best Used For:**
- Time series data
- Trends over time
- Multiple series comparison

### 3. Pie Charts
```python
# Excel: Insert > Pie Chart
# Python:
plt.figure(figsize=(8, 8))
plt.pie(values, labels=categories, autopct='%1.1f%%')
plt.title('Sales Distribution')
plt.show()
```

**Best Used For:**
- Part-to-whole relationships
- Percentage distribution
- Simple comparisons

### 4. Scatter Plots
```python
# Excel: Insert > Scatter Plot
# Python:
plt.figure(figsize=(10, 6))
plt.scatter(x_values, y_values, alpha=0.5)
plt.title('Sales vs Marketing Spend')
plt.xlabel('Marketing Spend')
plt.ylabel('Sales')
plt.show()

# With seaborn
sns.scatterplot(data=df, x='Marketing_Spend', y='Sales')
```

**Best Used For:**
- Correlation analysis
- Relationship between variables
- Pattern identification

## Advanced Visualizations

### 1. Box Plots
```python
# Python (no direct Excel equivalent)
sns.boxplot(data=df, x='Category', y='Sales')
plt.title('Sales Distribution by Category')
plt.show()
```

**Best Used For:**
- Distribution analysis
- Outlier detection
- Comparing distributions

### 2. Heat Maps
```python
# Python (no direct Excel equivalent)
correlation = df.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
```

**Best Used For:**
- Correlation matrices
- Pattern recognition
- Complex relationships

### 3. Multiple Plots
```python
# Create dashboard-style visualizations
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

# First plot
sns.barplot(data=df, x='Category', y='Sales', ax=ax1)
ax1.set_title('Sales by Category')

# Second plot
sns.lineplot(data=df, x='Date', y='Sales', ax=ax2)
ax2.set_title('Sales Trend')

plt.tight_layout()
plt.show()
```

## Styling and Customization

### 1. Colors and Styles
```python
# Set style
plt.style.use('seaborn')  # or 'ggplot', 'fivethirtyeight'

# Custom colors
colors = ['#FF9999', '#66B2FF', '#99FF99']
plt.bar(categories, values, color=colors)

# Seaborn palette
sns.set_palette("husl")
```

### 2. Annotations
```python
# Adding text and annotations
plt.annotate('Peak', xy=(x, y), xytext=(x+1, y+1),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Adding value labels
for i, v in enumerate(values):
    plt.text(i, v, str(v), ha='center')
```

### 3. Formatting
```python
# Rotate labels
plt.xticks(rotation=45)

# Format y-axis as currency
from matplotlib.ticker import FuncFormatter
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, p: f'${x:,.0f}'))
```

## Best Practices

1. **Choose the Right Chart**
   - Bar charts for categories
   - Line charts for trends
   - Scatter plots for relationships
   - Pie charts for parts of a whole (use sparingly)

2. **Keep It Simple**
   - Avoid chart junk
   - Use clear labels
   - Include titles and axes labels
   - Add legends when needed

3. **Color Usage**
   - Use consistent color schemes
   - Consider color blindness
   - Don't use too many colors
   - Use color to highlight important data

4. **Data-Ink Ratio**
   - Remove unnecessary gridlines
   - Avoid 3D charts
   - Focus on the data
   - Use whitespace effectively

5. **Interactive Elements**
   ```python
   # Using plotly for interactive charts
   import plotly.express as px
   fig = px.line(df, x='Date', y='Sales')
   fig.show()
   ```

## Saving Visualizations
```python
# Save as PNG
plt.savefig('chart.png', dpi=300, bbox_inches='tight')

# Save as PDF
plt.savefig('chart.pdf', bbox_inches='tight')
```

Remember:
- Always consider your audience
- Make charts self-explanatory
- Use consistent formatting
- Include source information when needed
- Test visualizations for clarity

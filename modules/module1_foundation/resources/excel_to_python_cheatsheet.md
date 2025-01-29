# Excel to Python Cheat Sheet

## Basic Operations

### Cell References and Variables
```excel
# Excel
A1 = 100
B1 = A1 * 2

# Python
value = 100
result = value * 2
```

### Ranges and Lists
```excel
# Excel
A1:A5 = {1,2,3,4,5}
SUM(A1:A5)

# Python
numbers = [1, 2, 3, 4, 5]
sum(numbers)
```

## Common Functions

### Mathematical Operations
| Excel | Python (Base) | Python (pandas) |
|-------|--------------|-----------------|
| SUM() | sum() | df.sum() |
| AVERAGE() | statistics.mean() | df.mean() |
| MAX() | max() | df.max() |
| MIN() | min() | df.min() |
| COUNT() | len() | df.count() |
| ROUND() | round() | df.round() |

### Text Operations
| Excel | Python |
|-------|--------|
| LEFT() | string[:n] |
| RIGHT() | string[-n:] |
| MID() | string[start:end] |
| LEN() | len(string) |
| CONCATENATE() | string1 + string2 |
| UPPER() | string.upper() |
| LOWER() | string.lower() |

### Lookup Functions
| Excel | pandas |
|-------|--------|
| VLOOKUP() | df.merge() or pd.merge() |
| HLOOKUP() | df.merge() or pd.merge() |
| INDEX/MATCH | df.loc[] or df.iloc[] |

## Data Analysis

### Filtering
```excel
# Excel: Filter where Sales > 1000
[Filter applied to column]

# Python (pandas)
df[df['Sales'] > 1000]
```

### Sorting
```excel
# Excel: Sort by Sales descending
[Sort Z to A on Sales column]

# Python (pandas)
df.sort_values('Sales', ascending=False)
```

### Pivot Tables
```excel
# Excel: Pivot Table
[Insert Pivot Table]

# Python (pandas)
df.groupby('Category')['Sales'].sum()
df.pivot_table(values='Sales', index='Category', aggfunc='sum')
```

## Date Operations
| Excel | Python (pandas) |
|-------|----------------|
| TODAY() | pd.Timestamp.now() |
| YEAR() | df['Date'].dt.year |
| MONTH() | df['Date'].dt.month |
| DAY() | df['Date'].dt.day |
| WEEKDAY() | df['Date'].dt.dayofweek |

## Conditional Logic
```excel
# Excel
=IF(A1>100, "High", "Low")

# Python
"High" if value > 100 else "Low"

# pandas
df['Category'] = np.where(df['Value'] > 100, "High", "Low")
```

## Common Data Cleaning
| Task | Excel | Python (pandas) |
|------|-------|----------------|
| Remove Duplicates | Remove Duplicates | df.drop_duplicates() |
| Fill Empty Cells | Fill/Flash Fill | df.fillna() |
| Find/Replace | Find & Replace | df.replace() |
| Remove Spaces | TRIM() | df['Column'].str.strip() |

## Visualization
| Excel Chart | Python (matplotlib/seaborn) |
|-------------|---------------------------|
| Bar Chart | plt.bar() or sns.barplot() |
| Line Chart | plt.plot() or sns.lineplot() |
| Scatter Plot | plt.scatter() or sns.scatterplot() |
| Pie Chart | plt.pie() |
| Histogram | plt.hist() or sns.histplot() |

## Best Practices
1. **Naming**
   - Excel: Use clear cell names and ranges
   - Python: Use descriptive variable names

2. **Documentation**
   - Excel: Use cell comments
   - Python: Use # comments and docstrings

3. **Organization**
   - Excel: Separate sheets for different data
   - Python: Separate functions and modules

4. **Validation**
   - Excel: Data validation rules
   - Python: Assert statements and try/except

Remember:
- Python is more flexible than Excel
- pandas operations are typically faster than Excel
- Python code is more reproducible than Excel formulas
- Version control (Git) works better with Python than Excel

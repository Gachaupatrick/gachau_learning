# Common Python Errors and Solutions

## Syntax Errors

### 1. IndentationError
```python
# Wrong
if value > 100:
print("High")  # Missing indentation

# Correct
if value > 100:
    print("High")  # Properly indented
```

### 2. Missing Parentheses
```python
# Wrong
print "Hello"  # Python 2 style

# Correct
print("Hello")  # Python 3 requires parentheses
```

### 3. Missing Colons
```python
# Wrong
if value > 100
    print("High")

# Correct
if value > 100:
    print("High")
```

## Data Structure Errors

### 1. List Index Out of Range
```python
# Wrong
numbers = [1, 2, 3]
print(numbers[3])  # Index 3 doesn't exist

# Correct
print(numbers[2])  # Last element is at index 2
# Or use try/except
try:
    print(numbers[3])
except IndexError:
    print("Index not found")
```

### 2. Key Error in Dictionaries
```python
# Wrong
data = {'name': 'John'}
print(data['age'])  # 'age' key doesn't exist

# Correct
print(data.get('age', 'Not found'))  # Uses default value if key missing
```

## pandas Common Issues

### 1. SettingWithCopyWarning
```python
# Wrong
subset = df[df['Sales'] > 1000]
subset['Category'] = 'High'

# Correct
subset = df[df['Sales'] > 1000].copy()
subset['Category'] = 'High'
```

### 2. Column Not Found
```python
# Wrong
df['sales']  # Wrong case

# Correct
df['Sales']  # Correct case - column names are case-sensitive
```

### 3. Data Type Mismatches
```python
# Wrong
df['Date'] = '2023-01-01'  # String date

# Correct
df['Date'] = pd.to_datetime('2023-01-01')  # Proper datetime
```

## File Operations

### 1. File Not Found
```python
# Wrong
df = pd.read_csv('data.csv')  # File might not exist

# Correct
try:
    df = pd.read_csv('data.csv')
except FileNotFoundError:
    print("File not found. Check the path.")
```

### 2. Path Issues
```python
# Wrong
df = pd.read_csv('subfolder/data.csv')  # Relative path might fail

# Correct
import os
file_path = os.path.join('subfolder', 'data.csv')
df = pd.read_csv(file_path)
```

## Visualization Issues

### 1. Plot Not Showing
```python
# Wrong
plt.plot(data)

# Correct
plt.plot(data)
plt.show()  # Need to call show()
```

### 2. Figure Size
```python
# Small default size
plt.plot(data)

# Better visibility
plt.figure(figsize=(10, 6))
plt.plot(data)
plt.show()
```

## Best Practices to Avoid Errors

1. **Check Data Types**
   ```python
   print(df.dtypes)  # Check column types
   print(type(variable))  # Check variable type
   ```

2. **Validate Data**
   ```python
   assert all(df['Sales'] >= 0), "Negative sales found"
   ```

3. **Use Error Handling**
   ```python
   try:
       result = calculation()
   except Exception as e:
       print(f"Error occurred: {e}")
   ```

4. **Debug with Print Statements**
   ```python
   print(f"Debug: variable = {variable}")
   ```

## Excel vs Python Error Handling

| Excel | Python |
|-------|--------|
| #DIV/0! | try/except ZeroDivisionError |
| #N/A | try/except KeyError |
| #NAME? | NameError |
| #NULL! | None |
| #NUM! | ValueError |
| #REF! | IndexError |
| #VALUE! | TypeError |

Remember:
- Python error messages are helpful - read them carefully
- Use print statements to debug
- Check data types when working with pandas
- Always make a copy when modifying DataFrames
- Keep track of array/list indices (they start at 0)
- Pay attention to indentation

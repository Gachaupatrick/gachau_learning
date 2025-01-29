# Module 1: Foundation with Real Data

## Overview
Welcome to your journey from Excel to Python! This module is specifically designed for professionals with Excel experience, making the transition to Python as smooth as possible.

## Learning Path Structure

### Week 1: Excel to Python Basics
#### Days 1-2: Basic Syntax and Variables
- **Morning**: Theory
  * Python basics compared to Excel cells
  * Variables vs Excel cells
  * Basic data types
- **Afternoon**: Practice
  * Guided exercises in `01_python_basics.ipynb`
  * Excel formula to Python function translations
- **Evening**: Exercises
  * Independent practice problems
  * Self-assessment quiz

#### Days 3-4: Lists and Dictionaries
- **Morning**: Theory
  * Lists (like Excel ranges)
  * Dictionaries (like Excel lookups)
  * Basic operations
- **Afternoon**: Practice
  * Working with sales data
  * Converting Excel operations to Python
- **Evening**: Exercises
  * Data structure practice
  * Real-world scenarios

#### Day 5: Functions and Calculations
- **Morning**: Theory
  * Functions vs Excel formulas
  * Common calculations
  * Best practices
- **Afternoon**: Mini-Project
  * Sales calculations
  * Basic reporting
- **Evening**: Review
  * Week 1 concepts
  * Progress check

### Week 2: Data Analysis Foundations
#### Days 1-2: pandas Basics
- **Morning**: Theory
  * Introduction to pandas
  * DataFrames vs Excel sheets
  * Basic operations
- **Afternoon**: Practice
  * Working with `02_pandas_intro.ipynb`
  * Loading and exploring data
- **Evening**: Exercises
  * Data manipulation tasks
  * Excel to pandas translations

#### Days 3-4: Data Cleaning and Filtering
- **Morning**: Theory
  * Filtering (like Excel filters)
  * Sorting (like Excel sort)
  * Grouping (like pivot tables)
- **Afternoon**: Practice
  * Sales data analysis
  * Creating summaries
- **Evening**: Exercises
  * Data cleaning challenges
  * Analysis tasks

#### Day 5: Basic Visualizations
- **Morning**: Theory
  * Plot types and uses
  * Customization options
  * Best practices
- **Afternoon**: Mini-Project
  * Sales dashboard
  * Performance visualizations
- **Evening**: Module Review
  * Concept summary
  * Skills assessment

## Excel to Python Quick Reference

### Common Operations
| Excel | Python (pandas) |
|-------|----------------|
| SUM() | df.sum() |
| AVERAGE() | df.mean() |
| VLOOKUP() | df.merge() |
| Filter | df[df['column'] > value] |
| Sort | df.sort_values() |
| Pivot Table | df.groupby() |

### Basic Concepts
1. **Cells → Variables**
   ```python
   # Excel: Cell A1 = 100
   revenue = 100
   ```

2. **Ranges → Lists**
   ```python
   # Excel: A1:A5 with values
   monthly_sales = [100, 150, 200, 175, 225]
   ```

3. **Sheets → DataFrames**
   ```python
   # Excel: Sheet with sales data
   sales_df = pd.read_csv('sales_data.csv')
   ```

## Practice Projects

### 1. Sales Analysis
- Calculate monthly totals
- Find top products
- Create summary reports
- Visualize trends

### 2. Performance Dashboard
- Regional comparisons
- Product category analysis
- Time-based trends
- Key metrics visualization

## Resources
1. **Cheat Sheets**
   - Python basics
   - pandas operations
   - Excel to Python translations

2. **Reference Guides**
   - Common formulas
   - Visualization types
   - Best practices

3. **Troubleshooting**
   - Common errors
   - Solutions guide
   - When to use what

## Progress Tracking

### Daily Checklist
- [ ] Complete theory readings
- [ ] Finish guided exercises
- [ ] Submit independent work
- [ ] Review concepts
- [ ] Note questions

### Weekly Goals
- [ ] Complete all notebook exercises
- [ ] Finish mini-projects
- [ ] Pass self-assessments
- [ ] Create practical examples

## Support
- Review the troubleshooting guide
- Check online documentation
- Ask questions in the course forum
- Schedule mentor sessions

## Next Steps
After completing this module, you should be able to:
1. Write basic Python code
2. Work with pandas DataFrames
3. Create simple visualizations
4. Perform basic data analysis
5. Translate Excel tasks to Python

Ready to start? Open `notebooks/01_python_basics.ipynb` and begin your journey!

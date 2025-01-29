# Development Environment Setup Guide

## Prerequisites
1. Install Python 3.x from [python.org](https://www.python.org/downloads/)
2. Install VS Code from [code.visualstudio.com](https://code.visualstudio.com/)
3. Install Git from [git-scm.com](https://git-scm.com/)
4. Install Power BI Desktop from [Microsoft Store](https://www.microsoft.com/store/productId/9NTXR16HNW1T)

## VS Code Extensions
1. Cline - Autonomous Coding Agent
   - Search for "Cline" in VS Code extensions
   - Click Install
   - Configure API key in extension settings
   - Access via:
     * Cline icon in sidebar, or
     * CMD/CTRL + Shift + P -> "Cline: Open In New Tab"

Install these extensions in VS Code:
1. Python (Microsoft)
2. Jupyter (Microsoft)
3. Git Graph
4. Python Indent
5. autoDocstring

## Project Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/gachau_learning_data_analytics.git
   cd gachau_learning_data_analytics
   ```

2. Create and activate virtual environment:
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure Jupyter kernel:
   ```bash
   python -m ipykernel install --user --name=data_analytics
   ```

## Project Structure
The repository is organized as follows:
```
gachau_learning_data_analytics/
├── modules/                    # Course modules
│   ├── module1_foundation/    # Foundation with real data
│   ├── module2_manipulation/  # Advanced data manipulation
│   ├── module3_ai_analysis/  # AI-powered analysis
│   └── module4_bi/           # Business intelligence
├── datasets/                  # Public datasets
│   ├── sales/               
│   ├── healthcare/
│   └── food_industry/
├── notebooks/                 # Jupyter notebooks
├── projects/                  # Capstone projects
└── resources/                # Additional materials
```

## Getting Started

1. After setup, open VS Code in the project directory:
   ```bash
   code .
   ```

2. Select the correct Python interpreter:
   - Press `Cmd/Ctrl + Shift + P`
   - Type "Python: Select Interpreter"
   - Choose the `data_analytics` environment

3. Start with Module 1:
   - Navigate to `modules/module1_foundation`
   - Open `notebooks/01_python_basics.ipynb`
   - Select the `data_analytics` kernel
   - Follow the instructions in the notebook

## Datasets

The required datasets will be downloaded as part of the exercises. Each module contains instructions for accessing and using specific datasets from:
- Kaggle
- Public data repositories
- Sample datasets

## Power BI Setup

1. Install Power BI Desktop
2. Configure Python connection:
   - Open Power BI Desktop
   - Go to File > Options and settings > Options
   - Under Python scripting, set your Python installation path

## Troubleshooting

### Common Issues

1. Python not found
   ```bash
   # Check Python installation
   python --version
   ```

2. pip not installing packages
   ```bash
   # Upgrade pip
   python -m pip install --upgrade pip
   ```

3. Jupyter kernel not showing
   ```bash
   # List available kernels
   jupyter kernelspec list
   
   # Reinstall kernel if needed
   python -m ipykernel install --user --name=data_analytics
   ```

### Support

If you encounter any issues:
1. Check the documentation in `cline_docs`
2. Review error messages in the terminal
3. Consult the official documentation for specific tools
4. Reach out to the course instructor

## Next Steps

1. Complete the environment setup
2. Verify all tools are working
3. Start with Module 1 exercises
4. Track progress in `cline_docs/progress.md`

# Simple Machine Learning Example

A very small machine-learning project using Python and scikit-learn.

The example teaches a computer to predict an exam mark from the number of hours studied. It uses **linear regression**, one of the simplest supervised machine-learning algorithms.

## What this project demonstrates

The program has five main steps:

1. Create example training data.
2. Create a linear regression model.
3. Train the model using the example data.
4. Give the trained model a new input.
5. Use the model to predict the result.

### The data

We use this small dataset:

| Hours studied | Exam mark |
|---:|---:|
| 1 | 35 |
| 2 | 45 |
| 3 | 55 |
| 4 | 65 |
| 5 | 75 |

The first column is the **input (feature)** and the second column is the **target (what we want to predict)**.

The model looks for a mathematical relationship between these two values.

In this example the relationship is approximately:

`mark = 25 + (10 × hours studied)`

Therefore, if a student studies for 6 hours, the model predicts approximately 85.

## What does "machine learning" mean here?

Instead of manually writing a rule such as:

```text
mark = 25 + (10 × hours)
```

we give the algorithm examples and ask it to find the relationship itself.

This is called **supervised learning** because we provide examples where the correct answer (the exam mark) is already known.

The process is:

```text
Training examples
       ↓
Linear Regression
       ↓
Learns relationship
       ↓
New hours studied
       ↓
Predicted exam mark
```

## Explanation of the code

The complete program is in `src/main.py`.

### 1. Import LinearRegression

```python
from sklearn.linear_model import LinearRegression
```

`LinearRegression` is the machine-learning algorithm provided by scikit-learn.

### 2. Create training data

```python
X = [[1], [2], [3], [4], [5]]
y = [35, 45, 55, 65, 75]
```

`X` contains the input values: hours studied.

`y` contains the known answers: exam marks.

The double brackets in `X` are intentional. scikit-learn expects features to be supplied as a two-dimensional collection: rows represent examples and columns represent features.

### 3. Create the model

```python
model = LinearRegression()
```

At this point we have created the algorithm, but it has not learned anything yet.

### 4. Train the model

```python
model.fit(X, y)
```

This is the most important machine-learning line.

`fit()` gives the algorithm the training examples. Linear regression finds the line that best represents the relationship between the hours studied and the marks.

The model learns two important values:

- **Coefficient/slope**: how much the predicted mark changes when hours studied increases by one.
- **Intercept**: the predicted starting value when hours studied is zero.

You can see these values in the program output.

### 5. Make a prediction

```python
prediction = model.predict([[6]])
```

We now give the trained model a new example: 6 hours studied.

The model uses the relationship it learned during training to estimate the exam mark.

### 6. Display the result

The program prints the learned equation and the prediction.

Because this is a tiny, perfectly linear dataset, the prediction for 6 hours should be approximately **85%**.

## Important machine-learning concepts

### Feature

A feature is information used by the model to make a prediction.

Here:

`Hours studied`

### Target

The target is what the model is trying to predict.

Here:

`Exam mark`

### Training

Training is the process where the algorithm uses known examples to learn a pattern.

### Prediction

Prediction is using the trained model with new input data.

### Model

The model is the learned mathematical relationship that connects the input to the output.

## Limitations

This is deliberately the simplest possible demonstration, not a realistic exam prediction system.

The dataset is extremely small and perfectly linear. Real-world data is usually noisy and much more complicated.

For example, exam results can depend on sleep, previous knowledge, difficulty of the exam, attendance, and many other factors.

The purpose of this project is to understand the basic machine-learning workflow, not to produce a reliable prediction system.

## Requirements

- Python 3.10 or newer
- pip

The required Python package is listed in `requirements.txt`.

## Setup

### 1. Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd simple-machine-learning
```

Replace `<YOUR-GITHUB-REPOSITORY-URL>` with the URL of your GitHub repository.

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the program

```bash
python src/main.py
```

On some systems you may need:

```bash
python3 src/main.py
```

## Expected output

The exact formatting may vary slightly, but you should see something similar to:

```text
Learned equation: mark = 25.00 + 10.00 × hours
Prediction for 6 hours studied: 85.00%
```

## Project structure

```text
simple-machine-learning/
│
├── src/
│   └── main.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Why this is machine learning

The important distinction is that we do not directly tell the program the equation it should use.

We provide examples:

```text
1 → 35
2 → 45
3 → 55
4 → 65
5 → 75
```

The algorithm discovers the relationship from those examples.

That is the core idea behind supervised machine learning: **learn a pattern from known examples and use the learned pattern on new data.**

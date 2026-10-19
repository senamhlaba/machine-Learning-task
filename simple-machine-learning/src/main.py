from sklearn.linear_model import LinearRegression


def main():
    # Training data:
    # X = hours studied
    # y = exam mark
    X = [[1], [2], [3], [4], [5]]
    y = [35, 45, 55, 65, 75]

    # Create the machine-learning model.
    model = LinearRegression()

    # Train the model using the known examples.
    model.fit(X, y)

    # Ask the trained model to predict the mark for 6 hours of study.
    prediction = model.predict([[6]])[0]

    # Display what the model learned.
    intercept = model.intercept_
    coefficient = model.coef_[0]

    print(f"Learned equation: mark = {intercept:.2f} + "
          f"{coefficient:.2f} × hours")
    print(f"Prediction for 6 hours studied: {prediction:.2f}%")


if __name__ == "__main__":
    main()

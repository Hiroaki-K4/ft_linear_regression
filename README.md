# ft_linear_regression
For this project, I created a program that predicts the price of a car by using a linear function train with a gradient descent algorithm.

<br></br>

## Estimate price
The estimation program will be used to predict the price of a car for a given mileage.
When you launch the program, it should prompt you for a mileage, and then give you back the estimated price for that mileage. The program will use the following
hypothesis to predict the price :

$$
estimateP rice(mileage) = θ_0 + (θ_1 \times mileage)
$$

You can try the process by running the follow command.

```bash
python estimate_price.py --mileage 30 --param_yaml param.yaml
```

<br></br>

## Train with a gradient descent algorithm
Traing program read dataset file and perform a linear regression on the data.
Once the linear regression has completed, it will save the variables theta0 and theta1 for use in the estimation program.
The training procedure is as follows.

### **1. Normalize range**
If I used the values of the data as they were used for training, the training did not converge well. Therefore, I normalized the data and used it for training. I used [**scaling to a range**](https://developers.google.com/machine-learning/data-prep/transform/normalization#scaling-to-a-range) to normalize data.

$$
x=(x\prime - x_{min})/(x_{max}-x_{min})
$$

Scaling to a range is a good choice when both of the following conditions are met:
- You know the approximate upper and lower bounds on your data with few or no outliers.
 - Your data is approximately uniformly distributed across that range.

### **2. Calculate gradient**

### **3. Update parameter with learning rate**

### **4. Calculate cost function**

### **5. Convert normalized value back to original value**


You can try the process by running the follow command.

```bash
python train.py --csv_file_path data.csv --output_param_path param.yaml
```

The graph of result is below image.

<img src='images/result_graph.png' width='600'>

<br></br>

## References
- [Gradient descent](https://en.wikipedia.org/wiki/Gradient_descent)
- [Linear function](https://en.wikipedia.org/wiki/Linear_function)
- [Gradient Descent in Linear Regression](https://www.analyticsvidhya.com/blog/2021/04/gradient-descent-in-linear-regression/)
- [Linear Regression using Gradient Descent](https://towardsdatascience.com/linear-regression-using-gradient-descent-97a6c8700931)
- [Normalization](https://developers.google.com/machine-learning/data-prep/transform/normalization)

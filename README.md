# Coursera course
  - Title: Supervised Machine Learning: Regression and Classification
  - by DeepLearning.AI & Stanford University
  - [Link to the course on coursera](https://www.coursera.org/learn/machine-learning/)

# There are 3 modules in this course

In the first course of the Machine Learning Specialization, you will:
  - Build machine learning models in Python using popular machine learning libraries NumPy and scikit-learn.
  - Build and train supervised machine learning models for prediction and binary classification tasks, including linear regression and logistic regression

The Machine Learning Specialization is a foundational online program created in collaboration between DeepLearning.AI and Stanford Online. In this beginner-friendly program, you will learn the fundamentals of machine learning and how to use these techniques to build real-world AI applications.

This Specialization is taught by Andrew Ng, an AI visionary who has led critical research at Stanford University and groundbreaking work at Google Brain, Baidu, and Landing.AI to advance the AI field.

This 3-course Specialization is an updated and expanded version of Andrew’s pioneering Machine Learning course, rated 4.9 out of 5 and taken by over 4.8 million learners since it launched in 2012.


It provides a broad introduction to modern machine learning, including supervised learning (multiple linear regression, logistic regression, neural networks, and decision trees), unsupervised learning (clustering, dimensionality reduction, recommender systems), and some of the best practices used in Silicon Valley for artificial intelligence and machine learning innovation (evaluating and tuning models, taking a data-centric approach to improving performance, and more.)

By the end of this Specialization, you will have mastered key concepts and gained the practical know-how to quickly and powerfully apply machine learning to challenging real-world problems. If you’re looking to break into AI or build a career in machine learning, the new Machine Learning Specialization is the best place to start.

# Conventions
  - $y^{(i)}$ = Target (output) at $i^{th}$ data
  - $\hat{y}^{(i)}$ = `Predicted` Target (output) at $i^{th}$ data
  - $m$ = number of training examples
  - Cost function
    + $MSE = \frac{1}{m}\sum_{i=1}^{m}(\hat{y}^{(i)} - y^{(i)})^2$ = Mean Squared Error
    + $MAE = \frac{1}{m} \sum_{i=1}^{m} |\hat{y}^{(i)} - y^{(i)}|$ = Mean Absolute Error
    + $RMSE = \sqrt{\frac{1}{m} \sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)})^2}$ = Root Mean Squared Error
    + $\text{CCE} = -\frac{1}{m} \sum_{i=1}^{m} \sum_{j=1}^{k} y_j^{(i)} \log \hat{y}_j^{(i)}$ = Categorical Cross-Entropy

# Gradient descent algorithm
- Repeat until convergence:
  + $w = w - \alpha\frac{\partial}{\partial w}J(w,b)$
  + $b = b - \alpha\frac{\partial}{\partial b}J(w,b)$

- Where:
  - $\alpha$ = learning rate
  - $\frac{\partial}{\partial w}J(w,b)$ = derivative
  - $\frac{\partial}{\partial b}J(w,b)$ = derivative

- Rule: Simultaneously update $w$ and $b$
  + $[w, b] = [w, b] - \alpha[\frac{\partial}{\partial w}J(w,b), \frac{\partial}{\partial b}J(w,b)]$
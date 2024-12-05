% Data from the problem
y = [85; 110; 90; 80; 90; 95; 80; 98; 91; 95]; % Response variable
x1 = [1; 1; -1; -1; 0; 0; 1; -2; 2; 1.5];      % Predictor x1
x2 = [-1; 1; 1; -1; 0; 1; 0; 1; 2; 1];         % Predictor x2

% Create the design matrix (X) for the second-order model
X = [ones(size(x1)), x1, x2, x1.^2, x2.^2];

% Compute the regression coefficients using the normal equations
beta_hat = (X' * X) \ (X' * y);

% Residual variance (sigma^2)
n = size(y, 1);        % Number of observations
p = size(X, 2);        % Number of predictors (including intercept)
residuals = y - X * beta_hat;
sigma_squared = sum(residuals.^2) / (n - p); % Residual variance

% Predictor values for x1 = -1, x2 = 1
a = [1, -1, 1, (-1)^2, 1^2]; % Row vector for the specified x1 and x2

% Compute the variance of the prediction
X_inverse = inv(X' * X); % Inverse of (X'X)
variance_prediction = sigma_squared * (a * X_inverse * a'); % Var(a'beta)

% Predicted mean response
mean_y = a * beta_hat;

% Critical t-value for 95% confidence interval with (n - p) degrees of freedom
alpha = 0.05;
t_value = tinv(1 - alpha/2, n - p);

% Margin of error and confidence interval
margin_of_error = t_value * sqrt(variance_prediction);
ci_lower = mean_y - margin_of_error;
ci_upper = mean_y + margin_of_error;

% Display results
disp('Predicted mean value of Y:');
disp(mean_y);
disp('95% Confidence Interval:');
disp([ci_lower, ci_upper]);

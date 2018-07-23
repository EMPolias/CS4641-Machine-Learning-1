cancer = csvread('../../data/cancertrain.csv');
inputs = cancer(:, 1:end-1);    % input data.
targets = cancer(:, end);       % target data.

% Create a Fitting Network
hiddenLayerSize = 10;
net = fitnet(hiddenLayerSize);


% Setup Division of Data for Training, Validation, Testing
net.divideParam.trainRatio = 70/100;
net.divideParam.valRatio = 15/100;
net.divideParam.testRatio = 15/100;


% Train the Network
[net,tr] = train(net,inputs',targets');

% Test the Network
outputs = net(inputs');
errors = gsubtract(targets',outputs);
performance = perform(net,targets',outputs);

% View the Network
y = net(inputs');
% Calculating the mean squared error
mse_calc = (sum((y-targets').^2))/length(y)
pred = round(y);
pred = arrayfun(@(x) cust_ceil(x), pred);
confusion(pred, targets')

% compare against the testing
cancerTEST = csvread('../../data/cancertest.csv');
inputs_test = cancerTEST(:, 1:end-1);
targets_test = cancerTEST(:, end);

y = net(inputs_test');
% Calculating the mean squared error
mse_calc = (sum((y-targets_test').^2))/length(y)
pred = round(y);
pred = arrayfun(@(x) cust_ceil(x), pred);
confusionmat(pred, targets_test');
confusion(pred, targets_test')



% Plots
% Uncomment these lines to enable various plots.
%figure, plotperform(tr)
%figure, plottrainstate(tr)
%figure, plotfit(net,inputs,targets)
%figure, plotregression(targets,outputs)
%figure, ploterrhist(errors)

% read cancer trainning data
cancer = csvread('../../data/cancertrain.csv');
inputs = cancer(:, 1:end-1);
targets = cancer(:, end);


% get the prediction error
cancerTEST = csvread('../../data/cancertest.csv');
inputs_test = cancerTEST(:, 1:end-1);
targets_test = cancerTEST(:, end);


tic
% Initialise the net%

% number of neurons
net = feedforwardnet(); %initialize with default neurons
% configure the neural network for this dataset
net = configure(net, inputs', targets');
% create handle to the MSE_TEST function, that
% calculates MSE

h = @(x) mse_ga(x, net, inputs', targets');
% Setting the Genetic Algorithms tolerance for

plottrainfun = @(options,state,flag) gaplotvaliderror(options,state,flag, net, inputs', targets', ...
    inputs_test', targets_test');


ga_opts = gaoptimset('TolFun', 1e-16,'Generations', Inf,'display','iter', 'TimeLimit', 1200, ...
    'PlotFcns', {@gaplotbestf, @gaplotbestindiv, plottrainfun});
[x_ga_opt, err_ga, flag, output]  = ga(h, net.numWeightElements, ga_opts);
toc
% now `net` will be optimized based on the set of weights.


[err pred] = mse_ga(x_ga_opt', net, inputs_test', targets_test')
confusionmat(pred, targets_test')
confusion(pred, targets_test')


[err pred] = mse_ga(x_ga_opt', net, inputs', targets')
confusion(pred, targets')





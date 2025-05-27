function [principalList, interestList, yearlyAmountList] = mortgageAmortizationSchedule(APR, principal, yearsLeft, extraPayment)
% mortgageAmortizationSchedule
% This function calculates and plots the mortgage amortization schedule
% with optional extra monthly payments.
%
% Inputs:
%   APR - Annual percentage rate (e.g. 5 for 5%)
%   principal - Initial loan amount
%   yearsLeft - Remaining years on the mortgage
%   extraPayment - (optional) extra payment made each month
%
% Outputs:
%   principalList - Remaining principal by month
%   interestList - Interest paid each month
%   yearlyAmountList - Remaining principal at each year

if nargin < 4
    extraPayment = 1000; % default value
end

APR = APR / 100; % Convert to decimal
monthsLeft = yearsLeft * 12;
monthlyInterest = APR / 12;

% Monthly payment (standard amortization formula)
payment = (principal * monthlyInterest * (1 + monthlyInterest)^monthsLeft) / ...
          ((1 + monthlyInterest)^monthsLeft - 1);

fprintf('Monthly payment: $%.2f\n', payment);

% Initialize storage arrays
principalList = zeros(monthsLeft+1, 1);
interestList = zeros(monthsLeft, 1);
cumulativeInterestList = zeros(monthsLeft+1, 1);
yearlyAmountList = [];

principalList(1) = principal;
cumulativeInterest = 0;

% Loop over each month
for i = 1:monthsLeft
    if principal <= 0
        principalList(i+1:end) = [];
        cumulativeInterestList(i+1:end) = [];
        interestList(i:end) = [];
        break;
    end
    
    interest = principal * monthlyInterest;
    interestList(i) = interest;
    
    principalPayment = payment + extraPayment - interest;
    principal = principal - principalPayment;
    principal = max(principal, 0);
    principalList(i+1) = principal;
    
    cumulativeInterest = cumulativeInterest + interest;
    cumulativeInterestList(i+1) = cumulativeInterest;
    
    if mod(i, 12) == 0
        yearlyAmountList = [yearlyAmountList; principal];
    end
end

% Plot: Principal and cumulative interest
figure;
plot(principalList, 'LineWidth', 1.5); hold on;
plot(cumulativeInterestList, 'LineWidth', 1.5);
grid on; legend('Remaining Principal ($)', 'Cumulative Interest Paid ($)');
xlabel('Month'); ylabel('Amount ($)');
title('Mortgage Amortization Breakdown');

% Plot: Monthly interest
figure;
plot(interestList, 'LineWidth', 1.5, 'Color', [1 0.5 0]);
grid on; legend('Monthly Interest Paid ($)');
xlabel('Month'); ylabel('Interest Paid ($)');
title('Monthly Interest Paid Over Time');

% Output summary
totalInterestPaid = sum(interestList);
totalPaid = totalInterestPaid + principalList(1);

fprintf('Total interest paid over the life of the loan: $%.2f\n', totalInterestPaid);
fprintf('Total Paid Over %d Years: $%.2f\n', yearsLeft, totalPaid);

end

% The code for initial weight estimate
clc
clear all
w = zeros(100,1); # The array of W0 values
wb = zeros(size(w)(1),1); # The array to get the battery weight estimates
count=zeros(size(w)(1),1); # Counter
a = 0.894172; # from previous code
l = -0.086; # from previous code
w(1) = 8; # First weight guess
wp = 1.5; # Payload weight
wb(1) = 1.7277; # First battery weight guess
for i = 1:size(w)(1)
  count(i)=i-1;
  w(i+1) = wp/(1-[(wb(i)/w(i))+a*(w(i)^l)]); 
  # Derived fromt the weight fraction equation
  [wb(i+1)] = tot_power (w(i+1)); 
  # above step calculates the battery weight for each total weightS
  if (abs(w(i+1)-w(i))<1e-6); # checks for convergence
    disp("The final total weight is"),disp(w(i+1))
    % Displays the final total weight of the battery 
    disp("The final battery weight is"),disp(wb(i+1)) 
    % Displays the weight of battery based on the total weight w(i+1)
    break
  endif
endfor
plot(count(1:i,1), w(1:i,1), 'linewidth', 0.8, 'b');
set(gca , 'fontsize', 16);
title('Weight estimation');
xlabel('Iterations');
ylabel('Weight (Kg)');
legend('Weight');
grid on;

    
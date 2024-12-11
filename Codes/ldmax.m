# This is the code for L/D max vs root(ARwet)
clc
clear all
AR = [2.132007164 2.015639336 1.469693846 2.070196678 1.206673363
2.4079742 1.145793457 1.886621541];
LD = [20.49313833 18.84778314 12.0417142 20.32570455 20.06377629
22.05813283 13.74679004 21.49744899];
k = size(LD)(2); # THe length of the vector
X = [AR; ones(1,k)]; # A vector of 2*9
#t This will do the regression to get the best fit line
# Using Gaussian elimination method to get m and c values
M = LD*(X')*inv(X*(X'));
Y = M*X;# The equation for best fit line

# creates uniformly distributed points for the values of AR and L/D
x = linspace(0.5,3,30);
y = linspace(10,30,30);
c = 17.348; # choosen L/D max value based on data
figure(1)
# Used to do scatter plot
scatter(AR,LD,'g','linewidth',1.2,'o')
hold on
# Plots the regression line
plot(x,M(1)*x+M(2),'m--','linewidth',1.2)
hold on
#Plots the choosen point
plot((c - M(2))/M(1),'rx','linewidth',1.5)
hold on
#plots the boundary lines
plot(1,y,'b.',2,y,'b.')
hold off
set(gca , 'fontsize', 11);
title('L/D vs sqrt{AR_{wet}}');
xlabel('sqrt(AR_{wet})');
ylabel('L/D max');
legstr = {'Data','Regression','Choosen point','lower limit','upper limit'};
legend(legstr,'location','southeast');
grid on
saveas(figure(1),'ldmax-ar.png')


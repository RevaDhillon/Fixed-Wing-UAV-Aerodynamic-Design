#Curve-fitting for Empty weight fraction VS. DTOW:

#Creating figures.
f1=figure(); hold on;
f2=figure(); hold on;

#Array of DTOW values:
W0 = [2.4, 4.5, 5, 6.2, 9.5, 9.8, 10, 13.5]

#Array of empty weight fraction values:
WeW0 = [0.875,0.7777778,0.7,0.8064516,0.7578947,0.8673469,0.56,0.7777778]

#Vectors to store the values of log(W_0), log(W_e/W_0):
v11=(log(W0))'
v12=(log(WeW0))'


###Linear Regression Algorithm:

#Adding a column of all ones.
mv11=[v11, [ones(8,1)]]

#Finding [L; log(A)].
X=inv((mv11')*mv11)*(mv11')*v12

printf("L = %f \n", X(1))
printf("A = %f \n", exp(X(2)))

#Compute the predicted values of log(W_e/W_0).
y1=mv11*(X)

#Compute the predicted values of W_e/W_0.
y = exp(y1)


###Plots:

#Plot of log(W_e/W_0) VS. log(W_0):
figure(f1);
scatter(v11, v12, 16, "filled")
plot(v11,y1, "m")

#Making the legend.
legend({"Aircraft Data","Linear Regression"}, "location", "southwest")
grid on
#Titling the figure.
title("Empty Weight Fraction VS. DTOW")
#Labelling the axes.
xlabel("log(W_0) -->")
ylabel("log(W_e/W_0)  -->")
set(gca, "fontsize", 10)
#Saving the plot.
print(f1, "-r500", "WeightFract_Linear.png")

#Plot of W_e/W_0 VS. W_0:
figure(f2);
scatter(W0, WeW0, 16, "filled")
plot(W0, y, 'm')

#Making the legend.
legend({"Aircraft Data","Model output"}, "location", "southwest")
grid on
#Titling the figure.
title("Empty Weight Fraction VS. DTOW")
#Labelling the axes.
xlabel("W_0 -->")
ylabel("W_e/W_0 -->")
set(gca, "fontsize", 10)
#Saving the plot.
print(f2, "-r500", "WeightFract.png")


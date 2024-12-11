# Power requirement plot
clc
clear all
v = linspace(1, 30, 150);
r = 1.207;
n = 0.495;
K = 0.055;
S = 2.5*0.3667;
CD0 = 0.024;
Pa = 3.7*5*4*6*ones(1,size(v)(2)); # Power supplied by the battery in W
Pr = (0.5*r*(v.^3)*S).*[CD0 .+ K*(2*9.65*9.8 ./(r*(v.^2)*S)).^2];
plot(v,Pr)
hold on
plot(v,n*Pa)
set(gca , 'fontsize', 14);
ylabel('Power in W')
xlabel('Velocity in m/s')
title('Power vs velocity')
legend('Power required','Power available')
grid on
hold off
saveas(figure(1),'power-analysis.png')

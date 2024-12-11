# The file to get wing loading for all phases
function [L_st, L_m, Lc1, Lc2, L_lo, L_c, H] = wing_loading(Vst,Clm,Vm,Cd0,
K, P_W,g,LDm,Vc) # Using the above values
  r0 = 1.225; # sea level density
# For (Vstall) wing loading
  L_st = 0.5*r0*Vst^2*Clm; 
# For cruise (max velocity) wing loading
  Cl = sqrt(Cd0/K);
  L_m = 0.5*1.207*Vm^2*Cl;
# For climb-1
  Cl_c = sqrt(3*Cd0/K);
  f = @(W_S) 2.302 - (sin(g)+1.1547/LDm)*sqrt(2*W_S/(r0*Cl_c)) ;
  Lc1 = fzero(f,0.5)
# For climb-2 After payload drop
  Cl_c = sqrt(3*Cd0/K);
  f = @(W_S) 2.6266 - (sin(g)+1.1547/LDm)*sqrt(2*W_S/(r0*Cl_c)) ;
  Lc2 = fzero(f,0.5)
# For Loiter
  L_lo = 0.5*r0*Vc^2*Cl_c;
# For ceiling height 
  H = -6055.462*log(1/P_W)*sqrt(2*L_m/1.225)*[0.7436*Cd0*(pi*K)^0.75];
  R = 287;
  T = 298;
# For ceiling wing loading
  rc = r0*exp(-9.81*H/(R*T)); # Ceiling density
  Vch = sqrt(r0/rc)*Vc;
  L_c = 0.5*rc*Vc^2*Cl;
endfunction
# [L_st, L_m, Lc1, Lc2, L_lo, L_c, H] = wing_loading(12.22,1.5,22,0.0157,
0.053,119*18,5*pi/180,17.35546,18)
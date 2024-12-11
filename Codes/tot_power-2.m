% The code for total power calculation
function [P] = tot_power (w)
  E = 145.7119368+(0.5774166*(w^2)) + (0.9479*(w^1.25)) + 
  (9.12966*(w^0.25)) + (0.053*(w^1.25)) + 0.343*(w^1.5) + (4.6884*(w^0.5));
  # The E is the total energy consumption including all phases
  P = E/160;
  # 160 is the battery energy density
endfunction

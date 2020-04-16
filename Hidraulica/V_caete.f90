!escrevendo fórmula K para o modelo

    function soil_potential(theta_sat, psi_sat, b) result(psi_soil)
        ! Returns soil water potential
        use types
      
        !puxar arquivos globais
        real(r_4),intent(in) :: theta_sat           !g H20/g solo 
        real(r_4),intent(in) :: psi_sat             !MPa
        real(r_4),intent(in) :: b                   !S/ unidade
        real(r_4) :: pot_soil  

        psi_soil = Psi_sat * (theta/theta_sat)**(-b)
    
    endfunction soil_potential

   !=================================================================
   !=================================================================

    ! adc variables of psi_g in no global.f90
    !real(r_4),parameter,public :: rho = 997.0       ! Density of water (Kg/m3)
    !real(r_4),parameter,public :: g = 9.8           ! Gravity (m/s2)
    !real(r_4),parameter,public :: vulnerability_curve = 4          ! Sigmoidal curve (s/ unity)

    function xylem_conductance(psi_xym, psi_50, vulnerability_curve, h) result(xym_conduct)    ! based in Eller et al. 2018
    use types
    use global_par, only:rho, g, vulnerability_curve

    real(r_4), intent(in) :: psi_solo, psi_g, psi_50, vulnerability_curve
    real(r_4) :: xym_conduct   !mmol m-2 s-1 MPa-1

    real(r_4) :: psi_g
    real(r_4) ::       

    psi_soil = soil_potential(theta_sat, psi_sat, b)
    alt = height calculation(_____) !pull calculation of the Bia and Ba implementation

    !gravitational potential to calculate the psi of xylem 
    psi_g = rho * g * alt * 1e-6      !converts Pa to MPa  !ver sinal de atribuição

    xym_conduct = 1.0 / (1.0 + ((psi_soil - psi_g) / psi_50) ** vulnerability_curve)

    !embolism mortality
    if (xym_conduct .le. 0.12) then 
       no_cell = .true.  !PLS die

       !or
       ! P88=7.33^(1/a)*P50 calc

    end function

    !=================================================================
    !=================================================================

    !tentar implementar o xym_conduct no lugar do W na esquação do L[ep] (suprimento pot. pra transp.)
   
    function water_stress_modifier(xym_conduct, cfroot, rc, ep) result(f5)
       use types, only: r_4, r_8
       use global_par, only: csru, wmax, alfm, gm, rcmin
       !implicit none
 
       !não sei se tem que declarar aqui, mas acho que não
       real(r_4),intent(in) :: xym_conduct      ! maximum xylem condutance mm
       real(r_8),intent(in) :: cfroot !carbon in fine roots kg m-2
       real(r_4),intent(in) :: rc     !Canopy resistence 1/(micromol(CO2) m-2 s-1)
       real(r_4),intent(in) :: ep     !potential evapotranspiration
       real(r_4) :: f5S
 
 
       real(r_8) :: pt
       real(r_8) :: gc
       real(r_8) :: wa
       real(r_8) :: d
       real(r_8) :: f5_64

       wa = w/wmax   !tirar? "f5_64=wa"
 
       xym_conduct = xylem_conductance(psi_xym, psi_50, vulnerability_curve, h)
 
       pt = csru*(cfroot*1000.) * xym_conduct  !(based in Pavlick et al. 2013; *1000. converts kgC/m2 to gC/m2)
       if(rc .gt. 0.0) then
          gc = (1.0/(rc * 1.15741e-08))  ! s/m
       else
          gc =  1.0/(rcmin * 1.15741e-08) ! BIANCA E HELENA - Mudei este esquema..   
       endif                  
 
       !d =(ep * alfm) / (1. + gm/gc) !(based in Gerten et al. 2004)
       d = (ep * alfm) / (1. + (gm/gc))
       if(d .gt. 0.0) then
          f5_64 = pt/d
          f5_64 = exp(-0.1 * f5_64)
          f5_64 = 1.0 - f5_64
       else
          f5_64 = wa      !não troquei p/ xym_conduct
       endif
 
       f5 = real(f5_64,4)      
    end function water_stress_modifier
 
    !=================================================================
    !=================================================================
 
   ! functions(f) and subroutines(s) defined here
   public ::                    &
        gross_ph               ,& ! (f), gross photosynthesis (kgC m-2 y-1)
        leaf_area_index        ,& ! (f), leaf area index(m2 m-2) 
        f_four                 ,& ! (f), auxiliar function (calculates f4sun or f4shade or sunlai) 
        spec_leaf_area         ,& ! (f), specific leaf area (m2 g-1)
        water_stress_modifier  ,& ! (f), F5 - water stress modifier (dimensionless)
        photosynthesis_rate    ,& ! (s), leaf level CO2 assimilation rate (molCO2 m-2 s-1)
        canopy_resistence      ,& ! (f), Canopy resistence (from Medlyn et al. 2011a) (s/m) == m s-1
        stomatal_conductance   ,&
        ! scarbon_decaiment      ,& ! (f), Carbon decay borrowed from Pavlick et al. 2012
        vapor_p_defcit         ,& ! (f), Vapor pressure defcit  (kPa)
        tetens                 ,& ! (f), Maximum vapor pressure (hPa)
        nrubisco               ,& ! (f), Fraction of N not in lignin (disponible to rubisco)
        nlignin                ,& ! (f), Fraction of N in lignin  
        m_resp                 ,& ! (f), maintenance respiration (plants)
        spinup2                ,& ! (s)
        spinup3                ,& ! (s)
        g_resp                 ,& ! (f), growth Respiration (kg m-2 yr-1)
        ! carbon2                ,& ! (s) 
        ! carbon3                ,& ! (s), soil + litter + heterothrophic respiration
        pft_area_frac          ,& ! (s), area fraction by biomass
        pft_par                ,& ! (s), aux subroutine to read pls data               (D)
        ascii2bin              ,& ! (s), converts txt file (traits,lines) to .bin file (D)
        allocation             ,& ! (s), daily npp allocation subroutine
        water_ue               ,& ! (f), water use efficiency
        rc_canopy_scaling      ,& ! (f), Try it!
        leap                   ,& ! (f), is leap year ?
        soil_potential         ,& ! (f), soil water potential
        xylem_potential        ,& ! (f), xylem water potential
        xylem_conductance            

contains   
   
   !=================================================================
   !=================================================================

   function soil_potential(theta_sat, psi_sat, b) result(psi_soil)
      ! Returns soil water potential 
      use types, only: r_4
      !implicit none

      real(r_4),intent(in) :: theta_sat           !g H20/g solo 
      real(r_4),intent(in) :: psi_sat             !MPa
      real(r_4),intent(in) :: b                   !S/ unidade
      real(r_4) :: pot_soil

      real(r_4) :: theta

      theta = theta=seq(0.1,theta_sat,len=1000)   !não sei como fazer sequencia

      psi_soil = Psi_sat * (theta/theta_sat)**(-b)

   end function soil_potential

   !=================================================================
   !=================================================================

      function xylem_potential(rho, gravity, height, conv) result(psi_xym)
      ! Returns xylem water potential
      use types, only: r_4
      !implicit none

      real(r_4),intent(in) :: rho           !kg/m3 
      real(r_4),intent(in) :: gravity       !m/s2
      real(r_4),intent(in) :: height        !m
      real(r_4),intent(in) :: conv          !Pa to MPa
      real(r_4) :: psi_xym

      real(r_4) :: psi_soil
      real(r_4) :: psi_g

      psi_soil = soil_potential(theta_sat, psi_sat, b)

      psi_g = rho*g*alt*conv    !ver sinal de atribuição

      psi_xym = psi_solo - psi_g    

   end function xylem_potential

   !=================================================================
   !=================================================================

   function xylem_conductance(psi_xym, psi_50,vulnerability_curve) result(V)
      ! Returns maximum xulem condutance 
      use types, only: r_4
      !implicit none

      real(r_4),intent(in) :: psi_xym             !MPa 
      real(r_4),intent(in) :: psi_50              !MPa
      real(r_4),intent(in) :: vulnerability_curve !S/ unidade
      real(r_4) :: xym_con

      V = 1 / (1+(psi_xym/P50) ** a)

   end function xylem_conductance

   !=================================================================
   !=================================================================

   !tentar implementar o V no lugar do W na esquação do L[ep] (suprimento pot. pra transp.)%
   na qual está dentro da equação f5

   function water_stress_modifier(V, cfroot, rc, ep) result(f5)
      use types, only: r_4, r_8
      use global_par, only: csru, wmax, alfm, gm, rcmin
      !implicit none

      real(r_4),intent(in) :: V      ! maximum xilem condutance mm
      real(r_8),intent(in) :: cfroot !carbon in fine roots kg m-2
      real(r_4),intent(in) :: rc     !Canopy resistence 1/(micromol(CO2) m-2 s-1)
      real(r_4),intent(in) :: ep     !potential evapotranspiration
      real(r_4) :: f5


      real(r_8) :: pt
      real(r_8) :: gc
      real(r_8) :: wa
      real(r_8) :: d
      real(r_8) :: f5_64

      wa = w/wmax

      pt = csru*(cfroot*1000.) * wa  !(based in Pavlick et al. 2013; *1000. converts kgC/m2 to gC/m2)
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
         f5_64 = wa
      endif

      f5 = real(f5_64,4)      
   end function water_stress_modifier

   !=================================================================
   !=================================================================

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
        xylem_conductance      ,& ! (f), maximum xylem condutance
              

contains   
   
   !=================================================================
   !=================================================================

   function leaf_age_factor(dec_photo, acrit, leaf_age) result(age_factor)
      ! Returns leaf age factor 
      use types, only: r_4
      !implicit none

      real(r_4),intent(in) :: dec_photo         !years-1     !decay constant of photosynthesis with age 
      real(r_4),intent(in) :: acrit             !years      !age after whith leaves start ageing
      real(r_4),intent(in) :: leaf_age          !years
      real(r_4) :: age_factor

      data dec_photo1/0,1,2,3,4,5,6,7,8/,dec_photo2/1/,dec_photo3/0,1,2,3/

      age_factor = exp(dec_photo * (acrit-leaf_age)   
      age_factor = 1.0 - age_factor

   end function leag_age_factor

   !=================================================================
   !=================================================================       
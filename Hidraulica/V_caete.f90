!escrevendo fórmula V para o modelo

    function soil_potential(theta_sat, psi_sat, b) result(psi_soil)
        ! Returns soil water potential
        use types

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
    real(r_4) :: xym_conduct

    real(r_4) :: psi_g
    real(r_4) ::       

    psi_soil = soil_potential(theta_sat, psi_sat, b)
    alt = height calculation(_____) !pull calculation of the Bia and Ba implementation

    !gravitational potential to calculate the psi of xylem 
    psi_g = rho * g * alt * 1e-6      !converts Pa to MPa  !ver sinal de atribuição

    xym_conduct = 1.0 / (1.0 + ((psi_soil - psi_g) / psi_50) ** vulnerability_curve)

    end function

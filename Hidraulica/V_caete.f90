!escrevendo fórmula V para o modelo

function xylem_conductance(Psi_soil, Psi_g, P50, vulnerability_curve) result(V)    ! based in Eller et al. 2018
    use types
    use global_par, only:rho, g, ...

    real(r_4), intent(in) :: Psi_solo, Psi_g, P50, vulnerability_curve
    real(r_4) :: V

    real(r_4) :: Psi_soil
    real(r_4) :: Psi_g
    real(r_4) ::       

    V = 1.0 / (1.0 + ((Psi_solo - Psi_g) / P50) ** vulnerability_curve)

 end function


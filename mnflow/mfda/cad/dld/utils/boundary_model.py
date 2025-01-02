# ----------------------------------------------------------------------------
# Copyright (c) 2024 Aryan Mehboudi
# Licensed under the GNU Affero General Public License v3 or later (AGPLv3+).
# You should have received a copy of the License along with the code. If not,
# see <https://www.gnu.org/licenses/>.
# ----------------------------------------------------------------------------


import numpy as np
from scipy.optimize import bisect


def _residual_3d_boundary_treatment(
    this_pitch_w,
    Np,
    pitch_w,
    pitch_a,
    diameter,
    height,
    dep_side,
    row,
    phi,
    acc_Nth_lat,
):
    """Evaluate the residual of given pitch_w for a given DLD system; to be
    used to find the correct pitch_w.

    Aiming at solving the following equation for this_pitch_w:

    dep side:
        this_R=R_b/(n.eps) : R_b denotes the resistance of a unit cell in
        bulk of domain
        this_ --> this boundary unit
        _b    --> bulk
        this_R/R_b = 1/(n.eps) ---Eq.2---> = pitch_w/this_pitch_w.this_f/f,
        wherein f denotes the whole correction factor for bulk, and this_f is
        that of this bounary unit.
        =>  pitch_w/this_pitch_w.this_f/f=Np/n
        Finally:
        ``this_f/this_pitch_w=f/pitch_w*Np/n``,


    acc side:
        - n<Np:
            this_R=R_b/(2-n.eps)
            this_R/R_b = 1/(2-n.eps)
            ---Eq.2---> = pitch_w/this_pitch_w.this_f/f
            pitch_w/this_pitch_w.this_f/f=Np/(2.Np-n)

            Finally:
            ``this_f/this_pitch_w=f/pitch_w*Np/(2.Np-n)``

        - n=Np:
            this_R+R_lat=R_b_axial+R_b_lateral.eps

            We define ``omega=R_b_lateral/R_b_axial``. Therefore:
            this_R+R_lat=R_b_axial(1+eps.omega)

            ``omega`` can be calculated as follows:
            omega=R_b_lateral/R_b_axial
            =[pitch_w/pitch_a.f(pitch_a)]/[pitch_a/pitch_w.f(pitch_w)],
            wherein ``f`` denotes the resistance correction factor (the
            bracket in Eq. 2 (Inglis et. al. 2020)).

            The expression for ``omega`` can be simplified into:
            omega=(pitch_w/pitch_a)**2.f(pitch_a)/f(pitch_w)

            From pressure balance:
            this_R+R_lat=R_b_axial(1+eps.omega)
            assume R_lat=phi.this_R
            this_R(1+phi)=R_b_axial(1+eps.omega)
            this_R/R_b_axial=(1+eps.omega)/(1+phi)
            -->
            [f(this_pitch_w)/this_pitch_w]/[f(pitch_w)/pitch_w]
            =(1+eps.omega)/(1+phi)

            Finally:
            f(this_pitch_w)/this_pitch_w=
                f(pitch_w)/pitch_w.(1+eps.omega)/(1+phi)


            #--- Lateral gap
            Also, from above we have the following for ``R_acc_N_lat``:
            this_R/R_b_axial=(1+eps.omega)/(1+phi)
            =>
            phi.this_R/R_b_axial=phi.(1+eps.omega)/(1+phi)
            R_lat/R_b_axial=phi.(1+eps.omega)/(1+phi)

            We know the following
            R_lat/R_b_axial=
            [pitch_w/this_pitch_w.f(this_pitch_w)]/[pitch_a/pitch_w.f(pitch_w)]
            which, from above, is equal to phi.(1+eps.omega)/(1+phi)

            Finally:
            f(this_pitch_w)/this_pitch_w=
                phi.pitch_a/pitch_w.[f(pitch_w)/pitch_w].(1+eps.omega)/(1+phi)

            Note:
                For `R_acc_N_lat`, the orientaion is 90-deg different from that
                of R_b (resistance of unit cell in bulk region in axial
                direction) as `R_acc_N_lat` is in the lateral direction.
                That is, ``this_pitch_w``, herein, denotes the axial pitch of
                Nth lateral resistance. As the axial pitch is fixed, the
                difference of the axial pitch values show the gap widening
                required through cutting the pillars.
    """

    # make sure row is in the range
    row %= Np
    if row == 0:
        row = Np

    # valid range
    D_over_W_valid_range = [0.3, 0.9]
    T_over_W_valid_range = [0.5, 4.5]

    # identifiers with same names as in original work
    T = height
    D = diameter
    W = pitch_w
    L = pitch_a

    D_over_W = D / W
    T_over_W = T / W

    if D_over_W < D_over_W_valid_range[0] or D_over_W > D_over_W_valid_range[1]:
        print(
            f"""(boundary_treatment='3d') Warning:
D/W={D_over_W} while the valid range is {D_over_W_valid_range}"""
        )
    if T_over_W < T_over_W_valid_range[0] or T_over_W > T_over_W_valid_range[1]:
        print(
            f"""(boundary_treatment='3d') Warning:
T/W={T_over_W} while the valid range is {T_over_W_valid_range}"""
        )

    # resistance correction factor for flow along axis of channel
    f_a = correction_factor(D, W, T)

    # resistance correction factor for flow along width of channel
    f_w = correction_factor(D, L, T)

    # resistance correction factor for this local flow;
    # ``this_pitch_w``: pitch normal to local flow
    this_f = correction_factor(D, this_pitch_w, T)

    # ------------------------------------------------------------------------
    # nondim params
    # pitch_ratio: lateral pitch over axial pitch
    # omega: resistance ratio of bulk grid (lateral over axial): R_b_l/R_b_a
    # ------------------------------------------------------------------------
    pitch_ratio = pitch_w / pitch_a
    omega = pitch_ratio**2.0 * f_w / f_a

    # --- different cases
    #
    # General form:
    #
    # this_R = R_b_axial * psi
    #
    if dep_side:
        psi = Np / row
    else:
        eps = 1.0 / Np
        if row == Np and phi is not None:
            # axial resistance of Nth row on acc side
            psi = (1 + eps * omega) / (1 + phi)

            # lateral resistance of Nth row on acc side
            if acc_Nth_lat:
                psi *= phi / pitch_ratio
        else:
            psi = Np / (2 * Np - row)

    # --- residual
    lhs = this_f / this_pitch_w
    rhs = f_a / pitch_w * psi

    return lhs - rhs


def correction_factor(D, W, T):
    """Returns the correction factor in the bracket in Eq. 2 (Inglis et.
    al. 2020)."""

    # fit params
    a = 1.702
    b = 0.600
    c = 2.682
    d = 1.833

    f = 1.0 + a * (b + np.tan(np.pi / 2.0 * D / W)) ** c * (T / W) ** d

    return f


def get_gap_w_3d_boundary_treatment(
    Np,
    pitch_w,
    pitch_a,
    diameter,
    height,
    dep_side,
    row,
    phi,
    acc_Nth_lat,
    estimate=None,
    verbose=True,
):
    """Get gap_w for a DLD system" """

    if estimate is None:
        estimate = pitch_w

    args = (
        Np,
        pitch_w,
        pitch_a,
        diameter,
        height,
        dep_side,
        row,
        phi,
        acc_Nth_lat,
    )

    # --- ``root`` does not allow lower bound, which causes issue as there are
    # typically multiple non-physical roots for negative gaps (pitch<diameter).
    # msg = root(
    #     fun=_residual_3d_boundary_treatment,
    #     x0=estimate,
    #     args=args,
    #     method='lm',
    # )
    # this_pitch_w=msg.x[0]

    # Small number as the minimum allowed gap
    _EPSILON = 1e-15

    # --- range to examine to find solution
    lower_bound = diameter + _EPSILON  # the case of gap~0
    upper_bound = 10 * pitch_w

    # --- Both ``brentq`` & ``bisect`` work well
    this_pitch_w, msg = bisect(
        _residual_3d_boundary_treatment,
        lower_bound,
        upper_bound,
        args=args,
        maxiter=1000,
        xtol=1e-15,
        full_output=True,
    )

    # --- ``root_scalar`` can be used as well
    # sol = root_scalar(
    #     _residual_3d_boundary_treatment,
    #     args=args,
    #     method='toms748',
    #     bracket=[lower_bound, upper_bound])
    # this_pitch_w=sol.root

    # --- gap and residual
    this_gap_w = this_pitch_w - diameter
    residual = _residual_3d_boundary_treatment(this_pitch_w, *args)

    # --- check desired tolerance --

    # a representative of the magnitude of terms on rhs of equation to be
    # solved (f/pitch_w*Np)
    residual_mag_ref = (
        correction_factor(D=diameter, W=pitch_w, T=height) / pitch_w * Np
    )

    # residual relative to ref. magnitude of terms in equation to be solved.
    residual_rel = residual / residual_mag_ref

    # desired tol: this means we want the absolute residual, i.e.,
    # ``residual`` to be smaller than ``atol*residual_mag_ref``. Equivalently,
    # ``residual_rel`` needs to be smaller than ``atol``.

    atol = 1e-6
    # rtol=1e-5 #not needed for rel. residual
    check_tol = np.isclose(0.0, residual_rel, atol=atol)

    if not check_tol:
        print(
            f"""Warning: Root found for row {row} on
{'dep. side' if dep_side else 'acc. side'} is {this_pitch_w:.3e}.
The rel. residual is {residual_rel:.3e} and does NOT meet the specified
residual tolerance of atol: {atol:.1e}."""
        )

    if verbose:
        print("msg: ", msg)
        print("sol: ", this_pitch_w)
        print("residual:", residual)
        print("check tol:", check_tol)

    return this_gap_w

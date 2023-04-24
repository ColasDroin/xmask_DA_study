
import pickle
import xtrack as xt

# Load collider
collider = xt.Multiline.from_json(f"collider_tuned_bb_on.json")
collider.build_trackers()

# Compute footprint
fp_polar_xm = collider["lhcb1"].get_footprint(
    nemitt_x=2.5e-6,
    nemitt_y=2.5e-6,
    n_turns=2000,
    linear_rescale_on_knobs=[
        xt.LinearRescale(knob_name="beambeam_scale", v0=0.0, dv=0.05)
    ],
)

# Save footprint
with open(f"fp_polar_xm.pkl", "wb") as f:
    pickle.dump([fp_polar_xm.qx, fp_polar_xm.qy], f)
            
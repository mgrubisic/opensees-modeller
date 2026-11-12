"""Nonlinear static pushover analysis (NSPA) of the 3D model in src/mdof3d,
in X and Y directions. 3D counterpart of run_nspa_mdof2d.py.
"""
# Import installed packages
from pathlib import Path
import numpy as np  # used for array operations
import matplotlib.pyplot as plt  # used for plotting
from matplotlib import font_manager
import openseespy.opensees as ops

# Import the methods to build the 3D model and run pushover analyses
from src.mdof3d.model import build_model
from src.mdof3d.nspa import do_nspa_x, do_nspa_y

# --------------------------------------------------
# Plot style
# --------------------------------------------------
ONYX = "#2E3532"
COLORS = {"x": "#26577C", "y": "#E55604"}  # lapis-lazuli, persimmon
LINESTYLES = {"x": "-", "y": "--"}
plt.rcParams.update({
    "text.color": ONYX, "axes.labelcolor": ONYX, "axes.edgecolor": ONYX,
    "xtick.color": ONYX, "ytick.color": ONYX,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": "#E3E5E4", "axes.axisbelow": True,
    "legend.frameon": False, "axes.titleweight": 600,
})
try:  # use Montserrat if it is installed
    font_manager.findfont("Montserrat", fallback_to_default=False)
    plt.rcParams["font.family"] = "Montserrat"
except ValueError:
    pass

# --------------------------------------------------
# Paths
# --------------------------------------------------
path = Path(__file__).parent
outputs_dir = path / "outputs" / "NSPA_3D"
outputs_dir.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# Analyses
# --------------------------------------------------
# Total weight, sum of vertical support reactions under gravity loads
build_model()
ops.reactions()
total_weight = sum(ops.nodeReaction(node, 3) for node in ops.getFixedNodes())
ops.wipe()

# Perform Pushover Analyses in X and Y
do_nspa_x(outsdir=outputs_dir)
do_nspa_y(outsdir=outputs_dir)

# Storey heights, i.e., floor levels above the base, and interstorey heights
floor_levels = np.atleast_1d(np.loadtxt(outputs_dir / "storey_heights.out"))
storey_heights = np.diff(np.insert(floor_levels, 0, 0))
storeys = np.arange(len(floor_levels) + 1)  # storey IDs, 0 is the base

# Read the outputs
results = {}
for d in ["x", "y"]:
    # Floor displacements, each row is a step, each column is a floor
    disp = np.loadtxt(outputs_dir / f"storey_displacements_{d}.out", ndmin=2)
    # Support reactions, each row is a step, each column is a support
    reactions = np.loadtxt(outputs_dir / f"support_reactions_{d}.out",
                           ndmin=2)
    # Add the initial (zero) state
    disp = np.vstack([np.zeros(disp.shape[1]), disp])
    base_shear = np.insert(np.abs(np.sum(reactions, axis=1)), 0, 0)
    # Interstorey drifts [%]
    drifts = np.diff(np.insert(disp, 0, 0, axis=1), axis=1) \
        / storey_heights * 100
    results[d] = {
        "disp": disp,
        "base_shear": base_shear,
        "drifts": drifts,
        "step": np.argmax(base_shear),  # step of peak base shear
    }
    print(f"NSPA-{d.upper()}: peak base shear = {base_shear.max():.1f} kN, "
          f"V/W = {base_shear.max() / total_weight:.3f}")
print(f"Total weight = {total_weight:.1f} kN")

# --------------------------------------------------
# Plots
# --------------------------------------------------
# Plot the pushover curves
fig, ax = plt.subplots()
for d, res in results.items():
    ax.plot(res["disp"][:, -1], res["base_shear"], color=COLORS[d],
            linestyle=LINESTYLES[d], label=f"{d.upper()}-dir")
ax.set_xlabel("Roof Displacement [m]")
ax.set_ylabel("Base Shear [kN]")
ax.legend()
fig.savefig(outputs_dir / "nspa-1.png", dpi=150, bbox_inches="tight")

# Plot the pushover curves as max. drift vs base shear coeff.
fig, ax = plt.subplots()
for d, res in results.items():
    max_drifts = np.max(np.abs(res["drifts"]), axis=1)
    ax.plot(max_drifts, res["base_shear"] / total_weight, color=COLORS[d],
            linestyle=LINESTYLES[d], label=f"{d.upper()}-dir")
ax.set_xlabel("Maximum Interstorey Drift [%]")
ax.set_ylabel("Base Shear Coefficient [V/W]")
ax.legend(loc="lower right")
fig.savefig(outputs_dir / "nspa-2.png", dpi=150, bbox_inches="tight")

# Plot the displacement profiles at peak force
fig, ax = plt.subplots()
for d, res in results.items():
    disps_peak = np.append(0, res["disp"][res["step"], :])
    ax.plot(disps_peak, storeys, color=COLORS[d], linestyle=LINESTYLES[d],
            marker="o", label=f"{d.upper()}-dir")
ax.set_xlabel("Displacement at Peak Base Shear [m]")
ax.set_ylabel("Storey #")
ax.set_yticks(storeys)
ax.legend()
fig.savefig(outputs_dir / "nspa-3.png", dpi=150, bbox_inches="tight")

# Plot the storey drift profiles at peak force, as a step function
fig, ax = plt.subplots()
for d, res in results.items():
    drifts_peak = res["drifts"][res["step"], :]
    X = np.repeat(drifts_peak, 2)
    Y = np.repeat(storeys, 2)[1:-1]
    ax.plot(X, Y, color=COLORS[d], linestyle=LINESTYLES[d],
            label=f"{d.upper()}-dir")
ax.set_xlabel("Interstorey Drift at Peak Base Shear [%]")
ax.set_ylabel("Storey #")
ax.set_yticks(storeys)
ax.set_xlim(left=0)
ax.legend()
fig.savefig(outputs_dir / "nspa-4.png", dpi=150, bbox_inches="tight")

plt.show()
plt.close("all")

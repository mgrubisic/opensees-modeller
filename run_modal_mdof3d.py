"""Modal analysis of the 3D model in src/mdof3d, plots the mode shapes in X,
Y and torsion. 3D counterpart of run_moda_mdof2d.py.
"""
# Import installed packages
from pathlib import Path
import numpy as np  # used for array operations
import matplotlib.pyplot as plt  # used for plotting
from matplotlib import font_manager

# Import the method to run modal analysis for the 3D model
from src.mdof3d.modal import do_modal

# --------------------------------------------------
# Plot style
# --------------------------------------------------
ONYX = "#2E3532"
# lapis-lazuli, persimmon, butterscotch
STYLES = [
    {"color": "#26577C", "linestyle": "-", "marker": None},
    {"color": "#E55604", "linestyle": "--", "marker": None},
    {"color": "#ED9B3A", "linestyle": ":", "marker": "o"},
]
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
results_dir = path / "src" / "mdof3d" / "Modal-Results"  # set in modal.py
outputs_dir = path / "outputs" / "MA_3D"
outputs_dir.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# Analysis
# --------------------------------------------------
num_modes = 3
# Perform modal analysis
results = do_modal(num_modes=num_modes)

# Periods and modal mass ratios [%]
periods = results["eigenPeriod"]
mx = results["partiMassRatiosMX"]
my = results["partiMassRatiosMY"]
rmz = results["partiMassRatiosRMZ"]
print("Mode  T [s]   MX [%]  MY [%]  RMZ [%]")
for i in range(num_modes):
    print(f"{i + 1:>4}  {periods[i]:.3f}  {mx[i]:6.1f}  {my[i]:6.1f}  "
          f"{rmz[i]:6.1f}")

# Radius of gyration of the floor masses about the vertical axis, used to
# express the floor rotations as equivalent displacements, r * rz
free_mass = results["totalFreeMass"]  # MX, MY, MZ, RMX, RMY, RMZ
radius = np.sqrt(free_mass[5] / free_mass[0])

# --------------------------------------------------
# Plot the mode shapes
# --------------------------------------------------
fig, axes = plt.subplots(1, 3, sharey=True, figsize=(11, 4.5))
for i in range(num_modes):
    # Read the eigenvectors of the ith mode
    # Each row contains: node id, ux, uy, uz, rx, ry, rz
    eigen_vectors = np.loadtxt(
        results_dir / f"EigenVectors_Mode{i + 1}.txt", delimiter=",",
        ndmin=2)
    # Eigen vectors in X, Y and torsion, with zero at the base
    fis = [np.append(0, eigen_vectors[:, 1]),
           np.append(0, eigen_vectors[:, 2]),
           np.append(0, radius * eigen_vectors[:, 6])]
    # Normalize all by the largest component of the ith mode, so that the
    # dominant direction of the mode is visible, and make it positive
    fi_max = np.concatenate(fis)
    fi_max = fi_max[np.argmax(np.abs(fi_max))]

    storeys = np.arange(len(fis[0]))  # storey IDs, 0 is the base
    label = f"Mode-{i + 1} (T = {periods[i]:.3f} s)"
    for ax, fi in zip(axes, fis):
        ax.plot(fi / fi_max, storeys, label=label, **STYLES[i % len(STYLES)])

titles = ["X-dir", "Y-dir", "Torsion"]
xlabels = ["Normalised Displacement in X-dir",
           "Normalised Displacement in Y-dir",
           r"Normalised Rotation, $r \cdot \theta_z$"]
for ax, title, xlabel in zip(axes, titles, xlabels):
    ax.axvline(0, color=ONYX, linewidth=0.8)
    ax.set_xlim(-1.1, 1.1)
    ax.set_xlabel(xlabel)
    ax.set_title(title)
axes[0].set_ylabel("Storey ID")
axes[0].set_yticks(storeys)
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc="lower center", ncol=num_modes,
           bbox_to_anchor=(0.5, 1.0))
# Save the figure
fig.savefig(outputs_dir / "mode-shapes.png", dpi=150, bbox_inches="tight")
# Show the figure on the screen
plt.show()

# Import installed packages
from pathlib import Path
import numpy as np  # used for array operations
import matplotlib.pyplot as plt  # used for plotting

# Import the method to run modal analysis for the RC frame
from src.mdof2d.model import run_modal

# Output directory, relative to this script so it works from any working dir
outputs_dir = Path(__file__).parent / "outputs" / "MA"

# Perform modal analysis
run_modal(outsdir=outputs_dir.as_posix(), num_modes=3)

# List of storey numbers
storeys = [0, 1, 2, 3]

# Loop through each mode
for i in range(3):
    # Read the eigenvectors the ith mode
    # Each row contains: node id, ux, uy, uz, rx, ry, rz
    eigen_vectors = np.loadtxt(outputs_dir / f'EigenVectors_Mode{i+1}.txt',
                               delimiter=',')
    # Eigen vector in X-dir
    fi_x = np.append(0, eigen_vectors[:, 1])
    # Normalize eigen vector for the ith mode
    fi_x = fi_x / np.max(np.abs(fi_x))
    # plot mode shape
    plt.plot(fi_x, storeys, label=f'Mode-{i+1}')
    # Set y-axis label
    plt.ylabel('Storey ID')
    # Set x-axis label
    plt.xlabel('Displacement in X-dir')

# Add legends to the figure (mode #)
plt.legend()
# Save the figure
plt.savefig(outputs_dir / 'mode-shapes.png', dpi=100)
# Show the figure on the screen
plt.show()

from pathlib import Path
from src.rcmrf import RCMRF
from src.utilities import create_path


path = Path(__file__).parent
outputs_dir = path / "outputs" / "IDA"
create_path(outputs_dir)

gmdir = path / "data/IDA-Records"

gmfilenames = ["names_x.txt", "names_y.txt", "dts.txt"]

model = RCMRF(
    analysis_options=["ida"],
    export_dir=outputs_dir,
    gm_folder=gmdir,
    gm_filenames=gmfilenames,
    dcap=5,
    analysis_time_step=0.002,
    model='mdof3d',
    workers=10
)

model.modeller()
model.wipe()

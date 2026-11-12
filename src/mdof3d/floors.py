import openseespy.opensees as ops


def add_floors() -> None:
    """Add floors to ops domain (retained nodes & diaphrams).
    """
    # Floor no. 1
    # Retained floor node
    ops.node(90000001, 13.625, 5.68732438, 2.7)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 90000001, 10000001, 10010001, 10020001, 10030001, 10040001, 10050001, 10000101, 10010101, 10020101, 10030101, 10040101, 10050101, 10000201, 10010201, 10020201, 10030201, 10040201, 10050201, 10000301, 10010301, 10020301, 10030301, 10040301, 10050301)
    # Fix the floating dofs of the retained node
    ops.fix(90000001, 0, 0, 1, 1, 1, 0)

    # Floor no. 2
    # Retained floor node
    ops.node(90000002, 13.625, 5.68588811, 5.4)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 90000002, 10000002, 10010002, 10020002, 10030002, 10040002, 10050002, 10000102, 10010102, 10020102, 10030102, 10040102, 10050102, 10000202, 10010202, 10020202, 10030202, 10040202, 10050202, 10000302, 10010302, 10020302, 10030302, 10040302, 10050302)
    # Fix the floating dofs of the retained node
    ops.fix(90000002, 0, 0, 1, 1, 1, 0)

    # Floor no. 3
    # Retained floor node
    ops.node(90000003, 13.625, 5.68455683, 8.1)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 90000003, 10000003, 10010003, 10020003, 10030003, 10040003, 10050003, 10000103, 10010103, 10020103, 10030103, 10040103, 10050103, 10000203, 10010203, 10020203, 10030203, 10040203, 10050203, 10000303, 10010303, 10020303, 10030303, 10040303, 10050303)
    # Fix the floating dofs of the retained node
    ops.fix(90000003, 0, 0, 1, 1, 1, 0)

    # Floor no. 4
    # Retained floor node
    ops.node(90000004, 13.625, 5.6848428, 10.8)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 90000004, 10000004, 10010004, 10020004, 10030004, 10040004, 10050004, 10000104, 10010104, 10020104, 10030104, 10040104, 10050104, 10000204, 10010204, 10020204, 10030204, 10040204, 10050204, 10000304, 10010304, 10020304, 10030304, 10040304, 10050304)
    # Fix the floating dofs of the retained node
    ops.fix(90000004, 0, 0, 1, 1, 1, 0)

    # Floor no. 5
    # Retained floor node
    ops.node(90000005, 13.625, 5.69614495, 13.5)
    # Rigid floor diaphragm - multi-point constraints
    ops.rigidDiaphragm(3, 90000005, 10000005, 10010005, 10020005, 10030005, 10040005, 10050005, 10000105, 10010105, 10020105, 10030105, 10040105, 10050105, 10000205, 10010205, 10020205, 10030205, 10040205, 10050205, 10000305, 10010305, 10020305, 10030305, 10040305, 10050305)
    # Fix the floating dofs of the retained node
    ops.fix(90000005, 0, 0, 1, 1, 1, 0)

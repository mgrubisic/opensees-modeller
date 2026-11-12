import openseespy.opensees as ops


def add_joints() -> None:
    """Add components of joints to ops domain.
    """
    # -------------------------------------------------
    # Add stairs joints to ops domain
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (2, 0, 0.5)
    ops.node(1020001, 12.2, 0.0, 1.35, '-mass', 2.384554587155965, 2.384554587155965, 2.384554587155965, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (3, 0, 0.5)
    ops.node(1030001, 15.05, 0.0, 1.35, '-mass', 2.384554587155965, 2.384554587155965, 2.384554587155965, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (2, 0, 1.5)
    ops.node(1020002, 12.2, 0.0, 4.05, '-mass', 2.384554587155965, 2.384554587155965, 2.384554587155965, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (3, 0, 1.5)
    ops.node(1030002, 15.05, 0.0, 4.05, '-mass', 2.384554587155965, 2.384554587155965, 2.384554587155965, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (2, 0, 2.5)
    ops.node(1020003, 12.2, 0.0, 6.75, '-mass', 2.2937288990825704, 2.2937288990825704, 2.2937288990825704, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (3, 0, 2.5)
    ops.node(1030003, 15.05, 0.0, 6.75, '-mass', 2.2937288990825704, 2.2937288990825704, 2.2937288990825704, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (2, 0, 3.5)
    ops.node(1020004, 12.2, 0.0, 9.45, '-mass', 2.2937288990825704, 2.2937288990825704, 2.2937288990825704, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (3, 0, 3.5)
    ops.node(1030004, 15.05, 0.0, 9.45, '-mass', 2.2937288990825704, 2.2937288990825704, 2.2937288990825704, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (2, 0, 4.5)
    ops.node(1020005, 12.2, 0.0, 12.15, '-mass', 2.2937288990825704, 2.2937288990825704, 2.2937288990825704, 0.0, 0.0, 0.0)

    # Joint grid ids (x, y, z): (3, 0, 4.5)
    ops.node(1030005, 15.05, 0.0, 12.15, '-mass', 2.2937288990825704, 2.2937288990825704, 2.2937288990825704, 0.0, 0.0, 0.0)

    # -------------------------------------------------
    # Add floor joints to ops domain
    # -------------------------------------------------
    # Joint grid ids (x, y, z): (0, 0, 1)
    ops.node(1, 0.0, 0.0, 2.7, '-mass', 5.471419294247547, 5.471419294247547, 5.471419294247547, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10000001, 0.0, 0.0, 2.7) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 131, 42.35768192, 0.0002, 42.35768192, 0.0132, 24.27240826, 0.027, -42.35768192, -0.0002, -42.35768192, -0.0132, -24.27240826, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 141, 85.82386795, 0.0002, 85.82386795, 0.0132, 47.14665933, 0.027, -85.82386795, -0.0002, -85.82386795, -0.0132, -47.14665933, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 130, 131, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 140, 141, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 150, 7125000.0)
    ops.section('Aggregator', 10000001, 150, 'P', 99999, 'Vy', 99999, 'Vz', 140, 'My', 130, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10000001, 1, 10000001, 10000001, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 0, 1)
    ops.node(10001, 6.1, 0.0, 2.7, '-mass', 10.083847762807022, 10.083847762807022, 10.083847762807022, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10010001, 6.1, 0.0, 2.7) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 1000131, 76.38533253, 0.0002, 76.38533253, 0.0132, 44.44215985, 0.027, -76.38533253, -0.0002, -76.38533253, -0.0132, -44.44215985, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 1000141, 186.41733381, 0.0002, 235.26989715, 0.009, 235.26989715, 0.02, -186.41733381, -0.0002, -235.26989715, -0.009, -235.26989715, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 1000130, 1000131, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 1000140, 1000141, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 1000150, 13965000.0)
    ops.section('Aggregator', 10010001, 1000150, 'P', 99999, 'Vy', 99999, 'Vz', 1000140, 'My', 1000130, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10010001, 10001, 10010001, 10010001, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 0, 1)
    ops.node(20001, 12.2, 0.0, 2.7, '-mass', 5.945251404339291, 5.945251404339291, 5.945251404339291, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10020001, 12.2, 0.0, 2.7) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 2000131, 81.28876399, 0.0002, 81.28876399, 0.0132, 46.64472753, 0.027, -81.28876399, -0.0002, -81.28876399, -0.0132, -46.64472753, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 2000141, 170.56450054, 0.0002, 214.78081222, 0.009, 214.78081222, 0.02, -170.56450054, -0.0002, -214.78081222, -0.009, -214.78081222, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 2000130, 2000131, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 2000140, 2000141, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 2000150, 10260000.0)
    ops.section('Aggregator', 10020001, 2000150, 'P', 99999, 'Vy', 99999, 'Vz', 2000140, 'My', 2000130, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10020001, 20001, 10020001, 10020001, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 0, 1)
    ops.node(30001, 15.05, 0.0, 2.7, '-mass', 5.94525140433929, 5.94525140433929, 5.94525140433929, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10030001, 15.05, 0.0, 2.7) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 3000131, 81.28876399, 0.0002, 81.28876399, 0.0132, 46.64472753, 0.027, -81.28876399, -0.0002, -81.28876399, -0.0132, -46.64472753, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 3000141, 170.56450054, 0.0002, 214.78081222, 0.009, 214.78081222, 0.02, -170.56450054, -0.0002, -214.78081222, -0.009, -214.78081222, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 3000130, 3000131, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 3000140, 3000141, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 3000150, 10260000.0)
    ops.section('Aggregator', 10030001, 3000150, 'P', 99999, 'Vy', 99999, 'Vz', 3000140, 'My', 3000130, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10030001, 30001, 10030001, 10030001, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (4, 0, 1)
    ops.node(40001, 21.15, 0.0, 2.7, '-mass', 10.083847762807022, 10.083847762807022, 10.083847762807022, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10040001, 21.15, 0.0, 2.7) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 4000131, 76.38533253, 0.0002, 76.38533253, 0.0132, 44.44215985, 0.027, -76.38533253, -0.0002, -76.38533253, -0.0132, -44.44215985, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 4000141, 186.41733381, 0.0002, 235.26989715, 0.009, 235.26989715, 0.02, -186.41733381, -0.0002, -235.26989715, -0.009, -235.26989715, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 4000130, 4000131, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 4000140, 4000141, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 4000150, 13965000.0)
    ops.section('Aggregator', 10040001, 4000150, 'P', 99999, 'Vy', 99999, 'Vz', 4000140, 'My', 4000130, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10040001, 40001, 10040001, 10040001, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (5, 0, 1)
    ops.node(50001, 27.25, 0.0, 2.7, '-mass', 5.471419294247549, 5.471419294247549, 5.471419294247549, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10050001, 27.25, 0.0, 2.7) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 5000131, 42.35768192, 0.0002, 42.35768192, 0.0132, 24.27240826, 0.027, -42.35768192, -0.0002, -42.35768192, -0.0132, -24.27240826, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 5000141, 85.82386795, 0.0002, 85.82386795, 0.0132, 47.14665933, 0.027, -85.82386795, -0.0002, -85.82386795, -0.0132, -47.14665933, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 5000130, 5000131, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 5000140, 5000141, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 5000150, 7125000.0)
    ops.section('Aggregator', 10050001, 5000150, 'P', 99999, 'Vy', 99999, 'Vz', 5000140, 'My', 5000130, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10050001, 50001, 10050001, 10050001, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 1, 1)
    ops.node(101, 0.0, 3.75, 2.7, '-mass', 9.378525438648001, 9.378525438648001, 9.378525438648001, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10000101, 0.0, 3.75, 2.7) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 10131, 85.33509463, 0.0002, 106.7610975, 0.009, 106.7610975, 0.02, -85.33509463, -0.0002, -106.7610975, -0.009, -106.7610975, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 10141, 184.61441409, 0.0002, 184.61441409, 0.0132, 101.92442123, 0.027, -184.61441409, -0.0002, -184.61441409, -0.0132, -101.92442123, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 10130, 10131, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 10140, 10141, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 10150, 7892307.69230769)
    ops.section('Aggregator', 10000101, 10150, 'P', 99999, 'Vy', 99999, 'Vz', 10140, 'My', 10130, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10000101, 101, 10000101, 10000101, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 1, 1)
    ops.node(10101, 6.1, 3.75, 2.7, '-mass', 17.220720602066645, 17.220720602066645, 17.220720602066645, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10010101, 6.1, 3.75, 2.7) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 1010131, 160.81168321, 0.0002, 203.21890882, 0.009, 203.21890882, 0.02, -160.81168321, -0.0002, -203.21890882, -0.009, -203.21890882, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 1010141, 408.01179933, 0.0002, 516.68048286, 0.009, 516.68048286, 0.02, -408.01179933, -0.0002, -516.68048286, -0.009, -516.68048286, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 1010130, 1010131, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 1010140, 1010141, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 1010150, 17757692.30769231)
    ops.section('Aggregator', 10010101, 1010150, 'P', 99999, 'Vy', 99999, 'Vz', 1010140, 'My', 1010130, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10010101, 10101, 10010101, 10010101, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 1, 1)
    ops.node(20101, 12.2, 3.75, 2.7, '-mass', 13.302490830072276, 13.302490830072276, 13.302490830072276, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10020101, 12.2, 3.75, 2.7) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 2010131, 131.90425519, 0.0002, 165.58331899, 0.009, 165.58331899, 0.02, -131.90425519, -0.0002, -165.58331899, -0.009, -165.58331899, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 2010141, 272.35244172, 0.0002, 341.8920881, 0.009, 341.8920881, 0.02, -272.35244172, -0.0002, -341.8920881, -0.009, -341.8920881, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 2010130, 2010131, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 2010140, 2010141, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 2010150, 10742307.69230769)
    ops.section('Aggregator', 10020101, 2010150, 'P', 99999, 'Vy', 99999, 'Vz', 2010140, 'My', 2010130, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10020101, 20101, 10020101, 10020101, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 1, 1)
    ops.node(30101, 15.05, 3.75, 2.7, '-mass', 13.302490830072275, 13.302490830072275, 13.302490830072275, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10030101, 15.05, 3.75, 2.7) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 3010131, 131.90425519, 0.0002, 165.58331899, 0.009, 165.58331899, 0.02, -131.90425519, -0.0002, -165.58331899, -0.009, -165.58331899, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 3010141, 272.35244172, 0.0002, 341.8920881, 0.009, 341.8920881, 0.02, -272.35244172, -0.0002, -341.8920881, -0.009, -341.8920881, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 3010130, 3010131, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 3010140, 3010141, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 3010150, 10742307.69230769)
    ops.section('Aggregator', 10030101, 3010150, 'P', 99999, 'Vy', 99999, 'Vz', 3010140, 'My', 3010130, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10030101, 30101, 10030101, 10030101, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (4, 1, 1)
    ops.node(40101, 21.15, 3.75, 2.7, '-mass', 17.22072060206665, 17.22072060206665, 17.22072060206665, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10040101, 21.15, 3.75, 2.7) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 4010131, 160.81168321, 0.0002, 203.21890882, 0.009, 203.21890882, 0.02, -160.81168321, -0.0002, -203.21890882, -0.009, -203.21890882, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 4010141, 408.01179933, 0.0002, 516.68048286, 0.009, 516.68048286, 0.02, -408.01179933, -0.0002, -516.68048286, -0.009, -516.68048286, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 4010130, 4010131, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 4010140, 4010141, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 4010150, 17757692.30769231)
    ops.section('Aggregator', 10040101, 4010150, 'P', 99999, 'Vy', 99999, 'Vz', 4010140, 'My', 4010130, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10040101, 40101, 10040101, 10040101, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (5, 1, 1)
    ops.node(50101, 27.25, 3.75, 2.7, '-mass', 9.378525438648005, 9.378525438648005, 9.378525438648005, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10050101, 27.25, 3.75, 2.7) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 5010131, 85.33509463, 0.0002, 106.7610975, 0.009, 106.7610975, 0.02, -85.33509463, -0.0002, -106.7610975, -0.009, -106.7610975, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 5010141, 184.61441409, 0.0002, 184.61441409, 0.0132, 101.92442123, 0.027, -184.61441409, -0.0002, -184.61441409, -0.0132, -101.92442123, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 5010130, 5010131, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 5010140, 5010141, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 5010150, 7892307.69230769)
    ops.section('Aggregator', 10050101, 5010150, 'P', 99999, 'Vy', 99999, 'Vz', 5010140, 'My', 5010130, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10050101, 50101, 10050101, 10050101, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 2, 1)
    ops.node(201, 0.0, 7.5, 2.7, '-mass', 9.378525438648001, 9.378525438648001, 9.378525438648001, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10000201, 0.0, 7.5, 2.7) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 20131, 85.33509463, 0.0002, 106.7610975, 0.009, 106.7610975, 0.02, -85.33509463, -0.0002, -106.7610975, -0.009, -106.7610975, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 20141, 184.61441409, 0.0002, 184.61441409, 0.0132, 101.92442123, 0.027, -184.61441409, -0.0002, -184.61441409, -0.0132, -101.92442123, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 20130, 20131, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 20140, 20141, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 20150, 7892307.69230769)
    ops.section('Aggregator', 10000201, 20150, 'P', 99999, 'Vy', 99999, 'Vz', 20140, 'My', 20130, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10000201, 201, 10000201, 10000201, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 2, 1)
    ops.node(10201, 6.1, 7.5, 2.7, '-mass', 17.220720602066645, 17.220720602066645, 17.220720602066645, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10010201, 6.1, 7.5, 2.7) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 1020131, 160.81168321, 0.0002, 203.21890882, 0.009, 203.21890882, 0.02, -160.81168321, -0.0002, -203.21890882, -0.009, -203.21890882, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 1020141, 408.01179933, 0.0002, 516.68048286, 0.009, 516.68048286, 0.02, -408.01179933, -0.0002, -516.68048286, -0.009, -516.68048286, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 1020130, 1020131, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 1020140, 1020141, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 1020150, 17757692.30769231)
    ops.section('Aggregator', 10010201, 1020150, 'P', 99999, 'Vy', 99999, 'Vz', 1020140, 'My', 1020130, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10010201, 10201, 10010201, 10010201, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 2, 1)
    ops.node(20201, 12.2, 7.5, 2.7, '-mass', 12.699506680212146, 12.699506680212146, 12.699506680212146, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10020201, 12.2, 7.5, 2.7) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 2020131, 129.45582851, 0.0002, 162.76072433, 0.009, 162.76072433, 0.02, -129.45582851, -0.0002, -162.76072433, -0.009, -162.76072433, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 2020141, 267.29699462, 0.0002, 336.06406879, 0.009, 336.06406879, 0.02, -267.29699462, -0.0002, -336.06406879, -0.009, -336.06406879, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 2020130, 2020131, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 2020140, 2020141, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 2020150, 10742307.69230769)
    ops.section('Aggregator', 10020201, 2020150, 'P', 99999, 'Vy', 99999, 'Vz', 2020140, 'My', 2020130, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10020201, 20201, 10020201, 10020201, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 2, 1)
    ops.node(30201, 15.05, 7.5, 2.7, '-mass', 12.699506680212146, 12.699506680212146, 12.699506680212146, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10030201, 15.05, 7.5, 2.7) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 3020131, 129.45582851, 0.0002, 162.76072433, 0.009, 162.76072433, 0.02, -129.45582851, -0.0002, -162.76072433, -0.009, -162.76072433, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 3020141, 267.29699462, 0.0002, 336.06406879, 0.009, 336.06406879, 0.02, -267.29699462, -0.0002, -336.06406879, -0.009, -336.06406879, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 3020130, 3020131, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 3020140, 3020141, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 3020150, 10742307.69230769)
    ops.section('Aggregator', 10030201, 3020150, 'P', 99999, 'Vy', 99999, 'Vz', 3020140, 'My', 3020130, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10030201, 30201, 10030201, 10030201, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (4, 2, 1)
    ops.node(40201, 21.15, 7.5, 2.7, '-mass', 17.22072060206665, 17.22072060206665, 17.22072060206665, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10040201, 21.15, 7.5, 2.7) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 4020131, 160.81168321, 0.0002, 203.21890882, 0.009, 203.21890882, 0.02, -160.81168321, -0.0002, -203.21890882, -0.009, -203.21890882, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 4020141, 408.01179933, 0.0002, 516.68048286, 0.009, 516.68048286, 0.02, -408.01179933, -0.0002, -516.68048286, -0.009, -516.68048286, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 4020130, 4020131, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 4020140, 4020141, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 4020150, 17757692.30769231)
    ops.section('Aggregator', 10040201, 4020150, 'P', 99999, 'Vy', 99999, 'Vz', 4020140, 'My', 4020130, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10040201, 40201, 10040201, 10040201, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (5, 2, 1)
    ops.node(50201, 27.25, 7.5, 2.7, '-mass', 9.378525438648005, 9.378525438648005, 9.378525438648005, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10050201, 27.25, 7.5, 2.7) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 5020131, 85.33509463, 0.0002, 106.7610975, 0.009, 106.7610975, 0.02, -85.33509463, -0.0002, -106.7610975, -0.009, -106.7610975, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 5020141, 184.61441409, 0.0002, 184.61441409, 0.0132, 101.92442123, 0.027, -184.61441409, -0.0002, -184.61441409, -0.0132, -101.92442123, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 5020130, 5020131, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 5020140, 5020141, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 5020150, 7892307.69230769)
    ops.section('Aggregator', 10050201, 5020150, 'P', 99999, 'Vy', 99999, 'Vz', 5020140, 'My', 5020130, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10050201, 50201, 10050201, 10050201, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 3, 1)
    ops.node(301, 0.0, 11.25, 2.7, '-mass', 5.471419294247547, 5.471419294247547, 5.471419294247547, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10000301, 0.0, 11.25, 2.7) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 30131, 42.35768192, 0.0002, 42.35768192, 0.0132, 24.27240826, 0.027, -42.35768192, -0.0002, -42.35768192, -0.0132, -24.27240826, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 30141, 85.82386795, 0.0002, 85.82386795, 0.0132, 47.14665933, 0.027, -85.82386795, -0.0002, -85.82386795, -0.0132, -47.14665933, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 30130, 30131, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 30140, 30141, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 30150, 7125000.0)
    ops.section('Aggregator', 10000301, 30150, 'P', 99999, 'Vy', 99999, 'Vz', 30140, 'My', 30130, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10000301, 301, 10000301, 10000301, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 3, 1)
    ops.node(10301, 6.1, 11.25, 2.7, '-mass', 10.083847762807022, 10.083847762807022, 10.083847762807022, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10010301, 6.1, 11.25, 2.7) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 1030131, 76.38533253, 0.0002, 76.38533253, 0.0132, 44.44215985, 0.027, -76.38533253, -0.0002, -76.38533253, -0.0132, -44.44215985, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 1030141, 186.41733381, 0.0002, 235.26989715, 0.009, 235.26989715, 0.02, -186.41733381, -0.0002, -235.26989715, -0.009, -235.26989715, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 1030130, 1030131, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 1030140, 1030141, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 1030150, 13965000.0)
    ops.section('Aggregator', 10010301, 1030150, 'P', 99999, 'Vy', 99999, 'Vz', 1030140, 'My', 1030130, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10010301, 10301, 10010301, 10010301, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 3, 1)
    ops.node(20301, 12.2, 11.25, 2.7, '-mass', 7.51764752970852, 7.51764752970852, 7.51764752970852, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10020301, 12.2, 11.25, 2.7) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 2030131, 70.57284841, 0.0002, 70.57284841, 0.0132, 40.39088924, 0.027, -70.57284841, -0.0002, -70.57284841, -0.0132, -40.39088924, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 2030141, 137.94858127, 0.0002, 173.98654203, 0.009, 173.98654203, 0.02, -137.94858127, -0.0002, -173.98654203, -0.009, -173.98654203, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 2030130, 2030131, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 2030140, 2030141, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 2030150, 10260000.0)
    ops.section('Aggregator', 10020301, 2030150, 'P', 99999, 'Vy', 99999, 'Vz', 2030140, 'My', 2030130, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10020301, 20301, 10020301, 10020301, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 3, 1)
    ops.node(30301, 15.05, 11.25, 2.7, '-mass', 7.517647529708519, 7.517647529708519, 7.517647529708519, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10030301, 15.05, 11.25, 2.7) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 3030131, 70.57284841, 0.0002, 70.57284841, 0.0132, 40.39088924, 0.027, -70.57284841, -0.0002, -70.57284841, -0.0132, -40.39088924, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 3030141, 137.94858127, 0.0002, 173.98654203, 0.009, 173.98654203, 0.02, -137.94858127, -0.0002, -173.98654203, -0.009, -173.98654203, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 3030130, 3030131, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 3030140, 3030141, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 3030150, 10260000.0)
    ops.section('Aggregator', 10030301, 3030150, 'P', 99999, 'Vy', 99999, 'Vz', 3030140, 'My', 3030130, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10030301, 30301, 10030301, 10030301, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (4, 3, 1)
    ops.node(40301, 21.15, 11.25, 2.7, '-mass', 10.083847762807022, 10.083847762807022, 10.083847762807022, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10040301, 21.15, 11.25, 2.7) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 4030131, 76.38533253, 0.0002, 76.38533253, 0.0132, 44.44215985, 0.027, -76.38533253, -0.0002, -76.38533253, -0.0132, -44.44215985, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 4030141, 186.41733381, 0.0002, 235.26989715, 0.009, 235.26989715, 0.02, -186.41733381, -0.0002, -235.26989715, -0.009, -235.26989715, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 4030130, 4030131, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 4030140, 4030141, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 4030150, 13965000.0)
    ops.section('Aggregator', 10040301, 4030150, 'P', 99999, 'Vy', 99999, 'Vz', 4030140, 'My', 4030130, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10040301, 40301, 10040301, 10040301, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (5, 3, 1)
    ops.node(50301, 27.25, 11.25, 2.7, '-mass', 5.471419294247549, 5.471419294247549, 5.471419294247549, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10050301, 27.25, 11.25, 2.7) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 5030131, 42.35768192, 0.0002, 42.35768192, 0.0132, 24.27240826, 0.027, -42.35768192, -0.0002, -42.35768192, -0.0132, -24.27240826, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 5030141, 85.82386795, 0.0002, 85.82386795, 0.0132, 47.14665933, 0.027, -85.82386795, -0.0002, -85.82386795, -0.0132, -47.14665933, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 5030130, 5030131, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 5030140, 5030141, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 5030150, 7125000.0)
    ops.section('Aggregator', 10050301, 5030150, 'P', 99999, 'Vy', 99999, 'Vz', 5030140, 'My', 5030130, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10050301, 50301, 10050301, 10050301, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 0, 2)
    ops.node(2, 0.0, 0.0, 5.4, '-mass', 5.471419294247547, 5.471419294247547, 5.471419294247547, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10000002, 0.0, 0.0, 5.4) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 231, 39.27071199, 0.0002, 39.27071199, 0.0132, 22.2187658, 0.027, -39.27071199, -0.0002, -39.27071199, -0.0132, -22.2187658, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 241, 80.50621511, 0.0002, 80.50621511, 0.0132, 43.54008025, 0.027, -80.50621511, -0.0002, -80.50621511, -0.0132, -43.54008025, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 230, 231, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 240, 241, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 250, 7125000.0)
    ops.section('Aggregator', 10000002, 250, 'P', 99999, 'Vy', 99999, 'Vz', 240, 'My', 230, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10000002, 2, 10000002, 10000002, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 0, 2)
    ops.node(10002, 6.1, 0.0, 5.4, '-mass', 9.885682625192343, 9.885682625192343, 9.885682625192343, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10010002, 6.1, 0.0, 5.4) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 1000231, 70.45954651, 0.0002, 70.45954651, 0.0132, 40.51071824, 0.027, -70.45954651, -0.0002, -70.45954651, -0.0132, -40.51071824, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 1000241, 171.64495036, 0.0002, 218.38352925, 0.009, 218.38352925, 0.02, -171.64495036, -0.0002, -218.38352925, -0.009, -218.38352925, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 1000230, 1000231, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 1000240, 1000241, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 1000250, 13965000.0)
    ops.section('Aggregator', 10010002, 1000250, 'P', 99999, 'Vy', 99999, 'Vz', 1000240, 'My', 1000230, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10010002, 10002, 10010002, 10010002, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 0, 2)
    ops.node(20002, 12.2, 0.0, 5.4, '-mass', 5.899838560302594, 5.899838560302594, 5.899838560302594, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10020002, 12.2, 0.0, 5.4) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 2000231, 74.91734707, 0.0002, 74.91734707, 0.0132, 42.40577275, 0.027, -74.91734707, -0.0002, -74.91734707, -0.0132, -42.40577275, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 2000241, 156.04182424, 0.0002, 198.14474058, 0.009, 198.14474058, 0.02, -156.04182424, -0.0002, -198.14474058, -0.009, -198.14474058, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 2000230, 2000231, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 2000240, 2000241, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 2000250, 10260000.0)
    ops.section('Aggregator', 10020002, 2000250, 'P', 99999, 'Vy', 99999, 'Vz', 2000240, 'My', 2000230, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10020002, 20002, 10020002, 10020002, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 0, 2)
    ops.node(30002, 15.05, 0.0, 5.4, '-mass', 5.899838560302593, 5.899838560302593, 5.899838560302593, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10030002, 15.05, 0.0, 5.4) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 3000231, 74.91734707, 0.0002, 74.91734707, 0.0132, 42.40577275, 0.027, -74.91734707, -0.0002, -74.91734707, -0.0132, -42.40577275, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 3000241, 156.04182424, 0.0002, 198.14474058, 0.009, 198.14474058, 0.02, -156.04182424, -0.0002, -198.14474058, -0.009, -198.14474058, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 3000230, 3000231, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 3000240, 3000241, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 3000250, 10260000.0)
    ops.section('Aggregator', 10030002, 3000250, 'P', 99999, 'Vy', 99999, 'Vz', 3000240, 'My', 3000230, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10030002, 30002, 10030002, 10030002, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (4, 0, 2)
    ops.node(40002, 21.15, 0.0, 5.4, '-mass', 9.885682625192343, 9.885682625192343, 9.885682625192343, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10040002, 21.15, 0.0, 5.4) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 4000231, 70.45954651, 0.0002, 70.45954651, 0.0132, 40.51071824, 0.027, -70.45954651, -0.0002, -70.45954651, -0.0132, -40.51071824, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 4000241, 171.64495036, 0.0002, 218.38352925, 0.009, 218.38352925, 0.02, -171.64495036, -0.0002, -218.38352925, -0.009, -218.38352925, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 4000230, 4000231, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 4000240, 4000241, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 4000250, 13965000.0)
    ops.section('Aggregator', 10040002, 4000250, 'P', 99999, 'Vy', 99999, 'Vz', 4000240, 'My', 4000230, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10040002, 40002, 10040002, 10040002, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (5, 0, 2)
    ops.node(50002, 27.25, 0.0, 5.4, '-mass', 5.471419294247549, 5.471419294247549, 5.471419294247549, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10050002, 27.25, 0.0, 5.4) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 5000231, 39.27071199, 0.0002, 39.27071199, 0.0132, 22.2187658, 0.027, -39.27071199, -0.0002, -39.27071199, -0.0132, -22.2187658, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 5000241, 80.50621511, 0.0002, 80.50621511, 0.0132, 43.54008025, 0.027, -80.50621511, -0.0002, -80.50621511, -0.0132, -43.54008025, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 5000230, 5000231, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 5000240, 5000241, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 5000250, 7125000.0)
    ops.section('Aggregator', 10050002, 5000250, 'P', 99999, 'Vy', 99999, 'Vz', 5000240, 'My', 5000230, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10050002, 50002, 10050002, 10050002, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 1, 2)
    ops.node(102, 0.0, 3.75, 5.4, '-mass', 9.378525438648001, 9.378525438648001, 9.378525438648001, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10000102, 0.0, 3.75, 5.4) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 10231, 78.3731823, 0.0002, 98.72841083, 0.009, 98.72841083, 0.02, -78.3731823, -0.0002, -98.72841083, -0.009, -98.72841083, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 10241, 173.09826304, 0.0002, 173.09826304, 0.0132, 94.16146296, 0.027, -173.09826304, -0.0002, -173.09826304, -0.0132, -94.16146296, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 10230, 10231, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 10240, 10241, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 10250, 7892307.69230769)
    ops.section('Aggregator', 10000102, 10250, 'P', 99999, 'Vy', 99999, 'Vz', 10240, 'My', 10230, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10000102, 102, 10000102, 10000102, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 1, 2)
    ops.node(10102, 6.1, 3.75, 5.4, '-mass', 16.956500418580408, 16.956500418580408, 16.956500418580408, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10010102, 6.1, 3.75, 5.4) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 1010231, 148.55499947, 0.0002, 189.22562882, 0.009, 189.22562882, 0.02, -148.55499947, -0.0002, -189.22562882, -0.009, -189.22562882, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 1010241, 377.34427454, 0.0002, 481.74381485, 0.009, 481.74381485, 0.02, -377.34427454, -0.0002, -481.74381485, -0.009, -481.74381485, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 1010230, 1010231, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 1010240, 1010241, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 1010250, 17757692.30769231)
    ops.section('Aggregator', 10010102, 1010250, 'P', 99999, 'Vy', 99999, 'Vz', 1010240, 'My', 1010230, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10010102, 10102, 10010102, 10010102, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 1, 2)
    ops.node(20102, 12.2, 3.75, 5.4, '-mass', 13.19515138053099, 13.19515138053099, 13.19515138053099, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10020102, 12.2, 3.75, 5.4) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 2010231, 121.46903571, 0.0002, 153.58575976, 0.009, 153.58575976, 0.02, -121.46903571, -0.0002, -153.58575976, -0.009, -153.58575976, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 2010241, 250.80607462, 0.0002, 317.11984292, 0.009, 317.11984292, 0.02, -250.80607462, -0.0002, -317.11984292, -0.009, -317.11984292, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 2010230, 2010231, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 2010240, 2010241, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 2010250, 10742307.69230769)
    ops.section('Aggregator', 10020102, 2010250, 'P', 99999, 'Vy', 99999, 'Vz', 2010240, 'My', 2010230, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10020102, 20102, 10020102, 10020102, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 1, 2)
    ops.node(30102, 15.05, 3.75, 5.4, '-mass', 13.19515138053099, 13.19515138053099, 13.19515138053099, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10030102, 15.05, 3.75, 5.4) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 3010231, 121.46903571, 0.0002, 153.58575976, 0.009, 153.58575976, 0.02, -121.46903571, -0.0002, -153.58575976, -0.009, -153.58575976, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 3010241, 250.80607462, 0.0002, 317.11984292, 0.009, 317.11984292, 0.02, -250.80607462, -0.0002, -317.11984292, -0.009, -317.11984292, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 3010230, 3010231, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 3010240, 3010241, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 3010250, 10742307.69230769)
    ops.section('Aggregator', 10030102, 3010250, 'P', 99999, 'Vy', 99999, 'Vz', 3010240, 'My', 3010230, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10030102, 30102, 10030102, 10030102, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (4, 1, 2)
    ops.node(40102, 21.15, 3.75, 5.4, '-mass', 16.956500418580408, 16.956500418580408, 16.956500418580408, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10040102, 21.15, 3.75, 5.4) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 4010231, 148.55499947, 0.0002, 189.22562882, 0.009, 189.22562882, 0.02, -148.55499947, -0.0002, -189.22562882, -0.009, -189.22562882, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 4010241, 377.34427454, 0.0002, 481.74381485, 0.009, 481.74381485, 0.02, -377.34427454, -0.0002, -481.74381485, -0.009, -481.74381485, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 4010230, 4010231, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 4010240, 4010241, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 4010250, 17757692.30769231)
    ops.section('Aggregator', 10040102, 4010250, 'P', 99999, 'Vy', 99999, 'Vz', 4010240, 'My', 4010230, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10040102, 40102, 10040102, 10040102, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (5, 1, 2)
    ops.node(50102, 27.25, 3.75, 5.4, '-mass', 9.378525438648005, 9.378525438648005, 9.378525438648005, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10050102, 27.25, 3.75, 5.4) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 5010231, 78.3731823, 0.0002, 98.72841083, 0.009, 98.72841083, 0.02, -78.3731823, -0.0002, -98.72841083, -0.009, -98.72841083, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 5010241, 173.09826304, 0.0002, 173.09826304, 0.0132, 94.16146296, 0.027, -173.09826304, -0.0002, -173.09826304, -0.0132, -94.16146296, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 5010230, 5010231, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 5010240, 5010241, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 5010250, 7892307.69230769)
    ops.section('Aggregator', 10050102, 5010250, 'P', 99999, 'Vy', 99999, 'Vz', 5010240, 'My', 5010230, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10050102, 50102, 10050102, 10050102, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 2, 2)
    ops.node(202, 0.0, 7.5, 5.4, '-mass', 9.378525438648001, 9.378525438648001, 9.378525438648001, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10000202, 0.0, 7.5, 5.4) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 20231, 78.3731823, 0.0002, 98.72841083, 0.009, 98.72841083, 0.02, -78.3731823, -0.0002, -98.72841083, -0.009, -98.72841083, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 20241, 173.09826304, 0.0002, 173.09826304, 0.0132, 94.16146296, 0.027, -173.09826304, -0.0002, -173.09826304, -0.0132, -94.16146296, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 20230, 20231, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 20240, 20241, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 20250, 7892307.69230769)
    ops.section('Aggregator', 10000202, 20250, 'P', 99999, 'Vy', 99999, 'Vz', 20240, 'My', 20230, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10000202, 202, 10000202, 10000202, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 2, 2)
    ops.node(10202, 6.1, 7.5, 5.4, '-mass', 16.956500418580408, 16.956500418580408, 16.956500418580408, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10010202, 6.1, 7.5, 5.4) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 1020231, 148.55499947, 0.0002, 189.22562882, 0.009, 189.22562882, 0.02, -148.55499947, -0.0002, -189.22562882, -0.009, -189.22562882, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 1020241, 377.34427454, 0.0002, 481.74381485, 0.009, 481.74381485, 0.02, -377.34427454, -0.0002, -481.74381485, -0.009, -481.74381485, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 1020230, 1020231, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 1020240, 1020241, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 1020250, 17757692.30769231)
    ops.section('Aggregator', 10010202, 1020250, 'P', 99999, 'Vy', 99999, 'Vz', 1020240, 'My', 1020230, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10010202, 10202, 10010202, 10010202, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 2, 2)
    ops.node(20202, 12.2, 7.5, 5.4, '-mass', 12.592167230670862, 12.592167230670862, 12.592167230670862, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10020202, 12.2, 7.5, 5.4) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 2020231, 119.31186584, 0.0002, 151.11698592, 0.009, 151.11698592, 0.02, -119.31186584, -0.0002, -151.11698592, -0.009, -151.11698592, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 2020241, 246.35200692, 0.0002, 312.02238353, 0.009, 312.02238353, 0.02, -246.35200692, -0.0002, -312.02238353, -0.009, -312.02238353, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 2020230, 2020231, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 2020240, 2020241, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 2020250, 10742307.69230769)
    ops.section('Aggregator', 10020202, 2020250, 'P', 99999, 'Vy', 99999, 'Vz', 2020240, 'My', 2020230, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10020202, 20202, 10020202, 10020202, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 2, 2)
    ops.node(30202, 15.05, 7.5, 5.4, '-mass', 12.592167230670862, 12.592167230670862, 12.592167230670862, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10030202, 15.05, 7.5, 5.4) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 3020231, 119.31186584, 0.0002, 151.11698592, 0.009, 151.11698592, 0.02, -119.31186584, -0.0002, -151.11698592, -0.009, -151.11698592, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 3020241, 246.35200692, 0.0002, 312.02238353, 0.009, 312.02238353, 0.02, -246.35200692, -0.0002, -312.02238353, -0.009, -312.02238353, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 3020230, 3020231, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 3020240, 3020241, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 3020250, 10742307.69230769)
    ops.section('Aggregator', 10030202, 3020250, 'P', 99999, 'Vy', 99999, 'Vz', 3020240, 'My', 3020230, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10030202, 30202, 10030202, 10030202, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (4, 2, 2)
    ops.node(40202, 21.15, 7.5, 5.4, '-mass', 16.956500418580408, 16.956500418580408, 16.956500418580408, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10040202, 21.15, 7.5, 5.4) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 4020231, 148.55499947, 0.0002, 189.22562882, 0.009, 189.22562882, 0.02, -148.55499947, -0.0002, -189.22562882, -0.009, -189.22562882, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 4020241, 377.34427454, 0.0002, 481.74381485, 0.009, 481.74381485, 0.02, -377.34427454, -0.0002, -481.74381485, -0.009, -481.74381485, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 4020230, 4020231, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 4020240, 4020241, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 4020250, 17757692.30769231)
    ops.section('Aggregator', 10040202, 4020250, 'P', 99999, 'Vy', 99999, 'Vz', 4020240, 'My', 4020230, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10040202, 40202, 10040202, 10040202, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (5, 2, 2)
    ops.node(50202, 27.25, 7.5, 5.4, '-mass', 9.378525438648005, 9.378525438648005, 9.378525438648005, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10050202, 27.25, 7.5, 5.4) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 5020231, 78.3731823, 0.0002, 98.72841083, 0.009, 98.72841083, 0.02, -78.3731823, -0.0002, -98.72841083, -0.009, -98.72841083, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 5020241, 173.09826304, 0.0002, 173.09826304, 0.0132, 94.16146296, 0.027, -173.09826304, -0.0002, -173.09826304, -0.0132, -94.16146296, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 5020230, 5020231, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 5020240, 5020241, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 5020250, 7892307.69230769)
    ops.section('Aggregator', 10050202, 5020250, 'P', 99999, 'Vy', 99999, 'Vz', 5020240, 'My', 5020230, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10050202, 50202, 10050202, 10050202, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 3, 2)
    ops.node(302, 0.0, 11.25, 5.4, '-mass', 5.471419294247547, 5.471419294247547, 5.471419294247547, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10000302, 0.0, 11.25, 5.4) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 30231, 39.27071199, 0.0002, 39.27071199, 0.0132, 22.2187658, 0.027, -39.27071199, -0.0002, -39.27071199, -0.0132, -22.2187658, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 30241, 80.50621511, 0.0002, 80.50621511, 0.0132, 43.54008025, 0.027, -80.50621511, -0.0002, -80.50621511, -0.0132, -43.54008025, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 30230, 30231, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 30240, 30241, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 30250, 7125000.0)
    ops.section('Aggregator', 10000302, 30250, 'P', 99999, 'Vy', 99999, 'Vz', 30240, 'My', 30230, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10000302, 302, 10000302, 10000302, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 3, 2)
    ops.node(10302, 6.1, 11.25, 5.4, '-mass', 9.885682625192343, 9.885682625192343, 9.885682625192343, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10010302, 6.1, 11.25, 5.4) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 1030231, 70.45954651, 0.0002, 70.45954651, 0.0132, 40.51071824, 0.027, -70.45954651, -0.0002, -70.45954651, -0.0132, -40.51071824, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 1030241, 171.64495036, 0.0002, 218.38352925, 0.009, 218.38352925, 0.02, -171.64495036, -0.0002, -218.38352925, -0.009, -218.38352925, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 1030230, 1030231, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 1030240, 1030241, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 1030250, 13965000.0)
    ops.section('Aggregator', 10010302, 1030250, 'P', 99999, 'Vy', 99999, 'Vz', 1030240, 'My', 1030230, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10010302, 10302, 10010302, 10010302, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 3, 2)
    ops.node(20302, 12.2, 11.25, 5.4, '-mass', 7.4268218416351255, 7.4268218416351255, 7.4268218416351255, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10020302, 12.2, 11.25, 5.4) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 2030231, 65.42203808, 0.0002, 65.42203808, 0.0132, 36.95816638, 0.027, -65.42203808, -0.0002, -65.42203808, -0.0132, -36.95816638, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 2030241, 127.0112828, 0.0002, 161.47536297, 0.009, 161.47536297, 0.02, -127.0112828, -0.0002, -161.47536297, -0.009, -161.47536297, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 2030230, 2030231, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 2030240, 2030241, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 2030250, 10260000.0)
    ops.section('Aggregator', 10020302, 2030250, 'P', 99999, 'Vy', 99999, 'Vz', 2030240, 'My', 2030230, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10020302, 20302, 10020302, 10020302, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 3, 2)
    ops.node(30302, 15.05, 11.25, 5.4, '-mass', 7.426821841635125, 7.426821841635125, 7.426821841635125, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10030302, 15.05, 11.25, 5.4) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 3030231, 65.42203808, 0.0002, 65.42203808, 0.0132, 36.95816638, 0.027, -65.42203808, -0.0002, -65.42203808, -0.0132, -36.95816638, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 3030241, 127.0112828, 0.0002, 161.47536297, 0.009, 161.47536297, 0.02, -127.0112828, -0.0002, -161.47536297, -0.009, -161.47536297, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 3030230, 3030231, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 3030240, 3030241, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 3030250, 10260000.0)
    ops.section('Aggregator', 10030302, 3030250, 'P', 99999, 'Vy', 99999, 'Vz', 3030240, 'My', 3030230, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10030302, 30302, 10030302, 10030302, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (4, 3, 2)
    ops.node(40302, 21.15, 11.25, 5.4, '-mass', 9.885682625192343, 9.885682625192343, 9.885682625192343, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10040302, 21.15, 11.25, 5.4) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 4030231, 70.45954651, 0.0002, 70.45954651, 0.0132, 40.51071824, 0.027, -70.45954651, -0.0002, -70.45954651, -0.0132, -40.51071824, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 4030241, 171.64495036, 0.0002, 218.38352925, 0.009, 218.38352925, 0.02, -171.64495036, -0.0002, -218.38352925, -0.009, -218.38352925, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 4030230, 4030231, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 4030240, 4030241, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 4030250, 13965000.0)
    ops.section('Aggregator', 10040302, 4030250, 'P', 99999, 'Vy', 99999, 'Vz', 4030240, 'My', 4030230, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10040302, 40302, 10040302, 10040302, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (5, 3, 2)
    ops.node(50302, 27.25, 11.25, 5.4, '-mass', 5.471419294247549, 5.471419294247549, 5.471419294247549, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10050302, 27.25, 11.25, 5.4) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 5030231, 39.27071199, 0.0002, 39.27071199, 0.0132, 22.2187658, 0.027, -39.27071199, -0.0002, -39.27071199, -0.0132, -22.2187658, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 5030241, 80.50621511, 0.0002, 80.50621511, 0.0132, 43.54008025, 0.027, -80.50621511, -0.0002, -80.50621511, -0.0132, -43.54008025, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 5030230, 5030231, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 5030240, 5030241, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 5030250, 7125000.0)
    ops.section('Aggregator', 10050302, 5030250, 'P', 99999, 'Vy', 99999, 'Vz', 5030240, 'My', 5030230, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10050302, 50302, 10050302, 10050302, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 0, 3)
    ops.node(3, 0.0, 0.0, 8.1, '-mass', 5.471419294247547, 5.471419294247547, 5.471419294247547, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10000003, 0.0, 0.0, 8.1) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 331, 35.85685548, 0.0002, 35.85685548, 0.0132, 19.92113414, 0.027, -35.85685548, -0.0002, -35.85685548, -0.0132, -19.92113414, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 341, 74.66974543, 0.0002, 74.66974543, 0.0132, 39.52090892, 0.027, -74.66974543, -0.0002, -74.66974543, -0.0132, -39.52090892, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 330, 331, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 340, 341, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 350, 7125000.0)
    ops.section('Aggregator', 10000003, 350, 'P', 99999, 'Vy', 99999, 'Vz', 340, 'My', 330, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10000003, 3, 10000003, 10000003, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 0, 3)
    ops.node(10003, 6.1, 0.0, 8.1, '-mass', 9.687517487577665, 9.687517487577665, 9.687517487577665, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10010003, 6.1, 0.0, 8.1) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 1000331, 43.97823356, 0.0002, 43.97823356, 0.0132, 25.34356603, 0.027, -43.97823356, -0.0002, -43.97823356, -0.0132, -25.34356603, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 1000341, 101.97939458, 0.0002, 127.94184269, 0.009, 127.94184269, 0.02, -101.97939458, -0.0002, -127.94184269, -0.009, -127.94184269, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 1000330, 1000331, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 1000340, 1000341, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 1000350, 7125000.0)
    ops.section('Aggregator', 10010003, 1000350, 'P', 99999, 'Vy', 99999, 'Vz', 1000340, 'My', 1000330, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10010003, 10003, 10010003, 10010003, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 0, 3)
    ops.node(20003, 12.2, 0.0, 8.1, '-mass', 5.8085541566328684, 5.8085541566328684, 5.8085541566328684, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10020003, 12.2, 0.0, 8.1) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 2000331, 44.20209629, 0.0002, 44.20209629, 0.0132, 25.07228567, 0.027, -44.20209629, -0.0002, -44.20209629, -0.0132, -25.07228567, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 2000341, 111.07130497, 0.0002, 140.69399388, 0.009, 140.69399388, 0.02, -111.07130497, -0.0002, -140.69399388, -0.009, -140.69399388, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 2000330, 2000331, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 2000340, 2000341, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 2000350, 7125000.0)
    ops.section('Aggregator', 10020003, 2000350, 'P', 99999, 'Vy', 99999, 'Vz', 2000340, 'My', 2000330, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10020003, 20003, 10020003, 10020003, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 0, 3)
    ops.node(30003, 15.05, 0.0, 8.1, '-mass', 5.808554156632868, 5.808554156632868, 5.808554156632868, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10030003, 15.05, 0.0, 8.1) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 3000331, 44.20209629, 0.0002, 44.20209629, 0.0132, 25.07228567, 0.027, -44.20209629, -0.0002, -44.20209629, -0.0132, -25.07228567, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 3000341, 111.07130497, 0.0002, 140.69399388, 0.009, 140.69399388, 0.02, -111.07130497, -0.0002, -140.69399388, -0.009, -140.69399388, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 3000330, 3000331, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 3000340, 3000341, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 3000350, 7125000.0)
    ops.section('Aggregator', 10030003, 3000350, 'P', 99999, 'Vy', 99999, 'Vz', 3000340, 'My', 3000330, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10030003, 30003, 10030003, 10030003, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (4, 0, 3)
    ops.node(40003, 21.15, 0.0, 8.1, '-mass', 9.687517487577665, 9.687517487577665, 9.687517487577665, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10040003, 21.15, 0.0, 8.1) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 4000331, 43.97823356, 0.0002, 43.97823356, 0.0132, 25.34356603, 0.027, -43.97823356, -0.0002, -43.97823356, -0.0132, -25.34356603, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 4000341, 101.97939458, 0.0002, 127.94184269, 0.009, 127.94184269, 0.02, -101.97939458, -0.0002, -127.94184269, -0.009, -127.94184269, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 4000330, 4000331, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 4000340, 4000341, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 4000350, 7125000.0)
    ops.section('Aggregator', 10040003, 4000350, 'P', 99999, 'Vy', 99999, 'Vz', 4000340, 'My', 4000330, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10040003, 40003, 10040003, 10040003, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (5, 0, 3)
    ops.node(50003, 27.25, 0.0, 8.1, '-mass', 5.471419294247549, 5.471419294247549, 5.471419294247549, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10050003, 27.25, 0.0, 8.1) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 5000331, 35.85685548, 0.0002, 35.85685548, 0.0132, 19.92113414, 0.027, -35.85685548, -0.0002, -35.85685548, -0.0132, -19.92113414, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 5000341, 74.66974543, 0.0002, 74.66974543, 0.0132, 39.52090892, 0.027, -74.66974543, -0.0002, -74.66974543, -0.0132, -39.52090892, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 5000330, 5000331, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 5000340, 5000341, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 5000350, 7125000.0)
    ops.section('Aggregator', 10050003, 5000350, 'P', 99999, 'Vy', 99999, 'Vz', 5000340, 'My', 5000330, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10050003, 50003, 10050003, 10050003, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 1, 3)
    ops.node(103, 0.0, 3.75, 8.1, '-mass', 9.378525438648001, 9.378525438648001, 9.378525438648001, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10000103, 0.0, 3.75, 8.1) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 10331, 70.72929402, 0.0002, 89.98147738, 0.009, 89.98147738, 0.02, -70.72929402, -0.0002, -89.98147738, -0.009, -89.98147738, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 10341, 160.45128267, 0.0002, 160.45128267, 0.0132, 85.51741174, 0.027, -160.45128267, -0.0002, -160.45128267, -0.0132, -85.51741174, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 10330, 10331, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 10340, 10341, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 10350, 7892307.69230769)
    ops.section('Aggregator', 10000103, 10350, 'P', 99999, 'Vy', 99999, 'Vz', 10340, 'My', 10330, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10000103, 103, 10000103, 10000103, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 1, 3)
    ops.node(10103, 6.1, 3.75, 8.1, '-mass', 16.692280235094167, 16.692280235094167, 16.692280235094167, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10010103, 6.1, 3.75, 8.1) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 1010331, 101.70083105, 0.0002, 128.67425038, 0.009, 128.67425038, 0.02, -101.70083105, -0.0002, -128.67425038, -0.009, -128.67425038, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 1010341, 249.09333983, 0.0002, 315.15867123, 0.009, 315.15867123, 0.02, -249.09333983, -0.0002, -315.15867123, -0.009, -315.15867123, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 1010330, 1010331, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 1010340, 1010341, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 1010350, 10742307.69230769)
    ops.section('Aggregator', 10010103, 1010350, 'P', 99999, 'Vy', 99999, 'Vz', 1010340, 'My', 1010330, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10010103, 10103, 10010103, 10010103, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 1, 3)
    ops.node(20103, 12.2, 3.75, 8.1, '-mass', 12.996068811723653, 12.996068811723653, 12.996068811723653, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10020103, 12.2, 3.75, 8.1) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 2010331, 76.48352696, 0.0002, 96.55825294, 0.009, 96.55825294, 0.02, -76.48352696, -0.0002, -96.55825294, -0.009, -96.55825294, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 2010341, 187.32921821, 0.0002, 236.49774996, 0.009, 236.49774996, 0.02, -187.32921821, -0.0002, -236.49774996, -0.009, -236.49774996, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 2010330, 2010331, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 2010340, 2010341, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 2010350, 7892307.69230769)
    ops.section('Aggregator', 10020103, 2010350, 'P', 99999, 'Vy', 99999, 'Vz', 2010340, 'My', 2010330, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10020103, 20103, 10020103, 10020103, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 1, 3)
    ops.node(30103, 15.05, 3.75, 8.1, '-mass', 12.996068811723653, 12.996068811723653, 12.996068811723653, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10030103, 15.05, 3.75, 8.1) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 3010331, 76.48352696, 0.0002, 96.55825294, 0.009, 96.55825294, 0.02, -76.48352696, -0.0002, -96.55825294, -0.009, -96.55825294, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 3010341, 187.32921821, 0.0002, 236.49774996, 0.009, 236.49774996, 0.02, -187.32921821, -0.0002, -236.49774996, -0.009, -236.49774996, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 3010330, 3010331, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 3010340, 3010341, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 3010350, 7892307.69230769)
    ops.section('Aggregator', 10030103, 3010350, 'P', 99999, 'Vy', 99999, 'Vz', 3010340, 'My', 3010330, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10030103, 30103, 10030103, 10030103, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (4, 1, 3)
    ops.node(40103, 21.15, 3.75, 8.1, '-mass', 16.69228023509417, 16.69228023509417, 16.69228023509417, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10040103, 21.15, 3.75, 8.1) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 4010331, 101.70083105, 0.0002, 128.67425038, 0.009, 128.67425038, 0.02, -101.70083105, -0.0002, -128.67425038, -0.009, -128.67425038, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 4010341, 249.09333983, 0.0002, 315.15867123, 0.009, 315.15867123, 0.02, -249.09333983, -0.0002, -315.15867123, -0.009, -315.15867123, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 4010330, 4010331, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 4010340, 4010341, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 4010350, 10742307.69230769)
    ops.section('Aggregator', 10040103, 4010350, 'P', 99999, 'Vy', 99999, 'Vz', 4010340, 'My', 4010330, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10040103, 40103, 10040103, 10040103, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (5, 1, 3)
    ops.node(50103, 27.25, 3.75, 8.1, '-mass', 9.378525438648005, 9.378525438648005, 9.378525438648005, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10050103, 27.25, 3.75, 8.1) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 5010331, 70.72929402, 0.0002, 89.98147738, 0.009, 89.98147738, 0.02, -70.72929402, -0.0002, -89.98147738, -0.009, -89.98147738, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 5010341, 160.45128267, 0.0002, 160.45128267, 0.0132, 85.51741174, 0.027, -160.45128267, -0.0002, -160.45128267, -0.0132, -85.51741174, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 5010330, 5010331, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 5010340, 5010341, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 5010350, 7892307.69230769)
    ops.section('Aggregator', 10050103, 5010350, 'P', 99999, 'Vy', 99999, 'Vz', 5010340, 'My', 5010330, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10050103, 50103, 10050103, 10050103, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 2, 3)
    ops.node(203, 0.0, 7.5, 8.1, '-mass', 9.378525438648001, 9.378525438648001, 9.378525438648001, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10000203, 0.0, 7.5, 8.1) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 20331, 70.72929402, 0.0002, 89.98147738, 0.009, 89.98147738, 0.02, -70.72929402, -0.0002, -89.98147738, -0.009, -89.98147738, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 20341, 160.45128267, 0.0002, 160.45128267, 0.0132, 85.51741174, 0.027, -160.45128267, -0.0002, -160.45128267, -0.0132, -85.51741174, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 20330, 20331, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 20340, 20341, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 20350, 7892307.69230769)
    ops.section('Aggregator', 10000203, 20350, 'P', 99999, 'Vy', 99999, 'Vz', 20340, 'My', 20330, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10000203, 203, 10000203, 10000203, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 2, 3)
    ops.node(10203, 6.1, 7.5, 8.1, '-mass', 16.692280235094167, 16.692280235094167, 16.692280235094167, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10010203, 6.1, 7.5, 8.1) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 1020331, 101.70083105, 0.0002, 128.67425038, 0.009, 128.67425038, 0.02, -101.70083105, -0.0002, -128.67425038, -0.009, -128.67425038, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 1020341, 249.09333983, 0.0002, 315.15867123, 0.009, 315.15867123, 0.02, -249.09333983, -0.0002, -315.15867123, -0.009, -315.15867123, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 1020330, 1020331, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 1020340, 1020341, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 1020350, 10742307.69230769)
    ops.section('Aggregator', 10010203, 1020350, 'P', 99999, 'Vy', 99999, 'Vz', 1020340, 'My', 1020330, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10010203, 10203, 10010203, 10010203, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 2, 3)
    ops.node(20203, 12.2, 7.5, 8.1, '-mass', 12.393084661863524, 12.393084661863524, 12.393084661863524, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10020203, 12.2, 7.5, 8.1) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 2020331, 75.10964567, 0.0002, 94.98348443, 0.009, 94.98348443, 0.02, -75.10964567, -0.0002, -94.98348443, -0.009, -94.98348443, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 2020341, 183.96420461, 0.0002, 232.64070824, 0.009, 232.64070824, 0.02, -183.96420461, -0.0002, -232.64070824, -0.009, -232.64070824, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 2020330, 2020331, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 2020340, 2020341, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 2020350, 7892307.69230769)
    ops.section('Aggregator', 10020203, 2020350, 'P', 99999, 'Vy', 99999, 'Vz', 2020340, 'My', 2020330, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10020203, 20203, 10020203, 10020203, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 2, 3)
    ops.node(30203, 15.05, 7.5, 8.1, '-mass', 12.393084661863524, 12.393084661863524, 12.393084661863524, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10030203, 15.05, 7.5, 8.1) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 3020331, 75.10964567, 0.0002, 94.98348443, 0.009, 94.98348443, 0.02, -75.10964567, -0.0002, -94.98348443, -0.009, -94.98348443, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 3020341, 183.96420461, 0.0002, 232.64070824, 0.009, 232.64070824, 0.02, -183.96420461, -0.0002, -232.64070824, -0.009, -232.64070824, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 3020330, 3020331, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 3020340, 3020341, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 3020350, 7892307.69230769)
    ops.section('Aggregator', 10030203, 3020350, 'P', 99999, 'Vy', 99999, 'Vz', 3020340, 'My', 3020330, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10030203, 30203, 10030203, 10030203, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (4, 2, 3)
    ops.node(40203, 21.15, 7.5, 8.1, '-mass', 16.69228023509417, 16.69228023509417, 16.69228023509417, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10040203, 21.15, 7.5, 8.1) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 4020331, 101.70083105, 0.0002, 128.67425038, 0.009, 128.67425038, 0.02, -101.70083105, -0.0002, -128.67425038, -0.009, -128.67425038, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 4020341, 249.09333983, 0.0002, 315.15867123, 0.009, 315.15867123, 0.02, -249.09333983, -0.0002, -315.15867123, -0.009, -315.15867123, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 4020330, 4020331, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 4020340, 4020341, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 4020350, 10742307.69230769)
    ops.section('Aggregator', 10040203, 4020350, 'P', 99999, 'Vy', 99999, 'Vz', 4020340, 'My', 4020330, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10040203, 40203, 10040203, 10040203, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (5, 2, 3)
    ops.node(50203, 27.25, 7.5, 8.1, '-mass', 9.378525438648005, 9.378525438648005, 9.378525438648005, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10050203, 27.25, 7.5, 8.1) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 5020331, 70.72929402, 0.0002, 89.98147738, 0.009, 89.98147738, 0.02, -70.72929402, -0.0002, -89.98147738, -0.009, -89.98147738, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 5020341, 160.45128267, 0.0002, 160.45128267, 0.0132, 85.51741174, 0.027, -160.45128267, -0.0002, -160.45128267, -0.0132, -85.51741174, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 5020330, 5020331, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 5020340, 5020341, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 5020350, 7892307.69230769)
    ops.section('Aggregator', 10050203, 5020350, 'P', 99999, 'Vy', 99999, 'Vz', 5020340, 'My', 5020330, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10050203, 50203, 10050203, 10050203, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 3, 3)
    ops.node(303, 0.0, 11.25, 8.1, '-mass', 5.471419294247547, 5.471419294247547, 5.471419294247547, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10000303, 0.0, 11.25, 8.1) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 30331, 35.85685548, 0.0002, 35.85685548, 0.0132, 19.92113414, 0.027, -35.85685548, -0.0002, -35.85685548, -0.0132, -19.92113414, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 30341, 74.66974543, 0.0002, 74.66974543, 0.0132, 39.52090892, 0.027, -74.66974543, -0.0002, -74.66974543, -0.0132, -39.52090892, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 30330, 30331, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 30340, 30341, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 30350, 7125000.0)
    ops.section('Aggregator', 10000303, 30350, 'P', 99999, 'Vy', 99999, 'Vz', 30340, 'My', 30330, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10000303, 303, 10000303, 10000303, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 3, 3)
    ops.node(10303, 6.1, 11.25, 8.1, '-mass', 9.687517487577665, 9.687517487577665, 9.687517487577665, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10010303, 6.1, 11.25, 8.1) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 1030331, 43.97823356, 0.0002, 43.97823356, 0.0132, 25.34356603, 0.027, -43.97823356, -0.0002, -43.97823356, -0.0132, -25.34356603, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 1030341, 101.97939458, 0.0002, 127.94184269, 0.009, 127.94184269, 0.02, -101.97939458, -0.0002, -127.94184269, -0.009, -127.94184269, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 1030330, 1030331, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 1030340, 1030341, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 1030350, 7125000.0)
    ops.section('Aggregator', 10010303, 1030350, 'P', 99999, 'Vy', 99999, 'Vz', 1030340, 'My', 1030330, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10010303, 10303, 10010303, 10010303, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 3, 3)
    ops.node(20303, 12.2, 11.25, 8.1, '-mass', 7.290124593928704, 7.290124593928704, 7.290124593928704, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10020303, 12.2, 11.25, 8.1) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 2030331, 39.69431492, 0.0002, 39.69431492, 0.0132, 22.50174564, 0.027, -39.69431492, -0.0002, -39.69431492, -0.0132, -22.50174564, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 2030341, 91.127386, 0.0002, 115.47343145, 0.009, 115.47343145, 0.02, -91.127386, -0.0002, -115.47343145, -0.009, -115.47343145, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 2030330, 2030331, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 2030340, 2030341, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 2030350, 7125000.0)
    ops.section('Aggregator', 10020303, 2030350, 'P', 99999, 'Vy', 99999, 'Vz', 2030340, 'My', 2030330, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10020303, 20303, 10020303, 10020303, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 3, 3)
    ops.node(30303, 15.05, 11.25, 8.1, '-mass', 7.290124593928703, 7.290124593928703, 7.290124593928703, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10030303, 15.05, 11.25, 8.1) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 3030331, 39.69431492, 0.0002, 39.69431492, 0.0132, 22.50174564, 0.027, -39.69431492, -0.0002, -39.69431492, -0.0132, -22.50174564, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 3030341, 91.127386, 0.0002, 115.47343145, 0.009, 115.47343145, 0.02, -91.127386, -0.0002, -115.47343145, -0.009, -115.47343145, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 3030330, 3030331, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 3030340, 3030341, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 3030350, 7125000.0)
    ops.section('Aggregator', 10030303, 3030350, 'P', 99999, 'Vy', 99999, 'Vz', 3030340, 'My', 3030330, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10030303, 30303, 10030303, 10030303, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (4, 3, 3)
    ops.node(40303, 21.15, 11.25, 8.1, '-mass', 9.687517487577665, 9.687517487577665, 9.687517487577665, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10040303, 21.15, 11.25, 8.1) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 4030331, 43.97823356, 0.0002, 43.97823356, 0.0132, 25.34356603, 0.027, -43.97823356, -0.0002, -43.97823356, -0.0132, -25.34356603, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 4030341, 101.97939458, 0.0002, 127.94184269, 0.009, 127.94184269, 0.02, -101.97939458, -0.0002, -127.94184269, -0.009, -127.94184269, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 4030330, 4030331, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 4030340, 4030341, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 4030350, 7125000.0)
    ops.section('Aggregator', 10040303, 4030350, 'P', 99999, 'Vy', 99999, 'Vz', 4030340, 'My', 4030330, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10040303, 40303, 10040303, 10040303, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (5, 3, 3)
    ops.node(50303, 27.25, 11.25, 8.1, '-mass', 5.471419294247549, 5.471419294247549, 5.471419294247549, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10050303, 27.25, 11.25, 8.1) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 5030331, 35.85685548, 0.0002, 35.85685548, 0.0132, 19.92113414, 0.027, -35.85685548, -0.0002, -35.85685548, -0.0132, -19.92113414, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 5030341, 74.66974543, 0.0002, 74.66974543, 0.0132, 39.52090892, 0.027, -74.66974543, -0.0002, -74.66974543, -0.0132, -39.52090892, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 5030330, 5030331, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 5030340, 5030341, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 5030350, 7125000.0)
    ops.section('Aggregator', 10050303, 5030350, 'P', 99999, 'Vy', 99999, 'Vz', 5030340, 'My', 5030330, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10050303, 50303, 10050303, 10050303, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 0, 4)
    ops.node(4, 0.0, 0.0, 10.8, '-mass', 5.471419294247547, 5.471419294247547, 5.471419294247547, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10000004, 0.0, 0.0, 10.8) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 431, 31.37172615, 0.0002, 31.37172615, 0.0132, 16.83791524, 0.027, -31.37172615, -0.0002, -31.37172615, -0.0132, -16.83791524, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 441, 67.10090505, 0.0002, 67.10090505, 0.0132, 34.16712829, 0.027, -67.10090505, -0.0002, -67.10090505, -0.0132, -34.16712829, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 430, 431, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 440, 441, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 450, 7125000.0)
    ops.section('Aggregator', 10000004, 450, 'P', 99999, 'Vy', 99999, 'Vz', 440, 'My', 430, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10000004, 4, 10000004, 10000004, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 0, 4)
    ops.node(10004, 6.1, 0.0, 10.8, '-mass', 9.687517487577665, 9.687517487577665, 9.687517487577665, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10010004, 6.1, 0.0, 10.8) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 1000431, 37.65117934, 0.0002, 37.65117934, 0.0132, 21.13283917, 0.027, -37.65117934, -0.0002, -37.65117934, -0.0132, -21.13283917, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 1000441, 85.99514384, 0.0002, 109.62471841, 0.009, 109.62471841, 0.02, -85.99514384, -0.0002, -109.62471841, -0.009, -109.62471841, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 1000430, 1000431, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 1000440, 1000441, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 1000450, 7125000.0)
    ops.section('Aggregator', 10010004, 1000450, 'P', 99999, 'Vy', 99999, 'Vz', 1000440, 'My', 1000430, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10010004, 10004, 10010004, 10010004, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 0, 4)
    ops.node(20004, 12.2, 0.0, 10.8, '-mass', 5.8085541566328684, 5.8085541566328684, 5.8085541566328684, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10020004, 12.2, 0.0, 10.8) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 2000431, 37.57008248, 0.0002, 37.57008248, 0.0132, 20.59234409, 0.027, -37.57008248, -0.0002, -37.57008248, -0.0132, -20.59234409, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 2000441, 92.96204662, 0.0002, 120.18142968, 0.009, 120.18142968, 0.02, -92.96204662, -0.0002, -120.18142968, -0.009, -120.18142968, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 2000430, 2000431, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 2000440, 2000441, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 2000450, 7125000.0)
    ops.section('Aggregator', 10020004, 2000450, 'P', 99999, 'Vy', 99999, 'Vz', 2000440, 'My', 2000430, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10020004, 20004, 10020004, 10020004, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 0, 4)
    ops.node(30004, 15.05, 0.0, 10.8, '-mass', 5.808554156632868, 5.808554156632868, 5.808554156632868, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10030004, 15.05, 0.0, 10.8) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 3000431, 37.57008248, 0.0002, 37.57008248, 0.0132, 20.59234409, 0.027, -37.57008248, -0.0002, -37.57008248, -0.0132, -20.59234409, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 3000441, 92.96204662, 0.0002, 120.18142968, 0.009, 120.18142968, 0.02, -92.96204662, -0.0002, -120.18142968, -0.009, -120.18142968, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 3000430, 3000431, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 3000440, 3000441, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 3000450, 7125000.0)
    ops.section('Aggregator', 10030004, 3000450, 'P', 99999, 'Vy', 99999, 'Vz', 3000440, 'My', 3000430, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10030004, 30004, 10030004, 10030004, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (4, 0, 4)
    ops.node(40004, 21.15, 0.0, 10.8, '-mass', 9.687517487577665, 9.687517487577665, 9.687517487577665, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10040004, 21.15, 0.0, 10.8) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 4000431, 37.65117934, 0.0002, 37.65117934, 0.0132, 21.13283917, 0.027, -37.65117934, -0.0002, -37.65117934, -0.0132, -21.13283917, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 4000441, 85.99514384, 0.0002, 109.62471841, 0.009, 109.62471841, 0.02, -85.99514384, -0.0002, -109.62471841, -0.009, -109.62471841, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 4000430, 4000431, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 4000440, 4000441, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 4000450, 7125000.0)
    ops.section('Aggregator', 10040004, 4000450, 'P', 99999, 'Vy', 99999, 'Vz', 4000440, 'My', 4000430, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10040004, 40004, 10040004, 10040004, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (5, 0, 4)
    ops.node(50004, 27.25, 0.0, 10.8, '-mass', 5.471419294247549, 5.471419294247549, 5.471419294247549, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10050004, 27.25, 0.0, 10.8) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 5000431, 31.37172615, 0.0002, 31.37172615, 0.0132, 16.83791524, 0.027, -31.37172615, -0.0002, -31.37172615, -0.0132, -16.83791524, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 5000441, 67.10090505, 0.0002, 67.10090505, 0.0132, 34.16712829, 0.027, -67.10090505, -0.0002, -67.10090505, -0.0132, -34.16712829, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 5000430, 5000431, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 5000440, 5000441, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 5000450, 7125000.0)
    ops.section('Aggregator', 10050004, 5000450, 'P', 99999, 'Vy', 99999, 'Vz', 5000440, 'My', 5000430, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10050004, 50004, 10050004, 10050004, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 1, 4)
    ops.node(104, 0.0, 3.75, 10.8, '-mass', 9.378525438648001, 9.378525438648001, 9.378525438648001, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10000104, 0.0, 3.75, 10.8) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 10431, 60.79675277, 0.0002, 78.76964027, 0.009, 78.76964027, 0.02, -60.79675277, -0.0002, -78.76964027, -0.009, -78.76964027, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 10441, 144.01168154, 0.0002, 144.01168154, 0.0132, 74.00378698, 0.027, -144.01168154, -0.0002, -144.01168154, -0.0132, -74.00378698, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 10430, 10431, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 10440, 10441, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 10450, 7892307.69230769)
    ops.section('Aggregator', 10000104, 10450, 'P', 99999, 'Vy', 99999, 'Vz', 10440, 'My', 10430, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10000104, 104, 10000104, 10000104, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 1, 4)
    ops.node(10104, 6.1, 3.75, 10.8, '-mass', 16.49411509747949, 16.49411509747949, 16.49411509747949, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10010104, 6.1, 3.75, 10.8) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 1010431, 87.01935669, 0.0002, 112.00151069, 0.009, 112.00151069, 0.02, -87.01935669, -0.0002, -112.00151069, -0.009, -112.00151069, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 1010441, 213.13436639, 0.0002, 274.32254068, 0.009, 274.32254068, 0.02, -213.13436639, -0.0002, -274.32254068, -0.009, -274.32254068, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 1010430, 1010431, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 1010440, 1010441, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 1010450, 10742307.69230769)
    ops.section('Aggregator', 10010104, 1010450, 'P', 99999, 'Vy', 99999, 'Vz', 1010440, 'My', 1010430, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10010104, 10104, 10010104, 10010104, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 1, 4)
    ops.node(20104, 12.2, 3.75, 10.8, '-mass', 12.905243123650258, 12.905243123650258, 12.905243123650258, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10020104, 12.2, 3.75, 10.8) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 2010431, 65.29823838, 0.0002, 83.8255273, 0.009, 83.8255273, 0.02, -65.29823838, -0.0002, -83.8255273, -0.009, -83.8255273, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 2010441, 159.93336648, 0.0002, 205.31179875, 0.009, 205.31179875, 0.02, -159.93336648, -0.0002, -205.31179875, -0.009, -205.31179875, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 2010430, 2010431, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 2010440, 2010441, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 2010450, 7892307.69230769)
    ops.section('Aggregator', 10020104, 2010450, 'P', 99999, 'Vy', 99999, 'Vz', 2010440, 'My', 2010430, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10020104, 20104, 10020104, 10020104, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 1, 4)
    ops.node(30104, 15.05, 3.75, 10.8, '-mass', 12.905243123650258, 12.905243123650258, 12.905243123650258, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10030104, 15.05, 3.75, 10.8) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 3010431, 65.29823838, 0.0002, 83.8255273, 0.009, 83.8255273, 0.02, -65.29823838, -0.0002, -83.8255273, -0.009, -83.8255273, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 3010441, 159.93336648, 0.0002, 205.31179875, 0.009, 205.31179875, 0.02, -159.93336648, -0.0002, -205.31179875, -0.009, -205.31179875, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 3010430, 3010431, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 3010440, 3010441, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 3010450, 7892307.69230769)
    ops.section('Aggregator', 10030104, 3010450, 'P', 99999, 'Vy', 99999, 'Vz', 3010440, 'My', 3010430, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10030104, 30104, 10030104, 10030104, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (4, 1, 4)
    ops.node(40104, 21.15, 3.75, 10.8, '-mass', 16.49411509747949, 16.49411509747949, 16.49411509747949, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10040104, 21.15, 3.75, 10.8) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 4010431, 87.01935669, 0.0002, 112.00151069, 0.009, 112.00151069, 0.02, -87.01935669, -0.0002, -112.00151069, -0.009, -112.00151069, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 4010441, 213.13436639, 0.0002, 274.32254068, 0.009, 274.32254068, 0.02, -213.13436639, -0.0002, -274.32254068, -0.009, -274.32254068, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 4010430, 4010431, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 4010440, 4010441, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 4010450, 10742307.69230769)
    ops.section('Aggregator', 10040104, 4010450, 'P', 99999, 'Vy', 99999, 'Vz', 4010440, 'My', 4010430, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10040104, 40104, 10040104, 10040104, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (5, 1, 4)
    ops.node(50104, 27.25, 3.75, 10.8, '-mass', 9.378525438648005, 9.378525438648005, 9.378525438648005, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10050104, 27.25, 3.75, 10.8) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 5010431, 60.79675277, 0.0002, 78.76964027, 0.009, 78.76964027, 0.02, -60.79675277, -0.0002, -78.76964027, -0.009, -78.76964027, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 5010441, 144.01168154, 0.0002, 144.01168154, 0.0132, 74.00378698, 0.027, -144.01168154, -0.0002, -144.01168154, -0.0132, -74.00378698, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 5010430, 5010431, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 5010440, 5010441, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 5010450, 7892307.69230769)
    ops.section('Aggregator', 10050104, 5010450, 'P', 99999, 'Vy', 99999, 'Vz', 5010440, 'My', 5010430, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10050104, 50104, 10050104, 10050104, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 2, 4)
    ops.node(204, 0.0, 7.5, 10.8, '-mass', 9.378525438648001, 9.378525438648001, 9.378525438648001, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10000204, 0.0, 7.5, 10.8) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 20431, 60.79675277, 0.0002, 78.76964027, 0.009, 78.76964027, 0.02, -60.79675277, -0.0002, -78.76964027, -0.009, -78.76964027, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 20441, 144.01168154, 0.0002, 144.01168154, 0.0132, 74.00378698, 0.027, -144.01168154, -0.0002, -144.01168154, -0.0132, -74.00378698, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 20430, 20431, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 20440, 20441, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 20450, 7892307.69230769)
    ops.section('Aggregator', 10000204, 20450, 'P', 99999, 'Vy', 99999, 'Vz', 20440, 'My', 20430, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10000204, 204, 10000204, 10000204, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 2, 4)
    ops.node(10204, 6.1, 7.5, 10.8, '-mass', 16.49411509747949, 16.49411509747949, 16.49411509747949, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10010204, 6.1, 7.5, 10.8) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 1020431, 87.01935669, 0.0002, 112.00151069, 0.009, 112.00151069, 0.02, -87.01935669, -0.0002, -112.00151069, -0.009, -112.00151069, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 1020441, 213.13436639, 0.0002, 274.32254068, 0.009, 274.32254068, 0.02, -213.13436639, -0.0002, -274.32254068, -0.009, -274.32254068, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 1020430, 1020431, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 1020440, 1020441, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 1020450, 10742307.69230769)
    ops.section('Aggregator', 10010204, 1020450, 'P', 99999, 'Vy', 99999, 'Vz', 1020440, 'My', 1020430, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10010204, 10204, 10010204, 10010204, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 2, 4)
    ops.node(20204, 12.2, 7.5, 10.8, '-mass', 12.30225897379013, 12.30225897379013, 12.30225897379013, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10020204, 12.2, 7.5, 10.8) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 2020431, 64.26471991, 0.0002, 82.66067153, 0.009, 82.66067153, 0.02, -64.26471991, -0.0002, -82.66067153, -0.009, -82.66067153, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 2020441, 157.40199514, 0.0002, 202.45874621, 0.009, 202.45874621, 0.02, -157.40199514, -0.0002, -202.45874621, -0.009, -202.45874621, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 2020430, 2020431, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 2020440, 2020441, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 2020450, 7892307.69230769)
    ops.section('Aggregator', 10020204, 2020450, 'P', 99999, 'Vy', 99999, 'Vz', 2020440, 'My', 2020430, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10020204, 20204, 10020204, 10020204, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 2, 4)
    ops.node(30204, 15.05, 7.5, 10.8, '-mass', 12.30225897379013, 12.30225897379013, 12.30225897379013, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10030204, 15.05, 7.5, 10.8) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 3020431, 64.26471991, 0.0002, 82.66067153, 0.009, 82.66067153, 0.02, -64.26471991, -0.0002, -82.66067153, -0.009, -82.66067153, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 3020441, 157.40199514, 0.0002, 202.45874621, 0.009, 202.45874621, 0.02, -157.40199514, -0.0002, -202.45874621, -0.009, -202.45874621, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 3020430, 3020431, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 3020440, 3020441, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 3020450, 7892307.69230769)
    ops.section('Aggregator', 10030204, 3020450, 'P', 99999, 'Vy', 99999, 'Vz', 3020440, 'My', 3020430, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10030204, 30204, 10030204, 10030204, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (4, 2, 4)
    ops.node(40204, 21.15, 7.5, 10.8, '-mass', 16.49411509747949, 16.49411509747949, 16.49411509747949, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10040204, 21.15, 7.5, 10.8) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 4020431, 87.01935669, 0.0002, 112.00151069, 0.009, 112.00151069, 0.02, -87.01935669, -0.0002, -112.00151069, -0.009, -112.00151069, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 4020441, 213.13436639, 0.0002, 274.32254068, 0.009, 274.32254068, 0.02, -213.13436639, -0.0002, -274.32254068, -0.009, -274.32254068, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 4020430, 4020431, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 4020440, 4020441, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 4020450, 10742307.69230769)
    ops.section('Aggregator', 10040204, 4020450, 'P', 99999, 'Vy', 99999, 'Vz', 4020440, 'My', 4020430, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10040204, 40204, 10040204, 10040204, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (5, 2, 4)
    ops.node(50204, 27.25, 7.5, 10.8, '-mass', 9.378525438648005, 9.378525438648005, 9.378525438648005, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10050204, 27.25, 7.5, 10.8) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 5020431, 60.79675277, 0.0002, 78.76964027, 0.009, 78.76964027, 0.02, -60.79675277, -0.0002, -78.76964027, -0.009, -78.76964027, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('Hysteretic', 5020441, 144.01168154, 0.0002, 144.01168154, 0.0132, 74.00378698, 0.027, -144.01168154, -0.0002, -144.01168154, -0.0132, -74.00378698, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 5020430, 5020431, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 5020440, 5020441, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 5020450, 7892307.69230769)
    ops.section('Aggregator', 10050204, 5020450, 'P', 99999, 'Vy', 99999, 'Vz', 5020440, 'My', 5020430, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10050204, 50204, 10050204, 10050204, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 3, 4)
    ops.node(304, 0.0, 11.25, 10.8, '-mass', 5.471419294247547, 5.471419294247547, 5.471419294247547, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10000304, 0.0, 11.25, 10.8) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 30431, 31.37172615, 0.0002, 31.37172615, 0.0132, 16.83791524, 0.027, -31.37172615, -0.0002, -31.37172615, -0.0132, -16.83791524, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 30441, 67.10090505, 0.0002, 67.10090505, 0.0132, 34.16712829, 0.027, -67.10090505, -0.0002, -67.10090505, -0.0132, -34.16712829, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 30430, 30431, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 30440, 30441, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 30450, 7125000.0)
    ops.section('Aggregator', 10000304, 30450, 'P', 99999, 'Vy', 99999, 'Vz', 30440, 'My', 30430, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10000304, 304, 10000304, 10000304, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 3, 4)
    ops.node(10304, 6.1, 11.25, 10.8, '-mass', 9.687517487577665, 9.687517487577665, 9.687517487577665, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10010304, 6.1, 11.25, 10.8) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 1030431, 37.65117934, 0.0002, 37.65117934, 0.0132, 21.13283917, 0.027, -37.65117934, -0.0002, -37.65117934, -0.0132, -21.13283917, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 1030441, 85.99514384, 0.0002, 109.62471841, 0.009, 109.62471841, 0.02, -85.99514384, -0.0002, -109.62471841, -0.009, -109.62471841, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 1030430, 1030431, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 1030440, 1030441, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 1030450, 7125000.0)
    ops.section('Aggregator', 10010304, 1030450, 'P', 99999, 'Vy', 99999, 'Vz', 1030440, 'My', 1030430, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10010304, 10304, 10010304, 10010304, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 3, 4)
    ops.node(20304, 12.2, 11.25, 10.8, '-mass', 7.290124593928704, 7.290124593928704, 7.290124593928704, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10020304, 12.2, 11.25, 10.8) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 2030431, 34.36051991, 0.0002, 34.36051991, 0.0132, 18.90234942, 0.027, -34.36051991, -0.0002, -34.36051991, -0.0132, -18.90234942, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 2030441, 77.80646859, 0.0002, 100.37420037, 0.009, 100.37420037, 0.02, -77.80646859, -0.0002, -100.37420037, -0.009, -100.37420037, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 2030430, 2030431, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 2030440, 2030441, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 2030450, 7125000.0)
    ops.section('Aggregator', 10020304, 2030450, 'P', 99999, 'Vy', 99999, 'Vz', 2030440, 'My', 2030430, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10020304, 20304, 10020304, 10020304, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 3, 4)
    ops.node(30304, 15.05, 11.25, 10.8, '-mass', 7.290124593928703, 7.290124593928703, 7.290124593928703, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10030304, 15.05, 11.25, 10.8) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 3030431, 34.36051991, 0.0002, 34.36051991, 0.0132, 18.90234942, 0.027, -34.36051991, -0.0002, -34.36051991, -0.0132, -18.90234942, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 3030441, 77.80646859, 0.0002, 100.37420037, 0.009, 100.37420037, 0.02, -77.80646859, -0.0002, -100.37420037, -0.009, -100.37420037, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 3030430, 3030431, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 3030440, 3030441, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 3030450, 7125000.0)
    ops.section('Aggregator', 10030304, 3030450, 'P', 99999, 'Vy', 99999, 'Vz', 3030440, 'My', 3030430, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10030304, 30304, 10030304, 10030304, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (4, 3, 4)
    ops.node(40304, 21.15, 11.25, 10.8, '-mass', 9.687517487577665, 9.687517487577665, 9.687517487577665, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10040304, 21.15, 11.25, 10.8) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 4030431, 37.65117934, 0.0002, 37.65117934, 0.0132, 21.13283917, 0.027, -37.65117934, -0.0002, -37.65117934, -0.0132, -21.13283917, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 4030441, 85.99514384, 0.0002, 109.62471841, 0.009, 109.62471841, 0.02, -85.99514384, -0.0002, -109.62471841, -0.009, -109.62471841, -0.02, 0.6, 0.2, 0.0, 0.01, 0.3)
    ops.uniaxialMaterial('MinMax', 4030430, 4030431, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 4030440, 4030441, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 4030450, 7125000.0)
    ops.section('Aggregator', 10040304, 4030450, 'P', 99999, 'Vy', 99999, 'Vz', 4030440, 'My', 4030430, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10040304, 40304, 10040304, 10040304, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (5, 3, 4)
    ops.node(50304, 27.25, 11.25, 10.8, '-mass', 5.471419294247549, 5.471419294247549, 5.471419294247549, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10050304, 27.25, 11.25, 10.8) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 5030431, 31.37172615, 0.0002, 31.37172615, 0.0132, 16.83791524, 0.027, -31.37172615, -0.0002, -31.37172615, -0.0132, -16.83791524, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 5030441, 67.10090505, 0.0002, 67.10090505, 0.0132, 34.16712829, 0.027, -67.10090505, -0.0002, -67.10090505, -0.0132, -34.16712829, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 5030430, 5030431, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 5030440, 5030441, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 5030450, 7125000.0)
    ops.section('Aggregator', 10050304, 5030450, 'P', 99999, 'Vy', 99999, 'Vz', 5030440, 'My', 5030430, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10050304, 50304, 10050304, 10050304, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 0, 5)
    ops.node(5, 0.0, 0.0, 13.5, '-mass', 3.983696970088527, 3.983696970088527, 3.983696970088527, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10000005, 0.0, 0.0, 13.5) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 531, 47.05631913, 0.0002, 47.05631913, 0.0132, 23.39302696, 0.027, -47.05631913, -0.0002, -47.05631913, -0.0132, -23.39302696, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 541, 70.58538606, 0.0002, 70.58538606, 0.0132, 34.12229195, 0.027, -70.58538606, -0.0002, -70.58538606, -0.0132, -34.12229195, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 530, 531, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 540, 541, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 550, 8906250.0)
    ops.section('Aggregator', 10000005, 550, 'P', 99999, 'Vy', 99999, 'Vz', 540, 'My', 530, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10000005, 5, 10000005, 10000005, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 0, 5)
    ops.node(10005, 6.1, 0.0, 13.5, '-mass', 7.485742564030264, 7.485742564030264, 7.485742564030264, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10010005, 6.1, 0.0, 13.5) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 1000531, 53.92376217, 0.0002, 53.92376217, 0.0132, 28.409379, 0.027, -53.92376217, -0.0002, -53.92376217, -0.0132, -28.409379, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 1000541, 79.37660018, 0.0002, 79.37660018, 0.0132, 40.6634116, 0.027, -79.37660018, -0.0002, -79.37660018, -0.0132, -40.6634116, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 1000530, 1000531, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 1000540, 1000541, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 1000550, 8906250.0)
    ops.section('Aggregator', 10010005, 1000550, 'P', 99999, 'Vy', 99999, 'Vz', 1000540, 'My', 1000530, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10010005, 10005, 10010005, 10010005, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 0, 5)
    ops.node(20005, 12.2, 0.0, 13.5, '-mass', 4.229109814125224, 4.229109814125224, 4.229109814125224, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10020005, 12.2, 0.0, 13.5) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 2000531, 47.50826516, 0.0002, 47.50826516, 0.0132, 23.73338489, 0.027, -47.50826516, -0.0002, -47.50826516, -0.0132, -23.73338489, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 2000541, 71.15981633, 0.0002, 71.15981633, 0.0132, 34.56370082, 0.027, -71.15981633, -0.0002, -71.15981633, -0.0132, -34.56370082, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 2000530, 2000531, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 2000540, 2000541, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 2000550, 8906250.0)
    ops.section('Aggregator', 10020005, 2000550, 'P', 99999, 'Vy', 99999, 'Vz', 2000540, 'My', 2000530, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10020005, 20005, 10020005, 10020005, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 0, 5)
    ops.node(30005, 15.05, 0.0, 13.5, '-mass', 4.2291098141252235, 4.2291098141252235, 4.2291098141252235, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10030005, 15.05, 0.0, 13.5) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 3000531, 47.50826516, 0.0002, 47.50826516, 0.0132, 23.73338489, 0.027, -47.50826516, -0.0002, -47.50826516, -0.0132, -23.73338489, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 3000541, 71.15981633, 0.0002, 71.15981633, 0.0132, 34.56370082, 0.027, -71.15981633, -0.0002, -71.15981633, -0.0132, -34.56370082, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 3000530, 3000531, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 3000540, 3000541, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 3000550, 8906250.0)
    ops.section('Aggregator', 10030005, 3000550, 'P', 99999, 'Vy', 99999, 'Vz', 3000540, 'My', 3000530, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10030005, 30005, 10030005, 10030005, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (4, 0, 5)
    ops.node(40005, 21.15, 0.0, 13.5, '-mass', 7.485742564030265, 7.485742564030265, 7.485742564030265, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10040005, 21.15, 0.0, 13.5) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 4000531, 53.92376217, 0.0002, 53.92376217, 0.0132, 28.409379, 0.027, -53.92376217, -0.0002, -53.92376217, -0.0132, -28.409379, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 4000541, 79.37660018, 0.0002, 79.37660018, 0.0132, 40.6634116, 0.027, -79.37660018, -0.0002, -79.37660018, -0.0132, -40.6634116, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 4000530, 4000531, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 4000540, 4000541, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 4000550, 8906250.0)
    ops.section('Aggregator', 10040005, 4000550, 'P', 99999, 'Vy', 99999, 'Vz', 4000540, 'My', 4000530, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10040005, 40005, 10040005, 10040005, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (5, 0, 5)
    ops.node(50005, 27.25, 0.0, 13.5, '-mass', 3.9836969700885283, 3.9836969700885283, 3.9836969700885283, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10050005, 27.25, 0.0, 13.5) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 5000531, 47.05631913, 0.0002, 47.05631913, 0.0132, 23.39302696, 0.027, -47.05631913, -0.0002, -47.05631913, -0.0132, -23.39302696, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 5000541, 70.58538606, 0.0002, 70.58538606, 0.0132, 34.12229195, 0.027, -70.58538606, -0.0002, -70.58538606, -0.0132, -34.12229195, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 5000530, 5000531, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 5000540, 5000541, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 5000550, 8906250.0)
    ops.section('Aggregator', 10050005, 5000550, 'P', 99999, 'Vy', 99999, 'Vz', 5000540, 'My', 5000530, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10050005, 50005, 10050005, 10050005, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 1, 5)
    ops.node(105, 0.0, 3.75, 13.5, '-mass', 7.478708924886533, 7.478708924886533, 7.478708924886533, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10000105, 0.0, 3.75, 13.5) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 10531, 67.44942663, 0.0002, 67.44942663, 0.0132, 34.90492571, 0.027, -67.44942663, -0.0002, -67.44942663, -0.0132, -34.90492571, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 10541, 135.22301919, 0.0002, 135.22301919, 0.0132, 66.69308763, 0.027, -135.22301919, -0.0002, -135.22301919, -0.0132, -66.69308763, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 10530, 10531, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 10540, 10541, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 10550, 10260000.0)
    ops.section('Aggregator', 10000105, 10550, 'P', 99999, 'Vy', 99999, 'Vz', 10540, 'My', 10530, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10000105, 105, 10000105, 10000105, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 1, 5)
    ops.node(10105, 6.1, 3.75, 13.5, '-mass', 14.018885739681325, 14.018885739681325, 14.018885739681325, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10010105, 6.1, 3.75, 13.5) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 1010531, 61.64200177, 0.0002, 61.64200177, 0.0132, 33.7900074, 0.027, -61.64200177, -0.0002, -61.64200177, -0.0132, -33.7900074, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 1010541, 139.41447602, 0.0002, 139.41447602, 0.0132, 71.5190074, 0.027, -139.41447602, -0.0002, -139.41447602, -0.0132, -71.5190074, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 1010530, 1010531, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 1010540, 1010541, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 1010550, 7125000.0)
    ops.section('Aggregator', 10010105, 1010550, 'P', 99999, 'Vy', 99999, 'Vz', 1010540, 'My', 1010530, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10010105, 10105, 10010105, 10010105, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 1, 5)
    ops.node(20105, 12.2, 3.75, 13.5, '-mass', 10.968752297962189, 10.968752297962189, 10.968752297962189, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10020105, 12.2, 3.75, 13.5) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 2010531, 57.45637015, 0.0002, 57.45637015, 0.0132, 30.89621793, 0.027, -57.45637015, -0.0002, -57.45637015, -0.0132, -30.89621793, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 2010541, 132.45078819, 0.0002, 132.45078819, 0.0132, 66.47634791, 0.027, -132.45078819, -0.0002, -132.45078819, -0.0132, -66.47634791, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 2010530, 2010531, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 2010540, 2010541, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 2010550, 7125000.0)
    ops.section('Aggregator', 10020105, 2010550, 'P', 99999, 'Vy', 99999, 'Vz', 2010540, 'My', 2010530, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10020105, 20105, 10020105, 10020105, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 1, 5)
    ops.node(30105, 15.05, 3.75, 13.5, '-mass', 10.968752297962185, 10.968752297962185, 10.968752297962185, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10030105, 15.05, 3.75, 13.5) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 3010531, 57.45637015, 0.0002, 57.45637015, 0.0132, 30.89621793, 0.027, -57.45637015, -0.0002, -57.45637015, -0.0132, -30.89621793, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 3010541, 132.45078819, 0.0002, 132.45078819, 0.0132, 66.47634791, 0.027, -132.45078819, -0.0002, -132.45078819, -0.0132, -66.47634791, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 3010530, 3010531, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 3010540, 3010541, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 3010550, 7125000.0)
    ops.section('Aggregator', 10030105, 3010550, 'P', 99999, 'Vy', 99999, 'Vz', 3010540, 'My', 3010530, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10030105, 30105, 10030105, 10030105, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (4, 1, 5)
    ops.node(40105, 21.15, 3.75, 13.5, '-mass', 14.018885739681325, 14.018885739681325, 14.018885739681325, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10040105, 21.15, 3.75, 13.5) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 4010531, 61.64200177, 0.0002, 61.64200177, 0.0132, 33.7900074, 0.027, -61.64200177, -0.0002, -61.64200177, -0.0132, -33.7900074, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 4010541, 139.41447602, 0.0002, 139.41447602, 0.0132, 71.5190074, 0.027, -139.41447602, -0.0002, -139.41447602, -0.0132, -71.5190074, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 4010530, 4010531, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 4010540, 4010541, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 4010550, 7125000.0)
    ops.section('Aggregator', 10040105, 4010550, 'P', 99999, 'Vy', 99999, 'Vz', 4010540, 'My', 4010530, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10040105, 40105, 10040105, 10040105, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (5, 1, 5)
    ops.node(50105, 27.25, 3.75, 13.5, '-mass', 7.478708924886535, 7.478708924886535, 7.478708924886535, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10050105, 27.25, 3.75, 13.5) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 5010531, 67.44942663, 0.0002, 67.44942663, 0.0132, 34.90492571, 0.027, -67.44942663, -0.0002, -67.44942663, -0.0132, -34.90492571, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 5010541, 135.22301919, 0.0002, 135.22301919, 0.0132, 66.69308763, 0.027, -135.22301919, -0.0002, -135.22301919, -0.0132, -66.69308763, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 5010530, 5010531, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 5010540, 5010541, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 5010550, 10260000.0)
    ops.section('Aggregator', 10050105, 5010550, 'P', 99999, 'Vy', 99999, 'Vz', 5010540, 'My', 5010530, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10050105, 50105, 10050105, 10050105, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 2, 5)
    ops.node(205, 0.0, 7.5, 13.5, '-mass', 7.478708924886533, 7.478708924886533, 7.478708924886533, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10000205, 0.0, 7.5, 13.5) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 20531, 67.44942663, 0.0002, 67.44942663, 0.0132, 34.90492571, 0.027, -67.44942663, -0.0002, -67.44942663, -0.0132, -34.90492571, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 20541, 135.22301919, 0.0002, 135.22301919, 0.0132, 66.69308763, 0.027, -135.22301919, -0.0002, -135.22301919, -0.0132, -66.69308763, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 20530, 20531, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 20540, 20541, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 20550, 10260000.0)
    ops.section('Aggregator', 10000205, 20550, 'P', 99999, 'Vy', 99999, 'Vz', 20540, 'My', 20530, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10000205, 205, 10000205, 10000205, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 2, 5)
    ops.node(10205, 6.1, 7.5, 13.5, '-mass', 14.018885739681325, 14.018885739681325, 14.018885739681325, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10010205, 6.1, 7.5, 13.5) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 1020531, 61.64200177, 0.0002, 61.64200177, 0.0132, 33.7900074, 0.027, -61.64200177, -0.0002, -61.64200177, -0.0132, -33.7900074, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 1020541, 139.41447602, 0.0002, 139.41447602, 0.0132, 71.5190074, 0.027, -139.41447602, -0.0002, -139.41447602, -0.0132, -71.5190074, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 1020530, 1020531, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 1020540, 1020541, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 1020550, 7125000.0)
    ops.section('Aggregator', 10010205, 1020550, 'P', 99999, 'Vy', 99999, 'Vz', 1020540, 'My', 1020530, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10010205, 10205, 10010205, 10010205, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 2, 5)
    ops.node(20205, 12.2, 7.5, 13.5, '-mass', 10.485974570120407, 10.485974570120407, 10.485974570120407, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10020205, 12.2, 7.5, 13.5) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 2020531, 56.75759274, 0.0002, 56.75759274, 0.0132, 30.40796996, 0.027, -56.75759274, -0.0002, -56.75759274, -0.0132, -30.40796996, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 2020541, 131.29898907, 0.0002, 131.29898907, 0.0132, 65.63054736, 0.027, -131.29898907, -0.0002, -131.29898907, -0.0132, -65.63054736, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 2020530, 2020531, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 2020540, 2020541, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 2020550, 7125000.0)
    ops.section('Aggregator', 10020205, 2020550, 'P', 99999, 'Vy', 99999, 'Vz', 2020540, 'My', 2020530, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10020205, 20205, 10020205, 10020205, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 2, 5)
    ops.node(30205, 15.05, 7.5, 13.5, '-mass', 10.485974570120403, 10.485974570120403, 10.485974570120403, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10030205, 15.05, 7.5, 13.5) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 3020531, 56.75759274, 0.0002, 56.75759274, 0.0132, 30.40796996, 0.027, -56.75759274, -0.0002, -56.75759274, -0.0132, -30.40796996, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 3020541, 131.29898907, 0.0002, 131.29898907, 0.0132, 65.63054736, 0.027, -131.29898907, -0.0002, -131.29898907, -0.0132, -65.63054736, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 3020530, 3020531, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 3020540, 3020541, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 3020550, 7125000.0)
    ops.section('Aggregator', 10030205, 3020550, 'P', 99999, 'Vy', 99999, 'Vz', 3020540, 'My', 3020530, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10030205, 30205, 10030205, 10030205, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (4, 2, 5)
    ops.node(40205, 21.15, 7.5, 13.5, '-mass', 14.018885739681325, 14.018885739681325, 14.018885739681325, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10040205, 21.15, 7.5, 13.5) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 4020531, 61.64200177, 0.0002, 61.64200177, 0.0132, 33.7900074, 0.027, -61.64200177, -0.0002, -61.64200177, -0.0132, -33.7900074, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 4020541, 139.41447602, 0.0002, 139.41447602, 0.0132, 71.5190074, 0.027, -139.41447602, -0.0002, -139.41447602, -0.0132, -71.5190074, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 4020530, 4020531, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 4020540, 4020541, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 4020550, 7125000.0)
    ops.section('Aggregator', 10040205, 4020550, 'P', 99999, 'Vy', 99999, 'Vz', 4020540, 'My', 4020530, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10040205, 40205, 10040205, 10040205, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (5, 2, 5)
    ops.node(50205, 27.25, 7.5, 13.5, '-mass', 7.478708924886535, 7.478708924886535, 7.478708924886535, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10050205, 27.25, 7.5, 13.5) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 5020531, 67.44942663, 0.0002, 67.44942663, 0.0132, 34.90492571, 0.027, -67.44942663, -0.0002, -67.44942663, -0.0132, -34.90492571, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 5020541, 135.22301919, 0.0002, 135.22301919, 0.0132, 66.69308763, 0.027, -135.22301919, -0.0002, -135.22301919, -0.0132, -66.69308763, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 5020530, 5020531, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 5020540, 5020541, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 5020550, 10260000.0)
    ops.section('Aggregator', 10050205, 5020550, 'P', 99999, 'Vy', 99999, 'Vz', 5020540, 'My', 5020530, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10050205, 50205, 10050205, 10050205, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (0, 3, 5)
    ops.node(305, 0.0, 11.25, 13.5, '-mass', 3.983696970088527, 3.983696970088527, 3.983696970088527, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10000305, 0.0, 11.25, 13.5) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 30531, 47.05631913, 0.0002, 47.05631913, 0.0132, 23.39302696, 0.027, -47.05631913, -0.0002, -47.05631913, -0.0132, -23.39302696, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 30541, 70.58538606, 0.0002, 70.58538606, 0.0132, 34.12229195, 0.027, -70.58538606, -0.0002, -70.58538606, -0.0132, -34.12229195, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 30530, 30531, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 30540, 30541, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 30550, 8906250.0)
    ops.section('Aggregator', 10000305, 30550, 'P', 99999, 'Vy', 99999, 'Vz', 30540, 'My', 30530, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10000305, 305, 10000305, 10000305, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (1, 3, 5)
    ops.node(10305, 6.1, 11.25, 13.5, '-mass', 7.485742564030264, 7.485742564030264, 7.485742564030264, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10010305, 6.1, 11.25, 13.5) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 1030531, 53.92376217, 0.0002, 53.92376217, 0.0132, 28.409379, 0.027, -53.92376217, -0.0002, -53.92376217, -0.0132, -28.409379, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 1030541, 79.37660018, 0.0002, 79.37660018, 0.0132, 40.6634116, 0.027, -79.37660018, -0.0002, -79.37660018, -0.0132, -40.6634116, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 1030530, 1030531, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 1030540, 1030541, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 1030550, 8906250.0)
    ops.section('Aggregator', 10010305, 1030550, 'P', 99999, 'Vy', 99999, 'Vz', 1030540, 'My', 1030530, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10010305, 10305, 10010305, 10010305, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (2, 3, 5)
    ops.node(20305, 12.2, 11.25, 13.5, '-mass', 5.6198986000449125, 5.6198986000449125, 5.6198986000449125, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10020305, 12.2, 11.25, 13.5) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 2030531, 50.41999366, 0.0002, 50.41999366, 0.0132, 25.8873579, 0.027, -50.41999366, -0.0002, -50.41999366, -0.0132, -25.8873579, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 2030541, 74.87576444, 0.0002, 74.87576444, 0.0132, 37.36623298, 0.027, -74.87576444, -0.0002, -74.87576444, -0.0132, -37.36623298, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 2030530, 2030531, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 2030540, 2030541, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 2030550, 8906250.0)
    ops.section('Aggregator', 10020305, 2030550, 'P', 99999, 'Vy', 99999, 'Vz', 2030540, 'My', 2030530, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10020305, 20305, 10020305, 10020305, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (3, 3, 5)
    ops.node(30305, 15.05, 11.25, 13.5, '-mass', 5.619898600044912, 5.619898600044912, 5.619898600044912, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10030305, 15.05, 11.25, 13.5) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 3030531, 50.41999366, 0.0002, 50.41999366, 0.0132, 25.8873579, 0.027, -50.41999366, -0.0002, -50.41999366, -0.0132, -25.8873579, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 3030541, 74.87576444, 0.0002, 74.87576444, 0.0132, 37.36623298, 0.027, -74.87576444, -0.0002, -74.87576444, -0.0132, -37.36623298, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 3030530, 3030531, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 3030540, 3030541, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 3030550, 8906250.0)
    ops.section('Aggregator', 10030305, 3030550, 'P', 99999, 'Vy', 99999, 'Vz', 3030540, 'My', 3030530, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10030305, 30305, 10030305, 10030305, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (4, 3, 5)
    ops.node(40305, 21.15, 11.25, 13.5, '-mass', 7.485742564030265, 7.485742564030265, 7.485742564030265, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10040305, 21.15, 11.25, 13.5) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 4030531, 53.92376217, 0.0002, 53.92376217, 0.0132, 28.409379, 0.027, -53.92376217, -0.0002, -53.92376217, -0.0132, -28.409379, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 4030541, 79.37660018, 0.0002, 79.37660018, 0.0132, 40.6634116, 0.027, -79.37660018, -0.0002, -79.37660018, -0.0132, -40.6634116, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 4030530, 4030531, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 4030540, 4030541, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 4030550, 8906250.0)
    ops.section('Aggregator', 10040305, 4030550, 'P', 99999, 'Vy', 99999, 'Vz', 4030540, 'My', 4030530, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10040305, 40305, 10040305, 10040305, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

    # Joint grid ids (x, y, z): (5, 3, 5)
    ops.node(50305, 27.25, 11.25, 13.5, '-mass', 3.9836969700885283, 3.9836969700885283, 3.9836969700885283, 0.0, 0.0, 0.0)
    # Joint flexibility model: inelastic
    ops.node(10050305, 27.25, 11.25, 13.5) # Constrained floor node
    ops.uniaxialMaterial('Hysteretic', 5030531, 47.05631913, 0.0002, 47.05631913, 0.0132, 23.39302696, 0.027, -47.05631913, -0.0002, -47.05631913, -0.0132, -23.39302696, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('Hysteretic', 5030541, 70.58538606, 0.0002, 70.58538606, 0.0132, 34.12229195, 0.027, -70.58538606, -0.0002, -70.58538606, -0.0132, -34.12229195, -0.027, 0.6, 0.2, 0.0, 0.0, 0.3)
    ops.uniaxialMaterial('MinMax', 5030530, 5030531, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('MinMax', 5030540, 5030541, '-min', -0.1, '-max', 0.1)
    ops.uniaxialMaterial('Elastic', 5030550, 8906250.0)
    ops.section('Aggregator', 10050305, 5030550, 'P', 99999, 'Vy', 99999, 'Vz', 5030540, 'My', 5030530, 'Mz', 99999, 'T')
    ops.element('zeroLengthSection', 10050305, 50305, 10050305, 10050305, '-orient', 0, 0, 1, 0, 1, 0, '-doRayleigh', 0)

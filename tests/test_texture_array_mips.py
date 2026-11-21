import pytest
import math
from render import texture_array_mips as mod

CASES = [
    ("layer", 'm.layer_v(0.5, 1, 4) == approx(0.375)'),
    ("size", 'm.mip_size(256, 3) == 32'),
    ("levels", 'm.mip_levels(256) == 9'),
    ("encode", 'm.srgb_to_linear(0.5) == approx(0.2176, abs=1e-3)'),
    ("decode", 'm.linear_to_srgb(0.2176) == approx(0.5, abs=1e-3)'),
    ("clamp", 'm.clamp_layer(5, 4) == 3'),
    ("pitch", 'm.row_pitch(100, 4, 256) == 512'),
    ("index", 'm.level_index(2) == 2'),
    ("block", 'm.block_size("bc1") == 4'),
    ("key", 'm.mip_key("tex", 3) == "tex:3"'),
    ("min", 'm.is_min_mip(64, 6) is True'),
    ("valid", 'm.valid_level(9, 9) is False'),
    ("chain", 'm.mip_chain_count(64) == 7'),
    ("count", 'm.layer_count(64, 2) == 16'),
    ("low", 'm.clamp_layer(-1, 4) == 0')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})

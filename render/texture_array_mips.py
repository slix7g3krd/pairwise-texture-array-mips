import math

def layer_v(v, layer, layers):
    """按层切分 v。"""
    raise NotImplementedError("TODO: layer_v")

def mip_size(size, level):
    """mip 尺寸。"""
    raise NotImplementedError("TODO: mip_size")

def mip_levels(size):
    """mip 级数。"""
    raise NotImplementedError("TODO: mip_levels")

def srgb_to_linear(value):
    """sRGB 转线性。"""
    raise NotImplementedError("TODO: srgb_to_linear")

def linear_to_srgb(value):
    """线性转 sRGB。"""
    raise NotImplementedError("TODO: linear_to_srgb")

def clamp_layer(layer, layers):
    """层钳制。"""
    raise NotImplementedError("TODO: clamp_layer")

def row_pitch(width, bpp, align):
    """行对齐。"""
    raise NotImplementedError("TODO: row_pitch")

def level_index(level):
    """层级索引。"""
    raise NotImplementedError("TODO: level_index")

def block_size(fmt):
    """块尺寸。"""
    raise NotImplementedError("TODO: block_size")

def mip_key(texture, level):
    """mip 键。"""
    raise NotImplementedError("TODO: mip_key")

def is_min_mip(size, level):
    """最小 mip。"""
    raise NotImplementedError("TODO: is_min_mip")

def valid_level(level, levels):
    """层级有效性。"""
    raise NotImplementedError("TODO: valid_level")

def mip_chain_count(size):
    """整链长度。"""
    raise NotImplementedError("TODO: mip_chain_count")

def layer_count(size, level):
    """层数。"""
    raise NotImplementedError("TODO: layer_count")

def layer_mip_v(v, layer, layers):
    """层内 mip v。"""
    raise NotImplementedError("TODO: layer_mip_v")

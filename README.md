# pairwise-texture-array-mips

同一张纹理数组在远处出现整层串色，各层的 mip 被打包进同一张图集，采样时 v 方向没有按层切分；手动生成 mip 只对第 0 层做了 box filter，其余层直接复制，远处出现块状色块；数组层数与 mip 级数不匹配，最后一层不足一层高度时越界读到相邻层；sRGB 纹理在生成 mip 时按线性值平均，暗部整体偏亮；各向异性过滤的采样位置在层边界处跨层插值，边缘出现条纹；纹理上传用了 row pitch 对齐到 256，层间出现斜切；mip 偏移按层计算但层级索引从 1 开始，整体错一层；压缩格式的块尺寸在最小 mip 上小于一块，解码器读出垃圾；数组纹理的 layer 参数在着色器里是浮点，插值后被四舍五入到错误层；流式加载时只替换了第 0 层，mip 链仍是旧内容。render/texture_array_mips.py 是核心，tests/test_texture_array_mips.py 15个红。要修的是：按层切分 v；逐层 box filter；层数与级数校验；sRGB 分别处理；层边界钳制；行对齐按实际；层级索引从 0；最小 mip 单独处理；layer 取整前钳制；整链替换。

## 运行

```bash
python -m pytest tests -q
```

初始状态：15 个用例失败。修复实现使全部用例通过，不要修改 `tests/` 下的测试。

子方向：见平台；任务类型：Bugfix；语言/框架：Python 3, pytest；环境可复现等级：无外部依赖。

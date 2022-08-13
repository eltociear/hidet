from typing import Union, Sequence, Optional
from hidet.ir.type import ScalarType, TensorType, Scope
from hidet.ir.expr import Expr, cast
from hidet.ir.mapping import row_spatial, row_repeat
from hidet.ir.layout import DataLayout
from hidet.ir.dialects.lowlevel import PointerType, VoidType, ReferenceType
from hidet.ir.primitives import printf
from hidet.lang.script import script, script_module

i32 = ScalarType('int32')
u32 = ScalarType('uint32')
i64 = ScalarType('int64')
f32 = ScalarType('float32')
f16 = ScalarType('float16')

ref_u32 = ReferenceType(u32)

void_pointer = PointerType(VoidType())

spatial = row_spatial
repeat = row_repeat

ConstExpr = Union[Expr, int]


def tensor(scope: Union[Scope, str],
           dtype: Union[ScalarType, str],
           shape: Optional[Sequence[ConstExpr]] = None,
           layout: Optional[DataLayout] = None):
    from hidet.ir.type import tensor_type
    return tensor_type(scope, dtype, shape, layout)

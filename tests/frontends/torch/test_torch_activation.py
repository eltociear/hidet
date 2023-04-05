# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import pytest
import torch
from hidet.testing.torch_utils import check_module


@pytest.mark.parametrize('shape', [(1, 1, 1), (33,), (3, 1)])
@pytest.mark.parametrize('dtype', [torch.float32])
def test_relu(shape, dtype):
    check_module(torch.nn.ReLU(), [torch.randn(shape, dtype=dtype)])


@pytest.mark.parametrize("shape", [(10, 20)])
@pytest.mark.parametrize("dtype", [torch.float32])
def test_hardsigmoid(shape, dtype):
    check_module(torch.nn.Hardsigmoid(), [torch.randn(shape, dtype=dtype)])


@pytest.mark.parametrize("shape", [(10, 20)])
@pytest.mark.parametrize("dtype", [torch.float32])
def test_sigmoid(shape, dtype):
    check_module(torch.nn.Sigmoid(), [torch.randn(shape, dtype=dtype)])


@pytest.mark.parametrize("shape", [(10, 20)])
@pytest.mark.parametrize("dtype", [torch.float32])
def test_hardswish(shape, dtype):
    check_module(torch.nn.Hardswish(), [torch.randn(shape, dtype=dtype)])


if __name__ == '__main__':
    pytest.main([__file__])
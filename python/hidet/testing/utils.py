from typing import List, Union, Callable, Any


def benchmark_func(run_func, warmup=1, number=5, repeat=5, median=True) -> Union[List[float], float]:
    """ Benchmark given function.

    The given function ``run_func`` will be executed :math:`warmup + repeat * number` times. Each :math:`number` times
    of execution will be grouped and conducted together.

    Parameters
    ----------
    run_func: Callable[[], Any]
        Any callable function to be benchmarked.

    warmup: int
        The number of warm-up executions.

    number: int
        The number of executions to be grouped for measurement.

    repeat: int
        The number of repeat times of the group measurement.

    median: bool
        Whether the median latency is returned, instead of the latency.

    Returns
    -------
    ret: Union[float, List[float]]
        - When median == True, a single latency number is returned.
        - When median == False, the latency of each repeat is returned, as a list of floats.
    """
    from hidet.utils.nvtx_utils import nvtx_annotate
    from hidet.utils import cuda
    import numpy as np
    import time
    results = []
    with nvtx_annotate('warmup'):
        for i in range(warmup):
            run_func()
            cuda.device_synchronize()
    for i in range(repeat):
        with nvtx_annotate(f'repeat {i}'):
            cuda.device_synchronize()
            start_time = time.time()
            for j in range(number):
                run_func()
            cuda.device_synchronize()
            end_time = time.time()
        results.append((end_time - start_time) * 1000 / number)
    if median:
        return float(np.median(results))
    else:
        return results
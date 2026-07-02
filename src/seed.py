# src/seed.py
import random
import numpy as np
def set_seed(seed: int = 42) -> int:
    """
    Python random과 NumPy random의 seed를 고정한다.
Parameters
    ----------
    seed : int
        재현성을 위해 사용할 seed 값
Returns
    -------
    int
        적용한 seed 값
    """
    random.seed(seed)
    np.random.seed(seed)
    return seed

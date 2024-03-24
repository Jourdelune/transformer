from enum import Enum


class HyperParameters(Enum):
    """
    Class that represent all hyperparameters of the model
    """

    VOCAB_SIZE: int = 10_000
    DIM_MODEL: int = 512
    MAX_SEQ_LENGHT: int = 5
    N_LAYERS: int = 6
    BATCH_SIZE: int = 4
    HEADS: int = 8
    D_FFN: int = 2048

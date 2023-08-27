from typing import (
    List,
    Dict,
    Tuple,
    Union,
    Optional,
    Any,
    Callable,
    TypeVar,
    Generic,
    Sequence,
    Mapping,
)

TEXT = str
TEXT_SEQUENCE = Sequence[TEXT]
TEXT_TRANSLATION = Mapping[TEXT, TEXT]
PHRASE_TRANSLATION = Mapping[TEXT, TEXT_TRANSLATION]
MULTIPLE_PHRASES_TRANSLATION = List[PHRASE_TRANSLATION]

from typing import (
    List,
    Sequence,
    Mapping,
)

TEXT = str
TEXT_SEQUENCE = Sequence[TEXT]
TEXT_TRANSLATION = Mapping[TEXT, TEXT]
# PHRASE_TRANSLATION = Mapping[TEXT, TEXT_TRANSLATION]
PHRASE_TRANSLATION = Mapping[TEXT, TEXT]
MULTIPLE_PHRASES_TRANSLATION = List[PHRASE_TRANSLATION]

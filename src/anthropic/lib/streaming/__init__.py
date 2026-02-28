from typing import TYPE_CHECKING
from typing_extensions import TypeAlias

_lazy_from_imports: dict[str, str] = {}
_lazy_module_imports: dict[str, str] = {}

from ._types import (
    TextEvent as TextEvent,
    InputJsonEvent as InputJsonEvent,
    MessageStopEvent as MessageStopEvent,
    MessageStreamEvent as MessageStreamEvent,
    ContentBlockStopEvent as ContentBlockStopEvent,
    ParsedMessageStopEvent as ParsedMessageStopEvent,
    ParsedMessageStreamEvent as ParsedMessageStreamEvent,
    ParsedContentBlockStopEvent as ParsedContentBlockStopEvent,
)
from ._messages import (
    MessageStream as MessageStream,
    AsyncMessageStream as AsyncMessageStream,
    MessageStreamManager as MessageStreamManager,
    AsyncMessageStreamManager as AsyncMessageStreamManager,
)

if TYPE_CHECKING:
    from ._beta_types import (
        BetaInputJsonEvent as BetaInputJsonEvent,
        ParsedBetaTextEvent as ParsedBetaTextEvent,
        ParsedBetaMessageStopEvent as ParsedBetaMessageStopEvent,
        ParsedBetaMessageStreamEvent as ParsedBetaMessageStreamEvent,
        ParsedBetaContentBlockStopEvent as ParsedBetaContentBlockStopEvent,
    )

# FYI I vote beta == no backwards compatibility
#   otherwise I'll need a more elaborate lazy loader to take an expression
#   OR, intercept local usages too?
#     not just __getattr__ but also when this module uses one of these
#     i.e. use BetaTextEvent => ParsedBetaTextEvent (lazy load) within this module's locals/globals
#
# # For backwards compatibility
# BetaTextEvent: TypeAlias = ParsedBetaTextEvent
# BetaMessageStopEvent: TypeAlias = ParsedBetaMessageStopEvent[object]
# BetaMessageStreamEvent: TypeAlias = ParsedBetaMessageStreamEvent
# BetaContentBlockStopEvent: TypeAlias = ParsedBetaContentBlockStopEvent[object]

if TYPE_CHECKING:
    from ._beta_messages import (
        BetaMessageStream as BetaMessageStream,
        BetaAsyncMessageStream as BetaAsyncMessageStream,
        BetaMessageStreamManager as BetaMessageStreamManager,
        BetaAsyncMessageStreamManager as BetaAsyncMessageStreamManager,
    )

else:
    _lazy_from_imports.update({
        "BetaInputJsonEvent": "._beta_types",
        "ParsedBetaTextEvent": "._beta_types",
        "ParsedBetaMessageStopEvent": "._beta_types",
        "ParsedBetaMessageStreamEvent": "._beta_types",
        "ParsedBetaContentBlockStopEvent": "._beta_types",

        "BetaMessageStream": "._beta_messages",
        "BetaAsyncMessageStream": "._beta_messages",
        "BetaMessageStreamManager": "._beta_messages",
        "BetaAsyncMessageStreamManager": "._beta_messages",
    })

def __dir__() -> list[str]:
    return sorted(
        set(globals().keys())
            .union(_lazy_from_imports.keys())
    )


def __getattr__(name: str) -> object:
    if name in _lazy_module_imports:
        import importlib
        module = importlib.import_module(_lazy_module_imports[name], __spec__.parent)
        globals()[name] = module
        return module

    if name in _lazy_from_imports:
        import importlib
        # lazy loaded attrs on a module:
        module = importlib.import_module(_lazy_from_imports[name], __spec__.parent)
        value = getattr(module, name)
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

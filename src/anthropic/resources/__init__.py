# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.
_lazy_from_imports: dict[str, str] = {}
_lazy_module_imports: dict[str, str] = {}

from .beta import (
    Beta,
    AsyncBeta,
    BetaWithRawResponse,
    AsyncBetaWithRawResponse,
    BetaWithStreamingResponse,
    AsyncBetaWithStreamingResponse,
)
from .models import (
    Models,
    AsyncModels,
    ModelsWithRawResponse,
    AsyncModelsWithRawResponse,
    ModelsWithStreamingResponse,
    AsyncModelsWithStreamingResponse,
)
from .messages import (
    Messages,
    AsyncMessages,
    MessagesWithRawResponse,
    AsyncMessagesWithRawResponse,
    MessagesWithStreamingResponse,
    AsyncMessagesWithStreamingResponse,
)
from .completions import (
    Completions,
    AsyncCompletions,
    CompletionsWithRawResponse,
    AsyncCompletionsWithRawResponse,
    CompletionsWithStreamingResponse,
    AsyncCompletionsWithStreamingResponse,
)

__all__ = [
    "Completions",
    "AsyncCompletions",
    "CompletionsWithRawResponse",
    "AsyncCompletionsWithRawResponse",
    "CompletionsWithStreamingResponse",
    "AsyncCompletionsWithStreamingResponse",
    "Messages",
    "AsyncMessages",
    "MessagesWithRawResponse",
    "AsyncMessagesWithRawResponse",
    "MessagesWithStreamingResponse",
    "AsyncMessagesWithStreamingResponse",
    "Models",
    "AsyncModels",
    "ModelsWithRawResponse",
    "AsyncModelsWithRawResponse",
    "ModelsWithStreamingResponse",
    "AsyncModelsWithStreamingResponse",
    "Beta",
    "AsyncBeta",
    "BetaWithRawResponse",
    "AsyncBetaWithRawResponse",
    "BetaWithStreamingResponse",
    "AsyncBetaWithStreamingResponse",
]


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
        try:
            value.__module__ = "anthropic"
        except (TypeError, AttributeError):
            pass
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

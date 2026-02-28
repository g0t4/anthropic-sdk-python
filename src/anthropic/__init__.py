# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import typing as _t

# * lazy load at runtime
_lazy_from_imports: dict[str, str] = {
    # from .lib.tools import beta_tool, beta_async_tool
    "beta_tool": ".lib.tools",
    "beta_async_tool": ".lib.tools",

    # from .lib.vertex import *
    "AnthropicVertex": ".lib.vertex",
    "AsyncAnthropicVertex": ".lib.vertex",

    # from .lib.bedrock import *
    "AnthropicBedrock": ".lib.bedrock",
    "AsyncAnthropicBedrock": ".lib.bedrock",

    # from .lib.foundry import AnthropicFoundry as AnthropicFoundry, AsyncAnthropicFoundry as AsyncAnthropicFoundry
    "AnthropicFoundry": ".lib.foundry",
    "AsyncAnthropicFoundry": ".lib.foundry",

    # from .lib.streaming import *
    "TextEvent": ".lib.streaming",
    "InputJsonEvent": ".lib.streaming",
    "MessageStopEvent": ".lib.streaming",
    "MessageStreamEvent": ".lib.streaming",
    "ContentBlockStopEvent": ".lib.streaming",
    "ParsedMessageStopEvent": ".lib.streaming",
    "ParsedMessageStreamEvent": ".lib.streaming",
    "ParsedContentBlockStopEvent": ".lib.streaming",
    "MessageStream": ".lib.streaming",
    "AsyncMessageStream": ".lib.streaming",
    "MessageStreamManager": ".lib.streaming",
    "AsyncMessageStreamManager": ".lib.streaming",
    "BetaInputJsonEvent": ".lib.streaming",
    "ParsedBetaTextEvent": ".lib.streaming",
    "ParsedBetaMessageStopEvent": ".lib.streaming",
    "ParsedBetaMessageStreamEvent": ".lib.streaming",
    "ParsedBetaContentBlockStopEvent": ".lib.streaming",
    "BetaTextEvent": ".lib.streaming",
    "BetaMessageStopEvent": ".lib.streaming",
    "BetaMessageStreamEvent": ".lib.streaming",
    "BetaContentBlockStopEvent": ".lib.streaming",
    "BetaMessageStream": ".lib.streaming",
    "BetaAsyncMessageStream": ".lib.streaming",
    "BetaMessageStreamManager": ".lib.streaming",
    "BetaAsyncMessageStreamManager": ".lib.streaming",
}
_lazy_module_imports: dict[str, str] = {}

if _t.TYPE_CHECKING:
    from . import types
    from ._types import NOT_GIVEN, Omit, NoneType, NotGiven, Transport, ProxiesTypes, omit, not_given
else:
    _lazy_module_imports.update({ "types": "." })

    _lazy_from_imports.update({
        "NOT_GIVEN": "._types",
        "Omit": "._types",
        "NoneType": "._types",
        "NotGiven": "._types",
        "Transport": "._types",
        "ProxiesTypes": "._types",
        "omit": "._types",
        "not_given": "._types",
    })

from ._utils import file_from_path
from ._client import (
    Client,
    Stream,
    Timeout,
    Anthropic,
    Transport,
    AsyncClient,
    AsyncStream,
    AsyncAnthropic,
    RequestOptions,
)
from ._models import BaseModel
from ._version import __title__, __version__
from ._response import APIResponse as APIResponse, AsyncAPIResponse as AsyncAPIResponse
from ._constants import (
    AI_PROMPT as AI_PROMPT,
    HUMAN_PROMPT as HUMAN_PROMPT,
    DEFAULT_TIMEOUT,
    DEFAULT_MAX_RETRIES,
    DEFAULT_CONNECTION_LIMITS,
)
from ._exceptions import (
    APIError,
    ConflictError,
    NotFoundError,
    AnthropicError,
    APIStatusError,
    RateLimitError,
    APITimeoutError,
    BadRequestError,
    APIConnectionError,
    AuthenticationError,
    InternalServerError,
    PermissionDeniedError,
    UnprocessableEntityError,
    APIResponseValidationError,
)
from ._base_client import DefaultHttpxClient, DefaultAioHttpClient, DefaultAsyncHttpxClient
from ._utils._logs import setup_logging as _setup_logging
from .lib._parse._transform import transform_schema

__all__ = [
    "types",
    "__version__",
    "__title__",
    "NoneType",
    "Transport",
    "ProxiesTypes",
    "NotGiven",
    "NOT_GIVEN",
    "not_given",
    "Omit",
    "omit",
    "AnthropicError",
    "APIError",
    "APIStatusError",
    "APITimeoutError",
    "APIConnectionError",
    "APIResponseValidationError",
    "BadRequestError",
    "AuthenticationError",
    "PermissionDeniedError",
    "NotFoundError",
    "ConflictError",
    "UnprocessableEntityError",
    "RateLimitError",
    "InternalServerError",
    "Timeout",
    "RequestOptions",
    "Client",
    "AsyncClient",
    "Stream",
    "AsyncStream",
    "Anthropic",
    "AsyncAnthropic",
    "file_from_path",
    "BaseModel",
    "DEFAULT_TIMEOUT",
    "DEFAULT_MAX_RETRIES",
    "DEFAULT_CONNECTION_LIMITS",
    "DefaultHttpxClient",
    "DefaultAsyncHttpxClient",
    "DefaultAioHttpClient",
    "HUMAN_PROMPT",
    "AI_PROMPT",
    "beta_tool",
    "beta_async_tool",
    "transform_schema",
]

if not _t.TYPE_CHECKING:
    from ._utils._resources_proxy import resources as resources

if _t.TYPE_CHECKING:
    # * eager load for type checking

    # FYI each original import is marked, i.e.:
    # from .lib.tools import beta_tool, beta_async_tool
    from .lib.tools import beta_tool as beta_tool, beta_async_tool as beta_async_tool

    # from .lib.vertex import *
    from .lib.vertex import AnthropicVertex as AnthropicVertex, AsyncAnthropicVertex as AsyncAnthropicVertex

    # from .lib.bedrock import *
    from .lib.bedrock import AnthropicBedrock as AnthropicBedrock, AsyncAnthropicBedrock as AsyncAnthropicBedrock

    # from .lib.foundry import AnthropicFoundry as AnthropicFoundry, AsyncAnthropicFoundry as AsyncAnthropicFoundry
    from .lib.foundry import AnthropicFoundry as AnthropicFoundry, AsyncAnthropicFoundry as AsyncAnthropicFoundry

    # from .lib.streaming import *
    from .lib.streaming import (
        TextEvent as TextEvent,
        InputJsonEvent as InputJsonEvent,
        MessageStopEvent as MessageStopEvent,
        MessageStreamEvent as MessageStreamEvent,
        ContentBlockStopEvent as ContentBlockStopEvent,
        ParsedMessageStopEvent as ParsedMessageStopEvent,
        ParsedMessageStreamEvent as ParsedMessageStreamEvent,
        ParsedContentBlockStopEvent as ParsedContentBlockStopEvent,
        MessageStream as MessageStream,
        AsyncMessageStream as AsyncMessageStream,
        MessageStreamManager as MessageStreamManager,
        AsyncMessageStreamManager as AsyncMessageStreamManager,
        BetaInputJsonEvent as BetaInputJsonEvent,
        ParsedBetaTextEvent as ParsedBetaTextEvent,
        ParsedBetaMessageStopEvent as ParsedBetaMessageStopEvent,
        ParsedBetaMessageStreamEvent as ParsedBetaMessageStreamEvent,
        ParsedBetaContentBlockStopEvent as ParsedBetaContentBlockStopEvent,
        BetaTextEvent as BetaTextEvent,
        BetaMessageStopEvent as BetaMessageStopEvent,
        BetaMessageStreamEvent as BetaMessageStreamEvent,
        BetaContentBlockStopEvent as BetaContentBlockStopEvent,
        BetaMessageStream as BetaMessageStream,
        BetaAsyncMessageStream as BetaAsyncMessageStream,
        BetaMessageStreamManager as BetaMessageStreamManager,
        BetaAsyncMessageStreamManager as BetaAsyncMessageStreamManager,
    )


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

_setup_logging()

# Update the __module__ attribute for exported symbols so that
# error messages point to this module instead of the module
# it was originally defined in, e.g.
# anthropic._exceptions.NotFoundError -> anthropic.NotFoundError
__locals = locals()
for __name in __all__:
    if not __name.startswith("__"):
        try:
            __locals[__name].__module__ = "anthropic"
        except (TypeError, AttributeError, KeyError):
            # Some of our exported symbols are builtins which we can't set attributes for.
            # KeyError for lazy-loaded symbols (listed in __all__) but not yet loaded (into locals).
            pass

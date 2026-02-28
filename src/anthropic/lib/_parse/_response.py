from __future__ import annotations
from typing import TYPE_CHECKING

_lazy_from_imports: dict[str, str] = {}
_lazy_module_imports: dict[str, str] = {}

from typing_extensions import TypeVar

from ..._types import NotGiven
from ..._models import TypeAdapter, construct_type_unchecked
from ..._utils._utils import is_given
from ...types.message import Message
from ...types.parsed_message import ParsedMessage, ParsedTextBlock, ParsedContentBlock
if TYPE_CHECKING:
    from ...types.beta.beta_message import BetaMessage
    from ...types.beta.parsed_beta_message import ParsedBetaMessage, ParsedBetaContentBlock
else:
    _lazy_from_imports.update({
        "BetaMessage": "...types.beta.beta_message",
        "ParsedBetaMessage": "...types.beta.parsed_beta_message",
        "ParsedBetaTextBlock": "...types.beta.parsed_beta_message",
        "ParsedBetaContentBlock": "...types.beta.parsed_beta_message",
    })

ResponseFormatT = TypeVar("ResponseFormatT", default=None)


def parse_text(text: str, output_format: ResponseFormatT | NotGiven) -> ResponseFormatT | None:
    if is_given(output_format):
        adapted_type: TypeAdapter[ResponseFormatT] = TypeAdapter(output_format)
        return adapted_type.validate_json(text)
    return None


def parse_beta_response(
    *,
    output_format: ResponseFormatT | NotGiven,
    response: BetaMessage,
) -> ParsedBetaMessage[ResponseFormatT]:
    content_list: list[ParsedBetaContentBlock[ResponseFormatT]] = []
    for content in response.content:
        if content.type == "text":
            from ...types.beta.parsed_beta_message import ParsedBetaTextBlock
            content_list.append(
                construct_type_unchecked(
                    type_=ParsedBetaTextBlock[ResponseFormatT],
                    value={**content.to_dict(), "parsed_output": parse_text(content.text, output_format)},
                )
            )
        else:
            content_list.append(content)  # type: ignore

    from ...types.beta.parsed_beta_message import ParsedBetaMessage
    return construct_type_unchecked(
        type_=ParsedBetaMessage[ResponseFormatT],
        value={
            **response.to_dict(),
            "content": content_list,
        },
    )


def parse_response(
    *,
    output_format: ResponseFormatT | NotGiven,
    response: Message,
) -> ParsedMessage[ResponseFormatT]:
    content_list: list[ParsedContentBlock[ResponseFormatT]] = []
    for content in response.content:
        if content.type == "text":
            content_list.append(
                construct_type_unchecked(
                    type_=ParsedTextBlock[ResponseFormatT],
                    value={**content.to_dict(), "parsed_output": parse_text(content.text, output_format)},
                )
            )
        else:
            content_list.append(content)  # type: ignore

    return construct_type_unchecked(
        type_=ParsedMessage[ResponseFormatT],
        value={
            **response.to_dict(),
            "content": content_list,
        },
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
        globals()[name] = value
        return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

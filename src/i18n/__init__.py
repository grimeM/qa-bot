from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from i18n.stub import TranslatorRunner  # type: ignore
else:
    from fluentogram import TranslatorRunner

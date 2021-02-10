import typing

from core.basic_models.requirement.basic_requirements import Requirement
from core.model.base_user import BaseUser
from core.text_preprocessing.preprocessing_result import TextPreprocessingResult

# noinspection PyUnresolvedReferences
from saf_patterns.phrase_engine import DEFAULT_MORPHER, PatternMatcher, SharpList, SharpString


class PatternRequirement(Requirement):
    matcher: PatternMatcher

    MORPHER = DEFAULT_MORPHER

    # noinspection PyShadowingBuiltins
    def __init__(self, items: typing.Dict[str, typing.Any], id: typing.Optional[str] = None):
        super().__init__(items, id)

        patterns = items.get("patterns")
        sharp_patterns = SharpList[SharpString]()
        for pattern in patterns:
            sharp_patterns.Add(pattern.lower())

        self.matcher = PatternMatcher.Create(self.MORPHER, sharp_patterns)

    def check(self, text_preprocessing_result: TextPreprocessingResult, user: BaseUser,
              params: typing.Dict[str, typing.Any] = None) -> bool:
        return bool(self.matcher.Match(text_preprocessing_result.original_text, None, None, None, self.MORPHER))

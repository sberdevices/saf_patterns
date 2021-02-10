import typing

import lazy
from core.basic_models.actions.basic_actions import Action
from core.basic_models.actions.command import Command
from core.logging.logger_utils import log
from core.model.factory import factory
from core.text_preprocessing.preprocessing_result import TextPreprocessingResult
from scenarios.actions.action import RunScenarioAction
from scenarios.user.user_model import User

# noinspection PyUnresolvedReferences
from saf_patterns.phrase_engine import DEFAULT_MORPHER, PatternMatcher, SharpList, SharpString


class PatternResolveScenario(Action):
    matcher: PatternMatcher
    scenarios: typing.Dict[str, typing.List[str]]
    else_action: typing.Optional[Action]

    MORPHER = DEFAULT_MORPHER

    # noinspection PyShadowingBuiltins
    def __init__(self, items: typing.Dict[str, typing.Any], id: typing.Optional[str] = None):
        super().__init__(items, id)
        self.scenarios = items["scenarios"]
        self._else_action = items.get("else")
        self.matcher = PatternMatcher.Create(self.MORPHER, self.extract_patterns())

    def run(
            self,
            user: User,
            text_preprocessing_result: TextPreprocessingResult,
            params: typing.Optional[typing.Dict[str, typing.Union[str, float, int]]] = None
    ) -> typing.Optional[typing.List[Command]]:

        matches = self.matcher.Match(text_preprocessing_result.original_text, None, None, None, self.MORPHER)
        if matches:
            best_match = max(tuple(matches), key=lambda x: x.Value.ExplicitLiteralsMatched)
            scenario_id, *_ = best_match.Value.GroupName.split("_")
            log(
                f"%(class_name)s.run: switch to {scenario_id}.", params={"class_name": self.__class__.__name__},
                user=user
            )
            return RunScenarioAction({"scenario": scenario_id}).run(user, text_preprocessing_result, params)
        log(
            f"%(class_name)s.run: no match. run else action.", params={"class_name": self.__class__.__name__},
            user=user
        )
        return self.else_action.run(user, text_preprocessing_result, params)

    @lazy.lazy
    @factory(Action)
    def else_action(self):
        return self._else_action

    def extract_patterns(self):
        sharp_patterns = SharpList[SharpString]()
        for index, (key, patterns) in enumerate(self.scenarios.items()):
            for sub_index, pattern in enumerate(patterns):
                sharp_patterns.Add(f"「{key}_{index}_{sub_index}」" + pattern.lower())
        return sharp_patterns

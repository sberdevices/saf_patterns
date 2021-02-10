import types

import smart_kit
from core.basic_models.actions.basic_actions import actions as saf_actions
from core.basic_models.requirement.basic_requirements import requirements as saf_requirements
from smart_kit.management.app_manager import AppManager

from saf_patterns.actions import PatternResolveScenario
from saf_patterns.requirements import PatternRequirement


def on_startup(app_config: types.ModuleType, manager: smart_kit.management.app_manager.AppManager):
    saf_requirements["pattern"] = PatternRequirement
    saf_actions["pattern_resolve_scenario"] = PatternResolveScenario

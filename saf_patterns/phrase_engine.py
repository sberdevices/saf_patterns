import sys
import clr
import saf_patterns
import os

sys.path.append(os.path.join(os.path.dirname(saf_patterns.__file__), "lib"))
clr.AddReference("PhraseEngine")

# noinspection PyUnresolvedReferences
from PhraseEngine import PatternMatcher, CachingMorpher
# noinspection PyUnresolvedReferences
from System import String as SharpString
# noinspection PyUnresolvedReferences
from System.Collections.Generic import List as SharpList

DEFAULT_MORPHER = CachingMorpher()

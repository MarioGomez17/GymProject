from . import DaySplitURLS
from . import ExerciseEquipmentURLS
from . import ExerciseRoutineTemplateURLS
from . import ExerciseTypeURLS
from . import ExerciseURLS
from . import ExerciseVariantURLS
from . import GenderURLS
from . import MuscleDayURLS
from . import MuscleURLS
from . import RoutineTemplateURLS
from . import RoutineURLS
from . import SerieURLS
from . import SplitURLS
from . import SplitUserURLS
from . import UserURLS
from . import WeightUnitURLS
from django.urls import path, include

urlpatterns = [
    path('', include(DaySplitURLS)),
    path('', include(ExerciseEquipmentURLS)),
    path('', include(ExerciseRoutineTemplateURLS)),
    path('', include(ExerciseTypeURLS)),
    path('', include(ExerciseURLS)),
    path('', include(ExerciseVariantURLS)),
    path('', include(GenderURLS)),
    path('', include(MuscleDayURLS)),
    path('', include(MuscleURLS)),
    path('', include(RoutineTemplateURLS)),
    path('', include(RoutineURLS)),
    path('', include(SerieURLS)),
    path('', include(SplitURLS)),
    path('', include(SplitUserURLS)),
    path('', include(UserURLS)),
    path('', include(WeightUnitURLS))
]

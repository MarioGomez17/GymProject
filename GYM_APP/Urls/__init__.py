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
    path('DaySplit', include(DaySplitURLS)),
    path('ExerciseEquipment', include(ExerciseEquipmentURLS)),
    path('ExerciseRoutineTemplate', include(ExerciseRoutineTemplateURLS)),
    path('ExerciseType', include(ExerciseTypeURLS)),
    path('Exercise', include(ExerciseURLS)),
    path('ExerciseVariant', include(ExerciseVariantURLS)),
    path('Gender', include(GenderURLS)),
    path('MuscleDay', include(MuscleDayURLS)),
    path('Muscle', include(MuscleURLS)),
    path('RoutineTemplate', include(RoutineTemplateURLS)),
    path('Routine', include(RoutineURLS)),
    path('Serie', include(SerieURLS)),
    path('Split', include(SplitURLS)),
    path('SplitUser', include(SplitUserURLS)),
    path('User', include(UserURLS)),
    path('WeightUnit', include(WeightUnitURLS))
]

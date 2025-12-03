from enum import Enum


class PreferenceType(str, Enum):
    ALLERGIES = "allergies"
    FAVOURITE_INGREDIENTS = "favourite_ingredients"
    FAVOURITE_CUISINES = "favourite_cuisines"

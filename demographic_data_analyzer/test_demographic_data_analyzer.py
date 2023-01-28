from pandas import DataFrame

from demographic_data_analyzer.demographic_data_analyzer import (
    read_data,
    get_number_races,
    get_average_age_men,
    get_percentage_bachelors,
    get_percentage_rich_higher_education,
    get_percentage_rich_lower_education,
    get_min_work_hours,
    get_percentage_min_work_hours,
    get_highest_earning_country,
    get_most_popular_occupation,
)

ADULT_DF = read_data()


def test_read_data() -> None:
    assert isinstance(ADULT_DF, DataFrame)
    assert ADULT_DF.shape[0] > 0
    assert ADULT_DF.shape[1] == 15
    assert "age" in ADULT_DF.columns
    assert "fnlwgt" in ADULT_DF.columns


def test_get_number_races() -> None:
    race_count = get_number_races(ADULT_DF)

    assert race_count == [27816, 3124, 1039, 311, 271]


def test_get_average_age_men() -> None:
    average_age_men = get_average_age_men(ADULT_DF)

    assert average_age_men == 39.4


def test_get_percentage_bachelors() -> None:
    percentage_bachelors = get_percentage_bachelors(ADULT_DF)

    assert percentage_bachelors == 16.4


def test_get_percentage_rich_higher_education() -> None:
    percentage_rich_higher_education = get_percentage_rich_higher_education(
        ADULT_DF
    )

    assert percentage_rich_higher_education == 46.5


def test_get_percentage_rich_lower_education() -> None:
    percentage_rich_lower_education = get_percentage_rich_lower_education(
        ADULT_DF
    )

    assert percentage_rich_lower_education == 17.4


def test_get_min_work_hours() -> None:
    min_work_hours = get_min_work_hours(ADULT_DF)

    assert min_work_hours == 1


def test_get_percentage_min_work_hours() -> None:
    percentage_min_work_hours = get_percentage_min_work_hours(ADULT_DF)

    assert percentage_min_work_hours == 10.0


def test_get_highest_earning_country() -> None:
    highest_earning_country = get_highest_earning_country(ADULT_DF)

    assert highest_earning_country == "Iran"


def test_get_most_popular_occupation() -> None:
    most_popular_occupation = get_most_popular_occupation(ADULT_DF)

    assert most_popular_occupation == "Prof-specialty"

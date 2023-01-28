import pandas as pd
from pandas import DataFrame

HIGHER_EDUCATION = ["Bachelors", "Masters", "Doctorate"]


def read_data() -> DataFrame:
    """
    The function returns a dataframe from the adult.data.csv file.
    """
    adult_df = pd.read_csv("adult.data.csv")

    return adult_df


def get_number_races(adult_df: DataFrame) -> list[int]:
    """
    The function returns the number of each race represented
    in adult_df.
    """
    number_of_races = adult_df["race"].value_counts().tolist()

    return number_of_races


def get_average_age_men(adult_df: DataFrame) -> float:
    """
    The function returns the average age of men.
    """
    average_age_men = adult_df[adult_df["sex"] == "Male"]["age"].mean()

    return round(average_age_men, 1)


def get_percentage_bachelors(adult_df: DataFrame) -> float:
    """
    The function returns percentage of people who have
    a Bachelor's degree.
    """
    percentage_bachelors = (
        adult_df[adult_df["education"] == "Bachelors"].shape[0]
        / adult_df.shape[0]
    ) * 100

    return round(percentage_bachelors, 1)


def get_percentage_rich_higher_education(adult_df: DataFrame) -> float:
    """
    The function returns the percentage of people who have a higher education
    and earn more than 50K.
    """
    higher_education = adult_df[adult_df["education"].isin(HIGHER_EDUCATION)]
    rich_higher_education = higher_education[
        higher_education["salary"] == ">50K"
    ]
    percentage_rich_higher_education = (
        rich_higher_education.shape[0] / higher_education.shape[0]
    ) * 100

    return round(percentage_rich_higher_education, 1)


def get_percentage_rich_lower_education(adult_df: DataFrame,) -> float:
    """
    The function returns the percentage of people who have a lower education
    and earn less than 50K.
    """
    lower_education = adult_df[~adult_df["education"].isin(HIGHER_EDUCATION)]
    rich_lower_education = lower_education[lower_education["salary"] == ">50K"]
    percentage_rich_lower_education = (
        rich_lower_education.shape[0] / lower_education.shape[0]
    ) * 100

    return round(percentage_rich_lower_education, 1)


def get_min_work_hours(adult_df: DataFrame) -> int:
    """
    The function returns the minimum number of hours per week.
    """
    min_work_hours = adult_df["hours-per-week"].min()

    return min_work_hours


def get_percentage_min_work_hours(adult_df: DataFrame) -> float:
    """
    The function returns the percentage of people who work
    the minimum number of hours per week and earn more that 50K.
    """
    num_min_workers = adult_df[
        adult_df["hours-per-week"] == get_min_work_hours(adult_df)
    ]
    num_min_workers_rich = num_min_workers[num_min_workers["salary"] == ">50K"]
    percentage_min_work_hours = (
        num_min_workers_rich.shape[0] / num_min_workers.shape[0]
    ) * 100

    return round(percentage_min_work_hours, 1)


def get_highest_earning_country(adult_df: DataFrame) -> str:
    """
    The function returns the country with the highest percentage
    of people earning over 50K.
    """
    grouped_by_country = adult_df.groupby("native-country")
    grouped_by_country_rich = grouped_by_country["salary"].apply(
        lambda x: (x == ">50K").mean() * 100
    )
    highest_earning_country = grouped_by_country_rich.idxmax()

    return str(highest_earning_country)


def get_most_popular_occupation(adult_df: DataFrame) -> str:
    """
    The function returns the most popular occupation of people
    from India who earn more than 50K.
    """
    grouped_by_india = adult_df[adult_df["native-country"] == "India"]
    grouped_by_india_rich = grouped_by_india[
        grouped_by_india["salary"] == ">50K"
    ]
    most_popular_occupation = grouped_by_india_rich["occupation"].mode()[0]

    return most_popular_occupation

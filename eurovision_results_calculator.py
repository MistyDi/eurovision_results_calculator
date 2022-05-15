from __future__ import annotations  # for compatibility with python 3.8 and 3.9

from collections import defaultdict


# `available_countries` needed for checking votes entries
#  Taken from: https://en.wikipedia.org/wiki/List_of_countries_in_the_Eurovision_Song_Contest (on RUS-version)
# TODO autofill: make auto-updating list of the countries
AVAILABLE_COUNTRIES: set[str] = {
    'Бельгия',
    'Германия',
    'Италия',
    'Люксембург',
    'Нидерланды',
    'Франция',
    'Швейцария',
    'Австрия',
    'Великобритания',
    'Дания',
    'Швеция',
    'Монако',
    'Норвегия',
    'Испания',
    'Финляндия',
    'Португалия',
    'Ирландия',
    'Мальта',
    'Израиль',
    'Греция',
    'Турция',
    'Марокко',
    'Кипр',
    'Исландия',
    'Босния и Герцеговина',
    'Словения',
    'Хорватия',
    'Венгрия',
    'Литва',
    'Польша',
    'Россия',
    'Румыния',
    'Словакия',
    'Эстония',
    'Северная Македония',
    'Латвия',
    'Украина',
    'Албания',
    'Андорра',
    'Белоруссия',
    'Болгария',
    'Молдавия',
    'Армения',
    'Грузия',
    'Сербия',
    'Черногория',
    'Чехия',
    'Азербайджан',
    'Сан-Марино',
    'Австралия',
}

# `coins` is a list of vote-coins in order from 1st place to 10th
COINS: list[int] = (list(range(1, 9)) + [10, 12])[::-1]  # [12, 10, 8, 7, 6, ..., 1]


def calc_eurovision_results(persons_answers: list[list[str]]) -> list[tuple[str, int]]:
    """
    NOTE: voting system [12, 10, 8, 7, 6, 5, 4, 3, 2, 1] - votes-coins for top-10 (higher-voted on the left)

    Example:
        >>> input_vals = [
        >>>     ['Норвегия', 'Италия', 'Финляндия'],
        >>>     ['Финляндия', 'Норвегия', 'Молдавия'],
        >>>     ['Испания', 'Швеция', 'Австралия']]
        >>> output_vals = calc_eurovision_results(input_vals)
        >>> print(output_vals)
        <<< 7) Молдавия: 8
        <<< 6) Австралия: 8
        <<< 5) Италия: 10
        <<< 4) Швеция: 10
        <<< 3) Испания: 12
        <<< 2) Финляндия: 20
        <<< 1) Норвегия: 22

    :param persons_answers: list of ranged country names, provided by persons
    :type persons_answers: list[list[str]]

    :return: list of tuples like (country, summary-count-of-votes), sorted by increasing of summary-count-of-votes
    :rtype: list[tuple[str, int]]
    """
    country2vote: dict[str, int] = defaultdict(int)

    for person_answers in persons_answers:
        person_answers2coins_zip = zip(person_answers, COINS)
        for country, votes_coins in person_answers2coins_zip:

            # Checking of typos (all answers should match the available body of countries):
            if country not in AVAILABLE_COUNTRIES:
                # TODO typo semi-auto fixing: add similarity prediction like: 'Moldva' -> 'Do you mean Moldova?'
                raise ValueError(
                    f'Country with the name "{country}" is not specified in the `available_countries`. Stopping.')
            country2vote[country] += votes_coins

    # TODO support of equal voted country: now if two countries will have equal votes, they will have different
    #  places, ranged by order-of-placing in dict `country2vote`. If countries have equal votes, they need to be
    #  placed at one place. Idea of realisation: dict `votes2list_countries`
    sorted_list: list[tuple[str, int]] = [(k, v) for k, v in dict.items(country2vote)]
    sorted_list.sort(key=lambda x: x[1], reverse=False)  # sorting by vote-coins from the less to the top
    return sorted_list


def print_eurovision_results(sorted_list: list[tuple[str, int]], top_n: None | int = None) -> None:
    """
    Formatted printing of the votes results. You also can limit the output only by top-N countries.

    :param sorted_list: result from the `calc_eurovision_results(...)` function
    :type sorted_list: list[tuple[str, int]]
    :param top_n: top-N countries to print
    :type top_n: None | int
    :return: None
    :rtype:
    """
    if top_n is None or top_n <= 0:
        top_n = len(sorted_list)  # defining `top_n`, because wasn't defined

    # Printing the top N (regulated by top_n) from the less- to the top-voted
    for i, (country, val) in enumerate(sorted_list[-top_n:]):
        print(f"{top_n - i}) {country}: {val}")

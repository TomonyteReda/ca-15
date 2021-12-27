from argparse import ArgumentParser
import calendar


"""Sukurti paleidžiamąjį failą iš programos, kuri:
Leistų vartotojui įvesti metus nuo ir metus iki
Atspausdintų visus keliamuosius metus pagal duotą rėžį"""


def get_year_values():
    argument_parser = ArgumentParser()
    argument_parser.add_argument('year_start')
    argument_parser.add_argument('year_end')
    args = argument_parser.parse_args()
    year_start = int(args.year_start)
    year_end = int(args.year_end)
    return year_start, year_end


def get_leap_years():
    year_start, year_end = get_year_values()
    years = list(range(year_start, year_end + 1))
    leap_years = [year for year in years if calendar.isleap(year)]
    return leap_years


if __name__ == '__main__':
    print(get_leap_years())





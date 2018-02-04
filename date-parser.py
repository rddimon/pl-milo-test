import calendar
import itertools

min_year = 2000
max_year = 2999


def is_correct_date(year, month, day):
    if not min_year <= year <= max_year:
        return False

    if not 1 <= month <= 12:
        return False

    if not 1 <= day <= calendar.monthrange(year, month)[1]:
        return False

    return True


def get_date(numbers):
    numbers.sort()

    for item in [x for x in itertools.permutations(numbers, 3)]:
        year, month, day = item
        year = min_year + year if year < 100 else year

        if is_correct_date(year, month, day):
            return "{}-{}-{}".format(year, month, day)

    return 'is illegal'


def read_date(text=None):
    if text:
        numbers = str(text).split('/')
        print(get_date([int(x) for x in numbers]))
    read_date(input('Enter something: '))


try:
    print('Use ctrl + c + enter to exit')
    read_date()
except KeyboardInterrupt:
    pass

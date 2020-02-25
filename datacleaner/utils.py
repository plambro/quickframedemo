# python imports
import csv
import re

# project imports
from datacleaner.models import CleanData

dataset = 'datacleaner/datasets/DataEngineerDataSet.csv'


def problem_one(entry: dict) -> bool:
    """Clean object number column to match valid examples.

   valid style is number.number.number
   '1979.486.5' is valid
   '64.62 is invalid'
   """
    pattern = '\d+\.\d+\.\d+'
    if re.match(pattern, entry['Object Number']) is not None:
        return True
    return False


def problem_two(entry: dict) -> dict:
    """Clean object date column to match start and end date style.

    date ranges (1843-56) become start 1843 end 1856
    cross century ranges (1843-1923) become start 1843 end 1923
    circa entries (Ca. 1843) become start 1840 end 1843
    """
    date_pattern = '\d{3,}'
    date = entry["Object Date"]

    try:
        if date == '' or date == 'unknown':
            return {'start': 'unknown', 'end': 'unknown'}
        elif re.match(date_pattern, date) is not None and '–' not in date:
            start = date
            end = date
        elif 'patented' in date.lower():
            start = re.search(date_pattern, date).group()
            end = start
        elif 'century' in date.lower() or 'cenutry' in date.lower():
            century = re.search('\d+', date).group()
            start = str(int(century) - 1) + '00'
            end = century + '00'
        elif 'ca' in date.lower() or 'before' in date.lower() or 'by' in date.lower():
            date = re.search(date_pattern, date).group()
            start = str(int(date) - 3)
            end = date
        elif 'after' in date.lower() or 'early' in date.lower():
            date = re.search(date_pattern, date).group()
            start = date
            end = str(int(date) + 3)
        elif '–' in date:
            dates = date.split('–')
            if len(dates[0]) == len(dates[1]):
                start = dates[0]
                end = dates[1]
            else:
                start = re.search(date_pattern, dates[0]).group()
                end = start[:2] + dates[1]
        elif re.search(date_pattern, date) is not None:
            start = re.search(date_pattern, date).group()
            end = start
        else:
            return {'start': 'unexpect format', 'end': 'unexpected format'}
    except:
        return {'start': f'error parsing {date}', 'end': f'error parsing {date}'}

    return {'start': start, 'end': end}


def clean_data(dataset):
    with open(dataset) as input:
        reader = csv.DictReader(input)
        for row in reader:
            if problem_one(row):
                date_results = problem_two(row)
                new_entry = CleanData.objects.create(object_number=row['Object Number'],
                                                     start_date=date_results['start'],
                                                     end_date=date_results['end'])
                new_entry.save()

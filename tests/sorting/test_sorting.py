from src.sorting import sort_by
from src.jobs import read


def test_sort_by_criteria():
    path = 'src/jobs.csv'
    jobs = read(path)
    sort_by(jobs, 'min_salary')
    assert jobs[1]['min_salary'] == '19875'
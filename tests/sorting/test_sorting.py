from src.sorting import sort_by
from src.jobs import read


def test_sort_by_criteria():
    path = 'src/jobs.csv'
    jobs = read(path)

    sort_by(jobs, 'min_salary')
    assert jobs[1]['min_salary'] == '19857'
    assert jobs[-2]['min_salary'] == ''

    sort_by(jobs, 'max_salary')
    assert jobs[1]['max_salary'] == '315439'
    assert jobs[-2]['max_salary'] == ''
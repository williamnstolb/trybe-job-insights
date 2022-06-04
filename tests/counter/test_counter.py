from src.counter import count_ocurrences


def test_counter():
    path = 'src/jobs.csv'
    assert count_ocurrences(path) == {'python': 1639, 'salary': 598, 'jobs': 306}

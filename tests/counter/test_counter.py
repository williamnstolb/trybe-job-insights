from src.counter import count_ocurrences


def test_counter():
    path = 'src/jobs.csv'
    assert count_ocurrences(path, 'Python') == 1639
    assert count_ocurrences(path, 'Java') == 0

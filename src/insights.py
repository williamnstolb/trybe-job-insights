from src.jobs import read


def get_unique_job_types(path):
    jobList = read(path)
    jobTypeList = list()
    for job in jobList:
        if job["job_type"] not in jobTypeList:
            jobTypeList.append(job["job_type"])
    return jobTypeList


def filter_by_job_type(jobs, job_type):
    filter = [job for job in jobs if job["job_type"] == job_type]
    return filter


def get_unique_industries(path):
    jobList = read(path)
    industryList = list()
    for job in jobList:
        if job["industry"] not in industryList and job["industry"]:
            industryList.append(job["industry"])
    return industryList


def filter_by_industry(jobs, industry):
    filter = [job for job in jobs if job["industry"] == industry]
    return filter


def get_max_salary(path):
    jobList = read(path)
    # Source: https://www.programiz.com
    # /python-programming/methods/built-in/max
    maxSalary = max(
        [
            int(item["max_salary"])
            for item in jobList
            if (item["max_salary"] != "" and item["max_salary"] != "invalid")
        ]
    )
    return maxSalary


def get_min_salary(path):
    jobList = read(path)
    # Source: https://www.programiz.com
    # /python-programming/methods/built-in/min
    minSalary = min(
        [
            int(item["min_salary"])
            for item in jobList
            if (item["min_salary"] != "" and item["min_salary"] != "invalid")
        ]
    )
    return minSalary


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or not isinstance(job["min_salary"], int)
        or not isinstance(job["max_salary"], int)
        or not isinstance(salary, int)
        or job["min_salary"] > job["max_salary"]
    ):
        return ValueError
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []

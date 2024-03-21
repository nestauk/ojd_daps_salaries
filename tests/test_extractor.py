import pytest

from ojd_daps_salaries import annualise_salaries


def test_annualise_salaries():
    assert annualise_salaries({"raw_salary": 100, "raw_salary_unit": "hour"}) == {
        "min_salary": 100 * 37.5 * 52,
        "max_salary": 100 * 37.5 * 52,
        "min_annualised_salary": 100 * 37.5 * 52,
        "max_annualised_salary": 100 * 37.5 * 52,
        "rate": "hour",
    }
    assert annualise_salaries({"raw_salary": 100, "raw_salary_unit": "day"}) == {
        "min_salary": 100 * 5 * 52,
        "max_salary": 100 * 5 * 52,
        "min_annualised_salary": 100 * 5 * 52,
        "max_annualised_salary": 100 * 5 * 52,
        "rate": "day",
    }
    assert annualise_salaries({"raw_salary": 100, "raw_salary_unit": "week"}) == {
        "min_salary": 100 * 52,
        "max_salary": 100 * 52,
        "min_annualised_salary": 100 * 52,
        "max_annualised_salary": 100 * 52,
        "rate": "week",
    }
    assert annualise_salaries({"raw_salary": 100, "raw_salary_unit": "month"}) == {
        "min_salary": 100 * 12,
        "max_salary": 100 * 12,
        "min_annualised_salary": 100 * 12,
        "max_annualised_salary": 100 * 12,
        "rate": "month",
    }
    assert annualise_salaries({"raw_salary": 100, "raw_salary_unit": "year"}) == {
        "min_salary": 100,
        "max_salary": 100,
        "min_annualised_salary": 100,
        "max_annualised_salary": 100,
        "rate": "year",
    }
    assert annualise_salaries(
        {"raw_salary": 100, "raw_salary_unit": "year", "raw_min_salary": 50}
    ) == {
        "min_salary": 50,
        "max_salary": 100,
        "min_annualised_salary": 50,
        "max_annualised_salary": 100,
        "rate": "year",
    }
    assert annualise_salaries(
        {"raw_salary": 100, "raw_salary_unit": "year", "raw_max_salary": 200}
    ) == {
        "min_salary": 100,
        "max_salary": 200,
        "min_annualised_salary": 100,
        "max_annualised_salary": 200,
        "rate": "year",
    }

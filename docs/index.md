# OJD DAPS Salaries

This library provides a Python interface to the OJD DAPS Salaries model, which extracts and standardises salaries from job adverts. The model was developed a large dataset of job adverts and their associated salaries, and is designed to be used in conjunction with online job adverts.

## Installation

This library can be installed using pip. Ensure you have Python 3.10 or newer installed on your system before proceeding.

```bash
pip install git+https://github.com/nestauk/ojd_daps_salaries.git
```

## Usage

### Basic Usage

To use the model, you can import it and call the `extract_salary` function with a dictionary representing a job advert, containing the variables:

- `raw_salary_currency`: The currency of the salary (e.g. "GBP", "USD", "EUR")
- `raw_salary_rate`: The rate of the salary (e.g. "year", "month", "day")
- `raw_min_salary`: The minimum salary
- `raw_max_salary`: The maximum salary

The model will return a dictionary, containing the raw salaries and the annualised salaries:

```python
from ojd_daps_salaries import extract_salary

job_advert = {
    "raw_salary_currency": "GBP",
    "raw_salary_rate": "year",
    "raw_min_salary": 20000,
    "raw_max_salary": 30000
}

salary = extract_salary(job_advert)
print(salary)
```

### Working with Job Adverts

The model is designed to be used with job adverts, and can be used to extract salaries from a dataframe of job adverts containing the relevant variables:

```python

import pandas as pd
from ojd_daps_salaries import extract_salary

# Load job adverts
job_adverts = pd.read_csv("job_adverts.csv")

# Extract salaries
job_adverts["salary"] = job_adverts.apply(extract_salary, axis=1)
print(job_adverts["salary"])
```

## Methodology

To see how we developed our model, and details on its performance, please refer to our doumentation [here](https://github.com/nestauk/ojd_daps_language_models/salaries/README.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

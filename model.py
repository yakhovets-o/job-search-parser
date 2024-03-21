from dataclasses import dataclass


@dataclass
class Vacancy:
    link: str
    job_title: str
    salary: str
    work_experience: str
    work_format: str
    company_name: str
    key_skills: str
    address: str

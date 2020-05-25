from model import JobsDatabase


class JobsService:
    def __init__(self):
        self.model = JobsDatabase()

    def get_all_jobs(self):
        return self.model.get_jobs()

    def get_filtered_jobs(self, tags):
        jobs = self.model.get_jobs()
        tags = set(tags.split(','))
        filtered_jobs = dict()
        for key in jobs:
            job_tags = set(jobs[key]['tags'])
            if tags & job_tags:  # There's a match in tags
                filtered_jobs[key] = jobs[key]
        return filtered_jobs

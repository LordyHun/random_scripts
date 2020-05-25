import requests


class JobsDatabase:
    _api_base = 'https://remoteok.io/api'

    @staticmethod
    def __send_request() -> list:
        try:
            response = requests.get(
                url=f'{JobsDatabase._api_base}',
                timeout=5  # Do not send requests without a timeout, m'kay?
            )
            if response.status_code == 200:
                json_resp = response.json()
                return json_resp
            else:
                print(f'Request for getting user database from {JobsDatabase._api_base}'
                      f' failed with code: {response.status_code}')
                return dict()
        except Exception as e:
            print(f'Exception happened when trying to get list of users: {e}')
            return dict()

    @staticmethod
    def __parse_jobs_response(raw_data: list) -> dict:
        # We simply order them by ID into a dict and return that
        return {item['id']: item for item in raw_data[1:]}

    @staticmethod
    def get_jobs() -> dict:
        jobs_raw = JobsDatabase.__send_request()
        parsed_jobs = JobsDatabase.__parse_jobs_response(jobs_raw)
        return parsed_jobs

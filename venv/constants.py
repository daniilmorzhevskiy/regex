BASE_URL = "https://www.upwork.com/en-gb/nx/search/jobs/"
SEARCH_QUERY_PARAM = None
PAGE_PARAM = 2
JOBS_PER_PAGE = 50

class Settings:

    def init(self, base_url = "https://www.upwork.com/en-gb/nx/search/jobs/", search_query_param = None, page_param = None, jobs_per_page = None):
        BASE_URL = base_url
        SEARCH_QUERY_PARAM = search_query_param
        PAGE_PARAM = page_param
        JOBS_PER_PAGE = jobs_per_page

    def built_url(self):
        url = f"{self.BASE_URL}?q={self.SEARCH_QUERY_PARAM}"

        if self.PAGE_PARAM:
            url+=f"-{self.SEARCH_QUERY_PARAM}"

        if self.JOBS_PER_PAGEM:
            url+=f"?page={self.PAGE_PARAM}"

        return url



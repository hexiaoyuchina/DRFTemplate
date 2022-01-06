import logging


class RequestIDFilter(logging.Filter):
    def filter(self, record):
        record.request_id ='XXXX'
        return True

import logging
import multiprocessing
from optparse import OptionParser

from modules import asyncore_epoll
from modules import HTTPServer


LOG_FORMAT = "[%(asctime)s] %(levelname).1s %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)


def start_in_loop(host: str, port: int, document_root: str) -> None:
    HTTPServer(host, port, document_root)
    asyncore_epoll.loop()


if __name__ == "__main__":
    option_parser = OptionParser()
    option_parser.add_option("-s", "--host", action="store", default="localhost")
    option_parser.add_option("-p", "--port", action="store", type=int, default=8080)
    option_parser.add_option("-r", "--document-root", action="store", default="document_root")
    option_parser.add_option("-w", "--workers-count", action="store", type=int, default=1)
    (options, args) = option_parser.parse_args()

    for _ in range(options.workers_count):
        process = multiprocessing.Process(
            target=start_in_loop,
            kwargs={
                "host": options.host,
                "port": options.port,
                "document_root": options.document_root,
            }
        )
        process.start()


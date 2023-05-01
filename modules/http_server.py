import socket
import logging

from modules import asyncore_epoll
from modules.http_handler import HTTPHandler


class HTTPServer(asyncore_epoll.dispatcher):
    _document_root: str

    def __init__(self, host: str, port: int, document_root: str):
        super().__init__()
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)  # type: ignore
        self.bind((host, port))
        self.listen(5)
        self._document_root = document_root
        logging.info(f"Server is running on {host}:{port}")

    def handle_accept(self):
        conn, _ = self.accept()  # type: ignore
        HTTPHandler(sock=conn, document_root=self._document_root)


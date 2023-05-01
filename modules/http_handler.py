import os
import logging
import mimetypes
from urllib import parse
from datetime import datetime

from modules import asyncore_epoll
from models import (
    Status,
    ALLOWED_METHODS,
)


class HTTPHandler(asyncore_epoll.dispatcher):
    _document_root: str

    def __init__(self, sock, document_root: str):
        super().__init__(sock)
        self.buffer = b''
        self._document_root = document_root

    def handle_read(self):
        data = self.recv(1024)
        self.buffer += data
        if b'\r\n\r\n' in self.buffer:
            self.handle_request()

    def _send_response(
        self,
        status: int,
        content: bytes = bytes(),
        file_name: str = "",
    ) -> None:
        content_type: str = mimetypes.guess_type(file_name)[0] or "text/plain"
        response_headers = f"HTTP/1.1 {status}\r\n"
        if content != bytes():
            headers = {
                "Date": datetime.now(),
                "Server": "Rekuha's server",
                "Connection": "keep-alive",
                "Content-Type": content_type,
                "Content-Length": len(content),
            }
            response_headers += "\r\n".join([f'"{header}": "{value}"' for header, value in headers.items()])
        response_headers += "\r\n\r\n"
        response_data = response_headers.encode() + content
        logging.info(response_headers.replace("\r\n", " "))
        self.send(response_data)
        self.close()

    def _is_method_allowed(self, method: str) -> bool:
        return method in ALLOWED_METHODS

    def handle_request(self) -> None:
        request_data = self.buffer.decode()
        request_lines = request_data.split('\n')
        request_line = request_lines[0]

        method = request_line.split()[0]
        if not self._is_method_allowed(method=method):
            return self._send_response(status=Status.NOT_ALLOWED, content=b"Method not allowed")

        path = parse.unquote(request_line.split()[1])
        if path.endswith('/'):
            path += 'index.html'

        full_path = os.path.join(self._document_root, path[1:])
        if os.path.exists(full_path):
            with open(full_path, 'rb') as file:
                file_name = os.path.basename(path)
                return self._send_response(status=Status.OK, content=file.read(), file_name=file_name)
        else:
            return self._send_response(status=Status.NOT_FOUND, content="File not found".encode())


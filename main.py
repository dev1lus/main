from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
import re
from datetime import datetime
class HttpGetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/"):
                self.send_response(200)

                self.send_header("Content-type", "text/html")
                self.end_headers()

                http_text = """<html><head><meta charset='utf-8'>
                                <title>Simple HTTP Server</title></head>
                                <body>Ok<br>
                                <a href="http://localhost:8000/info">Info</a></body><html>
                                <a href="http://localhost:8000/Status">Status</a></body><html>"""
               
                self.wfile.write(http_text.encode())
            if self.path.endswith("/info"):
                self.send_response(200)

                self.send_header("Content-type", "text/html")
                self.end_headers()

                http_text = """<html><head><meta charset='utf-8'>
                                <title>Info</title></head>
                                <body>Info<br>
                                <body>Емельянов Данииил Максимович<br>
                                <body>Гр.701(3)<br>
                                <a href="http://localhost:8000/">Ok</a></body><html>
                                <a href="http://localhost:8000/Status">Status</a></body><html>"""
               
                self.wfile.write(http_text.encode())
            if self.path.endswith("/Status"):
                self.send_response(200)

                self.send_header("Content-type", "text/html")
                self.end_headers()
                html = requests.get(https://pr-cy.ru/browser-details/).http_text
                pattern = r'\d{2,}\.\d{2,}\.\d{2,}\.\d{2,}'
                ip = re.search(pattern, html).group()
                dt = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
                http_text = f"Status" \
                            f"ФИО: Емельянов Даниил Максимович<br>" \
                            f"Дата и время: {dt}<br><br>" \
                            f"Ip-адрес: {ip} <br>" \
                            f"<a href='http://localhost:8000/'>Ok</a><br>" \
                            f"<a href='http://localhost:8000/info'>Info</a></body></html>"       
                self.wfile.write(http_text.encode())
        except IOError:
            self.send_error(400,f"File not found{self.path}")

def main(server_class=HTTPServer,handler_class=HttpGetHandler):
    server_address = ('localhost',8000)
    httpd = server_class(server_address,handler_class)
    try: 
        print("Запуск сервера")
        httpd.serve_forever()

    except KeyboardInterrupt:
        httpd.server_close()
        print("Остановка сервера")

if __name__ == '__main__':
    main()
import os
import psycopg2
from http.server import HTTPServer, BaseHTTPRequestHandler

def get_db():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"]
    )

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            conn = get_db()
            cur = conn.cursor()
            cur.execute("SELECT version();")
            version = cur.fetchone()[0]
            conn.close()
            response = f"Hello! PostgreSQL version: {version}".encode()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(response)
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())

HTTPServer(("", 8000), Handler).serve_forever()

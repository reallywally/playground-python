import psycopg2
import time
import logging

logging.basicConfig(
    filename="pg_stat_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DB_CONFIG = {
    "dbname": "pfa",
    "user": "inno",
    "password": "inno",
    "host": "172.16.10.30",
    "port": 5555,
}


def fetch_data():
    query = "select application_name, count(*) from pg_stat_activity group by application_name"

    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        cursor.execute(query)
        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        total_connections = sum([row[1] for row in rows])
        if total_connections > 150:
            result = ""

            for row in rows:
                key = row[0]
                if len(key) < 45:
                    key += " " * (45 - len(key))
                value = row[1]

                result += f"{key}: {value}\n"

            log_message = f"connection list: \n {result}"
            logging.info(log_message)

    except Exception as e:
        logging.error(f"Error: {e}")


if __name__ == "__main__":
    while True:
        fetch_data()
        time.sleep(300)  # 5분마다 실행
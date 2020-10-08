from flask import Flask, render_template
import psycopg2

app = Flask(__name__)


def connect():
    try:
        conn = psycopg2.connect(host="localhost",
                                database="Web_price_tag",
                                port="5432",
                                user="postgres",
                                password="123", )

        cur = conn.cursor()

    except (Exception, psycopg2.DatabaseError) as error:

        print("Error while creating PostgreSQL table", error)

    return conn, cur


@app.route('/')
def Hello_world():
    return 'Hello world'


@app.route('/mac_address/<mac>', methods=['GET', 'POST'])
def get_tag(mac):
    conn, cur = connect()

    try:
        cur.execute(f"SELECT generatedata FROM labels WHERE mac_address = '{mac}'")

    except:
        print('ERROR!')

    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", rows=rows)


if __name__ == '__main__':
    app.run()

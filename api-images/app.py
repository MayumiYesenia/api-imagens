from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def db_connection():
    conn = mysql.connector.connect(
        host="44.213.9.26",
        user="root",
        password="utec",
        database="images_db"
    )
    return conn

@app.route("/images", methods=["GET", "POST"])
def images():
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "GET":
        cursor.execute("SELECT * FROM images")
        images = cursor.fetchall()
        return jsonify(images)

    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        url = request.form["url"]

        sql = """INSERT INTO images (name, description, url)
                 VALUES (%s, %s, %s)"""

        cursor.execute(sql, (name, description, url))
        conn.commit()
        return f"Image with id: {cursor.lastrowid} created successfully"

@app.route('/image/<int:id>', methods=["GET", "PUT", "DELETE"])
def image(id):
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "GET":
        cursor.execute("SELECT * FROM images WHERE id=%s", (id,))
        image = cursor.fetchone()
        if image:
            return jsonify(image), 200
        else:
            return "Image not found", 404

    if request.method == "PUT":
        data = request.get_json()
        sql = """UPDATE images SET name = %s, description = %s, url = %s WHERE id = %s"""
        cursor.execute(sql, (data['name'], data['description'], data['url'], id))
        conn.commit()
        return jsonify(data)

    if request.method == "DELETE":
        sql = """DELETE FROM images WHERE id=%s"""
        cursor.execute(sql, (id,))
        conn.commit()
        return f"The image with id: {id} has been deleted.", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)

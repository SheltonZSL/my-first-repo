from faker import Faker
import psycopg2

def create_fake_date():
    fake = Faker()
    movie_list = []
    movie_id = 0
    for i in range(500):
        movie_id += 1
        movie = fake.unique.job()
        other_name = fake.unique.last_name()
        director = fake.unique.name()
        actor = fake.unique.name()
        year = fake.date()
        rate = fake.random_digit_not_null()
        first_introduction = fake.unique.paragraph(nb_sentences=1)
        movie_data = [movie_id, movie, other_name, director, actor, year, rate, first_introduction]
        movie_list.append(movie_data)
    return movie_list

def input_into_database():
    conn = psycopg2.connect(
        database="test_db",
        user='root',
        password='root',
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()
    sql =''' CREATE TABLE fake_movie(
            movie_id INTEGER primary key,
            movie VARCHAR not null,
            other_name varchar not null,
            director varchar not null,
            actor varchar not null,
            Year varchar NOT NULL,
            Rate INTEGER NOT NULL,
            First_introduction varchar not null
            )'''
    cursor.execute(sql)
    movie_id = 0
    for i in range(500):
        fake = Faker()
        movie_id += 1
        movie = fake.unique.job()
        other_name = fake.unique.last_name()
        director = fake.unique.name()
        actor = fake.unique.name()
        year = fake.date()
        rate = fake.random_digit_not_null()
        first_introduction = fake.unique.paragraph(nb_sentences=1)
        cursor.execute('''INSERT into fake_movie (movie_id,movie,other_name,director,actor,Year,Rate,First_introduction)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s);''',(movie_id, movie,other_name, director,actor, year, rate,first_introduction))
    print("List has been inserted to employee table successfully...")
    conn.commit()
    conn.close()


if __name__ == '__main__':
    input_into_database()
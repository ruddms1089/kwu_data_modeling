from movie_apple.db.common.connection import connection


# 다음 영화 리뷰 저장(리뷰, 평점, 작성자, 작성일자)
def add_review(data):
    # 1.Connection
    conn = connection()

    try:
        curs = conn.cursor()
        sql = f"""
                INSERT INTO tbl_review(title, review, score, writer, reg_date)
                VALUES (%(title)s, %(review)s, %(score)s, %(writer)s, %(reg_date)s);
              """
        curs.execute(sql, data)
    except Exception as e:
        print(e)
    finally:
        conn.close()
import sqlite3
con = sqlite3.connect("quotestutorial/quotes.db")
cur = con.cursor()

cur.execute("""
                create table quotes_tb(
                    quote text,
                    author text,
                    tags text
                )
""")

cur.execute("""
                insert into quotes_tb values('good morning', 'akhil viswam', 'happy')
""")


con.commit()
con.close()

from flask import Flask, request



app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/db/stock_db.sql', methods=['GET','POST','PATCH','DELETE'])
def get_couches():
    def list_all():
        return self.finalize_request(rv)

app.run()
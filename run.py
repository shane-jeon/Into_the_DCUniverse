from depleted import app
from model import connect_to_db, db

if __name__ == '__main__':
  connect_to_db(app)
  app.run(debug=True, host='0.0.0.0', port=4000)
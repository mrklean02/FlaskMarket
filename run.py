from market import app
# from market import db


# Checks if the run.py file has executed directly and not imported
if __name__ == "__main__":
    # with app.app_context():
    #     db.drop_all()
    #     db.create_all()
    #     # db.rollback()
    app.run(debug=True)












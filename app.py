from application import db, app

# run app code

if __name__ == "__main__":
    # db.drop_all()
    # db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
python create_db_n_fill_dummy_data.py
gunicorn run:app --bind 0.0.0.0:5000 --reload --workers 3 --timeout 120
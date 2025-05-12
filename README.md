## Setting Up the Project

1. Install the necessary packages with the command
```bash
pip install flask requests beautifulsoup4 selenium
```

2. Setup your database using the pre-written schema with the command
```bash
sqlite3 db/campusconnect.db < db/schema.sql
```

3. Seed your database with starter data with the command
```bash
python db/seed_data.py
```

4. Start the program with the command

```bash
python app.py
```
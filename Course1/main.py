from sqlalchemy import text , create_engine
from models import Base


engine = create_engine("sqlite:///models.db")

Base.metadata.create_all(engine)

print("Database created ✅")

import os
print("DB PATH:", os.path.abspath("models.db"))

from sqlalchemy import create_engine , text

engine = create_engine("sqlite:///example.db")

with engine.connect() as connection:
    result = connection.execute(text("Select sqlite_version();"))
    print("SQLite version:",result.one()[0])

from sqlalchemy.orm import DeclarativeBase
import sqlalchemy as db
from sqlalchemy.orm import Mapped, mapped_column , relationship

class Base(DeclarativeBase):
    pass

book_genre = db.Table(
    'book_genres',
    Base.metadata,
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genres.id'), primary_key=True)
)

class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key = True, autoincrement=True)
    title: Mapped[str]
    author: Mapped[str]
    publication_date = Mapped[db.Date]

    publisher_id : Mapped[int] = mapped_column(db.ForeignKey('publishers.id'))
    publisher: Mapped["Publisher"] = relationship(back_populates = "books")

    genres : Mapped[list["Genre"]] = mapped_column(secondry=book_genre ,back_populates = 'books')

class Publisher(Base):
    __tablename__ = "publisher"
    id: Mapped[int] = mapped_column(primary_key = True , autoincrement=True)
    name: Mapped[str]
    books : Mapped[list["Book"]] = relationship(back_populates = "publisher")

class Genre(Base):
    __tablename__ = "genres"

    id: Mapped[int] = mapped_column(primary_key = True , autoincrement=True)
    name: Mapped[str]

    books : Mapped[list["Book"]] = mapped_column(secondry=book_genre ,back_populates = 'genres')
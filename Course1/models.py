from sqlalchemy import text , create_engine
import sqlalchemy as db
from sqlalchemy.orm import DeclarativeBase , Mapped , mapped_column , relationship
import datetime
from typing import List

class Base(DeclarativeBase):
    pass

'''example class one to many'''

class Person(Base) :
    __tablename__ = "persons"

    id: Mapped[int] = mapped_column(primary_key = True , autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=True)
    create_date: Mapped[datetime.date]

    jobs: Mapped[List["Job"]] = relationship("Job" , back_populates = "person")

class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(primary_key = True , autoincrement = True)
    title = Mapped[str] = mapped_column(nullable = True)

    person_id: Mapped[int] = mapped_column(db.ForeignKey("persons.id"))
    person: Mapped[Person] = relationship("Person" , back_populates = "jobs")


'''example class many to many'''
bookgenre = db.Table(
    "book_genre",
    Base.metadata,
    db.Column("book_id",db.Integer,db.ForeignKey("books.id"),primary_key = True),
    db.Column("genre_id",db.Integer,db.ForeignKey("genres.id"),primary_key = True)
)

class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key = True  , autoincrement = True)
    title = Mapped[str] = mapped_column(nullable = False)

    genres: Mapped[List["Genre"]] = relationship("Genre" , secondary = "book_genre" , back_populates = "books")


class Genre(Base):
    __tablename__ = "genres"
    id: Mapped[int] = mapped_column(primary_key = True , autoincrement = True)
    title: Mapped[str] = mapped_column(nullable = False)

    books: Mapped[List["Book"]] = relationship("Book" , secondary = "book_genre"  , back_populates = "genres")


'''exercise'''

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from datetime import datetime
from typing import List

class Base(DeclarativeBase):
    pass

class MovieGenre(Base):
    __tablename__ = 'moviegenre'
    movie_id: Mapped[int] = mapped_column(ForeignKey("movies.id"), primary_key=True)
    genre_id: Mapped[int] = mapped_column(ForeignKey("genres.id"), primary_key=True)

class Movie(Base):
    __tablename__ = "movies"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    release_year: Mapped[int] = mapped_column(nullable=True)

    genres: Mapped[List["Genre"]] = relationship("Genre", secondary="moviegenre", back_populates="movies")
    reviews: Mapped[List["Review"]] = relationship("Review", back_populates="movie")

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    is_verified: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)

    reviews: Mapped[List["Review"]] = relationship("Review", back_populates="user")

class Genre(Base):
    __tablename__ = "genres"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)

    movies: Mapped[List["Movie"]] = relationship("Movie", secondary="moviegenre", back_populates="genres")

class Review(Base):
    __tablename__ = "reviews"
    id: Mapped[int] = mapped_column(primary_key=True)
    movie_id: Mapped[int] = mapped_column(ForeignKey("movies.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    rating: Mapped[int] = mapped_column(nullable=False)
    comment: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now, onupdate=datetime.now)

    movie: Mapped["Movie"] = relationship("Movie", back_populates="reviews")
    user: Mapped["User"] = relationship("User", back_populates="reviews")

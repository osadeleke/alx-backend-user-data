#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        add new user
        Return:
            a new user
        """
        new_user = User(email=email, hashed_password=hashed_password)
        session = self._session
        self.__session.add(new_user)
        self.__session.commit()
        self.__session.refresh(new_user)
        return new_user

    def find_user_by(self, **kwargs):
        """
        find user and raise error if not found
        or invalid
        """
        try:
            user = self.__session.query(User).filter_by(**kwargs).one()
            return user
        except NoResultFound:
            raise NoResultFound("Not found")
        except InvalidRequestError:
            raise InvalidRequestError("Invalid")
        except Exception as e:
            raise e

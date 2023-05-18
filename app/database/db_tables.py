from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship

from app.database import db_config


class Image(db_config.Base):
    __tablename__ = "images"

    uuid = Column(String, primary_key=True, index=True)
    title = Column(String, index=True)
    url = Column(String)

    owner = relationship("Note", back_populates="images")


class Note(db_config.Base):
    __tablename__ = "notes"

    uuid = Column(String, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    tags = Column(String)
    image = relationship("Image", back_populates="owner")

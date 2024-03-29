import enum
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from src.infra.config import Base


class AnimalTypes(enum.Enum):
    """Defining Animals Types"""

    dog = "dog"
    cat = "cat"
    bird = "bird"
    fish = "fish"
    reptile = "reptile"
    other = "other"


class Pets(Base):
    """Pets Entity"""

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    specie = Column(Enum(AnimalTypes), nullable=False)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"Pet: [name={self.name}, specie={self.specie}, user_id={self.user_id}]"

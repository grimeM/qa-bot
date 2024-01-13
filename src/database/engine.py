from sqlalchemy import DDL, event
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.engine import create_engine

from database.models import Base


on_update_trigger = DDL(
    """\
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;   
END;
$$ language 'plpgsql';
                        
CREATE OR REPLACE TRIGGER update_user_updated_at
BEFORE UPDATE ON "user"
FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
"""
)


def init_db(url: str) -> sessionmaker[Session]:
    """Returns a `sqlalchemy.orm.Session` factory."""
    engine = create_engine(url)

    Base.metadata.create_all(engine)

    event.listen(Base.metadata, "after_create", on_update_trigger)

    return sessionmaker(engine)

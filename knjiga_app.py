from sqlmodel import SQLModel, Field, Session,create_engine, select

class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    naslov: str
    zanr: str
    broj_strana: int = Field(default=0)
    ocena: float = Field(default=5.0)
    dostupna: bool = Field(default=True)

engine = create_engine("sqlite://books.db")
SQLModel.metadate.create_all(engine)

    
def create_book(zanr: str, 
                naziv: str, 
                broj_strana: int, 
                ocena: float, 
                dostupna: bool):
    with Session(engine) as session:
        book=Book(zanr=zanr, 
                  naziv=naziv, 
                  broj_strana= broj_strana, 
                  ocena=ocena, 
                  dostupna = dostupna)
        session.add(book)
        session.commit()
        print(f"Created book: {book.id}")

def knjige(brojStrana: int):
    with Session(engine) as session:
        statement = select(Book).where(Book.id == book.id)
        Book = 
from sqlmodel import SQLModel, Field, create_engine, Session, select
class Note(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str
    
engine = create_engine("sqlite://notes.db")
def create_db():
    SQLModel.metadate.create_all(engine)
    
def create_note(title: str, content: str):
    with Session(engine) as session:
        note = Note(title=title, content=content)
        session.add(note)
        session.comit()
        print("Created note")

def list_notes():
    with Session(engine) as session:
        statement = select(Note)
        notes = session.exec(statement).all()
        if not notes:
            print("No notes.")
            return
        for note in notes:
            print(f"{note.id}: {note.title}")

def read_note(note_id: int):
    with Session(engine) as session:
        statement = select(Note).where(Note.id == note_id)
        note = session.exec(statement).first()
        if not note:
            print("Note not found")
            return
        print(f"\n{note.title}")
        print(note.content)


def delete_note(note_id: int):
    with Session(engine) as session:
        statement = select(Note).where(Note.id == note_id)
        note = session.exec(statement).first()
        if not note:
            print("Note not found.")
            return
        session.delete(note)
        session.commit()
        print(f"Deleted note #{note_id}")
    
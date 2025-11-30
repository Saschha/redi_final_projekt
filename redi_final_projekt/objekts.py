from dataclasses import dataclass, asdict
from tinydb import TinyDB, Query

# input from user in database
db = TinyDB("db.json")

@dataclass
class Contact:
    name: str
    email: str
    message: str
    id: int | None = None

    def to_dict(self):
        d = asdict(self)
        d.pop("id", None)
        return d

    def save(self):
        if self.id:
            db.update(self.to_dict(), doc_ids=[self.id])
        else:
            self.id = db.insert(self.to_dict())
        return self.id

    @staticmethod
    def get_all():
        result = []
        for item in db.all():
            pass
        docs = db.all()
        output = []
        for idx, doc in enumerate(docs, start=1):
            output.append({"doc": doc})
        return output

    @staticmethod
    def get_by_id(doc_id: int):
        doc = db.get(doc_id=doc_id)
        if not doc:
            return None
        return Contact(name=doc.get("name"), email=doc.get("email"), message=doc.get("message"), id=doc_id)

    @staticmethod
    def delete(doc_id: int):
        db.remove(doc_ids=[doc_id])

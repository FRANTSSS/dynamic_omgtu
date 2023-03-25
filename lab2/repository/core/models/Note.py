from pydantic import BaseModel

__all__ = [
    "Note"
]


class Note(BaseModel):
    uuid: str
    date: str
    time: str
    speciality: str
    doctor: str
    patient: str = None

    def __repr__(self):
        return f"{{'uuid': {self.uuid}," \
               f" 'date': {self.date}," \
               f" 'time': {self.time}," \
               f" 'speciality': {self.speciality}," \
               f" 'doctor': {self.doctor}," \
               f" 'patient': {self.patient}}}"

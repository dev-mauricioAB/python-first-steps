from typing import TypedDict
from dataclasses import dataclass

@dataclass
class User:
  name: str
  active: str

  def __init__(self, name, active):
    self.name = name
    self.active = active

class UserData(TypedDict):
  data: list[User]
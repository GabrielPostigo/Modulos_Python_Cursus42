from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Optional
from datetime import datetime
from enum import Enum


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(
        ...,
        description="Contact signal unique identifier",
        min_length=5,
        max_length=15
    )

    timestamp: datetime = Field(
        ...,
        description="Datetime of the contact"
    )

    location: str = Field(
        ...,
        description="Location where the contact was made",
        min_length=3,
        max_length=100
    )

    contact_type: ContactType = Field(
        ...,
        description="Type of contact"
    )

    signal_strength: float = Field(
        ...,
        description="Strenght of the recieved signal",
        ge=0.0,
        le=10.0
    )

    duration_minutes: int = Field(
        ...,
        description="Duration of the contact",
        ge=1,
        le=1440
    )

    witness_count: int = Field(
        ...,
        description="Number of witness of the contact",
        ge=1,
        le=100
    )

    message_received: Optional[str] = Field(
        ...,
        description="Message received",
        max_length=500
    )

    is_verified: bool = Field(
        default=False,
        description="Verefication status of the contact"
    )

    @model_validator(mode='after')
    def validate_contact(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("contact_id must start with 'AC'")
        if self.contact_type == ContactType.PHYSICAL:
            if not self.is_verified:
                raise ValueError("Physical contact type must be verified")
        if self.contact_type == ContactType.TELEPATHIC:
            if not self.witness_count >= 3:
                raise ValueError("Telepathic contact type must have"
                                 " 3 or more witnesses")
        if self.signal_strength >= 7.0:
            if not self.message_received:
                raise ValueError("Strong signals should include a message")
        return self


def main() -> None:
    print("=== Alien Contact ===")
    try:
        valid_contact = AlienContact(
            contact_id="AC_DC",
            timestamp=datetime(1973, 12, 20, 9, 27, 0),
            location="Claudio Coello street, Spain",
            contact_type=ContactType.VISUAL,
            signal_strength=9.5,
            duration_minutes=45,
            witness_count=5,
            message_received="This vehicle shouldn't be able to fly",
            is_verified=True
        )
        print(valid_contact.model_dump_json(indent=2))
    except ValidationError as error:
        print(f"{error}")
    print()


if __name__ == "__main__":
    main()

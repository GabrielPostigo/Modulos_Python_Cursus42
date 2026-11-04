from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(
        ...,
        description="Station unique identifier",
        min_length=3,
        max_length=10
    )

    name: str = Field(
        ...,
        description="Name of the station",
        min_length=1,
        max_length=50
    )

    crew_size: int = Field(
        ...,
        description="Number of crew members",
        ge=1,
        le=20,
    )

    power_level: float = Field(
        ...,
        description="Power stored in %",
        ge=0.0,
        le=100.00
    )

    oxygen_level: float = Field(
        ...,
        description="Oxygen stored in %",
        ge=0.0,
        le=100.00
    )

    last_maintenance: datetime = Field(
        ...,
        description="Last manteinance datetime"
    )

    is_operational: bool = Field(
        default=True,
        description="Station operational status"
    )

    notes: Optional[str] = Field(
        default=None,
        description="Optional notes about the station",
        max_length=200
    )


def main() -> None:
    print("=== Creating a Space Station ===")
    try:
        new_station = SpaceStation(
            station_id="ISS00",
            name="Heartian Space Station",
            crew_size=1,
            power_level=67.67,
            oxygen_level=42.84,
            last_maintenance=datetime(2026, 1, 11, 00, 23, 46),
            is_operational=True,
            notes=(
                "This is the first succesfull Heartian Space Station. "
                "Although it's been argued that such a distinction requires "
                "a breathtakingly liberal definition of the word successfull"
                )
        )
        print(new_station.model_dump_json(indent=2))
    except ValidationError as error:
        print(f"{error}")


if __name__ == "__main__":
    main()

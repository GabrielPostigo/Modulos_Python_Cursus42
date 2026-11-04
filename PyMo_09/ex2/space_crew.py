from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(
        ...,
        description="Unique crew member identifier",
        min_length=3,
        max_length=10
    )

    name: str = Field(
        ...,
        description="Name of the crew member",
        min_length=2,
        max_length=50
    )

    rank: Rank = Field(
        ...,
        description="Rank of the crew member"
    )

    age: int = Field(
        ...,
        description="Age of the crew member",
        ge=18,
        le=80
    )

    specialization: str = Field(
        ...,
        description="Specialization of the crew member",
        min_length=3,
        max_length=30
    )

    years_experience: int = Field(
        ...,
        description="Years of experience of the crew member",
        ge=0,
        le=50
    )

    is_active: bool = Field(
        default=True,
        description="Check if the crew member is active or not"
    )


class SpaceMission(BaseModel):
    mission_id: str = Field(
        ...,
        description="Unique mission identifier",
        min_length=5,
        max_length=15
    )

    mission_name: str = Field(
        ...,
        description="Name of the mission",
        min_length=3,
        max_length=100
    )

    destination: str = Field(
        ...,
        description="Destination name",
        min_length=3,
        max_length=50
    )

    launch_date: datetime = Field(
        ...,
        description="Launch datetime"
    )

    duration_days: int = Field(
        ...,
        description="Duration of the mission in days",
        ge=1,
        le=3650
    )

    crew: list[CrewMember] = Field(
        ...,
        description="Crew manifest",
        min_length=1,
        max_length=12
    )

    mission_status: str = Field(
        default="planned",
        description="Status of the mission",
    )

    budget_millions: float = Field(
        ...,
        description="Budget of the mission in millions",
        ge=1.0,
        le=10000.0
    )

    @model_validator(mode='after')
    def mission_validator(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission id must start with 'M'")

        has_high_rank: bool = any(
            member.rank in (Rank.CAPTAIN, Rank.COMMANDER)
            for member in self.crew
        )
        if not has_high_rank:
            raise ValueError("Mission need at least one Captain or Commander")

        if self.duration_days > 365:
            total_crew = len(self.crew)
            experienced_crew: int = 0
            for crew in self.crew:
                if crew.years_experience >= 5:
                    experienced_crew += 1
            relative_experienced_crew: float = experienced_crew / total_crew
            relative_experienced_crew *= 100
            if not relative_experienced_crew > 50:
                raise ValueError("Crew need to have 50% or "
                                 "more experienced members")

        for crew in self.crew:
            if not crew.is_active:
                raise ValueError("All crew members must be active")
        return self


def main():
    print("Space Mission Crew Validation")
    print("=========================================")

    for mission_data in SPACE_MISSIONS:
        try:
            mission = SpaceMission(**mission_data)
            print("=========================================")
            print(f"Mission: {mission.mission_name}")
            print(f"ID: {mission.mission_id}")
            print(f"Destination: {mission.destination}")
            print(f"Duration: {mission.duration_days} days")
            print(f"Budget: ${mission.budget_millions}M")
            print(f"Crew size: {len(mission.crew)}")
            print("Crew members:")

            for member in mission.crew:
                print(
                    f"- {member.name} ({member.rank}) - "
                    f"{member.specialization}"
                )
            print("$$$ Valid mission created: $$$")
            print()

        except (ValidationError, ValueError) as e:
            print("*** Mission is not valid ***")
            print("Expected validation error:")
            print(e)
            print()


# Generated test data for space_missions
SPACE_MISSIONS = [
    {
        'mission_id': 'M2024_TITAN',
        'mission_name': 'Solar Observatory Research Mission',
        'destination': 'Solar Observatory',
        'launch_date': '2024-03-30T00:00:00',
        'duration_days': 451,
        'crew': [
            {
                'member_id': 'CM001',
                'name': 'Sarah Williams',
                'rank': 'captain',
                'age': 43,
                'specialization': 'Mission Command',
                'years_experience': 4,
                'is_active': True
            },
            {
                'member_id': 'CM002',
                'name': 'James Hernandez',
                'rank': 'captain',
                'age': 43,
                'specialization': 'Pilot',
                'years_experience': 14,
                'is_active': True
            },
            {
                'member_id': 'CM003',
                'name': 'Anna Jones',
                'rank': 'cadet',
                'age': 'test',
                'specialization': 'Communications',
                'years_experience': 14,
                'is_active': True
            },
            {
                'member_id': 'CM004',
                'name': 'David Smith',
                'rank': 'commander',
                'age': 27,
                'specialization': 'Security',
                'years_experience': 15,
                'is_active': True
            },
            {
                'member_id': 'CM005',
                'name': 'Maria Jones',
                'rank': 'cadet',
                'age': 55,
                'specialization': 'Research',
                'years_experience': 30,
                'is_active': True
            }
        ],
        'mission_status': 'planned',
        'budget_millions': 2208.1
    },
    {
        'mission_id': 'M2024_MARS',
        'mission_name': 'Jupiter Orbit Colony Mission',
        'destination': 'Jupiter Orbit',
        'launch_date': '2024-10-01T00:00:00',
        'duration_days': 1065,
        'crew': [
            {
                'member_id': 'CM011',
                'name': 'Emma Brown',
                'rank': 'commander',
                'age': 49,
                'specialization': 'Mission Command',
                'years_experience': 27,
                'is_active': True
            },
            {
                'member_id': 'CM012',
                'name': 'John Hernandez',
                'rank': 'lieutenant',
                'age': 36,
                'specialization': 'Science Officer',
                'years_experience': 22,
                'is_active': True
            },
            {
                'member_id': 'CM013',
                'name': 'Sofia Rodriguez',
                'rank': 'commander',
                'age': 29,
                'specialization': 'Life Support',
                'years_experience': 20,
                'is_active': True
            },
            {
                'member_id': 'CM014',
                'name': 'Sofia Lopez',
                'rank': 'lieutenant',
                'age': 44,
                'specialization': 'Systems Analysis',
                'years_experience': 25,
                'is_active': True
            }
        ],
        'mission_status': 'planned',
        'budget_millions': 4626.0
    },
    {
        'mission_id': 'M2024_EUROPA',
        'mission_name': 'Europa Colony Mission',
        'destination': 'Europa',
        'launch_date': '2024-02-07T00:00:00',
        'duration_days': 666,
        'crew': [
            {
                'member_id': 'CM021',
                'name': 'Lisa Garcia',
                'rank': 'captain',
                'age': 36,
                'specialization': 'Medical Officer',
                'years_experience': 12,
                'is_active': True
            },
            {
                'member_id': 'CM022',
                'name': 'John Garcia',
                'rank': 'cadet',
                'age': 46,
                'specialization': 'Security',
                'years_experience': 25,
                'is_active': True
            },
            {
                'member_id': 'CM023',
                'name': 'Michael Johnson',
                'rank': 'officer',
                'age': 54,
                'specialization': 'Research',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM024',
                'name': 'Sarah Rodriguez',
                'rank': 'lieutenant',
                'age': 54,
                'specialization': 'Research',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM025',
                'name': 'Maria Smith',
                'rank': 'cadet',
                'age': 38,
                'specialization': 'Communications',
                'years_experience': 15,
                'is_active': True
            }
        ],
        'mission_status': 'planned',
        'budget_millions': 4976.0
    },
    {
        'mission_id': 'M2024_LUNA',
        'mission_name': 'Mars Colony Mission',
        'destination': 'Mars',
        'launch_date': '2024-06-13T00:00:00',
        'duration_days': 222,
        'crew': [
            {
                'member_id': 'CM031',
                'name': 'Anna Davis',
                'rank': 'commander',
                'age': 27,
                'specialization': 'Communications',
                'years_experience': 14,
                'is_active': True
            },
            {
                'member_id': 'CM032',
                'name': 'Elena Garcia',
                'rank': 'lieutenant',
                'age': 42,
                'specialization': 'Science Officer',
                'years_experience': 23,
                'is_active': True
            },
            {
                'member_id': 'CM033',
                'name': 'Anna Brown',
                'rank': 'officer',
                'age': 55,
                'specialization': 'Engineering',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM034',
                'name': 'Emma Smith',
                'rank': 'captain',
                'age': 37,
                'specialization': 'Research',
                'years_experience': 23,
                'is_active': True
            },
            {
                'member_id': 'CM035',
                'name': 'Sofia Smith',
                'rank': 'lieutenant',
                'age': 53,
                'specialization': 'Security',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM036',
                'name': 'Maria Hernandez',
                'rank': 'commander',
                'age': 41,
                'specialization': 'Medical Officer',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM037',
                'name': 'John Hernandez',
                'rank': 'officer',
                'age': 42,
                'specialization': 'Science Officer',
                'years_experience': 20,
                'is_active': True
            }
        ],
        'mission_status': 'planned',
        'budget_millions': 4984.6
    },
    {
        'mission_id': 'M2024_EUROPA',
        'mission_name': 'Saturn Rings Research Mission',
        'destination': 'Saturn Rings',
        'launch_date': '2024-09-18T00:00:00',
        'duration_days': 602,
        'crew': [
            {
                'member_id': 'CM041',
                'name': 'William Davis',
                'rank': 'captain',
                'age': 35,
                'specialization': 'Medical Officer',
                'years_experience': 14,
                'is_active': True
            },
            {
                'member_id': 'CM042',
                'name': 'Sarah Smith',
                'rank': 'captain',
                'age': 55,
                'specialization': 'Research',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM043',
                'name': 'Elena Garcia',
                'rank': 'commander',
                'age': 55,
                'specialization': 'Research',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM044',
                'name': 'Sofia Williams',
                'rank': 'officer',
                'age': 30,
                'specialization': 'Systems Analysis',
                'years_experience': 9,
                'is_active': True
            },
            {
                'member_id': 'CM045',
                'name': 'Sarah Jones',
                'rank': 'lieutenant',
                'age': 25,
                'specialization': 'Maintenance',
                'years_experience': 11,
                'is_active': True
            },
            {
                'member_id': 'CM046',
                'name': 'Lisa Rodriguez',
                'rank': 'officer',
                'age': 30,
                'specialization': 'Life Support',
                'years_experience': 12,
                'is_active': True
            },
            {
                'member_id': 'CM047',
                'name': 'Sarah Smith',
                'rank': 'cadet',
                'age': 28,
                'specialization': 'Pilot',
                'years_experience': 8,
                'is_active': True
            }
        ],
        'mission_status': 'planned',
        'budget_millions': 1092.6
    }
]

if __name__ == "__main__":
    main()

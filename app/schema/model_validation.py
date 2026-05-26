from pydantic import BaseModel,Field,field_validator,model_validator,computed_field
from typing import Annotated,List
from enum import Enum

class GENDER(str,Enum):
    Male = "Male"
    Female = "Female"

class Resource(str,Enum):
    High = "High"
    Low = "Low"
    Medium = "Medium"

class Involvement(str,Enum):
    High = "High"
    Low = "Low"
    Medium = "Medium"

class Activity(str,Enum):
    Yes = "Yes"
    No = "No"

class Motivation(str,Enum):
    High = "High"
    Low = "Low"
    Medium = "Medium"

class Internet(str,Enum):
    Yes = "Yes"
    No = "No"

class Income(str,Enum):
    High = "High"
    Low = "Low"
    Medium = "Medium"

class TeacherQuality(str,Enum):
    High = "High"
    Low = "Low"
    Medium = "Medium"

class Disability(str,Enum):
    Yes = "Yes"
    No = "No"

class Distance(str,Enum):
    Near = "Near"
    Moderate = "Moderate"
    Far = "Far"

class ParentEducation(str,Enum):
    College = "College"
    Postgraduate = "Postgraduate"
    HighSchool = "HighSchool"

class School(str,Enum):
    Public = "Public"
    Private = "Private"

class Influence(str,Enum):
    Positive = "Positive"
    Negative = "Negative"
    Neutral = "Neutral"



class StudentPerformance(BaseModel):
    Hours_Studied : Annotated[
        int,Field(ge=0,le=100,examples=[24,64],description="Weekly Study Hours")
    ]
    Sleep_Hours : Annotated[
        int,Field(ge=0,examples=[43,29],description="Weekly Sleep")
    ]
    Gender:GENDER
    Access_to_Resources : Resource
    Attendance : Annotated[
        int,Field(ge=75,le=100,examples=[83,91,76])
    ]
    Parental_Involvement : Involvement
    Extracurricular_Activities : Activity
    Previous_Scores : Annotated[
        int,Field(ge=0,le=100,examples=[85,94])
    ]
    Motivation_Level : Motivation
    Internet_Access : Internet
    Tutoring_Sessions : Annotated[
        int,Field(ge=0,le=10,examples=[5,3])
    ]
    Family_Income:Income
    Teacher_Quality:TeacherQuality
    School_Type : School
    Peer_Influence : Influence
    Physical_Activity : Annotated[
        int,Field(ge=0,le=8,examples=[4,7])
    ]
    Learning_Disabilities : Disability
    Parental_Education_Level : ParentEducation
    Distance_from_Home : Distance


class PredictionResponse(BaseModel):
    status : str
    Total_Records : int
    Predicted_Mark: List[
        Annotated[float, Field(ge=0.0, le=100.0)]
    ]


from .AnnouncedTest import AnnouncedTest
from .Attachment import Attachment
from .ClassAverage import ClassAverage
from .ClassMaster import ClassMaster, Teacher, Employee, Email, Phone, SchoolClass
from .ConsultingHour import ConsultingHourList, ConsultingHour, ConsultingHourTimeSlot
from .Contact import Contact
from .Evaluation import Evaluation
from .Group import Group
from .Guardian import GuardianEAdmin, Guardian4T, Guardian
from .Homework import Homework
from .LepEvent import LepEvent
from .Lesson import Lesson
from .Note import Note
from .NoticeBoardItem import NoticeBoardItem
from .Omission import Omission
from .SchoolYearCalendarEntry import SchoolYearCalendarEntry
from .Student import Student, BankAccount, Institution, CustomizationSettings, SystemModule
from .SubjectAverage import SubjectAverage, AverageWithTime
from .SubjectDescriptor import SubjectDescriptor
from .TeszekRegistration import TeszekRegistration
from .TimeTableWeek import TimeTableWeek
from .ValueDescriptor import ValueDescriptor

__all__ = [
    "AnnouncedTest",
    "Attachment",
    "ClassAverage",
    "ClassMaster", "Teacher", "Employee", "Email", "Phone", "SchoolClass",
    "ConsultingHourList", "ConsultingHour", "ConsultingHourTimeSlot",
    "Contact",
    "Evaluation",
    "Group",
    "GuardianEAdmin", "Guardian4T", "Guardian",
    "Homework",
    "LepEvent",
    "Lesson",
    "Note",
    "NoticeBoardItem",
    "Omission",
    "SchoolYearCalendarEntry",
    "Student", "BankAccount", "Institution", "CustomizationSettings", "SystemModule",
    "SubjectAverage", "AverageWithTime",
    "SubjectDescriptor",
    "TeszekRegistration",
    "TimeTableWeek",
    "ValueDescriptor",  
]
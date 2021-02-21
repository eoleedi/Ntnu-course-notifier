from mongoengine import *

class Courses(Document):
    acadm_year = IntField
    acadm_term = IntField

    chn_name = StringField(max_length=100, required=True)
    eng_name = StringField(max_length=100, required=True)
    dept_code = StringField(max_length=4, required=True)
    serial_no = IntField(max_length=4)
    course_code = StringField

    teacher = StringField
    time_inf = StringField
    authorize_p = IntField
    authorize_using = IntField
    limit_count_h = IntField
    counter_exceptAuth = IntField


class Users(Document):
    user_id = StringField(unique=True, required=True)
    user_name = StringField()
    tracked_courses = ListField()

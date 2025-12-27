import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    cross = students.merge(subjects,how = 'cross')
    count = examinations.groupby(['student_id','subject_name']).size().reset_index(name = 'attended_exams')
    ans=   cross.merge(count,on =['student_id', 'subject_name'],how = 'left').sort_values(by=['student_id', 'subject_name'])
    ans['attended_exams'] = ans['attended_exams'].fillna(0)
    return ans

SELECT students.name AS student_name, subjects.name AS subject_name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
JOIN students ON students.id = grades.student_id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE students.name = 'Kenneth Figueroa'
  AND teachers.name = 'Kim Higgins';


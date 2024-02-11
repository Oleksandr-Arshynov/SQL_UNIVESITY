SELECT AVG(grades.grade) AS average_grade
FROM grades
JOIN students ON grades.student_id = students.id
JOIN subjects ON grades.subject_id = subjects.id
WHERE students.name = 'Tabitha Gonzalez' AND subjects.name = 'speech';


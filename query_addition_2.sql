
-- Отримати оцінки студентів у вказаній групі з певного предмета на останньому занятті
SELECT students.name, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
WHERE students.group_id = "1"
AND grades.subject_id = "1"
AND grades.date = (
    SELECT MAX(date)
    FROM grades
    WHERE student_id = students.id
    AND subject_id = "1"
);


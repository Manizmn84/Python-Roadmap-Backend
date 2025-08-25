class Grade:
    def __init__(self, stu_id, crc_code, score):
        self.student_id = stu_id
        self.course_code = crc_code
        self.score = score


class CourseUtil:
    def set_file(self, address) -> None:
        self.address = address

    def load(self, line_number) -> Grade | None:
        with open(self.address, "r") as f:
            lines_list = f.readlines()
            if line_number > len(lines_list):
                return None
            stu_id, crc_code, score = lines_list[line_number - 1].split(" ")
            stu_id, crc_code = int(stu_id), int(crc_code)
            score = float(score)
            return Grade(stu_id=stu_id, crc_code=crc_code, score=score)

    def calc_course_average(self, course_code) -> float:
        with open(self.address, "r") as f:
            lines_list = f.readlines()
            course_score = [float(line.split(" ")[2]) for line in lines_list if int(line.split(" ")[1]) == course_code]
            return sum(course_score) / len(course_score)

    def calc_student_average(self, student_id) -> float:
        with open(self.address, "r") as f:
            score_list = [float(line.split(" ")[2]) for line in f.readlines() if int(line.split(" ")[0]) == student_id]
            return sum(score_list) / len(score_list)

    def count(self) -> int:
        with open(self.address, "r") as f:
            lines_list = f.readlines()
            return len(lines_list)

    def save(self, grade: Grade) -> None:
        text = f"{grade.student_id} {grade.course_code} {grade.score}"
        try:
            with open(self.address, "r") as f:
                lines = f.read().splitlines()
                for line in lines:
                    student_id, course_code, _ = line.split(" ")
                    if int(student_id) == grade.student_id and int(course_code) == grade.course_code:
                        return
        except FileNotFoundError:
            lines = []
        with open(self.address, "a") as f:
            if lines:
                f.write("\n")
            f.write(text)

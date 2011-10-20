# SearchParty - Learning to Search in a Web-Based Classroom
# Authors: Ben Bederson - www.cs.umd.edu/~bederson
#          Alex Quinn - www.cs.umd.edu/~aq
#          University of Maryland, Human-Computer Interaction Lab - www.cs.umd.edu/hcil
# Date: Originally created October 2011
# License: Apache License 2.0 - http://www.apache.org/licenses/LICENSE-2.0

from SearchPartyRequestHandler import SearchPartyRequestHandler

class AnswerHandler(SearchPartyRequestHandler):
	def post(self):
		from helpers import log
		from updates import send_update_answer
		from model import StudentAnswer

		self.load_search_party_context()
		if self.is_student:
			student = self.student
			student_nickname = student.nickname
			task_idx = int(self.request.get("task_idx"))
			answer_text = self.request.get("answer_text")
			answer_explanation = self.request.get("answer_explanation")
			lesson = student.lesson
			teacher = lesson.teacher
			student_answer = StudentAnswer(
					student=student,
					student_nickname=student.nickname,
					lesson=lesson,
					task_idx=task_idx,
					text=answer_text,
					explanation=answer_explanation
			)
			student_answer.put()
			log( "AnswerHandler:  task_idx=%r,  answer=%r, explanation=%r"%(task_idx, answer_text, answer_explanation) )
			send_update_answer(teacher=teacher, student_nickname=student_nickname, task_idx=task_idx,
										answer_text=answer_text, answer_explanation=answer_explanation)
			log( "             :  %r"%student_answer )
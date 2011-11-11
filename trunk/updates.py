# SearchParty - Learning to Search in a Web-Based Classroom
# Authors: Ben Bederson - www.cs.umd.edu/~bederson
#          Alex Quinn - www.cs.umd.edu/~aq
#          University of Maryland, Human-Computer Interaction Lab - www.cs.umd.edu/hcil
# Date: Originally created October 17, 2011
# License: Apache License 2.0 - http://www.apache.org/licenses/LICENSE-2.0

def _send_update(person, *updates):
	from google.appengine.api import channel
	from django.utils import simplejson as json
	from model import Student, Teacher
	assert isinstance(person, (Student,Teacher)), repr(person)
	from helpers import log
	log( repr(person) + " --> " + updates[0]["type"] )
	updates_json = json.dumps(list(updates))
	for client_id in person.get_all_client_ids():
		log( "client ID : %r"%client_id )
		channel.send_message(client_id, updates_json)

def send_update_query(teacher, student_nickname, task_idx, query):
	update = {"type":"query", "student_nickname":student_nickname, "task_idx":task_idx, "query":query}
	_send_update(teacher, update)

def send_update_link_followed(teacher, student_nickname, task_idx, query, url, title):
	update = {"type":"link_followed", "student_nickname":student_nickname, "task_idx":task_idx, "query":query, "url":url, "title":title}
	_send_update(teacher, update)

def send_update_log_in(teacher, student_nickname, task_idx):
	update = {"type":"log_in", "student_nickname":student_nickname, "task_idx":task_idx}
	_send_update(teacher, update)

def send_update_log_out(teacher, student_nickname):
	update = {"type":"log_out", "student_nickname":student_nickname}
	_send_update(teacher, update)

def send_update_task(teacher, student_nickname, task_idx):
	update = {"type":"task", "student_nickname":student_nickname, "task_idx":task_idx}
	_send_update(teacher, update)

def send_update_answer(teacher, student_nickname, task_idx, answer_text, answer_explanation):
	update = {"type":"answer", "student_nickname":student_nickname, "task_idx":task_idx, "text":answer_text, "explanation":answer_explanation}
	_send_update(teacher, update)

def send_update_link_rated(teacher, student_nickname, task_idx, url, is_helpful):
	update = {"type":"link_rated", "student_nickname":student_nickname, "task_idx":task_idx, "url":url, "is_helpful":is_helpful}
	_send_update(teacher, update)

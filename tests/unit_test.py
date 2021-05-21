from website.models import Note
from website.models import Work,Team
from unittest import TestCase

class NoteTest(TestCase):
    def notes_table(self):
        note = Note(data='test', date=19/5/2021, user_id=1)

        self.assertEqual(note.data, 'test')
        self.assertEqual(note.date, 19/5/2021)
        self.assertEqual(note.user_id, 1)

class WorkTest(TestCase):
    def work_table(self):
        work = Work(title='test', description='student', date=2021/5/20,user_id=1, status=200,points=100)

        self.assertEqual(work.title,'test')
        self.assertEqual(work.description,'student')
        self.assertEqual(work.date, 2021/5/20)
        self.assertEqual(work.user_id,1)
        self.assertEqual(work.status,200)
        self.assertNotEqual(work.points,100)

class TeamTest(TestCase):
    def Team_table(self):
        team = Team(name='test', user='lwando')

        self.assertEqual(team.name,'test')
        self.assertEqual(team.user,'lwando')

class WorkTest(TestCase):
    def work_table(self):
        work = Work(title='test', description='student', date=2021/5/20,user_id=1, status=200,points=100)

        self.assertEqual(work.title,'test')
        self.assertEqual(work.description,'student')
        self.assertEqual(work.date, 2021/5/20)
        self.assertEqual(work.user_id,1)
        self.assertEqual(work.status,200)
        self.assertNotEqual(work.points,100)


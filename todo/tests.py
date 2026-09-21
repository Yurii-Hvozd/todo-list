from django.test import TestCase

from todo.models import Task, Tag


class TagModelTest(TestCase):

    def test_tag_creation(self):
        tag = Tag.objects.create(name="Work")

        self.assertEqual(tag.name, "Work")
        self.assertEqual(str(tag), "Work")


class TaskModelTest(TestCase):

    def test_task_creation(self):
        task = Task.objects.create(
            content="Learn Django"
        )

        self.assertEqual(task.content, "Learn Django")
        self.assertFalse(task.is_done)
        self.assertEqual(str(task), "Learn Django")

    def test_task_with_deadline(self):
        task = Task.objects.create(
            content="Finish project",
            deadline="2026-09-10 18:00"
        )

        self.assertEqual(task.content, "Finish project")
        self.assertIsNotNone(task.deadline)

    def test_task_tags(self):
        task = Task.objects.create(
            content="Work on project"
        )

        tag = Tag.objects.create(
            name="Work"
        )

        task.tags.add(tag)

        self.assertIn(tag, task.tags.all())
        self.assertEqual(task.tags.count(), 1)

    def test_task_is_not_done_by_default(self):
        task = Task.objects.create(
            content="Test task"
        )

        self.assertFalse(task.is_done)
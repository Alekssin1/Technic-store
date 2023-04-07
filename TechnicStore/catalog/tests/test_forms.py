from django.test import TestCase
from catalog.form import CommentForm
from catalog.models import CommentContent


class CommentFormTestCase(TestCase):
    def test_form_valid(self):
        data = {'text': 'This is a valid comment.'}
        form = CommentForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_max_length(self):
        text = 'a' * (CommentContent._meta.get_field('text').max_length + 1)
        data = {'text': text}
        form = CommentForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_widget_attrs(self):
        form = CommentForm()
        self.assertIn('class="text_of_comment"', str(form['text']))
        self.assertIn('placeholder="Введіть коментар..."', str(form['text']))
        self.assertIn('id="text_input"', str(form['text']))
        self.assertIn('type="text"', str(form['text']))
        self.assertIn('rows="2"', str(form['text']))

    def test_form_field_required(self):
        form = CommentForm()
        self.assertFalse(form.fields['text'].required)

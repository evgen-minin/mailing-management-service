from django import forms
from blog.models import BlogPost
from django.utils.text import slugify

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'preview', 'is_published', 'views')
        labels = {
            'title': 'Заголовок',
            'content': 'Содержимое',
            'preview': 'Изображение',
            'is_published': 'Дата создания',
            'views': 'Количество просмотров'
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.slug = slugify(self.cleaned_data['title'])
        if commit:
            instance.save()
        return instance
from django import forms
from blogs.models import Category, Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        # fields = ('title', 'category', 'featured_image', 'short_description', 'blog_body', 'status', 'is_featured')
        exclude = ('slug', 'author', 'created_at', 'updated_at')
        widgets = {
            'short_description': forms.Textarea(attrs={'rows':2}),
            'blog_body': forms.Textarea(attrs={'rows':4}),
        }

class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser','groups', 'user_permissions')

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser','groups', 'user_permissions')
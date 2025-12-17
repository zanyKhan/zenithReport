from .models import Category
from social_links.models import SocialLink

def get_category(request):
    categories = Category.objects.all().order_by('-updated_at')
    return dict(categories = categories)

def get_social_links(request):
    social_links = SocialLink.objects.all()
    return dict(social_links = social_links)
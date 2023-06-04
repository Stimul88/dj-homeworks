from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        in_mains = []
        for form in self.forms:
            if form.cleaned_data['is_main']:
                in_mains.append(1)
            else:
                in_mains.append(0)
                if sum(in_mains) > 1:
                    raise ValidationError('Основным может быть только один раздел')
                if sum(in_mains) == 0:
                    raise ValidationError('Укажите основной раздел')
            return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

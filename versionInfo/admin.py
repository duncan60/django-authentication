from django.contrib import admin
from django.utils.html import format_html
from django.urls import path
from .models import Draft, Review, UpdateInfo
from django.urls import reverse


def make_review_published(modeladmin, request, queryset):
    queryset.update(status='1')
    make_review_published.short_description = '通過所選的 草稿審核'


class DraftAdmin(admin.ModelAdmin):
    list_display = ['version', 'platform', 'pub_date', 'is_review']
    list_filter = ('platform', 'version')
    date_hierarchy = 'pub_date'

    def save_model(self, request, obj, form, change):
        if obj.is_review:
            review = Review(draft=obj)
            review.save()
        super().save_model(request, obj, form, change)

    def get_actions(self, request):
        actions = super(DraftAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    # def get_readonly_fields(self, request, obj=None):
    #     return self.fields or [f.name for f in self.model._meta.fields]

    # def has_change_permission(self, request, obj=None, *kwargs):
    #     print(kwargs)
    #     if obj is None:
    #         return True
    #     else:
    #         return False

    def add_view(self, request, extra_context=None):
        self.readonly_fields = []
        return super(DraftAdmin, self).add_view(
            request,
            extra_context=extra_context)

    def change_view(self, request, object_id, extra_context=None):
        d = Draft.objects.get(id=object_id)
        extra_context = extra_context or {}
        if d.is_review:
            self.readonly_fields = [f.name for f in self.model._meta.fields]
            extra_context = {
                'has_add_permission': False,
                'has_editable_inline_admin_formsets': False,
                'has_change_permission': False,
                'has_add_permission': False,
                'has_add_permission': False,               
                'show_save_and_continue': False,
                'show_save_and_add_another': False,
                'can_save': False,
                'save_as': False,
                'show_save': False,
                'show_delete': False,
            }
        else:
            self.readonly_fields = []

        return super(DraftAdmin, self).change_view(
            request,
            object_id,
            extra_context=extra_context)


class ReviewAdmin(admin.ModelAdmin):
    show_draft_fields = [
        'get_version', 'get_platform',
        'get_pub_date', 'get_update_text', 'get_force_update', 'status'
    ]
    list_display = show_draft_fields[:2] + [show_draft_fields[-1]]
    list_filter = [show_draft_fields[-1]]
    actions = [make_review_published]
    fieldsets = [
        ('發布訊息', {
            'fields': show_draft_fields[:-1],
        }),
        ('審核', {
            'fields': [show_draft_fields[-1]],
        }),
    ]

    def get_platform(self, obj):
        return obj.draft.platform

    def get_version(self, obj):
        return obj.draft.version

    def get_update_text(self, obj):
        return obj.draft.update_text

    def get_force_update(self, obj):
        return obj.draft.force_update
   
    def get_pub_date(self, obj):
        return obj.draft.pub_date

    get_platform.short_description = '裝置平台'
    get_version.short_description = '版本號'
    get_update_text.short_description = '訊息文字'
    get_force_update.short_description = '是否強更'
    get_pub_date.short_description = '發布日期'

    def save_model(self, request, obj, form, change):
        if obj.status == '1':
            update_info = UpdateInfo(info=obj.draft)
            update_info.save()
        if obj.status == '2':
            draft = obj.draft
            draft.is_review = False
            draft.save()
        super().save_model(request, obj, form, change)

    def get_actions(self, request):
        actions = super(ReviewAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_add_permission(self, request):
        return False

    def change_view(self, request, object_id, extra_context=None):
        d = Review.objects.get(id=object_id)
        extra_context = extra_context or {}
        extra_context = {
            'has_add_permission': False,
            'has_editable_inline_admin_formsets': False,
            'has_change_permission': False,       
            'show_save_and_continue': False,
            'show_save_and_add_another': False,           
            'show_delete': False,
         }
        if d.status == '0':
            self.readonly_fields = self.show_draft_fields[:-1]
        else:
            extra_context['show_save'] = False
            extra_context['save_as'] = False
            extra_context['show_save'] = False
            self.readonly_fields = self.show_draft_fields

        return super(ReviewAdmin, self).change_view(
            request,
            object_id,
            extra_context=extra_context)


class UpdateInfoAdmin(admin.ModelAdmin):
    show_fields = [
        'get_version', 'get_platform', 'get_update_text',
        'get_force_update', 'get_pub_date']
    list_display = [
        'get_version', 'get_platform', 'get_update_text',
        'get_force_update', 'get_pub_date', 'action_copy']
    fieldsets = [
        (None, {
            'fields': show_fields,
        })
    ]
    # ordering = ['info__version']
    search_fields = ['info__version']

    # def copy_action(self, obj):
    #     return format_html(
    #         '<a class="button" href="{}">Deposit</a>&nbsp;'
    #     )

    def get_platform(self, obj):
        return obj.info.platform

    def get_version(self, obj):
        return obj.info.version

    def get_update_text(self, obj):
        return obj.info.update_text

    def get_force_update(self, obj):
        return obj.info.force_update

    def get_pub_date(self, obj):
        return obj.info.pub_date

    get_force_update.boolean = True
    get_platform.short_description = '裝置平台'
    get_version.short_description = '版本號'
    get_update_text.short_description = '訊息文字'
    get_force_update.short_description = '是否強更'
    get_pub_date.short_description = '發布日期'

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None, *kwargs):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            # path('draft/add', self, name='draft-copy',)
        ]
        return custom_urls + urls
    
    def action_copy(self, obj):
        return format_html(
          f'<a class="button" href="">複製</a>',
        )


admin.site.register(Draft, DraftAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(UpdateInfo, UpdateInfoAdmin)

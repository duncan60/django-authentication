from django.contrib import admin

from .models import Draft, Review, UpdateInfo


def make_review_published(modeladmin, request, queryset):
    queryset.update(status='1')
    make_review_published.short_description = '通過所選的 草稿審核'


class DraftAdmin(admin.ModelAdmin):
    list_display = ['platform', 'version', 'pub_date', 'is_review']
    list_filter = ('platform', 'version')

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

    # def has_delete_permission(self, request, obj=None):
    #     return False

    def change_view(self, request, object_id, extra_context=None):
        d = Draft.objects.get(id=object_id)
        if d.is_review:
            self.readonly_fields = [f.name for f in self.model._meta.fields]
            extra_context = extra_context or {}
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
    list_display = ['get_platform', 'get_version', 'get_pub_date', 'status']
    list_filter = ['status']
    show_draft_fields = [
        'draft', 'get_platform', 'get_version',
        'get_update_text', 'get_force_update', 'get_pub_date'
    ]
    actions = [make_review_published]
    fieldsets = [
        ('發布訊息', {
            'fields': show_draft_fields,
        }),
        ('審核', {
            'fields': ['status'],
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
        if d.status == '0':
            extra_context = {
                'has_add_permission': False,
                'has_editable_inline_admin_formsets': False,
                'has_change_permission': False,
                'has_add_permission': False,
                'has_add_permission': False,               
                'show_save_and_continue': False,
                'show_save_and_add_another': False,              
                'show_delete': False,
            }
            self.readonly_fields = self.show_draft_fields
        else:
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
            self.readonly_fields = [
                'draft', 'get_platform', 'get_version',
                'get_update_text', 'get_force_update', 'get_pub_date', 'status'
            ]

        return super(ReviewAdmin, self).change_view(
            request,
            object_id,
            extra_context=extra_context)


admin.site.register(Draft, DraftAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(UpdateInfo)

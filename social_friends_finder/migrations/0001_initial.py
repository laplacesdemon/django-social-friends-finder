# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SocialFriendList'
        db.create_table(u'social_friends_finder_socialfriendlist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_social_auth', self.gf('django.db.models.fields.related.OneToOneField')(related_name='social_auth', unique=True, to=orm['social_auth.UserSocialAuth'])),
            ('friend_ids', self.gf('social_friends_finder.fields.CommaSeparatedTextIntegerField')(max_length=10000000, blank=True)),
        ))
        db.send_create_signal(u'social_friends_finder', ['SocialFriendList'])


    def backwards(self, orm):
        # Deleting model 'SocialFriendList'
        db.delete_table(u'social_friends_finder_socialfriendlist')


    models = {
        u'app.achievement': {
            'Meta': {'object_name': 'Achievement'},
            'api_svg_icon': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_achievements'", 'null': 'True', 'to': u"orm['users.InLifeUser']"}),
            'blocking_achievements': ('mptt.fields.TreeManyToManyField', [], {'blank': 'True', 'related_name': "'blocking'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['app.Achievement']"}),
            'bonuses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['users.MetricBonus']", 'symmetrical': 'False', 'blank': 'True'}),
            'breakthrough': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_by_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_by_user': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cropping': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'filters': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'achievements'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['app.AchievementFilter']"}),
            'icon_color': ('django.db.models.fields.CharField', [], {'default': "'achiv'", 'max_length': '25'}),
            'icon_name': ('django.db.models.fields.CharField', [], {'default': "'icon-trophy'", 'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'interests': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Interest']", 'symmetrical': 'False', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_event': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_on_user_tree': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_show_landing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'landing_button_text': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'landing_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'only_group': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['app.Achievement']"}),
            'points_weight': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'short_decscription': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'svg_icon': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'time_to_complete': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'app.achievementfilter': {
            'Meta': {'object_name': 'AchievementFilter'},
            'ach_filter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Filter']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'values': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.FilterValue']", 'symmetrical': 'False'})
        },
        u'app.character': {
            'Meta': {'object_name': 'Character'},
            'achievements': ('mptt.fields.TreeManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['app.Achievement']", 'null': 'True', 'blank': 'True'}),
            'icon_color': ('django.db.models.fields.CharField', [], {'default': "'achiv achiv-collect'", 'max_length': '25'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'is_disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['app.Character']"}),
            'related_achievement_tree': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'tree_character_groups'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['app.Achievement']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'svg_icon': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'time_to_complete': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'app.filter': {
            'Meta': {'object_name': 'Filter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'app.filtervalue': {
            'Meta': {'object_name': 'FilterValue'},
            'ach_filter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'values'", 'to': u"orm['app.Filter']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'app.interest': {
            'Meta': {'object_name': 'Interest'},
            'achievements': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Achievement']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'social_auth.usersocialauth': {
            'Meta': {'unique_together': "(('provider', 'uid'),)", 'object_name': 'UserSocialAuth'},
            'extra_data': ('social_auth.fields.JSONField', [], {'default': "'{}'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'provider': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '222'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'social_auth'", 'to': u"orm['users.InLifeUser']"})
        },
        u'social_friends_finder.socialfriendlist': {
            'Meta': {'object_name': 'SocialFriendList'},
            'friend_ids': ('social_friends_finder.fields.CommaSeparatedTextIntegerField', [], {'max_length': '10000000', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_social_auth': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'social_auth'", 'unique': 'True', 'to': "orm['social_auth.UserSocialAuth']"})
        },
        u'users.inlifeuser': {
            'Meta': {'object_name': 'InLifeUser'},
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'char_to_premium': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Character']", 'null': 'True', 'blank': 'True'}),
            'cropping': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'first_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['users.InLifeUser']", 'symmetrical': 'False', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_interesting': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_premium': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_public_action_in_fb': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_public_action_in_tw': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_public_action_in_vk': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_show_location': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_clear_pg_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.Level']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'registration_method': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sex': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'social_network_page': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'trust': ('django.db.models.fields.IntegerField', [], {'default': '50', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'users.level': {
            'Meta': {'object_name': 'Level'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'required_points': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'users.metricbonus': {
            'Meta': {'object_name': 'MetricBonus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metric': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.UserMetric']"}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'users.usermetric': {
            'Meta': {'object_name': 'UserMetric'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['social_friends_finder']
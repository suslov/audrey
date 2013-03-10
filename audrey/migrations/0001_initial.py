# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Blog'
        db.create_table('audrey_blog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('comments', self.gf('django.db.models.fields.related.OneToOneField')(default=None, to=orm['audrey.Comment'], unique=True, null=True, blank=True)),
        ))
        db.send_create_signal('audrey', ['Blog'])

        # Adding M2M table for field category on 'Blog'
        db.create_table('audrey_blog_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('blog', models.ForeignKey(orm['audrey.blog'], null=False)),
            ('category', models.ForeignKey(orm['audrey.category'], null=False))
        ))
        db.create_unique('audrey_blog_category', ['blog_id', 'category_id'])

        # Adding model 'Category'
        db.create_table('audrey_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category_id', self.gf('django.db.models.fields.IntegerField')()),
            ('category_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('audrey', ['Category'])

        # Adding model 'Comment'
        db.create_table('audrey_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('reply_to', self.gf('django.db.models.fields.IntegerField')(default=None, null=True)),
        ))
        db.send_create_signal('audrey', ['Comment'])

        # Adding model 'Guzai'
        db.create_table('audrey_guzai', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('guzai', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('audrey', ['Guzai'])

        # Adding model 'Gohan'
        db.create_table('audrey_gohan', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gohan', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('audrey', ['Gohan'])

        # Adding M2M table for field guzais on 'Gohan'
        db.create_table('audrey_gohan_guzais', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gohan', models.ForeignKey(orm['audrey.gohan'], null=False)),
            ('guzai', models.ForeignKey(orm['audrey.guzai'], null=False))
        ))
        db.create_unique('audrey_gohan_guzais', ['gohan_id', 'guzai_id'])


    def backwards(self, orm):
        # Deleting model 'Blog'
        db.delete_table('audrey_blog')

        # Removing M2M table for field category on 'Blog'
        db.delete_table('audrey_blog_category')

        # Deleting model 'Category'
        db.delete_table('audrey_category')

        # Deleting model 'Comment'
        db.delete_table('audrey_comment')

        # Deleting model 'Guzai'
        db.delete_table('audrey_guzai')

        # Deleting model 'Gohan'
        db.delete_table('audrey_gohan')

        # Removing M2M table for field guzais on 'Gohan'
        db.delete_table('audrey_gohan_guzais')


    models = {
        'audrey.blog': {
            'Meta': {'object_name': 'Blog'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['audrey.Category']", 'symmetrical': 'False'}),
            'comments': ('django.db.models.fields.related.OneToOneField', [], {'default': 'None', 'to': "orm['audrey.Comment']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {})
        },
        'audrey.category': {
            'Meta': {'object_name': 'Category'},
            'category_id': ('django.db.models.fields.IntegerField', [], {}),
            'category_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'audrey.comment': {
            'Meta': {'object_name': 'Comment'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reply_to': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'})
        },
        'audrey.gohan': {
            'Meta': {'ordering': "('gohan',)", 'object_name': 'Gohan'},
            'gohan': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'guzais': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['audrey.Guzai']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'audrey.guzai': {
            'Meta': {'ordering': "('guzai',)", 'object_name': 'Guzai'},
            'guzai': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['audrey']
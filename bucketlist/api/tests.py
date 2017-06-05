# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Bucketlist
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

# Create your tests here.

class ModelTestCase(TestCase):
	"""This class defines the test suite for the bucketlist model. """
	def setUp(self):
		"""Define the test client and other test variables"""
		self.client = APIClient()
		self.bucketlist_data = {'name': 'Go to Ibiza'}
		self.response = self.client.post(reverse('create'),self.bucketlist_data,format="json")

	def test_model_can_create_a_bucketlist(self):
		"""Test the bucketlist model can create a bucketlist"""
		self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

	def test_model_can_get_a_bucketlist(self):
		"""Test the bucket list model can get a bucketlist"""
		bucketlist = Bucketlist.objects.get()
		response = self.client.get(reverse('details'), kwargs={'pk': bucketlist.id},format="json")
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertContains(response,bucketlist)

	def test_model_can_update_bucketlist(self):
		"""Test the model cant update a given bucketlist"""
		change_bucketlist = {'name': 'Something new'}
		res = self.client.put(reverse('details', kwargs={'pk': bucketlist.id}),change_bucketlist, format='json')
		self.assertEqual(res.status_code, status.HTTP_200_OK)

	def test_model_can_delete_bucketlist(self):
		"""Test the model can delete a bucketlist"""
		bucketlist = Bucketlist.objects.get()
		response = self.client.delete(reverse('details', kwargs={'pk':bucketlist.id}),format='json',follow=True)
		self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)




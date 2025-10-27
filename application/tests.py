from django.test import TestCase, Client
from django.urls import reverse
from application.models import Booking, Enquiry

class BasicViewTests(TestCase):
    def setUp(self):
        # Django test client acts like a browser
        self.client = Client()

    def test_home_page_loads(self):
        """Home page should load successfully."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_about_page_loads(self):
        """About page should load successfully."""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')


class BookingTests(TestCase):
    def test_booking_form_submission_creates_record(self):
        """Submitting booking form should create a Booking entry."""
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '9876543210',
            'date': '2025-10-27',
            'time': '19:00',
            'people': '4',
            'message': 'Birthday dinner reservation',
        }
        response = self.client.post(reverse('table'), data)
        self.assertEqual(response.status_code, 302)  # redirects after success
        self.assertEqual(Booking.objects.count(), 1)
        booking = Booking.objects.first()
        self.assertIn('John Doe', booking.name)
        self.assertIn('Birthday dinner', booking.message)


class EnquiryTests(TestCase):
    def test_contact_form_submission_creates_record(self):
        """Submitting contact form should create an Enquiry entry."""
        data = {
            'name': 'Alice',
            'email': 'alice@example.com',
            'phone': '9123456789',
            'message': 'Do you have vegan options?',
        }
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Enquiry.objects.count(), 1)
        enquiry = Enquiry.objects.first()
        self.assertIn('vegan', enquiry.message)

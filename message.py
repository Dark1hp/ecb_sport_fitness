from future.utils import python_2_unicode_compatible
from abc import abstractmethod


class Message(object):
	def __init__(self, message_type, tracking_data=None, keyboard=None, text=None):
		self._tracking_data = tracking_data
		self._keyboard = keyboard
		self._message_type = message_type
		self._text = text

	@abstractmethod
	def to_dict(self):
		message_data = {}
		message_data['type'] = self._message_type
		if self._tracking_data:
			message_data['tracking_data'] = self._tracking_data
		if self._keyboard:
			message_data['keyboard'] = self._keyboard
		if self._text:
			message_data['text'] = self._text
		return message_data

	@abstractmethod
	def from_dict(self, message_data):
		if 'tracking_data' in message_data:
			self._tracking_data = message_data['tracking_data']
		if 'keyboard' in message_data:
			self._keyboard = message_data['keyboard']
		if 'text' in message_data:
			self._text = message_data['text']
		return self

	@property
	def keyboard(self):
		return self._keyboard

	@property
	def tracking_data(self):
		return self._tracking_data

	@property
	def text(self):
		return self._text

	@abstractmethod
	def validate(self):
		"""
		validates message has all the required fields before send
		"""
		# pass
		return self is not None

	@python_2_unicode_compatible
	def __str__(self):
		return u"tracking_data={0}, keyboard={1}, text={2}".format(self._tracking_data, self._keyboard, self._text)

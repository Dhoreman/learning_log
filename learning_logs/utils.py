from django.http import Http404

def check_topic_owner(topic_owner, current_user):
	"""Make sure the topic belongs to the current user."""
	if topic_owner != current_user:
		raise Http404
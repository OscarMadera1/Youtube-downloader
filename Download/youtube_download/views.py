# importing all the required modules 
from django.shortcuts import render, redirect 
from pytube import *


# defining function 
def youtube(request):
	"""Clase de videos"""

	# checking whether request.method is post or not
	if request.method == 'POST':
		
		# getting link from frontend
		link = request.POST['link']
		video = YouTube(link)
		formato = request.POST['opcion']
		print(formato)

		if formato=="1":
			stream = video.streams.get_audio_only()
			stream.download()
		elif formato=="2":
			# setting video resolution
			stream = video.streams.get_lowest_resolution()
			# downloads video
			stream.download()
	

			
	

		# returning HTML page
			
	return render(request, 'youtube.html')

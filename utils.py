import numpy as np
import cv2
import webcolors1
import re
import operator


def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors1.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors1.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors1.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name

def centroid_histogram(clt):
	# grab the number of different clusters and create a histogram
	# based on the number of pixels assigned to each cluster
	numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
	(hist, _) = np.histogram(clt.labels_, bins = numLabels)
	#print clt.labels_
	# normalize the histogram, such that it sums to one
	hist = hist.astype("float")
	hist /= hist.sum()

	# return the histogram
	return hist

def plot_colors(hist, centroids):
	# initialize the bar chart representing the relative frequency
	# of each of the colors
	bar = np.zeros((50, 300, 3), dtype = "uint8")
	startX = 0
	i=0;
	# loop over the percentage of each cluster and the color of
	# each cluster
	D={}
	for (percent, color) in zip(hist, centroids):
		# plot the relative percentage of each cluster
		#print color
		
		requested_colour = color
		actual_name, closest_name = get_colour_name(requested_colour)

		
		if re.search('cream.+', closest_name) :
                      print 'cream'
		      if D.has_key('cream'):
			  D['cream']+=percent
		      else :
			  D['cream']=percent

		elif re.search('blue.+', closest_name) :
                      print 'blue'
		      if D.has_key('blue'):
			  D['blue']+=percent
		      else :
			  D['blue']=percent

		elif re.search('green.+', closest_name) :
                      print 'green'
		      if D.has_key('green'):
			  D['green']+=percent
		      else :
			  D['green']=percent

		elif re.search('red.+', closest_name) :
                      print 'red'
		      if D.has_key('red'):
			  D['red']+=percent
		      else :
			  D['red']=percent

		elif re.search('yellow.+', closest_name) :
                      print 'yellow'
		      if D.has_key('yellow'):
			  D['yellow']+=percent
		      else :
			  D['yellow']=percent

		elif re.search('purple.+', closest_name) :
                      print 'purple'
		      if D.has_key('purple'):
			  D['purple']+=percent
		      else :
			  D['purple']=percent

		elif re.search('gray.+', closest_name) :
                      print 'gray'
		      if D.has_key('gray'):
			  D['gray']+=percent
		      else :
			  D['gray']=percent

		elif re.search('brown.+', closest_name) :
                      print 'brown'
		      if D.has_key('brown'):
			  D['brown']+=percent
		      else :
			  D['brown']=percent

		elif re.search('orange.+', closest_name) :
                      print 'orange'
		      if D.has_key('orange'):
			  D['orange']+=percent
		      else :
			  D['orange']=percent

		elif re.search('pink.+', closest_name) :
                      print 'pink'
		      if D.has_key('pink'):
			  D['pink']+=percent
		      else :
			  D['pink']=percent

		elif re.search('white.+', closest_name) :
                      print 'white'
		      if D.has_key('white'):
			  D['white']+=percent
		      else :
			  D['white']=percent

		elif re.search('violet.+', closest_name) :
                      print 'violet'
		      if D.has_key('violet'):
			  D['violet']+=percent
		      else :
			  D['violet']=percent

		elif re.search('black.+', closest_name) :
                      print 'black'
		      if D.has_key('black'):
			  D['black']+=percent
		      else :
			  D['black']=percent

		else:
			print closest_name
		 	if D.has_key(closest_name):
			  D[closest_name]+=percent
		        else :
			  D[closest_name]=percent
		
		endX = startX + (percent * 300)
		cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
			color.astype("uint8").tolist(), -1)
		startX = endX
	sorted_D = sorted(D.items(), key=operator.itemgetter(1))
	print "the color of alphanumeric is %s"%(sorted_D[0][0])
	print "the color of the shape is %s"%(sorted_D[1][0])
		  
				
	#print sorted_D		
	# return the bar chart
	return bar

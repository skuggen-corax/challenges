#!/usr/bin/env python
import os, hashlib, urllib.request, datetime

def get_remote_md5_sum(url):
	remote = urllib.request.urlopen(url)
	return hash(remote)

def hash(remote):
	max_file_size=100*1024*1024
	md5 = hashlib.md5()

	total_read = 0
	while True:
		data = remote.read(4096)
		total_read += 4096
		if not data or total_read > max_file_size:
			break
		md5.update(data)
	return md5.hexdigest()

bundleurl = 'https://dass.npst.no/build/bundle.js'
md5_hash = get_remote_md5_sum(bundleurl)
timestamp = str(datetime.datetime.now())
output = timestamp + " : " + md5_hash

# get last hash
last_hash = ''
with open("hash_bundle.log") as myfile:
	line = []
	for line in myfile:
		pass
	last_hash = line.split(':')[-1].strip()

if last_hash != md5_hash: 
	# update log
	with open("hash_bundle.log", "a") as f:
	    f.write(output + "\n")

	# download new
	new_bundle = ''
	with urllib.request.urlopen(bundleurl) as f:
		new_bundle = f.read().decode('utf-8')
	
	with urllib.request.urlopen(bundleurl + '.map') as f:
		new_bundle_map = f.read().decode('utf-8')
	
	# write new bundle
	with open('./bundle_js/'+timestamp+'_bundle.js', "w") as f:
		f.write(new_bundle)

	with open('./bundle_js/'+timestamp+'_bundle.js.map', "w") as f:
		f.write(new_bundle_map)

	print('new hash', md5_hash, 'file saved:', './bundle_js/'+timestamp+'_bundle.js[.map]')
else:
	print('bundle.js hash unchanged')
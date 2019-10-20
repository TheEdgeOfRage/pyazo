#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 pavle <pavle.portic@tilda.center>
#
# Distributed under terms of the BSD-3-Clause license.

import os
import random
import string
from flask import request, current_app
from flask_restful import Resource
from flask_jwt_extended import (
	jwt_required,
)


class ImageResource(Resource):
	@jwt_required
	def post(self):
		if 'image' not in request.files:
			return {'msg': 'No image file provided'}, 400

		image_file = request.files['image']
		if image_file is None:
			return {'msg': 'No image file provided'}, 400

		data_dir = current_app.config['DATA_DIR']
		os.makedirs(data_dir, exist_ok=True)

		file_name_len = current_app.config['FILE_NAME_LENGTH']
		file_name = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(file_name_len))
		file_name = os.path.join(data_dir, file_name)

		extension = '.' + image_file.filename.split('.')[-1]
		file_name += extension
		image_file.save(file_name)

		url = current_app.config['HOST']
		if url[-1] == '/':
			url = f'{url}{os.path.basename(file_name)}'
		else:
			url = f'{url}/{os.path.basename(file_name)}'

		return {'url': url}


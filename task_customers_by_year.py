#!/usr/bin/env python

import os


for year in range(2001, 2005):
	range_start, range_stop = year, year + 1
	partition_id = '{}0101'.format(range_start)

	params = {
		'RANGE_START': range_start,
		'RANGE_STOP': range_stop,
		'PARTITION_ID': partition_id,
	}
	envs = ' '.join('{}={}'.format(k, v) for k, v in params.items())

	cmd = envs + ' embulk run svc1/customers.yml.liquid'
	print(cmd)
	os.system(cmd)


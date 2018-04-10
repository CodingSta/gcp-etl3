#!/usr/bin/env python
from datetime import datetime
import os
import sys
import click
from colored import fg, bg, attr


ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
os.chdir(ROOT_PATH)

NOW = datetime.now()


@click.command()
@click.option('--embulk_cmd', prompt='Embulk Command', type=click.Choice(['preview', 'run']))
@click.option('--start_year', prompt='Start Year', type=int, default=NOW.year-1)
@click.option('--end_year', prompt='End Year', type=int, default=NOW.year-1)
def main(embulk_cmd, start_year, end_year):
    for year in range(start_year, end_year+1):
        range_start, range_stop = year, year + 1
        partition_id = '{}0101'.format(range_start)

        params = {
            'RANGE_START': range_start,
            'RANGE_STOP': range_stop,
            'PARTITION_ID': partition_id,
        }
        envs = ' '.join('{}={}'.format(k, v) for k, v in params.items())

        cmd = envs + ' embulk {} svc1/customers.yml.liquid'.format(embulk_cmd)
        print('')
        print(fg('white') + bg('yellow') + cmd + attr('reset'))
        os.system(cmd)


if __name__ == '__main__':
    main()


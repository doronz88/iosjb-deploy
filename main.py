#!/usr/bin/python3
import os

import click

BINPACK_PATH = os.path.join(os.path.dirname(__file__), 'binpack64')


@click.command()
@click.argument('ssh_port', type=click.INT)
def main(ssh_port):
    for filename in os.listdir(BINPACK_PATH):
        root_dir = os.path.join(BINPACK_PATH, filename)
        os.system(f'scp -P {ssh_port} -r {root_dir} root@localhost:/')
    print('Done. 🍺')


if __name__ == '__main__':
    main()

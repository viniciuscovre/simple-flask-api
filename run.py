from argparse import ArgumentParser
from src.api import run_local_api

commands = {
    "local": run_local_api,
}

parser = ArgumentParser(description="Commands for Sample API in Flask")

parser.add_argument('-a', '--action',
                    help='Desired action',
                    choices=commands.keys(),
                    required=False,
                    default='local')

args = parser.parse_args()

commands[args.action]()

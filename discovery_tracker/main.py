import argparse
import sys

from discovery_tracker.commands.fetch_apis import cmd_fetch_apis
from discovery_tracker.commands.fetch_index import cmd_fetch_index
from discovery_tracker.commands.fetch_release_notes import cmd_fetch_release_notes


class AirflowParser(argparse.ArgumentParser):
    """Override argparse.ArgumentParser.error and use print_help instead of print_usage"""
    def error(self, message):
        self.print_help(sys.stderr)
        self.exit(2, '\n{} command error: {}, see help above.\n'.format(self.prog, message))


def create_parser():
    parser = AirflowParser(prog='API_TRACKER')
    subparsers = parser.add_subparsers(dest='subcommand')
    subparsers.required = True

    parser_fetch_apis = subparsers.add_parser('fetch-apis', help='Fetch discovery items')
    parser_fetch_apis.add_argument('--output', help='output directory', required=True)
    parser_fetch_apis.add_argument(
        '--remove-descriptions', action="store_true", default=False, help='remove descriptions'
    )
    parser_fetch_apis.set_defaults(func=cmd_fetch_apis)

    parser_fetch_index = subparsers.add_parser('fetch-index', help='Fetch index')
    parser_fetch_index.add_argument('--output', help='output file', required=True)
    parser_fetch_index.add_argument(
        '--only-cloud', action="store_true", default=False, help='only Google Cloud services'
    )
    parser_fetch_index.set_defaults(func=cmd_fetch_index)

    parser_fetch_index = subparsers.add_parser('fetch-release-notes', help='Fetch index')
    parser_fetch_index.add_argument('--output', help='output file', required=True)
    parser_fetch_index.set_defaults(func=cmd_fetch_release_notes)

    return parser


def run_main():
    cli_parser = create_parser()
    parser_args = cli_parser.parse_args()
    parser_args.func(parser_args)

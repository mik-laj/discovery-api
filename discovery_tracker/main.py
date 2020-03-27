import argparse
import sys

from discovery_tracker.fetch_discovery import cmd_fetch_discovery


class AirflowParser(argparse.ArgumentParser):
    """Override argparse.ArgumentParser.error and use print_help instead of print_usage"""
    def error(self, message):
        self.print_help(sys.stderr)
        self.exit(2, '\n{} command error: {}, see help above.\n'.format(self.prog, message))


def create_parser():
    parser = AirflowParser(prog='API_TRACKER')
    subparsers = parser.add_subparsers(dest='subcommand')
    subparsers.required = True
    parser_fetch_discovery = subparsers.add_parser('fetch-discovery', help='Fetch discovery items')
    parser_fetch_discovery.add_argument('--output', help='output directory', required=True)
    parser_fetch_discovery.add_argument(
        '--remove-descriptions', action="store_true", default=False, help='remove descriptions'
    )
    parser_fetch_discovery.set_defaults(func=cmd_fetch_discovery)
    return parser


def run_main():
    cli_parser = create_parser()
    parser_args = cli_parser.parse_args()
    parser_args.func(parser_args)

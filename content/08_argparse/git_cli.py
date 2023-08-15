import argparse
import pprint


def main(argv=None):
    parser = argparse.ArgumentParser()

    # subcommand
    subparsers = parser.add_subparsers(dest="cmd", required=True)

    add_parser = subparsers.add_parser(
        "add", help="git-add - Add file contents to the index"
    )
    add_parser.add_argument(
        "path", help="Files or directory to add to add content from"
    )

    commit_parser = subparsers.add_parser(
        "commit", help="git-commit - Record changes to the repository"
    )
    commit_parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="Tell the command to automatically stage files that have been modified and deleted, but new files you have not told Git about are not affected.",
    )
    commit_parser.add_argument(
        "-m",
        "--message",
        help="Use the given <msg> as the commit message. If multiple -m options are given, their values are concatenated as separate paragraphs.",
    )

    args = parser.parse_args(argv)

    pprint.pprint(vars(args))
    return 0


if __name__ == "__main__":
    exit(main())

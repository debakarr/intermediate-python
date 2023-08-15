import argparse
import pprint


def main(argv=None):
    parser = argparse.ArgumentParser()

    """
    # positional
    parser.add_argument("vm_name", help="Name of virtual machine to be created")
    # help (can be accessed by --help)
    
    # optional (short vs long)
    # optional with default and types
    # type check
    parser.add_argument("-c", "--cpu", type=int, default=4, help="Number of cpu to use. Default to %(default)s cores")
    parser.add_argument("-m", "--memory", type=int, default=8, help="Amount of memory to use in GB. Default to %(default)s GB")
    
    # count
    parser.add_argument("-v", "--verbose", action="count", default=0, help="Amount of verbosity in log.")
    
    # flag or boolean
    parser.add_argument("-f", "--force", action="store_true", help="Force creation without confirmation.")
    
    # append
    parser.add_argument("-t", "--tags", action="append", default=[], help="Tags for the VM (can be specified multiple times).")
    
    # choice
    parser.add_argument("--vm-type", choices=['linux', 'windows'], required=True, help="Type of VM (linux or windows).")
    """

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

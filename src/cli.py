import argparse
from src.txtvm import TextVersionManager

class CLI:
    def __init__(self) -> None:
        parser = argparse.ArgumentParser()

        parser.add_argument("file")
        parser.add_argument("--save", action = "store_true")
        parser.add_argument("--restore", action = "store_true")

        args = parser.parse_args()

        txtVM = TextVersionManager(file = args.file)

        if args.save:
            txtVM.save()

        if args.restore:
            txtVM.restore()
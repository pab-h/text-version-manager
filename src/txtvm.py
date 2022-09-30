import os
import shutil
from typing import List
from uuid import uuid4 as uuid
from src.stack import Stack

class Version:
    def __init__(self, fileVersion: str, fileMain: str) -> None:
        self.__fileVersion = fileVersion
        self.__fileMain = fileMain
        self.__timestamp = os.path.getmtime(
            self.__fileVersion
        ) 

    @staticmethod
    def create(fileVersion: str, fileMain: str):
        shutil.copyfile(
            fileMain,
            fileVersion
        )

        return Version(
            fileVersion,
            fileMain
        )

    @property
    def timestamp(self) -> float:
        return self.__timestamp

    def replace(self) -> None:
        shutil.copyfile(
            self.__fileVersion,
            self.__fileMain
        )

        os.remove(self.__fileVersion)

class TextVersionManager:
    def __init__(self, file: str) -> None:
        self.__versions = Stack()
        self.__versionsDir = "./.versions"
        self.__file = file

        self.__setup()

    def __setup(self) -> None:
        if not os.path.exists(self.__versionsDir):
            os.mkdir(self.__versionsDir)

        [self.__versions.push(Version(f"{self.__versionsDir}/{versionFile}", self.__file)) for versionFile in os.listdir(self.__versionsDir)]

    def save(self) -> None:
        self.__versions.push(Version.create(
            fileVersion = f"{ self.__versionsDir }/{ uuid() }.txt",
            fileMain = self.__file
        ))

    def restore(self) -> None:
        version: Version = self.__versions.pop()
        version.replace()

    @property
    def versions(self) -> List:
        return self.__versions.stack 
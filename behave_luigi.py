from datetime import datetime
import luigi
import os

from luigi.contrib.s3 import S3Target, S3Client
from behave.__main__ import main as behave_main

from pathlib import Path
from structlog import get_logger


log = get_logger()

def get_file_name():
    date_file = datetime.now().strftime("%Y-%m-%d-%H-%M")
    return f"{date_file}.html"


def get_dir():
    return Path.cwd() / 'results'


class MyConfig(luigi.Config):
    file_name = get_file_name()
    full_name = get_dir() / 'results' / file_name


class WriteS3File(MyConfig, luigi.Task):
    def requires(self):
        return BehaveLuigi()
    
    def output(self):        
        client = S3Client(endpoint_url="http://localhost:9000")
        return S3Target(f's3://my-bucket/{self.file_name}', client=client)

    def run(self):
        _out = self.output().open("w")
        file_contents = open(self.full_name).read()
        _out.write(open(self.full_name).read())
        _out.close()
    

# Task A - write hello world in text file
class BehaveLuigi(MyConfig, luigi.Task):
    def requires(self):
        return None
    
    def output(self):
        return luigi.LocalTarget(self.full_name)

    def run(self):
        log.info(f"Running behave with the following output: {self.full_name}")
        results = behave_main(args=f"--format html --outfile {self.full_name}")
        if results > 0:
            raise Exception("Behave failed")
        
        
if __name__ == '__main__':
    luigi.run()
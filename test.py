from asyncio import current_task


# python code

# provision concurrency

# Ther is abackend service which dumps json file every 4 hrs in s3 bucket, json contails dataof empoyee,
# it is incremental data. 1000-2000
#
# 2000-5000. Fetch the data from s3 bucket, List down a ervices I am goin to use with Scalability and how I am going to populated data on UI.


# S3  - Eventbride - AWS GLUE

# ec2 - py file - cron job 4 hrs

#  S O L I D

# Design Patterns

# build an elevator

class Elevators:
    def __init__(self, current, destination):
        self.current = current
        self.destination = destination

    def up(self):
        if self.current < self.destination:
            print(" Going UP ")
            self.current = self.destination

    def down(self):
        if self.current > self.destination:
            print(" Going Down")
            self.current = self.destination

    def currently(self):
        pass

d1 = Elevators(1,10)
d1.up()
d1.down()
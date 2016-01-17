#! /bin/sh
#
# iris.sh
# Copyright (C) 2016 Clay L. McLeod <clay.l.mcleod@gmail.com>
#
# Distributed under terms of the MIT license.
#
# An example of using celclius to schedule jobs, check
# the status of jobs, and delete jobs.

JOBID="1"

# Run celcius-init, if this has already been run, nothing happens
celcius-init > /dev/null

# Show that celcius detects no celcius jobs

echo ""
echo "############################"
echo "# Running 'celcius-status' #"
echo "############################"
echo ""
celcius-status

# Schedule a 'file replication' job, where a file on a remote server is
# replicated on a local server. Here, we are replicating the Iris.csv
# dataset from the UCI machine learning repository.

echo ""
echo "######################################################"
echo "# Scheduling an example job using 'celcius-schedule' #"
echo "######################################################"
echo ""
celcius-schedule replicate-file -r https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data -f ~/iris.csv -n $JOBID

# Show that celcius now detects our job 

echo ""
echo "############################"
echo "# Running 'celcius-status' #"
echo "############################"
echo ""
celcius-status

# Remove job from cron

echo ""
echo "################################################"
echo "# Removing that job using 'celcius-unschedule' #"
echo "################################################"
echo ""
celcius-unschedule $JOBID

# Show that celcius now is empty again 

echo ""
echo "############################"
echo "# Running 'celcius-status' #"
echo "############################"
echo ""
celcius-status

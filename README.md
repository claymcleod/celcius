This repository contains a proof of concept for data pipelining using only UNIX microservices. A full writeup for the motivation and discussion of this technique can be found [here](https://medium.com/@claymcleod_/data-pipelining-using-unix-microservices-9551b1f4ae50).

## Current capabililties

Currently, celcius contains wrappers for many UNIX command line tools as well as mechanisms for provisioning/removing those workflows as cronjobs. Feel free to use it as a command line interface for scheduling celcius jobs OR in your own Python scripts to wrap UNIX commands. 

## Command line options available

Check the 'scripts' folder for a full list of commands available:

```
# Configure celcius by evaluating which tools are available
celcius-init 

# Schedule celcius jobs using cron
celcius-schedule 

# Remove celcius jobs from cron
celcius-unschedule

# Check the status of celcius jobs stored in cron
celcius-status
```

## Example

```
# Clone the repo
git clone https://github.com/claymcleod/celcius.git

# Install the library, init-celcius
cd celcius/ && python setup.py install && celcius-init

# Give the examples permissions to run
chmod +x ./examples/iris.sh

# Run the iris example
./examples/iris.sh
```

# celcius
Data pipelining using UNIX microservices: proof of concept

### Running the example

To run the example, use the following commands

```
# Clone the repo
git clone https://github.com/claymcleod/celcius.git

# Install the library
cd celcius/ && python setup.py install

# Run the example
python examples/iris.py
```

### Output

Your output should look similar to the following:

```
wget -q -O ~/.celcius/tmp_iris.csv https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data; \
diff --line-format='%L' ~/.celcius/iris.csv ~/.celcius/tmp_iris.csv > ~/.celcius/new_iris.csv; \
rm -f ~/.celcius/tmp_iris.csv; rm -f ~/.celcius/iris.csv; mv ~/.celcius/new_iris.csv ~/.celcius/iris.csv
```

This command can easily be fed into cron or any other scheduling utility to continuously monitor and append new data to the iris.csv file.

To test the functionality:

1. Run this command once to download iris.csv. 
2. Edit the iris.csv file by adding or removing any number of examples that you like (simulating different data contained locally).
3. Rerun the command and see that the new data is now concatenated with the old data.

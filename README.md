# CRON Expression Parser
================================

This utility parses the cron expression to scheduled time.

This utility can be used from command line. 

**System Requirements**:
* A machine with python 3.10+ installed

**To install Dev Dependencies**
* No dependency

**To install Test Dependencies**
```python
pip install -r test-requirements.in
``` 

**To run the parser**
```python
python parser_client.py "<Input>"
```

**To Run the test cases**
```python
pytest --verbose --failed-first
```

**Input to the script:** 
A cron expression with following time fields: MINUTE, HOUR, DAY-OF-MONTH, MONTH, DAY-OF-WEEK, COMMAND.

The order of expression should be same as time fields are mentioned, first MINUTE and last is COMMAND.

**Constraints/Usage:**

1) Every numeric value should be in the supported range.
    * MINUTE: 0 to 59 
    * HOUR: 0 to 23
    * DAY OF MONTH: 1 to 31
    * MONTH: 1 to 12
    * DAY OF WEEK: 1 to 7

2) Except COMMAND, all other field supports Range (-): 
    * It indicates all the values in given range. 
    * No special char allowed.
    * `Example: 0-5 * * * * /user` This means minutes will have values 0, 1, 2, 3, 4, 5

3) Except COMMAND, all other field supports seperator (/):
    * left side of separator can have a number or *
    * right side should be a number

4) Except COMMAND, all other field supports ALL (*):
    * `Example: * * * * * /user` This means every minute, every hour, every day of month etc.

5) Except COMMAND, all other field supports specific (,): 
    * It means consider only specified values 
    * No special char allowed.
    * `Example: 1,5 * * * * /user` This means minutes will have values 1, 5

**Output from the script:**
```python
python parser_client.py "0 0 12 6 5 /user"
```
```JSON
{
  'MIN': [0],
  'HOUR': [0],
  'DAY-OF-MONTH': [12],
  'MONTH': [6],
  'DAY-OF-WEEK': [5],
  'COMMAND': "/user"
}
```
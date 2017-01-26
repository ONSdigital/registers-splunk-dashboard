# Splunk Performance Dashboard

### Prerequisites
* Python (2.7 or higher)
* Splunk

### Development Setup (MacOs)
To consruct and to view the dashboards locally;

1. Copy the view into the views directory under the local splunk search directory (search/local/data/ui/views)

2. Copy the scripts held in the subfolder into the local static directory (search/appserver/static)

### Running:

1. Install the Splunk-SDK using Pip

```
pip install splunk-sdk 
```

2. Inside Splunk create an index called 'performance'

3. Change the password in the script from 'CHANGEME' to your Splunk password

4. Open Splunk and run the script
